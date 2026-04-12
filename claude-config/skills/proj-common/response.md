# Result 响应类

> 支持国际化、语义化错误码的统一响应类
> 响应消息通过 ResponseBodyAdvice 自动国际化

---

## 一、Result 类实现

### 1.1 响应类定义

```java
package com.{company}.{project}.common.model;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;
import java.io.Serializable;

/**
 * 统一API响应结果
 * 支持国际化、语义化错误码
 */
@Data
@Schema(description = "统一响应结果")
public class Result<T> implements Serializable {

    private static final long serialVersionUID = 1L;

    @Schema(description = "错误码（语义化），成功为 common.success")
    private String code;

    @Schema(description = "提示信息（支持国际化）")
    private String message;

    @Schema(description = "响应数据")
    private T data;

    @Schema(description = "时间戳（毫秒）")
    private Long timestamp;

    @Schema(description = "跟踪ID")
    private String traceId;

    /**
     * 私有构造函数
     */
    private Result() {
        this.timestamp = System.currentTimeMillis();
    }

    // ========== 成功响应 ==========

    /**
     * 成功响应（无数据）
     */
    public static <T> Result<T> success() {
        Result<T> result = new Result<>();
        result.setCode("common.success");
        result.setMessage("common.success");  // 使用code作为i18n key
        return result;
    }

    /**
     * 成功响应（带数据）
     */
    public static <T> Result<T> success(T data) {
        Result<T> result = new Result<>();
        result.setCode("common.success");
        result.setMessage("common.success");
        result.setData(data);
        return result;
    }

    /**
     * 成功响应（自定义消息key+数据）
     * message传入i18n key
     */
    public static <T> Result<T> success(String messageKey, T data) {
        Result<T> result = new Result<>();
        result.setCode("common.success");
        result.setMessage(messageKey);
        result.setData(data);
        return result;
    }

    // ========== 失败响应 ==========

    /**
     * 失败响应（语义化错误码）
     */
    public static <T> Result<T> fail(String code) {
        Result<T> result = new Result<>();
        result.setCode(code);
        result.setMessage(code);  // 使用code作为i18n key
        return result;
    }

    /**
     * 失败响应（错误码+i18n key）
     */
    public static <T> Result<T> fail(String code, String messageKey) {
        Result<T> result = new Result<>();
        result.setCode(code);
        result.setMessage(messageKey);
        return result;
    }

    /**
     * 失败响应（使用ErrorCode枚举）
     */
    public static <T> Result<T> fail(ErrorCode errorCode) {
        Result<T> result = new Result<>();
        result.setCode(errorCode.getCode());
        result.setMessage(errorCode.getMessageKey());
        return result;
    }

    /**
     * 失败响应（ErrorCode枚举+参数）
     */
    public static <T> Result<T> fail(ErrorCode errorCode, Object... args) {
        Result<T> result = new Result<>();
        result.setCode(errorCode.getCode());
        result.setMessage(errorCode.getMessageKey());
        result.setArgs(args);
        return result;
    }

    // ========== 判断方法 ==========

    /**
     * 判断响应是否成功
     */
    public boolean isSuccess() {
        return "common.success".equals(this.code);
    }

    // ========== 链式调用 ==========

    public Result<T> setData(T data) {
        this.data = data;
        return this;
    }

    public Result<T> setMessage(String message) {
        this.message = message;
        return this;
    }

    public Result<T> setArgs(Object[] args) {
        // 设置国际化参数，由ResponseAdvice处理
        // 使用transient避免被序列化
        this.args = args;
        return this;
    }

    /**
     * 国际化参数（不序列化）
     */
    private transient Object[] args;

    public Object[] getArgs() {
        return args;
    }
}
```

---

## 二、响应国际化处理

### 2.1 ResponseBodyAdvice 响应拦截器

```java
package com.{company}.{project}.common.config;

import com.{company}.{project}.common.model.Result;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.MessageSource;
import org.springframework.context.i18n.LocaleContextHolder;
import org.springframework.core.MethodParameter;
import org.springframework.http.MediaType;
import org.springframework.http.converter.HttpMessageConverter;
import org.springframework.http.server.ServerHttpRequest;
import org.springframework.http.server.ServerHttpResponse;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.servlet.mvc.method.annotation.ResponseBodyAdvice;

/**
 * 响应体Advice
 * 自动处理Result消息的国际化
 */
@Slf4j
@RestControllerAdvice
@RequiredArgsConstructor
public class ResponseAdvice implements ResponseBodyAdvice<Result<?>> {

    private final MessageSource messageSource;
    private final ResponseProperties responseProperties;

    @Override
    public boolean supports(MethodParameter returnType,
                           Class<? extends HttpMessageConverter<?>> converterType) {
        // 只处理Result类型的响应
        return Result.class.isAssignableFrom(returnType.getParameterType());
    }

    @Override
    public Result<?> beforeBodyWrite(Result<?> body,
                                    MethodParameter returnType,
                                    MediaType selectedContentType,
                                    Class<? extends HttpMessageConverter<?>> selectedConverterType,
                                    ServerHttpRequest request,
                                    ServerHttpResponse response) {
        if (body == null) {
            return null;
        }

        // 处理国际化消息
        String i18nMessage = getI18nMessage(body.getMessage(), body.getArgs());
        body.setMessage(i18nMessage);

        // 添加Content-Language响应头
        String locale = LocaleContextHolder.getLocale().toString();
        response.getHeaders().add("Content-Language", locale);

        return body;
    }

    /**
     * 获取国际化消息
     */
    private String getI18nMessage(String key, Object[] args) {
        if (key == null || key.isEmpty()) {
            return "";
        }
        try {
            return messageSource.getMessage(key, args, key, LocaleContextHolder.getLocale());
        } catch (Exception e) {
            log.debug("国际化消息获取失败: key={}", key, e);
            return key;
        }
    }
}
```

### 2.2 响应配置属性

```java
package com.{company}.{project}.common.config;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

/**
 * 响应配置属性
 * 支持@Value动态配置
 */
@Data
@Component
@ConfigurationProperties(prefix = "response")
public class ResponseProperties {

    /**
     * 是否包含时间戳
     */
    private boolean includeTimestamp = true;

    /**
     * 是否在开发环境包含堆栈信息
     */
    private boolean includeStackTrace = false;

    /**
     * 是否启用响应国际化
     */
    private boolean i18nEnabled = true;

    /**
     * 成功响应的默认code
     */
    private String successCode = "common.success";

    /**
     * 成功响应的默认消息key
     */
    private String successMessageKey = "common.success";
}
```

### 2.3 配置文件

```yaml
# 响应配置
response:
  include-timestamp: true
  include-stack-trace: false
  i18n-enabled: true
  success-code: common.success
  success-message-key: common.success
```

---

## 三、PageResult 分页响应

```java
package com.{company}.{project}.common.model;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;
import java.io.Serializable;
import java.util.List;

/**
 * 分页响应结果
 */
@Data
@Schema(description = "分页响应结果")
public class PageResult<T> implements Serializable {

    private static final long serialVersionUID = 1L;

    @Schema(description = "数据列表")
    private List<T> records;

    @Schema(description = "总记录数")
    private Long total;

    @Schema(description = "当前页码")
    private Integer pageNo;

    @Schema(description = "每页数量")
    private Integer pageSize;

    @Schema(description = "总页数")
    private Integer pages;

    /**
     * 创建分页结果
     */
    public static <T> PageResult<T> of(List<T> records, long total, int pageNo, int pageSize) {
        PageResult<T> result = new PageResult<>();
        result.setRecords(records);
        result.setTotal(total);
        result.setPageNo(pageNo);
        result.setPageSize(pageSize);
        result.setPages((int) Math.ceil((double) total / pageSize));
        return result;
    }

    /**
     * 空分页结果
     */
    public static <T> PageResult<T> empty() {
        return of(List.of(), 0L, 1, 10);
    }
}
```

---

## 四、使用示例

### 4.1 Controller 使用

```java
@RestController
@RequestMapping("/api/v1/user")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    // 成功响应（带数据）
    // message会被ResponseAdvice国际化：common.success -> 成功 / Success
    @GetMapping("/{id}")
    public Result<UserResponse> detail(@PathVariable Long id) {
        UserResponse user = userService.getDetail(id);
        return Result.success(user);
    }

    // 成功响应（无数据）
    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        userService.deleteById(id);
        return Result.success();
    }

    // 成功响应（自定义消息key）
    // message传入i18n key，会被自动转换
    @PostMapping("/register")
    public Result<UserResponse> register(@RequestBody RegisterRequest request) {
        UserResponse user = userService.register(request);
        return Result.success("user.register.success", user);
        // messages.properties: user.register.success=注册成功
        // messages_en.properties: user.register.success=Register successfully
    }

    // 失败响应（语义化错误码）
    @PostMapping("/login")
    public Result<LoginResponse> login(@RequestBody LoginRequest request) {
        User user = userService.findByUsername(request.getUsername());
        if (user == null) {
            return Result.fail("user.not.found");
            // 会被国际化: user.not.found -> 用户不存在 / User not found
        }
        return Result.success(loginService.doLogin(user));
    }
}
```

### 4.2 Service 抛异常（推荐）

```java
@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    private final UserMapper userMapper;

    @Override
    public User getDetail(Long userId) {
        User user = userMapper.selectById(userId);
        if (user == null) {
            // 抛出异常，由GlobalExceptionHandler处理
            throw UserException.userNotFound(userId);
        }
        return user;
    }
}
```

---

## 五、响应格式

### 5.1 成功响应

```json
{
    "code": "common.success",
    "message": "成功",
    "data": {
        "id": 1,
        "username": "zhangsan"
    },
    "timestamp": 1704067200000
}
```

### 5.2 失败响应（语义化错误码）

```json
{
    "code": "user.not.found",
    "message": "用户不存在: 123",
    "data": null,
    "timestamp": 1704067200000
}
```

### 5.3 国际化响应对比

| 请求头 | code | message (中文) | message (英文) |
|--------|------|---------------|---------------|
| `Accept-Language: zh-CN` | `user.not.found` | 用户不存在: 123 | - |
| `Accept-Language: en-US` | `user.not.found` | - | User not found: 123 |
| `Accept-Language: zh-TW` | `user.not.found` | 用戶不存在: 123 | - |

---

## 六、响应头

| Header | 说明 | 示例 |
|--------|------|------|
| Content-Type | 响应内容类型 | `application/json;charset=UTF-8` |
| Content-Language | 响应语言（自动设置） | `zh-CN`, `en-US` |
| X-Request-Id | 请求追踪ID | 与请求头相同 |

---

## 七、国际化资源

### 7.1 messages.properties

```properties
# 公共
common.success=成功
common.param.invalid=参数校验失败
common.resource.not.found=资源不存在
common.system.error=系统错误，请稍后重试

# 用户
user.register.success=注册成功
user.not.found=用户不存在: {0}
user.auth.invalid.credentials=用户名或密码错误
```

### 7.2 messages_en.properties

```properties
# Common
common.success=Success
common.param.invalid=Invalid parameter
common.resource.not.found=Resource not found
common.system.error=System error, please try again later

# User
user.register.success=Register successfully
user.not.found=User not found: {0}
user.auth.invalid.credentials=Invalid username or password
```

---

## 八、前后端联调

### 8.1 前端请求示例

```javascript
// 设置语言
const headers = {
  'Content-Type': 'application/json',
  'Accept-Language': 'en-US'
};

// 发起请求
fetch('/api/v1/user/123', { headers })
  .then(res => res.json())
  .then(data => {
    if (data.code === 'common.success') {
      console.log('Success:', data.data);
    } else {
      // data.message 已经是国际化后的消息
      console.error('Failed:', data.code, data.message);
    }
  });
```

### 8.2 响应处理

```javascript
// 判断响应是否成功
function isSuccess(response) {
  return response.code === 'common.success';
}

// 获取错误消息（已国际化）
function getErrorMessage(response) {
  return response.message || '操作失败';
}
```

---

## 九、注意事项

1. **错误码语义化** - 使用 `user.not.found` 而非数字错误码
2. **消息自动国际化** - 通过 `ResponseAdvice` 自动处理响应消息国际化
3. **配置外置** - 默认值、开关等通过配置文件管理
4. **统一格式** - 所有接口返回统一的 Result 格式
5. **Content-Language** - 响应头自动包含当前语言
6. **message字段** - 存储的是i18n key，由ResponseAdvice转换为实际消息
