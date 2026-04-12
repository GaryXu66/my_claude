---
name: proj-common
description: 查看公共类规范和使用方式。包括Result响应类、错误码管理、异常处理、国际化、事务、缓存、并发控制、日志等。
---

# 公共类与通用规范

> 面向国际化、多模块微服务的公共类规范

## 任务文档同步

- 如引用本规范中的限制或约束，将关键约束记录到任务文档"上下文快照"

---

## 目录

1. [响应类](#1-响应类)
2. [错误码管理](#2-错误码管理)
3. [异常处理](#3-异常处理)
4. [国际化配置](#4-国际化配置)
5. [事务规范](#5-事务规范)
6. [缓存规范](#6-缓存规范)
7. [并发控制](#7-并发控制)
8. [日志规范](#8-日志规范)
9. [常量 vs 配置](#9-常量-vs-配置)
10. [阿里规范要点](#10-阿里规范要点)

---

## 1. 响应类

### 1.1 Result 统一响应

```java
@Data
public class Result<T> {
    private String code;      // 错误码
    private String message;   // 国际化消息
    private T data;           // 响应数据
    private Long timestamp;   // 时间戳
}
```

### 1.2 快速使用

```java
// 成功响应
return Result.success();
return Result.success(data);

// 失败响应
return Result.fail("10-01-001", "用户不存在");
return Result.fail(UserErrorCode.USER_NOT_FOUND);
```

**模板文件**：`/proj-common response`

---

## 2. 错误码管理

### 2.1 错误码格式

```
{服务码2位}-{模块码2位}-{具体码3位}

示例：10-01-001
│  │  │
│  │  └─ 具体错误 (001-999)
│  └──── 模块码 (01-99)
└─────── 服务码 (10-99)
```

### 2.2 服务码分配

| 服务码 | 服务名称 |
|-------|---------|
| 00 | 公共模块 |
| 10 | 用户服务 |
| 20 | 订单服务 |
| 30 | 商品服务 |
| 40 | 支付服务 |
| 50-89 | 其他业务服务 |
| 90-99 | 系统服务 |

### 2.3 ErrorCode 接口

```java
public interface ErrorCode {
    String getCode();                    // 错误码
    String getDefaultMessage();          // 默认消息(中文)
    HttpStatus getHttpStatus();          // HTTP状态
    default String getMessageKey() {     // 国际化key
        return "error." + getCode().replace("-", ".");
    }
}
```

### 2.4 使用方式

```java
// 枚举定义
public enum UserErrorCode implements ErrorCode {
    USER_NOT_FOUND("10-01-001", "用户不存在", HttpStatus.NOT_FOUND);
}

// 抛出异常
throw new BusinessException(UserErrorCode.USER_NOT_FOUND, userId);
```

**模板文件**：`/proj-common error-code`

---

## 3. 异常处理

### 3.1 异常层次

```
BaseException (抽象基类)
├── BusinessException (业务异常) - 可预期，不记录堆栈
├── SystemException (系统异常) - 需记录完整日志
└── WebException (Web层异常) - HTTP状态映射
```

### 3.2 快速使用

```java
// Service层 - 业务异常
throw UserModuleException.userNotFound(userId);

// Service层 - 系统异常
throw SystemException.externalServiceError("支付服务", cause);

// Controller层无需处理，GlobalExceptionHandler自动捕获
@GetMapping("/{id}")
public Result<User> get(@PathVariable Long id) {
    return Result.success(userService.getById(id));
}
```

### 3.3 模块异常示例

```java
// 用户模块异常
throw UserModuleException.userNotFound(userId);
throw UserModuleException.invalidCredentials();
throw UserModuleException.weakPassword();

// 订单模块异常
throw OrderModuleException.notFound(orderId);
throw OrderModuleException.insufficientStock(productId, stock, request);
```

**模板文件**：
- `/proj-common exception` - 异常处理完整文档
- `templates/exception-hierarchy.md` - 异常类结构
- `templates/global-exception-handler.md` - 全局异常处理器

---

## 4. 国际化配置

### 4.1 资源包结构

```
src/main/resources/i18n/
├── messages.properties           # 默认(中文)
├── messages_en.properties        # 英文
├── messages_zh_TW.properties     # 繁体
└── messages_ja.properties        # 日文
```

### 4.2 资源文件示例

```properties
# messages.properties
error.10.01.001=用户不存在: {0}
error.20.03.001=库存不足: 商品【{0}】库存{1}，需求{2}

# messages_en.properties
error.10.01.001=User not found: {0}
error.20.03.001=Insufficient stock: product【{0}】stock {1}, requested {2}
```

### 4.3 Locale 解析策略

| 优先级 | 来源 | 示例 |
|-------|------|------|
| 1 | 请求参数 `lang` | `?lang=en` |
| 2 | 请求头 `Accept-Language` | `Accept-Language: en-US` |
| 3 | Session | 之前选择的语言 |
| 4 | 默认 | 中文 |

### 4.4 前端请求示例

```javascript
// 方式1：请求头
fetch('/api/users/123', {
  headers: { 'Accept-Language': 'en-US' }
})

// 方式2：请求参数
fetch('/api/users/123?lang=en')
```

**相关命令**：
- `/proj-common i18n` - 异常国际化
- `/proj-i18n` - 完整国际化配置

---

## 5. 事务规范

### 5.1 使用场景

| 场景 | 是否需要事务 |
|------|-------------|
| 单表写操作 | 否（MyBatis-Plus 自动处理） |
| 多表写操作 | 是 |
| 先查后改 | 是（需保证一致性时） |
| 纯查询 | 否 |

### 5.2 标准用法

```java
// 写操作
@Transactional(rollbackFor = Exception.class)
public void bindUserRole(Long userId, List<Long> roleIds) {
    // 多表操作
}

// 只读事务
@Transactional(readOnly = true)
public UserDetailResponse getDetail(Long id) {
    // 多表查询需一致性
}
```

### 5.3 禁止事项

- 禁止在 Controller 层使用 `@Transactional`
- 禁止事务方法内调用同类的另一个事务方法（事务失效）
- 禁止事务内进行 RPC/HTTP 调用
- 禁止大事务（事务方法超过 20 行需拆分）

---

## 6. 缓存规范

### 6.1 Key 命名

```
{项目}:{模块}:{业务}:{标识}
```

示例：`demo:user:info:123`、`demo:order:detail:456`

### 6.2 过期时间

| 数据类型 | 过期时间 |
|----------|----------|
| 热点数据 | 1小时 |
| 普通数据 | 24小时 |
| 配置数据 | 7天 |
| 验证码 | 5分钟 |

### 6.3 缓存策略

```java
// 查询：先缓存后数据库
@Cacheable(value = "user", key = "#id")
public User getById(Long id) {
    return userMapper.selectById(id);
}

// 更新：先数据库后删缓存
@CacheEvict(value = "user", key = "#user.id")
public void update(User user) {
    userMapper.updateById(user);
}
```

### 6.4 防护措施

| 问题 | 解决方案 |
|------|----------|
| 缓存穿透 | 空值缓存或布隆过滤器 |
| 缓存击穿 | 分布式锁或永不过期+异步更新 |
| 缓存雪崩 | 过期时间加随机值 |

---

## 7. 并发控制

### 7.1 乐观锁（推荐）

```java
// Entity 添加版本字段
@Version
private Integer version;

// 更新时自动检查版本
userMapper.updateById(user);  // WHERE version = ?
```

适用：冲突概率低、读多写少

### 7.2 悲观锁

```java
@Select("SELECT * FROM user WHERE id = #{id} FOR UPDATE")
User selectForUpdate(Long id);
```

适用：冲突概率高、必须成功

### 7.3 分布式锁

```java
String lockKey = "order:lock:" + orderId;
boolean locked = redisTemplate.opsForValue()
    .setIfAbsent(lockKey, "1", 10, TimeUnit.SECONDS);

if (!locked) {
    throw BusinessException.tooManyRequests();
}

try {
    // 业务逻辑
} finally {
    redisTemplate.delete(lockKey);
}
```

---

## 8. 日志规范

### 8.1 日志级别

| 级别 | 使用场景 |
|-----|---------|
| ERROR | 系统异常、需要立即处理的问题 |
| WARN | 业务异常、可预期的问题 |
| INFO | 关键业务流程、状态变更 |
| DEBUG | 调试信息（生产环境关闭） |
| TRACE | 详细跟踪信息（生产环境关闭） |

### 8.2 日志格式

```java
// 业务异常 - WARN
log.warn("用户不存在: userId={}", userId);

// 系统异常 - ERROR + 堆栈
log.error("创建用户失败: request={}", request, e);

// 关键流程 - INFO
log.info("用户登录: username={}, ip={}", username, ip);
```

### 8.3 禁止事项

- 禁止在循环中打印日志
- 禁止打印敏感信息（密码、手机号、身份证）
- 禁止使用 `System.out.println`
- 禁止字符串拼接（使用占位符）

### 8.4 配置

```yaml
logging:
  level:
    root: INFO
    com.{company}: DEBUG
  pattern:
    console: "%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n"
```

---

## 9. 常量 vs 配置

### 9.1 设计原则

| 类型 | 使用场景 | 示例 |
|-----|---------|------|
| 常量类 | 永不变化的值 | π、HTTP状态码、状态 0/1 |
| 枚举 | 有限集合的状态值 | 订单状态、用户类型 |
| 配置文件 | 可能变化的值 | 超时时间、阈值、开关 |
| 配置中心 | 需要动态调整的值 | 限流阈值、功能开关 |

### 9.2 减少常量类，改用配置

**不推荐**：
```java
public class OrderConstants {
    public static final int TIMEOUT = 30;  // 硬编码
}
```

**推荐**：
```yaml
# application.yml
order:
  timeout: 30
  max-items: 100
```

```java
@ConfigurationProperties(prefix = "order")
@Data
public class OrderProperties {
    private int timeout;
    private int maxItems;
}
```

### 9.3 配置中心集成

```java
@NacosValue(value = "${order.timeout:30}", autoRefreshed = true)
private int timeout;

// 或使用
@RefreshScope
@ConfigurationProperties(prefix = "order")
public class OrderProperties {
    private int timeout;
}
```

---

## 10. 阿里规范要点

### 10.1 命名规范（强制）

| 规范 | 示例 |
|------|------|
| 类名使用 UpperCamelCase | `UserService` |
| 方法名使用 lowerCamelCase | `getUserById` |
| 常量名全部大写下划线 | `MAX_PAGE_SIZE` |
| 包名统一使用小写 | `com.example.demo.common` |

### 10.2 代码格式（强制）

| 规范 | 说明 |
|------|------|
| 缩进 | 采用4个空格 |
| 大括号 | 左括号前不换行 |
| 单行字符数 | 不超过120个 |
| 运算符 | 二元运算符左右加空格 |

### 10.3 集合处理（强制）

| 规范 | 说明 |
|------|------|
| 初始化指定容量 | `new ArrayList<>(100)` |
| 使用 Collections.isEmpty | 禁止 `size()==0` |
| 集合转数组 | `list.toArray(new String[0])` |

### 10.4 并发处理（强制）

| 规范 | 说明 |
|------|------|
| 线程池通过 ThreadPoolExecutor 创建 | 禁止使用 Executors |
| 使用 DateTimeFormatter | 禁止 SimpleDateFormat |
| 高并发使用 ConcurrentHashMap | 避免 HashMap 加锁 |

### 10.5 日志规范（强制）

| 规范 | 说明 |
|------|------|
| 使用 SLF4J 占位符 | `log.info("用户={}", user)` |
| 禁止打印敏感信息 | 密码、手机号需脱敏 |
| 区分日志级别 | ERROR-系统错误，WARN-潜在问题 |

---

## 快速使用

### 查看各模板

```
/proj-common response    # 查看响应类模板
/proj-common exception   # 查看异常处理模板
/proj-common error-code  # 查看错误码模板
/proj-common i18n        # 查看国际化模板
/proj-common transaction # 查看事务模板
/proj-common cache       # 查看缓存模板
/proj-common lock        # 查看并发控制模板
/proj-common log         # 查看日志模板
```

### 生成代码

使用 `/proj-gen` 生成代码时，会自动应用以上规范。
