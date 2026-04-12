# Claude Code Config Sync

自动同步 Claude Code 配置到 GitHub，实现多机同步。

## 目录结构

```
my_claude/
├── README.md                    # 使用说明
├── sync-to-github.sh            # 源机器同步脚本
├── restore-claude-config.sh     # 新电脑恢复脚本
├── idea_workhome/               # AI 生成的 .md 文件
│   ├── CLAUDE.md
│   ├── CLAUDE_ANALYSIS_RESULTS.md
│   ├── java-projects-overview.md
│   └── ...
└── claude-config/               # Claude 配置
    ├── settings.json            # Claude 设置（已移除敏感 token）
    ├── skills/                  # 自定义技能
    │   ├── proj-gen/            # 代码生成
    │   ├── proj-review/         # 代码审查
    │   ├── proj-fix/            # 问题修复
    │   ├── proj-deploy/         # 部署相关
    │   ├── java-code-review     # 外部 skill (symlink)
    │   └── ...
    ├── agents/                  # 自定义 agents
    │   └── third-jar-researcher.md
    └── projects/                # 项目级 CLAUDE.md 配置
```

## 新电脑使用方法

```bash
# 1. 克隆仓库
git clone git@github.com:GaryXu66/my_claude.git
cd my_claude

# 2. 运行恢复脚本（会自动安装 skills）
chmod +x restore-claude-config.sh
./restore-claude-config.sh

# 3. 设置你的 API Token
claude config set ANTHROPIC_AUTH_TOKEN <your-token>
```

## 自动同步（源机器）

同步任务已在 OpenClaw 中配置，每小时自动执行。

手动触发：
```bash
~/.openclaw/workspace/sync-scripts/sync-md-to-github.sh
```

## 外部 Skills

以下 skills 通过 `npx skills` 安装，恢复脚本会自动处理：

| Skill | 说明 |
|-------|------|
| `java-code-review` | Java 代码审查（null safety, concurrency, performance） |

## 注意事项

- **敏感信息不会上传**：API Token 需要在每台机器单独设置
- **项目路径不同**：projects 目录只同步 CLAUDE.md，路径差异不影响使用
- **外部 skills 自动安装**：恢复脚本会通过 `npx skills add` 安装