# Java 微服务项目 - Claude Code 分析整理报告

> 分析工具：Claude Code（本地调用）
> 整理时间：2026-03-26
> 项目根目录：`/home/heng_xu/work/program/idea_workhome`

---

## 📁 架构说明

**架构模式**: 独立工程集合（无根 POM / 无父子模块关系）

- 每个项目都是独立 Maven 工程，拥有独立 `pom.xml`
- 项目间通过依赖引用关联，无构建层面的父子关系
- 按业务域单独构建、部署

---

## 📊 分析状态

| 状态 | 数量 | 说明 |
|------|------|------|
| ✅ 已完成 | 0 | Claude Code 分析完成 |
| ⏳ 进行中 | 0 | 正在分析 |
| ⏸️ 待分析 | 198 | 等待 Claude Code 处理 |

---

## 📋 项目分析详情

> 每个项目包含：业务定位、核心功能、技术栈、代码规模、核心业务逻辑（200-300 字）

<!-- Claude Code 分析结果将整理至此 -->

---

## 🔄 使用说明

### 调用 Claude Code 分析单个项目

```bash
cd /home/heng_xu/work/program/idea_workhome/{项目名}
claude "请分析这个 Java 项目的核心业务逻辑，输出 200-300 字业务描述" --permission-mode bypassPermissions --print
```

### 批量分析（推荐分批进行）

```bash
# 分析前 10 个项目
for proj in $(ls -d */ | head -10); do
    cd "/home/heng_xu/work/program/idea_workhome/$proj"
    echo "### 分析：$proj" >> ANALYSIS_RESULTS.md
    claude "分析核心业务逻辑，200-300 字" --permission-mode bypassPermissions --print >> ANALYSIS_RESULTS.md
done
```

---

## 📝 输出格式模板

```markdown
### {项目名}

- **业务定位**: [一句话描述项目定位]
- **核心功能**: 
  - 功能 1
  - 功能 2
  - 功能 3
- **技术栈**: Spring Boot, MyBatis, Redis, MySQL 等
- **代码规模**: X 个 Controller, Y 个 Service, Z 个 Entity
- **核心业务逻辑**: 
  [200-300 字详细描述，包括：
   - 项目在企业架构中的角色
   - 主要业务流程
   - 关键功能实现
   - 与其他服务的协作关系]
```

---

*等待 Claude Code 分析完成后，将结果整理至此文档*
