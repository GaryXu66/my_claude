---
name: gen-weekly-report
description: Use when generating 徐衡的「AI原生日历会议小组」周报 —— 拉取禅道任务/Bug 和云之家「日历-小群」群消息后渲染 HTML 周报。触发：用户说"生成周报""周报""日历会议小组周报"，或要统计某日期范围的小组工作产出。
---

# 生成日历会议小组周报

## 概述
为徐衡的「AI原生日历会议小组」生成周报。数据来自两处：
- **禅道 MCP**（任务/Bug/动态）—— JSON-RPC over HTTP
- **云之家「日历-小群」群消息**（成员提交的周报原文）—— 主要内容来源

**机械数据采集已脚本化**（`collect_weekly.py` 一键出结构化 JSON）；**判断性内容**（概括/亮点/客户关联/下周P0P1）由你基于采集结果 + 群周报原文撰写——这部分无法自动化。

## 关键事实（复用，不要重新猜）
- 工具链目录：`/data/home/heng_xu/work/program/idea_workhome/docs/周报/scripts/`
- 禅道 MCP：`http://mcp.client.yzjop.com/mcp/zentao/stream`（注意是 HTTP JSON-RPC，不是 SSE）
- 主数据源群：「日历-小群」`groupId=6a327781e4b05fbbe5356aad`（仅本组成员、6/17 起）
- 花名册/账号映射：`team.json` + `account_map.json`（11/11 人禅道账号已全部定位；杨俊艺 2026-07-03、张姝 2026-07-20 已离职移出小组，不再统计）
- 基线/示例报告（含完整 CSS 与结构）：`docs/周报/AI原生日历会议小组-周报-20260615至20260624.html`
- 渲染模板：`docs/周报/scripts/report_template.html`
- 补充说明文档模板：`docs/周报/scripts/report_supplementary_template.html`
- 输出目录：`docs/周报/`，命名 `<小组名>-周报-<start>至<end>.html`；补充说明文档命名 `<小组名>-周报补充说明-<start>至<end>.html`

## 步骤
1. **采集**（生成 `report_data_<start>_<end>.json`）：
   ```
   cd /data/home/heng_xu/work/program/idea_workhome/docs/周报/scripts
   python3 collect_weekly.py --start 2026-06-22 --end 2026-06-28
   ```
   collect_weekly.py 内部会：取 openToken + 拉群消息 + 拉禅道数据 + **git fetch 各工程到最新并统计提交**（8 个已 clone 工程）。`--no-git` 可跳过代码产出。
2. **读 report_data JSON**，关注：
   - `summary` —— 统计卡片数字（done_tasks / resolved_bugs / closed_bugs / opened / active_tasks / unresolved_bugs_assigned / accounts_located）
   - `members.<姓名>` —— 每人 done/active 任务、resolved/closed/opened/active bug
   - `chat.weekly_report_candidates` —— 各成员周报原文（撰写叙述的依据）
   - `resolved_bugs_detail` / `closed_bugs_detail` / `active_bugs_detail` —— 带 id/title/severity/openedBy 的明细
   - `git.per_member` / `git.per_project` —— 每人/每工程的 commits/insertions/deletions/files/churn_ratio/recent_subjects
3. **拉取需求/bug 详情以提取客户信息**（本周交付所需）：
   - 对本周已完成的任务和已解决的 bug，逐一拉取详情：`python3 zentao.py bug <bugId>`、`python3 zentao.py task <taskId>`（或用 MCP 直接查）
   - 重点关注：**需求描述/备注中的客户名称**、**关联的"用户需求"所关联的客户**、**bug 标题或描述中提到的客户**
   - 客户信息提取后，在"本周交付"中按需求维度归类，**能提取到客户信息的着重标注客户名称**
4. **渲染周报**（`report_template.html` 为基线），填入：
   - 统计卡片 + Bug/任务明细表（数据全部取自 report_data，Bug 链接 `https://pms.kdweibo.cn:60443/zentao/bug-view-{id}.html`，任务 `task-view-{id}.html`）
   - **周报概括**：① 本周关键交付摘要 ② 跨组依赖 ③ 客户反馈 ④ 下周P0/P1 ⑤ 建议 —— 基于 `chat.weekly_report_candidates` + `summary` 撰写
   - **① 本周交付（禅道需求维度）**：按需求/功能模块归类，每条交付注明关联客户（如有）。格式示例：
     - `【客户：XX集团】日历共享权限优化（#1234, #5678）—— 张三`
     - `【客户：YY科技】会议重复创建问题修复（#bug-9012）—— 李四`
     - 无客户关联的交付按模块归类正常列出
   - ② 跨组依赖 ③ Bug进展明细 ④ 新增/未解决Bug ⑤ 下周P0/P1 ⑥ 群消息补充
   - **【评价原则】亮点/组员状态以"实际交付产出"为准**（功能上线、架构/组件落地、客户阻塞问题解决、需求推进、代码提交），**不要把 bug 解决数量当唯一或主要标准**。bug/commits 数只是佐证。禅道漏录但 git 有提交的（如吴洲峰），应按实际代码产出认可其贡献。
5. **渲染补充说明文档**（`report_supplementary_template.html` 为基线），将以下三部分填入：
   - **一、未达成与原因**：禅道零关闭/低活跃成员、外部阻塞（原周报②的数据）
   - **二、组员状态**：🌟 亮点（highlight-card）+ ⚠ 需要关注（warn-card）+ 📋 当前在手活跃任务表（原周报③的数据）
   - **三、代码产出与质量（git 维度）**：每人 commits/+行/-行/文件/工程/churn 表 + 效率与质量观察（原周报⑧的数据）
6. 另存到 `docs/周报/`：周报主文件和补充说明文档各一份。

## 常见坑（必读）
- **已关闭 bug 会漏查**：bug 解决后 status 变 `closed`。查 `resolvedBy` 必须 `status=all` 再按 `resolvedDate` 过滤，否则漏掉"本周解决且已关闭"的 bug。脚本已处理，手工查注意。
- **账号格式不规则**：武超=`chao_sw_wu`(带 infix)、孔维辰曦=`chenxi_kw`、吴洲峰=`zhoufeng_wu`。新增成员先查 `account_map.json`；没命中用 `python3 zentao.py actions <候选account>` 探测，再无命中用云之家 `fullPinyin` 变体。**注意：`user_actions` 返回 0 条不代表账号不存在**——可能是该人近期无动态(如吴洲峰曾被误判)，应用 `bugs`/`tasks` 命令二次确认或直接问用户。
- **人名匹配口径**：禅道 MCP 只返回拼音 account，**不**返回"武超-后端"这类带职位的真实姓名——所以匹配按 account 做；聊天侧姓名用 `yzj_chat.py userinfo <userId>` 权威解析。
- **未解决 bug 计数**可能含产品岗收集的需求 bug，写报告时区分"开发 bug"与"产品/需求 bug"。
- **群 6/17 才建立**：早于 6/17 的数据靠成员周报回顾 + 禅道记录补全。
- **数字必须可追溯**：报告里每个 bug/任务号/commits 都来自 report_data.json，**不得编造**。某项无数据就如实标"数据待补充"。
- **禅道≠git，必须交叉看**：禅道任务/Bug 漏录很常见（前端不关任务、后端不录禅道），判断产出要结合 git 提交。例：吴洲峰禅道 0 产出但 git 本周 23 commits 跨 4 工程。代码产出维度见补充说明文档。git 用 `fetch`（非 pull，避免工作分支冲突）；提交人按邮箱前缀映射 account_map，**密码已在 credential.helper=store 缓存，脚本里不要写密码**。
- **客户信息提取**：禅道需求描述/备注中的客户名称可能写法不一（简称/全称/行业），提取时尽量统一。若任务/bug 详情中无客户信息，不要编造，标注"通用优化"即可。

## 工具速查（手工排查用）
```
python3 zentao.py actions <account> [days]      # 查某人的禅道动态
python3 zentao.py bugs <account> [role] [status] [days]
python3 zentao.py tasks <account> [active|done] [days]
python3 zentao.py bug <bugId>                    # 查 bug 详情（提取客户信息）
python3 zentao.py task <taskId>                  # 查 task 详情（提取客户信息）
python3 yzj_chat.py token                       # 取 openToken
python3 yzj_chat.py msgs [groupId] [start] [end]
python3 yzj_chat.py userinfo <userId>           # 查发送人真实姓名
python3 yzj_chat.py resolve-msgs [groupId] [start] [end]
python3 git_stats.py fetch                      # 更新所有工程到最新(fetch)
python3 git_stats.py stats [start] [end]        # 提交统计
python3 git_stats.py all [start] [end]          # fetch+统计→json
```

## 小组成员（11 人）
武超(后端)、展会荣(测试)、林健宁(前端)、谭智文(后端)、刘飞洋(后端)、张艺琼(前端)、申明辉(前端)、李一萍(前端)、孔维辰曦(交互UI设计)、刘振兴(后端)、吴洲峰(后端)。组长徐衡。

**杨俊艺**（前端）已于 2026-07-03 离职、**张姝**（产品）已于 2026-07-20 离职，均已从花名册/账号映射中移除，后续周报不再统计。

## 输出结构总览

### 周报主文件（对外）
精简版，聚焦交付产出和客户价值：
- 周报概括（关键交付摘要 / 跨组依赖 / 客户反馈 / 下周P0P1 / 建议）
- 统计卡片
- ① 本周交付（**禅道需求维度**，突出客户关联）
- ② 跨组依赖
- ③ Bug进展明细
- ④ 新增/未解决Bug
- ⑤ 下周P0/P1
- 群消息补充

### 补充说明文档（内部参考）
管理细节，单独输出：
- 一、未达成与原因
- 二、组员状态（亮点 / 需关注 / 在手活跃任务）
- 三、代码产出与质量（git 维度）
