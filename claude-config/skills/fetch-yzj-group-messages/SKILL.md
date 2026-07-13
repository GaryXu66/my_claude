---
name: fetch-yzj-group-messages
description: Use when fetching/exporting 云之家(yunzhijia) group chat messages by date range for any group/person —— 按时间段拉取某个云之家群的聊天记录、解析发送人姓名并导出 JSON。触发：用户说"拉群消息""导出群聊天记录""获取群消息""云之家群消息""群聊记录"，或要按日期范围导出某个群的对话内容。
---

# 获取云之家群组消息

## 概述
独立通用工具，从 `gen-weekly-report` 工具链的 `yzj_chat.py` 提取而来。**只做一件事**：按时间段拉取某个云之家群的消息 → 解析每个发送人的真实姓名 → 导出结构化 JSON。不含禅道 / git / 周报渲染。

任何人都能用：凭证从 `config.json` 读取（每人填自己的 `o_id`），不绑定特定账号、不预设特定群。

## 工具位置
脚本目录：`~/.claude/skills/fetch-yzj-group-messages/scripts/`
- `fetch_chat.py` —— 主脚本
- `config.example.json` —— 配置模板（随 skill 分发，不含个人凭证）
- `config.json` —— 实际配置（自行创建，含个人 o_id，勿提交）

## 何时用这个 vs gen-weekly-report
- ✅ 本 skill：只要群消息 / 聊天记录 / 发送人解析 / 导出 JSON（给任何人、任何群用）
- ❌ 不要用本 skill：要生成日历会议小组周报（任务/Bug/git/HTML 渲染）→ 用 `gen-weekly-report`

## 步骤
1. **首次配置**（每个使用者一次性）：
   ```
   cd ~/.claude/skills/fetch-yzj-group-messages/scripts
   cp config.example.json config.json
   # 编辑 config.json，填入 o_id（必填）。appkey/signature 通常保持默认即可
   ```
2. **找目标群 groupId**：
   ```
   python3 fetch_chat.py groups          # 列内部群
   python3 fetch_chat.py groups 外部      # 列外部群
   ```
   从输出里 `groupId  群名` 找到目标群。
3. **拉取并导出**：
   ```
   python3 fetch_chat.py fetch <groupId> 2026-07-06 2026-07-10
   ```
   → 生成同目录 `messages_<群名>_<start>_<end>.json`。
4. **读 JSON**：`total_messages` / `senders{userId→姓名}` / `messages[]`（每条含 `time`/`sender`/`content`）。

## 命令速查
| 命令 | 作用 |
|------|------|
| `token` | 验证凭证、打印 openToken |
| `groups [内部\|外部]` | 列出可访问的群（找 groupId） |
| `fetch <gid> <start> <end>` | 拉消息 + 解析发送人 + **导出 JSON** |
| `msgs <gid> <start> <end>` | 同 fetch 但仅打印到屏幕 |
| `userinfo <userId>` | 查单个发送人姓名/部门/职位 |

日期格式 `YYYY-MM-DD`。

## 输出 JSON 结构
```json
{
  "group": {"groupId": "...", "groupName": "..."},
  "period": {"start": "2026-07-06", "end": "2026-07-10"},
  "fetched_at": "2026-07-13 ...",
  "total_messages": 87,
  "senders": {"<userId>": {"name": "姓名", "department": "...", "jobTitle": "..."}},
  "messages": [{"time": "...", "fromUserId": "...", "sender": "姓名", "msgType": 2, "content": "..."}]
}
```

## 常见坑
- **`o_id` 决定能访问哪些群**：openToken 是个人身份，你不在的群拉不到。换人用必须先改 `config.json` 里的 `o_id`。
- **appkey/signature 通常通用**：默认是云之家讯通开放应用凭证，整个应用通用；换了独立开放应用才需要改。若 `token` 命令报 `get_open_token 失败`，先核对 signature 是否匹配你的开放应用。
- **外部群发送人**：`fromUserId` 以 `_ext` 结尾，`userinfo` 接口原样使用即可。
- **时间窗口按 `sendTime` 过滤**：翻页用每批最早消息的 msgId 作游标向前回溯，到窗口起点停止。
- **消息量上限**：默认 `count=50 × max_pages=80 ≈ 4000` 条。超大群、超长周期可在 `fetch_chat.py` 里调大 `max_pages`。
- **`userInfo` 接口认证是通用服务账号**（已内置 `USER_INFO_AUTH`），与个人 openToken 无关；解析姓名失败多为该 userId 非本租户人员。

## 与 gen-weekly-report 的关系
本 skill 的 `fetch_chat.py` 是 `docs/周报/scripts/yzj_chat.py` 的通用化精简版：去掉硬编码凭证与「日历-小群」默认群，凭证改读 `config.json`，新增 `fetch` 命令导出 JSON。需要周报全套（群消息 + 禅道 + git + HTML 渲染）仍用 `gen-weekly-report`。
