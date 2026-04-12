# Claude Code Config Sync

自动同步 Claude Code 配置到 GitHub，实现多机同步。

## 同步内容

- `idea_workhome/` - AI 生成的 .md 文件
- `claude-config/`
  - `settings.json` - Claude 设置（自动移除敏感 token）
  - `skills/` - 自定义技能
  - `agents/` - 自定义 agents
  - `projects/` - 项目级 CLAUDE.md 配置

## 新电脑使用方法

```bash
# 1. 克隆仓库
git clone git@github.com:GaryXu66/my_claude.git
cd my_claude

# 2. 运行恢复脚本
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

## 注意事项

- **敏感信息不会上传**：API Token 需要在每台机器单独设置
- **项目路径不同**：projects 目录只同步 CLAUDE.md，路径差异不影响使用