---
name: gen-weekly-report
description: Use when generating 徐衡的「AI原生日历会议小组」周报 —— 拉取禅道任务/Bug 和云之家「日历-小群」群消息后渲染 HTML 周报。触发：用户说"生成周报""周报""日历会议小组周报"，或要统计某日期范围的小组工作产出。
---

# 生成日历会议小组周报

## 概述
为徐衡的「AI原生日历会议小组」生成周报。数据来自两处：
- **禅道 MCP**（任务/Bug/动态）—— JSON-RPC over HTTP
- **云之家「日历-小群」群消息**（成员提交的周报原文）—— 主要内容来源

**机械数据采集已脚本化**（`collect_weekly.py` 一键出结构化 JSON）；**判断性内容**（概括/亮点/未达成/下周P0P1）由你基于采集结果 + 群周报原文撰写——这部分无法自动化。

## 关键事实（复用，不要重新猜）
- 工具链目录：`/data/home/heng_xu/work/program/idea_workhome/docs/周报/scripts/`
- 禅道 MCP：`http://mcp.client.yzjop.com/mcp/zentao/stream`（注意是 HTTP JSON-RPC，不是 SSE）
- 主数据源群：「日历-小群」`groupId=6a327781e4b05fbbe5356aad`（仅本组成员、6/17 起）
- 花名册/账号映射：`team.json` + `account_map.json`（12/13 人禅道账号已定位；吴洲峰未定位）
- 基线/示例报告（含完整 CSS 与结构）：`docs/周报/AI原生日历会议小组-周报-20260615至20260624.html`
- 渲染模板：`docs/周报/scripts/report_template.html`
- 输出目录：`docs/周报/`，命名 `<小组名>-周报-<start>至<end>.html`

## 步骤
1. **采集**（生成 `report_data_<start>_<end>.json`）：
   ```
   cd /data/home/heng_xu/work/program/idea_workhome/docs/周报/scripts
   python3 collect_weekly.py --start 2026-06-22 --end 2026-06-28
   ```
   （日期范围用户指定，未指定则问；默认到"今天"。）
2. **读 report_data JSON**，关注：
   - `summary` —— 统计卡片数字（done_tasks / resolved_bugs / closed_bugs / opened / active_tasks / unresolved_bugs_assigned / accounts_located）
   - `members.<姓名>` —— 每人 done/active 任务、resolved/closed/opened/active bug
   - `chat.weekly_report_candidates` —— 各成员周报原文（撰写叙述的依据）
   - `resolved_bugs_detail` / `closed_bugs_detail` / `active_bugs_detail` —— 带 id/title/severity/openedBy 的明细
3. **渲染**：拷贝 `report_template.html`（或最近一期报告）作基线，填入：
   - 统计卡片 + Bug/任务明细表（数据全部取自 report_data，Bug 链接 `https://pms.kdweibo.cn:60443/zentao/bug-view-{id}.html`，任务 `task-view-{id}.html`）
   - 概括①-⑦、亮点/需关注、下周 P0/P1 —— 基于 `chat.weekly_report_candidates` + `summary` 撰写
4. 顶部"数据说明"块：更新统计周期、账号定位情况、人名匹配口径。
5. 另存到 `docs/周报/`。

## 常见坑（必读）
- **已关闭 bug 会漏查**：bug 解决后 status 变 `closed`。查 `resolvedBy` 必须 `status=all` 再按 `resolvedDate` 过滤，否则漏掉"本周解决且已关闭"的 bug。脚本已处理，手工查注意。
- **账号格式不规则**：武超=`chao_sw_wu`(带 infix)、孔维辰曦=`chenxi_kw`、张姝=`sugar_zhang`(昵称)。新增成员先查 `account_map.json`；没命中用 `python3 zentao.py actions <候选account>` 探测，再无命中用云之家 `fullPinyin` 变体。
- **人名匹配口径**：禅道 MCP 只返回拼音 account，**不**返回"武超-后端"这类带职位的真实姓名——所以匹配按 account 做；聊天侧姓名用 `yzj_chat.py userinfo <userId>` 权威解析。
- **未解决 bug 计数**含产品岗(张姝)收集的需求 bug，写报告时区分"开发 bug"与"产品/需求 bug"。
- **群 6/17 才建立**：早于 6/17 的数据靠成员周报回顾 + 禅道记录补全。
- **数字必须可追溯**：报告里每个 bug/任务号都来自 report_data.json，**不得编造**。某项无数据就如实标"数据待补充"。

## 工具速查（手工排查用）
```
python3 zentao.py actions <account> [days]      # 查某人的禅道动态
python3 zentao.py bugs <account> [role] [status] [days]
python3 zentao.py tasks <account> [active|done] [days]
python3 zentao.py bug <bugId>
python3 yzj_chat.py token                       # 取 openToken
python3 yzj_chat.py msgs [groupId] [start] [end]
python3 yzj_chat.py userinfo <userId>           # 查发送人真实姓名
python3 yzj_chat.py resolve-msgs [groupId] [start] [end]
```

## 小组成员（13 人）
武超(后端)、展会荣(测试)、林健宁(前端)、张姝(产品)、谭智文(后端)、刘飞洋(后端)、张艺琼(前端)、申明辉(前端)、李一萍(前端)、孔维辰曦(交互UI设计)、杨俊艺(前端)、刘振兴(后端)、吴洲峰(后端)。组长徐衡。
