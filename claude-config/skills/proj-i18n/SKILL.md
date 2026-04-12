---
name: proj-i18n
description: Spring 后端全球化(国际化)支持。用于搭建多语言系统、配置资源包、实现消息国际化、支持多地区语言。
---

# Spring 后端全球化支持

## 架构设计

### 核心概念

| 概念 | 说明 | 示例 |
|------|------|------|
| Locale | 语言地区标识 | zh_CN、en_US |
| MessageSource | Spring 资源包加载机制 | ResourceBundleMessageSource |
| ResourceBundle | Java 标准资源包 | message.properties |
| Key | 资源包中的唯一标识 | UserErrorNotFound |

---

## 实现方案

| 方案 | 适用场景 | 特点 | 参考模板 |
|------|---------|------|----------|
| MessageSource + I18n | 标准多语言需求 | Spring 内置，自动生成方法，静态调用 | [配置模板](templates/message-source-config.md) |
| 异步场景支持 | @Async 异步调用 | TaskDecorator 自动传递上下文 | [配置模板](templates/message-source-config.md) |

---

## 技术框架

| 技术 | 用途 |
|------|------|
| Spring MessageSource | 资源包管理 |
| Java Locale | 地区标识 |
| Properties 文件 | 资源存储（UTF-8） |
| AcceptHeaderLocaleResolver | 从请求头识别语言 |
| LocaleContextHolder | 线程隔离的 Locale 存储 |

---

## 资源包规范

### 目录结构

```
src/main/resources/
└── i18n/
    ├── message.properties           # 默认资源（英文）
    ├── message_zh_CN.properties     # 简体中文
    └── message_zh_TW.properties     # 繁体中文
```

### 文件命名规则

**格式：** `{baseName}[_{language}][_{country}].properties`

| 示例 | 说明 |
|------|------|
| message.properties | 默认资源 |
| message_zh_CN.properties | 简体中文-中国 |
| message_zh_TW.properties | 繁体中文-台湾 |

### Key 定义规范

**格式：** 帕斯卡命名（PascalCase），前缀模块名 + 具体含义

```
{模块名}{业务}{动作/状态}
```

- **首字母大写**：使用帕斯卡命名
- **模块前缀**：以模块名开头（如 User、Order、Common）
- **语义清晰**：见名知意

**示例：**
- `CommonSuccess` - 通用成功消息
- `UserErrorNotFound` - 用户不存在
- `OrderPaymentTimeout` - 支付超时
- `UserCreateSuccess` - 用户创建成功
- `ValidationErrorRequired` - 校验必填

### Properties 文件格式

```properties
# 普通文本（默认英文）
CommonSuccess=Operation successful

# 格式化替换（参数占位符）
UserCount={0} user(s)

# 含有单引号（使用两个单引号转义）
ValidationErrorRequired=Field ''{0}'' is required
```

---

## 配置规范

### Java 配置类

完整配置（MessageSource、Locale 解析、拦截器）见：[MessageSource 配置模板](templates/message-source-config.md)

---

## 支持语言清单

| 语言 | Locale 标识 | 文件名 |
|------|-----------|--------|
| 英文 | - | message.properties（默认） |
| 简体中文 | zh_CN | message_zh_CN.properties |
| 繁体中文 | zh_TW | message_zh_TW.properties |

**注意：** 添加新消息时，必须同时添加到所有语言文件中。

---

## 使用方式

### I18n 类自动生成

`I18n.java` 通过 Gradle 任务自动生成，每个 key 生成无参和带参两个方法：

```java
// 无参消息
I18n.commonSuccess();           // "Operation successful"

// 带参数消息
I18n.validationErrorAgeInvalid(18, 100);   // "Age must be between 18 and 100"
```

### 生成步骤

1. 在 `message.properties` 中添加新的 key
2. 运行 `.\gradlew.bat generateI18n` 自动生成方法
3. 编译前会自动执行（`compileJava.dependsOn generateI18n`）

完整的 Gradle 任务模板见：[MessageSource 配置模板 - I18n 类自动生成](templates/message-source-config.md#i18n-类自动生成)

---

## 关键实现细节

### 1. AcceptHeaderLocaleResolver

从 HTTP 请求头的 `Accept-Language` 识别客户端语言，无需额外配置。

### 2. LocaleContextHolder

使用 Spring 的 `LocaleContextHolder` 存储 Locale，基于 ThreadLocal 实现线程隔离。

### 3. 异步场景处理

使用 `TaskDecorator` 自动在主线程和子线程间传递 Locale，无需手动传递。

### 4. I18n 类设计

每个 key 自动生成无参和带参两个静态方法，通过内部 `Holder` 类访问 Spring Bean，避免静态注入。

---

## 注意事项

### 资源包配置

- 同一资源包的所有文件必须在同一目录
- 多个资源包按配置顺序查找，前面的优先
- 避免 key 重复
- 默认资源为英文，其他语言按需添加

### 性能考虑

- 设置合理的缓存时间（`setCacheSeconds`）
- 避免在循环中频繁调用 getMessage

### 异步场景

- 使用 `@Async` 时需配置 `TaskDecorator` 自动传递上下文
- 自定义线程池也需设置 `TaskDecorator`

---

## 常见问题

### Q: 如何支持更多语言？

A: 在 `i18n/` 目录下创建对应 Locale 的 properties 文件，参考：[资源包模板](templates/resource-bundle.md)

### Q: 消息显示的是 key 而不是翻译内容？

A: 检查资源包路径配置、key 是否存在，参考：[MessageSource 配置 - 常见问题](templates/message-source-config.md#常见问题排查)

### Q: 异步调用时无法获取正确的语言？

A: 配置 `TaskDecorator` 自动传递上下文，参考：[MessageSource 配置 - 常见问题 Q2](templates/message-source-config.md#q2-异步调用时消息获取失败)

---

## 模板文件

| 模板 | 内容 |
|------|------|
| [message-source-config.md](templates/message-source-config.md) | MessageSource 配置、I18n 类自动生成、使用示例、TaskDecorator、常见问题排查 |
| [resource-bundle.md](templates/resource-bundle.md) | Key 设计规范、资源包模板（英文/简中/繁中）、单复数处理 |

---

## 同步任务文档

- 产物清单记录全球化配置文件路径和资源包位置
- 记录支持的语言清单和 Locale 映射
- 流程状态总览标记"全球化支持"为已完成
- 更新下一步指令为"测试多语言功能"

---

## 相关资源

- [Spring MessageSource 文档](https://docs.spring.io/spring-framework/reference/features/i18n.html)
- [Java Locale 文档](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html)
- [Properties 文件格式](https://docs.oracle.com/javase/tutorial/i18n/resbundle/propfile.html)
