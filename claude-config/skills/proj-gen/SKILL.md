---
name: proj-gen
description: 代码生成统一入口。生成 MongoDB CRUD、API、枚举等代码。
---

# 代码生成

> 统一入口，根据参数生成不同类型的代码。

## 生成规范
- 代码生成请请遵从阿里规约
- 可以引入Hutool工具辅助生成代码
## 注释规范

- 类、方法、字段使用 Javadoc `/** */`
- 类必须有 `@author` 和 `@since`
---

## RULE 0 (强制门禁): 前置检查

生成代码前必须确认以下条件全部满足，**任何一项不满足时禁止生成代码**：

1. ✅ 全流程任务文档已创建并可追溯
2. ✅ 技术方案已确认且路径已记录在产物清单
3. ✅ 任务清单已拆分并确认

**门禁触发时的处理**：
- 检测到前置条件不满足时，立即停止生成
- 明确告知用户缺少哪项前置条件
- 指导用户如何补充缺失的文档或确认流程

## RULE 1: 代码生成规范
- 代码生成必须遵从阿里规约
- 引入Hutool工具辅助生成代码

## RULE 2: 健壮性
- 所有创建的代码，其方法参数，返回值，字段 都需要明确标注 NotNull 或 Nullable (来自 org.jetbrains.annotations )
- 参数应优先不支持传入 null，返回值不返回 null, 除非常见的惯例使用
- 类，方法和字段的可访问性应遵循尽量不公开、少公开的原则
- 字段尽可能设计成 final,减少复杂度
- 尽力避免静态方法，除非使用实例方法反而增加了复杂度

## 自动模式

当存在技术方案文档时，执行以下步骤：

1. **先分析上下文**（Before 生成代码）：
   - 读取任务文档中的产物清单，找到技术方案文档路径
   - 阅读技术方案文档，提取表结构、字段类型、接口定义
   - 检查项目中是否已有类似的实体或服务，分析命名和代码风格
   - 确认项目使用的技术栈版本（Java 8 + Spring Boot 1.5.22.RELEASE + MongoDb）

2. **再生成代码**（Then 生成代码）：
   - 根据分析结果，生成符合项目风格的代码
   - 确保导入的类和版本与现有代码一致
   - 遵循项目现有的命名规范和代码结构

**触发时机**：任务拆分完成后，开始编码前。

**注意**：自动模式生成的是代码骨架，业务逻辑仍需手动实现。

## 模板文件

### 标准模板（MongoDB + Spring Data MongoDB）

| 模板 | 文件 | 说明 |
|------|------|------|
| Domain | [domain.md](templates/domain.md) | 领域模型 |
| DAO | [dao.md](templates/dao.md) | 数据访问层 |
| Service | [service.md](templates/service.md) | 业务逻辑层 |
| Controller | [controller.md](templates/controller.md) | 接口层 |
| DTO | [dto.md](templates/dto.md) | 请求响应对象（含 QueryRequest、Response） |
| 枚举 | [enum.md](templates/enum.md) | 枚举定义 |
| Config | [config.md](templates/config.md) | 配置类（MongoDB、Redis、安全等） |
| SQL 建表 | [sql-reference.md](templates/sql-reference.md) | 字段类型、索引规范 |

## 使用方式

### 标准生成（推荐）
```bash
/proj-gen domain       - 生成 Domain 类
/proj-gen dao          - 生成 DAO 接口 + 实现
/proj-gen dto          - 生成所有 DTO (Create/Update/Query/Response)
/proj-gen service      - 生成 Service 接口 + 实现
/proj-gen controller   - 生成 Controller (Web + App)
/proj-gen enum         - 生成枚举类
/proj-gen config       - 生成配置类（MongoDB、Redis、安全等）
/proj-gen crud         - 生成完整 CRUD 代码（Domain + DAO + Service + Controller + DTO）
/proj-gen              - 自动模式（读取技术方案文档，智能生成）
```

### 生成顺序建议
```
1. domain → dao → dto → service → controller
2. 或使用 /proj-gen crud 一次性生成
```
## 自检清单（生成后验证）

代码生成完成后，**在返回代码前**，进行以下验证：

<self_verification>
对生成的每个文件，逐一回答以下问题：

1. **命名验证**：类名、方法名、变量名是否符合大驼峰/小驼峰规范？
2. **通用字段验证**：是否包含 id, delFlag, createBy, createTime, updateBy, updateTime？
3. **注解验证**：Controller方法是否有 @Operation？写操作是否有 @ApiLog？
4. **类型一致性验证**：ID类型在Controller层是Long，DAO层是String吗？
5. **枚举验证**：是否正确使用 StatusEnum？是否添加了空值检查？
6. **时间类型验证**：是否使用 LocalDateTime 而不是 Date？
7. **Hutool使用验证**：是否使用 ObjectUtil.isNotNull() 而不是 != null？

如果任何验证失败，修正代码后再返回。
</self_verification>

## 公共模块引用

```bash
/proj-common           # 查看公共类规范和使用方式
```

## 代码生成前参数验证

生成代码前，必须从用户输入中提取并验证以下参数：

<parameter_validation>
- 从用户的请求或对话上下文中提取：公司名、项目名、模块名
- 如果用户未提供，必须询问用户获取完整信息
- 验证参数格式：公司名和项目名必须是合法的包名格式（小写字母、数字、点）
- 验证集合名格式：必须是小写下划线格式（如：t_user_info）
- 验证实体名格式：必须是大驼峰格式（如：UserInfo）
- 验证描述：必须是中文，用于生成注释和文档
</parameter_validation>

<missing_parameter_handling>
如果缺少必需参数，按以下格式询问用户：
"请提供以下信息以生成代码：
- 公司名（com.example）
- 项目名（demo）
- 模块名（user）
- 作者名（Your Name）
- 集合名（t_user_info）
- 实体名（UserInfo）
- 描述（用户信息）
"
</missing_parameter_handling>

继续生成前确认：✅ 所有参数已提取并验证

## 代码生成后输出

代码生成完成后，**ONLY输出以下清单，不要添加任何额外对话或说明**：

<output_checklist>
- [ ] 文件路径列表（完整的包路径）
- [ ] 核心业务逻辑说明（创建/更新/删除/查询）
- [ ] 下一步操作（需手动实现、需配置内容、需创建索引）
</output_checklist>

❌ **禁止**：
- 不要说"代码已生成"或"生成完成"
- 不要说"请查看"或"祝您开发愉快"
- 不要添加任何额外说明

---

## Config 配置生成

使用 `/proj-gen config` 生成配置类，详见 [config.md](templates/config.md)