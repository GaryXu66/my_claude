# ErrorCode 错误码

> 面向国际化、多模块微服务的错误码规范（语义化错误码）

---

## 一、设计原则

### 1.1 核心原则

| 原则 | 说明 |
|-----|------|
| **语义化** | 错误码使用包名/服务名/模块名，易于理解 |
| **国际化** | 错误码直接对应国际化资源文件的key |
| **模块化** | common包只定义接口/基类，各模块自行实现 |
| **可读性** | 一眼就能看出错误来源和类型 |
| **可扩展** | 新增模块/服务无需统一协调分配数字 |

### 1.2 错误码格式

```
{服务名}.{模块}.{具体错误}

示例：
user.not.found              # 用户服务-用户模块-用户不存在
order.stock.insufficient    # 订单服务-库存模块-库存不足
common.param.invalid        # 公共模块-参数模块-参数校验失败
payment.gateway.timeout     # 支付服务-网关模块-超时
```

**与数字格式对比：**

| 语义化格式 | 数字格式 | 可读性 |
|-----------|---------|-------|
| `user.not.found` | `10-01-001` | 一目了然 |
| `order.stock.insufficient` | `20-03-001` | 一目了然 |
| `payment.gateway.timeout` | `40-05-001` | 一目了然 |

---

## 二、common 包 - 只定义接口/基类

### 2.1 ErrorCode 接口（在 common 包）

```java
package com.{company}.{project}.common.exception;

import org.springframework.http.HttpStatus;

/**
 * 错误码接口
 * common包只定义接口，各模块自行实现
 */
public interface ErrorCode {

    /**
     * 获取错误码
     * 格式：{服务}.{模块}.{具体错误}
     * 示例：user.not.found
     */
    String getCode();

    /**
     * 获取默认消息（中文，当国际化资源不存在时使用）
     */
    String getDefaultMessage();

    /**
     * 获取国际化消息key
     * 默认与错误码一致
     */
    default String getMessageKey() {
        return getCode();
    }

    /**
     * 获取HTTP状态码
     */
    HttpStatus getHttpStatus();

    /**
     * 是否需要记录日志
     */
    default boolean needLog() {
        return false;
    }

    /**
     * 日志级别
     */
    default String getLogLevel() {
        return "WARN";
    }
}
```

### 2.2 BaseException 基类（在 common 包）

```java
package com.{company}.{project}.common.exception;

import lombok.Getter;
import org.springframework.http.HttpStatus;

/**
 * 异常基类
 * common包只定义基类，各模块继承实现
 */
@Getter
public abstract class BaseException extends RuntimeException {

    private final String code;
    private final String defaultMessage;
    private final Object[] args;
    private final HttpStatus httpStatus;

    protected BaseException(ErrorCode errorCode, Object[] args) {
        super(errorCode.getDefaultMessage());
        this.code = errorCode.getCode();
        this.defaultMessage = errorCode.getDefaultMessage();
        this.args = args;
        this.httpStatus = errorCode.getHttpStatus();
    }

    protected BaseException(String code, String defaultMessage, HttpStatus httpStatus, Object[] args) {
        super(defaultMessage);
        this.code = code;
        this.defaultMessage = defaultMessage;
        this.args = args;
        this.httpStatus = httpStatus;
    }
}
```

### 2.3 国际化配置（在 common 包）

```java
package com.{company}.{project}.common.config;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.MessageSource;
import org.springframework.context.support.ResourceBundleMessageSource;
import org.springframework.stereotype.Component;

import java.nio.charset.StandardCharsets;
import java.util.List;

/**
 * 国际化配置
 */
@Data
@Component
@ConfigurationProperties(prefix = "i18n")
public class I18nProperties {

    /**
     * 是否启用国际化
     */
    private boolean enabled = true;

    /**
     * 默认语言
     */
    private String defaultLocale = "zh_CN";

    /**
     * 支持的语言列表
     */
    private List<String> supportedLocales = List.of("zh_CN", "en_US");

    /**
     * 资源包基名
     */
    private String basename = "i18n/messages";

    /**
     * 缓存时间（秒）
     */
    private int cacheSeconds = 3600;

    /**
     * 编码
     */
    private String encoding = "UTF-8";
}

/**
 * MessageSource 配置
 */
@Configuration
@RequiredArgsConstructor
public class I18nConfig {

    private final I18nProperties i18nProperties;

    @Bean
    public MessageSource messageSource() {
        ResourceBundleMessageSource messageSource = new ResourceBundleMessageSource();

        // 资源包基名（支持多个，逗号分隔）
        messageSource.setBasenames(i18nProperties.getBasename().split(","));

        // 编码
        messageSource.setDefaultEncoding(i18nProperties.getEncoding());

        // 缓存时间
        messageSource.setCacheSeconds(i18nProperties.getCacheSeconds());

        // 始终使用消息格式化
        messageSource.setAlwaysUseMessageFormat(true);

        // 不回退到系统Locale
        messageSource.setFallbackToSystemLocale(false);

        return messageSource;
    }
}
```

### 2.4 国际化工具类（在 common 包）

```java
package com.{company}.{project}.common.util;

import com.{company}.{project}.common.exception.ErrorCode;
import lombok.RequiredArgsConstructor;
import org.springframework.context.MessageSource;
import org.springframework.context.i18n.LocaleContextHolder;
import org.springframework.stereotype.Component;

import java.util.Locale;

/**
 * 国际化消息工具类
 * common包提供工具，各模块使用
 */
@Component
@RequiredArgsConstructor
public class I18nMessageUtil {

    private final MessageSource messageSource;

    /**
     * 获取国际化消息
     */
    public String getMessage(ErrorCode code, Object... args) {
        return getMessage(code.getMessageKey(), code.getDefaultMessage(), args);
    }

    /**
     * 获取国际化消息
     */
    public String getMessage(String key, String defaultMessage, Object... args) {
        try {
            return messageSource.getMessage(key, args, defaultMessage, LocaleContextHolder.getLocale());
        } catch (Exception e) {
            return defaultMessage;
        }
    }

    /**
     * 获取指定语言的国际化消息
     */
    public String getMessage(String key, String defaultMessage, Locale locale, Object... args) {
        try {
            return messageSource.getMessage(key, args, defaultMessage, locale);
        } catch (Exception e) {
            return defaultMessage;
        }
    }
}
```

---

## 三、各模块自行实现

### 3.1 公共模块错误码

```java
package com.{company}.{project}.common.errorcode;

import com.{company}.{project}.common.exception.ErrorCode;
import lombok.AllArgsConstructor;
import lombok.Getter;
import org.springframework.http.HttpStatus;

/**
 * 公共模块错误码
 * 按功能分组：common.{模块}.{具体错误}
 */
@Getter
@AllArgsConstructor
public enum CommonErrorCode implements ErrorCode {

    // ========== 成功 ==========
    SUCCESS("common.success", "成功", HttpStatus.OK),

    // ========== 参数校验 ==========
    PARAM_INVALID("common.param.invalid", "参数校验失败", HttpStatus.BAD_REQUEST),
    PARAM_MISSING("common.param.missing", "缺少必要参数", HttpStatus.BAD_REQUEST),
    PARAM_TYPE_MISMATCH("common.param.type.mismatch", "参数类型错误", HttpStatus.BAD_REQUEST),
    PARAM_FORMAT_ERROR("common.param.format.error", "参数格式错误", HttpStatus.BAD_REQUEST),

    // ========== 权限 ==========
    UNAUTHORIZED("common.auth.unauthorized", "未登录", HttpStatus.UNAUTHORIZED),
    FORBIDDEN("common.auth.forbidden", "无权限访问", HttpStatus.FORBIDDEN),
    TOKEN_EXPIRED("common.auth.token.expired", "登录已过期", HttpStatus.UNAUTHORIZED),
    TOKEN_INVALID("common.auth.token.invalid", "Token无效", HttpStatus.UNAUTHORIZED),

    // ========== 资源 ==========
    RESOURCE_NOT_FOUND("common.resource.not.found", "资源不存在", HttpStatus.NOT_FOUND),
    RESOURCE_ALREADY_EXISTS("common.resource.already.exists", "资源已存在", HttpStatus.CONFLICT),

    // ========== 业务规则 ==========
    OPERATION_NOT_ALLOWED("common.operation.not.allowed", "当前状态不允许此操作", HttpStatus.CONFLICT),
    RATE_LIMIT_EXCEEDED("common.operation.rate.limit.exceeded", "操作过于频繁", HttpStatus.TOO_MANY_REQUESTS),

    // ========== 系统 ==========
    SYSTEM_ERROR("common.system.error", "系统错误", HttpStatus.INTERNAL_SERVER_ERROR),
    SERVICE_UNAVAILABLE("common.service.unavailable", "服务暂时不可用", HttpStatus.SERVICE_UNAVAILABLE),

    // ========== 外部服务 ==========
    EXTERNAL_SERVICE_ERROR("common.external.service.error", "外部服务调用失败", HttpStatus.BAD_GATEWAY),
    EXTERNAL_SERVICE_TIMEOUT("common.external.service.timeout", "外部服务调用超时", HttpStatus.GATEWAY_TIMEOUT);

    private final String code;
    private final String defaultMessage;
    private final HttpStatus httpStatus;
}
```

### 3.2 用户模块错误码

```java
package com.{company}.{project}.user.errorcode;

import com.{company}.{project}.common.exception.ErrorCode;
import lombok.AllArgsConstructor;
import lombok.Getter;
import org.springframework.http.HttpStatus;

/**
 * 用户模块错误码
 * 格式：user.{子模块}.{具体错误}
 */
@Getter
@AllArgsConstructor
public enum UserErrorCode implements ErrorCode {

    // ========== 用户管理 ==========
    USER_NOT_FOUND("user.not.found", "用户不存在", HttpStatus.NOT_FOUND),
    USER_ALREADY_EXISTS("user.already.exists", "用户已存在", HttpStatus.CONFLICT),
    USER_DISABLED("user.disabled", "用户已被禁用", HttpStatus.FORBIDDEN),
    USER_LOCKED("user.locked", "用户已被锁定", HttpStatus.FORBIDDEN),

    // ========== 认证 ==========
    INVALID_CREDENTIALS("user.auth.invalid.credentials", "用户名或密码错误", HttpStatus.UNAUTHORIZED),
    PASSWORD_EXPIRED("user.auth.password.expired", "密码已过期", HttpStatus.UNAUTHORIZED),
    PASSWORD_WEAK("user.auth.password.weak", "密码强度不足", HttpStatus.BAD_REQUEST),
    PASSWORD_SAME_AS_OLD("user.auth.password.same.as.old", "新密码不能与旧密码相同", HttpStatus.BAD_REQUEST),

    // ========== 验证码 ==========
    VERIFICATION_CODE_INVALID("user.verify.code.invalid", "验证码错误", HttpStatus.BAD_REQUEST),
    VERIFICATION_CODE_EXPIRED("user.verify.code.expired", "验证码已过期", HttpStatus.BAD_REQUEST),
    VERIFICATION_CODE_LIMIT("user.verify.code.limit", "验证码发送次数过多", HttpStatus.TOO_MANY_REQUESTS);

    private final String code;
    private final String defaultMessage;
    private final HttpStatus httpStatus;
}
```

### 3.3 订单模块错误码

```java
package com.{company}.{project}.order.errorcode;

import com.{company}.{project}.common.exception.ErrorCode;
import lombok.AllArgsConstructor;
import lombok.Getter;
import org.springframework.http.HttpStatus;

/**
 * 订单模块错误码
 */
@Getter
@AllArgsConstructor
public enum OrderErrorCode implements ErrorCode {

    // ========== 订单管理 ==========
    ORDER_NOT_FOUND("order.not.found", "订单不存在", HttpStatus.NOT_FOUND),
    ORDER_EXPIRED("order.expired", "订单已过期", HttpStatus.GONE),
    ORDER_ALREADY_PAID("order.already.paid", "订单已支付", HttpStatus.CONFLICT),
    ORDER_ALREADY_CANCELLED("order.already.cancelled", "订单已取消", HttpStatus.CONFLICT),

    // ========== 订单状态 ==========
    ORDER_STATUS_INVALID("order.status.invalid", "订单状态不合法", HttpStatus.BAD_REQUEST),
    ORDER_CANNOT_CANCEL("order.cancel.not.allowed", "当前状态无法取消订单", HttpStatus.CONFLICT),
    ORDER_CANNOT_PAY("order.pay.not.allowed", "当前状态无法支付", HttpStatus.CONFLICT),
    ORDER_CANNOT_REFUND("order.refund.not.allowed", "当前状态无法退款", HttpStatus.CONFLICT),

    // ========== 库存 ==========
    STOCK_INSUFFICIENT("order.stock.insufficient", "库存不足", HttpStatus.CONFLICT),
    STOCK_LOCK_FAILED("order.stock.lock.failed", "库存锁定失败", HttpStatus.INTERNAL_SERVER_ERROR),
    STOCK_RELEASE_FAILED("order.stock.release.failed", "库存释放失败", HttpStatus.INTERNAL_SERVER_ERROR);

    private final String code;
    private final String defaultMessage;
    private final HttpStatus httpStatus;
}
```

### 3.4 支付模块错误码

```java
package com.{company}.{project}.payment.errorcode;

import com.{company}.{project}.common.exception.ErrorCode;
import lombok.AllArgsConstructor;
import lombok.Getter;
import org.springframework.http.HttpStatus;

/**
 * 支付模块错误码
 */
@Getter
@AllArgsConstructor
public enum PaymentErrorCode implements ErrorCode {

    // ========== 支付订单 ==========
    PAYMENT_ORDER_NOT_FOUND("payment.order.not.found", "支付订单不存在", HttpStatus.NOT_FOUND),
    PAYMENT_AMOUNT_MISMATCH("payment.amount.mismatch", "支付金额不匹配", HttpStatus.BAD_REQUEST),
    PAYMENT_TIMEOUT("payment.timeout", "支付超时", HttpStatus.REQUEST_TIMEOUT),
    PAYMENT_FAILED("payment.failed", "支付失败", HttpStatus.BAD_GATEWAY),

    // ========== 退款 ==========
    REFUND_FAILED("payment.refund.failed", "退款失败", HttpStatus.BAD_GATEWAY),
    REFUND_AMOUNT_EXCEEDED("payment.refund.amount.exceeded", "退款金额超限", HttpStatus.BAD_REQUEST),
    REFUND_DEADLINE_PASSED("payment.refund.deadline.passed", "已超过退款期限", HttpStatus.BAD_REQUEST),

    // ========== 支付网关 ==========
    GATEWAY_ERROR("payment.gateway.error", "支付网关错误", HttpStatus.BAD_GATEWAY),
    GATEWAY_TIMEOUT("payment.gateway.timeout", "支付网关超时", HttpStatus.GATEWAY_TIMEOUT);

    private final String code;
    private final String defaultMessage;
    private final HttpStatus httpStatus;
}
```

---

## 四、国际化资源包

### 4.1 目录结构

```
src/main/resources/i18n/
├── messages.properties              # 默认(中文)
├── messages_en.properties           # 英文
└── messages_zh_TW.properties        # 繁体
```

### 4.2 messages.properties (中文)

```properties
# ========== 公共错误 ==========
common.success=成功

# 参数校验
common.param.invalid=参数校验失败
common.param.missing=缺少必要参数: {0}
common.param.type.mismatch=参数类型错误
common.param.format.error=参数格式错误

# 权限
common.auth.unauthorized=未登录，请先登录
common.auth.forbidden=无权限访问
common.auth.token.expired=登录已过期
common.auth.token.invalid=Token无效

# 资源
common.resource.not.found=资源不存在
common.resource.already.exists=资源已存在

# 业务规则
common.operation.not.allowed=当前状态不允许此操作
common.operation.rate.limit.exceeded=操作过于频繁

# 系统
common.system.error=系统错误，请稍后重试
common.service.unavailable=服务暂时不可用

# 外部服务
common.external.service.error=外部服务调用失败
common.external.service.timeout=外部服务调用超时

# ========== 用户服务 ==========
# 用户管理
user.not.found=用户不存在: {0}
user.already.exists=用户已存在: {0}
user.disabled=用户已被禁用
user.locked=用户已被锁定

# 认证
user.auth.invalid.credentials=用户名或密码错误
user.auth.password.expired=密码已过期
user.auth.password.weak=密码强度不足，至少8位，包含字母和数字
user.auth.password.same.as.old=新密码不能与旧密码相同

# 验证码
user.verify.code.invalid=验证码错误
user.verify.code.expired=验证码已过期
user.verify.code.limit=验证码发送次数过多，请{0}分钟后再试

# ========== 订单服务 ==========
# 订单管理
order.not.found=订单不存在: {0}
order.expired=订单已过期
order.already.paid=订单已支付
order.already.cancelled=订单已取消

# 订单状态
order.status.invalid=订单状态不合法
order.cancel.not.allowed=当前状态无法取消订单
order.pay.not.allowed=当前状态无法支付
order.refund.not.allowed=当前状态无法退款

# 库存
order.stock.insufficient=库存不足: 商品【{0}】库存{1}，需求{2}
order.stock.lock.failed=库存锁定失败
order.stock.release.failed=库存释放失败

# ========== 支付服务 ==========
# 支付订单
payment.order.not.found=支付订单不存在
payment.amount.mismatch=支付金额不匹配
payment.timeout=支付超时
payment.failed=支付失败

# 退款
payment.refund.failed=退款失败
payment.refund.amount.exceeded=退款金额超限
payment.refund.deadline.passed=已超过退款期限

# 支付网关
payment.gateway.error=支付网关错误
payment.gateway.timeout=支付网关超时
```

### 4.3 messages_en.properties (英文)

```properties
# ========== Common ==========
common.success=Success

# Parameter validation
common.param.invalid=Parameter validation failed
common.param.missing=Missing required parameter: {0}
common.param.type.mismatch=Invalid parameter type
common.param.format.error=Invalid parameter format

# Authentication
common.auth.unauthorized=Unauthorized, please login first
common.auth.forbidden=Access denied
common.auth.token.expired=Session expired, please login again
common.auth.token.invalid=Invalid token

# Resource
common.resource.not.found=Resource not found
common.resource.already.exists=Resource already exists

# Business rules
common.operation.not.allowed=Operation not allowed in current status
common.operation.rate.limit.exceeded=Too many requests

# System
common.system.error=System error, please try again later
common.service.unavailable=Service temporarily unavailable

# External service
common.external.service.error=External service error
common.external.service.timeout=External service timeout

# ========== User service ==========
# User management
user.not.found=User not found: {0}
user.already.exists=User already exists: {0}
user.disabled=User has been disabled
user.locked=User has been locked

# Authentication
user.auth.invalid.credentials=Invalid username or password
user.auth.password.expired=Password expired
user.auth.password.weak=Password is too weak, at least 8 characters with letters and numbers
user.auth.password.same.as.old=New password cannot be the same as old password

# Verification
user.verify.code.invalid=Invalid verification code
user.verify.code.expired=Verification code expired
user.verify.code.limit=Too many verification codes sent, please try again in {0} minutes

# ========== Order service ==========
# Order management
order.not.found=Order not found: {0}
order.expired=Order has expired
order.already.paid=Order already paid
order.already.cancelled=Order already cancelled

# Order status
order.status.invalid=Invalid order status
order.cancel.not.allowed=Cannot cancel order in current status
order.pay.not.allowed=Cannot pay in current status
order.refund.not.allowed=Cannot refund in current status

# Stock
order.stock.insufficient=Insufficient stock: product【{0}】stock {1}, requested {2}
order.stock.lock.failed=Failed to lock stock
order.stock.release.failed=Failed to release stock

# ========== Payment service ==========
# Payment order
payment.order.not.found=Payment order not found
payment.amount.mismatch=Payment amount mismatch
payment.timeout=Payment timeout
payment.failed=Payment failed

# Refund
payment.refund.failed=Refund failed
payment.refund.amount.exceeded=Refund amount exceeded
payment.refund.deadline.passed=Refund deadline passed

# Gateway
payment.gateway.error=Payment gateway error
payment.gateway.timeout=Payment gateway timeout
```

---

## 五、配置参数

### 5.1 application.yml

```yaml
# 国际化配置
i18n:
  enabled: true
  default-locale: zh_CN
  supported-locales:
    - zh_CN
    - en_US
  basename: i18n/messages
  cache-seconds: 3600
  encoding: UTF-8
```

---

## 六、使用示例

### 6.1 抛出异常

```java
// Service层 - 用户模块
throw new BusinessException(UserErrorCode.USER_NOT_FOUND, userId);

// Service层 - 订单模块
throw new BusinessException(OrderErrorCode.STOCK_INSUFFICIENT, "iPhone", 10, 20);
```

### 6.2 前端请求

```javascript
// 请求参数方式
fetch('/api/users/123?lang=en')

// 请求头方式
fetch('/api/users/123', {
  headers: { 'Accept-Language': 'en-US' }
})
```

---

## 七、错误码命名规范

| 规范 | 示例 |
|-----|------|
| 使用小写+点分隔 | `user.not.found` |
| 服务名作为前缀 | `user.`, `order.`, `payment.` |
| 子模块作为二级前缀 | `user.auth.`, `user.verify.`, `order.stock.` |
| 具体错误使用描述性词汇 | `not.found`, `invalid`, `insufficient` |
| 单词间用点分隔，不使用下划线或连字符 | ✅ `user.not.found` ❌ `user_not_found` |
| 不使用数字 | ✅ `user.auth.password.weak` ❌ `user.auth.password.001` |

---

## 八、优势总结

| 优势 | 说明 |
|-----|------|
| **自解释** | `user.not.found` 一眼就知道是用户不存在 |
| **无需分配** | 新增模块无需协调分配数字段 |
| **直接映射** | 错误码 = 国际化key，无需转换 |
| **易于维护** | 修改错误码不影响其他模块 |
| **跨服务传递** | 语义化错误码在Feign调用中易于理解 |
| **文档友好** | API文档中错误码具有实际意义 |