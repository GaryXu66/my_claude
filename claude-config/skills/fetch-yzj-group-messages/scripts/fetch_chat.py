#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_chat.py — 云之家群组消息采集（独立通用版）

从 gen-weekly-report 工具链的 yzj_chat.py 提取而来，去掉了禅道 / git / 周报逻辑，
只保留「拉取云之家群消息 + 解析发送人姓名 + 导出 JSON」这一件事，做成任何人
都能用的通用工具。不绑定特定账号、不预设特定群。

== 凭证 ==
凭证从同目录的 config.json 读取（先把 config.example.json 复制为 config.json 再填）：
  - o_id      : 你本人的云之家 oId（取 openToken 用，决定能访问哪些群）—— 必填、每人不同
  - appkey    : 开放应用 appkey（默认云之家讯通开放应用，通常整个应用通用）
  - signature : 开放应用签名（同上，通常整个应用通用；换独立开放应用才需改）
USER_INFO_AUTH（查发送人姓名的接口认证）是通用服务账号，已内置，无需配置。

== 命令 ==
    python3 fetch_chat.py token                          # 验证凭证、打印 openToken
    python3 fetch_chat.py groups [内部|外部]              # 列出可访问的群（找 groupId/群名）
    python3 fetch_chat.py fetch <groupId> <start> <end>  # 拉消息+解析发送人+导出 JSON 文件
    python3 fetch_chat.py msgs  <groupId> <start> <end>  # 同上但仅打印到屏幕
    python3 fetch_chat.py userinfo <userId>              # 查单个 userId 的姓名/部门/职位

    日期格式 YYYY-MM-DD，例：
      python3 fetch_chat.py fetch 6a327781e4b05fbbe5356aad 2026-07-06 2026-07-10
"""
import json
import os
import re
import ssl
import sys
import urllib.request
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(HERE, "config.json")

BASE = "https://www.yunzhijia.com"
# 查发送人姓名用的通用服务账号 Basic 认证（kindee:yzj@... 与个人无关，全员通用）
USER_INFO_AUTH = "Basic a2luZ2RlZTp5empAMjIwMl9Hby1VUCE="
UA = ("oem:hongta;38882/10.0.4;Android 7.1.1;Meizu;PRO+6;102;1080*1920;"
      "deviceId:8883f035-5673-3ef6-9bbf-ea3e9b1d7669;deviceName:Meizu PRO+6;"
      "clientId:38882;os:Android 7.1.1;brand:Meizu;model:PRO+6;lang:zh-CN;")

_CTX = ssl.create_default_context()
_CTX.check_hostname = False
_CTX.verify_mode = ssl.CERT_NONE


# ----------------------------- 配置加载 -----------------------------
def load_config():
    """读取同目录 config.json；不存在或 o_id 为空时给出明确提示。"""
    if not os.path.exists(CONFIG_FILE):
        raise SystemExit(
            f"未找到配置文件 {CONFIG_FILE}\n"
            "请先复制模板：cp config.example.json config.json，"
            "填入你的 o_id（必填）后重试。")
    cfg = json.load(open(CONFIG_FILE, encoding="utf-8"))
    if not (cfg.get("o_id") or "").strip():
        raise SystemExit(f"{CONFIG_FILE} 中 o_id 为空，请填入你本人的云之家 oId 后重试。")
    return cfg


# ----------------------------- HTTP -----------------------------
def _post(url, headers, data):
    req = urllib.request.Request(
        url, data=json.dumps(data).encode("utf-8"),
        headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=60, context=_CTX) as r:
        return json.loads(r.read().decode("utf-8"))


# ----------------------------- 1) openToken -----------------------------
def get_open_token(cfg):
    """用 config 里的 oId + appkey + signature 换取 openToken（代表 o_id 这个人）。"""
    resp = _post(f"{BASE}/openaccess/user/getXTTokenByoId",
                 {"appkey": cfg.get("appkey", ""), "signature": cfg.get("signature", ""),
                  "Content-Type": "application/json"}, {"oId": cfg["o_id"]})
    if not resp.get("success"):
        raise RuntimeError(f"get_open_token 失败: {resp}")
    return resp["data"]


# ----------------------------- 2) 群组列表 -----------------------------
def group_list(token, external=False):
    path = "/xuntong/ecLite/convers/v3/extGroupList" if external \
        else "/xuntong/ecLite/convers/v3/groupList"
    return _post(f"{BASE}{path}",
                 {"openToken": token, "User-Agent": UA, "Content-Type": "application/json"},
                 {"lastUpdateTime": "2020-01-01 00:00:00", "count": 220, "offset": 0})


def find_group(token, group_id):
    """在内部群、外部群里依次找 groupId；找到返回群对象，否则 None。"""
    for ext in (False, True):
        for g in group_list(token, external=ext).get("data", {}).get("list", []) or []:
            if g.get("groupId") == group_id:
                return g
    return None


# ----------------------------- 3) 消息分页 -----------------------------
def pre_msg_list(token, group_id, msg_id, count=50):
    return _post(f"{BASE}/xuntong/ecLite/convers/preMsgList.action",
                 {"openToken": token, "Content-Type": "application/json; charset=utf-8"},
                 {"groupId": group_id, "type": "old", "msgId": msg_id,
                  "count": count, "useMS": True})


def fetch_messages(token, group_id, start_dt, end_dt, count=50, max_pages=80):
    """按 [start_dt, end_dt] 窗口向前分页拉取全部消息。
    start_dt/end_dt 形如 '2026-06-15 00:00:00'。
    翻页规则：用每批最早一条消息的 msgId 作为下一次游标，到窗口起点停止。
    返回 (messages, group_obj)。
    """
    lo, hi = start_dt[:19], end_dt[:19]
    g = find_group(token, group_id)
    if not g:
        raise RuntimeError(f"群组列表中未找到 groupId={group_id}（确认 o_id 对应的人在群里）")
    cursor = g.get("lastMsgId")
    if not cursor:
        raise RuntimeError(f"群 {group_id} 无 lastMsgId，可能是新群尚无消息")

    collected, seen = [], set()
    for _ in range(max_pages):
        resp = pre_msg_list(token, group_id, cursor, count)
        data = resp.get("data") or {}
        lst = data.get("list") or []
        if not lst:
            break
        for m in lst:
            st = (m.get("sendTime") or "")[:19]
            mid = m.get("msgId")
            if mid and mid not in seen and lo <= st <= hi:
                seen.add(mid)
                collected.append(m)
        oldest = min(lst, key=lambda m: m.get("sendTime") or "")
        oldest_t = (oldest.get("sendTime") or "")[:19]
        if oldest_t < lo:                       # 已早于窗口起点，停止
            break
        cursor = oldest.get("msgId")
        if data.get("more") is False:
            break
    collected.sort(key=lambda m: m.get("sendTime") or "")
    return collected, g


# ----------------------------- 4) userInfo 姓名解析 -----------------------------
def user_info(user_id):
    """根据 fromUserId 查人员详情(姓名/部门/职位)。
    外部群 fromUserId 以 '_ext' 结尾，URL 里原样使用即可。"""
    url = f"{BASE}/xuntong/manage/data/userInfo/{user_id}"
    resp = _post(url, {"Authorization": USER_INFO_AUTH, "Content-Type": "application/json"}, {})
    d = resp.get("data") or {}
    return {"userId": user_id, "name": d.get("name"), "department": d.get("department"),
            "jobTitle": d.get("jobTitle"), "pinyin": d.get("fullPinyin")}


def resolve_senders(messages):
    """对一批消息中的所有 fromUserId 批量解析姓名，返回 {userId: info}。
    跳过 BOT- 开头的机器人。"""
    out, seen = {}, set()
    for m in messages:
        uid = m.get("fromUserId")
        if not uid or uid in seen or str(uid).startswith("BOT-"):
            continue
        seen.add(uid)
        try:
            out[uid] = user_info(uid)
        except Exception as e:
            out[uid] = {"userId": uid, "name": f"ERR:{e}"}
    return out


# ----------------------------- 导出 -----------------------------
def _safe_filename(s):
    return re.sub(r"[\\/:*?\"<>|\s]+", "_", s or "").strip("_")[:40]


def export_json(messages, sender_map, group, start, end, outdir=HERE):
    """把消息 + 发送人映射合并导出为结构化 JSON，返回输出路径。"""
    enriched = []
    for m in messages:
        uid = m.get("fromUserId")
        enriched.append({
            "time": (m.get("sendTime") or "")[:19],
            "fromUserId": uid,
            "sender": (sender_map.get(uid) or {}).get("name") or uid,
            "msgType": m.get("msgType"),
            "content": m.get("content") or "",
        })
    payload = {
        "group": {"groupId": group.get("groupId"), "groupName": group.get("groupName")},
        "period": {"start": start, "end": end},
        "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_messages": len(enriched),
        "senders": sender_map,
        "messages": enriched,
    }
    tag = _safe_filename(group.get("groupName")) or (group.get("groupId") or "")[:8]
    outpath = os.path.join(outdir, f"messages_{tag}_{start}_{end}.json")
    json.dump(payload, open(outpath, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return outpath


# ----------------------------- CLI -----------------------------
def _cli():
    if len(sys.argv) < 2:
        print(__doc__); return
    cmd = sys.argv[1]

    # userinfo 只用通用服务账号，不需要 openToken / config
    if cmd == "userinfo":
        if len(sys.argv) < 3:
            print("用法: userinfo <userId>"); return
        print(json.dumps(user_info(sys.argv[2]), ensure_ascii=False, indent=2))
        return

    # token 只验证凭证
    if cmd == "token":
        print(get_open_token(load_config()))
        return

    # groups / msgs / fetch 都需要 openToken
    cfg = load_config()
    token = get_open_token(cfg)

    if cmd == "groups":
        external = len(sys.argv) > 2 and sys.argv[2] in ("外部", "ext", "external")
        lst = group_list(token, external=external).get("data", {}).get("list", []) or []
        print(f"共 {len(lst)} 个{'外部' if external else '内部'}群：")
        for g in lst:
            print(f"  {g.get('groupId')}  {g.get('groupName')}  last={g.get('lastMsgSendTime')}")

    elif cmd in ("msgs", "fetch"):
        if len(sys.argv) < 5:
            print(f"用法: {cmd} <groupId> <start YYYY-MM-DD> <end YYYY-MM-DD>"); return
        gid, start, end = sys.argv[2], sys.argv[3], sys.argv[4]
        msgs, group = fetch_messages(token, gid, start + " 00:00:00", end + " 23:59:59")
        smap = resolve_senders(msgs)
        gname = (group or {}).get("groupName") or gid
        print(f"群「{gname}」{start}~{end}：共 {len(msgs)} 条消息，{len(smap)} 个发送人")
        if cmd == "msgs":
            for m in msgs:
                uid = m.get("fromUserId")
                name = (smap.get(uid) or {}).get("name") or uid
                print(f"  [{(m.get('sendTime') or '')[:19]}] {name}: {(m.get('content') or '')[:80]}")
        else:  # fetch
            outpath = export_json(msgs, smap, group or {"groupId": gid}, start, end)
            print(f"✅ 已导出：{outpath}")
    else:
        print("未知命令:", cmd); print(__doc__)


if __name__ == "__main__":
    _cli()
