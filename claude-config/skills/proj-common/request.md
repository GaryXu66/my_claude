# 请求规范

> 支持国际化、动态配置的请求规范

---

## 一、请求头

### 1.1 标准请求头

| Header | 说明 | 必填 | 示例 |
|--------|------|------|------|
| Content-Type | 内容类型 | 是 | `application/json` |
| Authorization | 认证令牌 | 是* | `Bearer {token}` |
| Accept-Language | 语言偏好 | 否 | `zh-CN`, `en-US` |
| X-Request-Id | 请求追踪ID | 否 | `uuid` |
| X-Client-Version | 客户端版本 | 否 | `1.0.0` |
| X-Platform | 平台标识 | 否 | `ios`, `android`, `web` |

> *Authorization 在需要登录的接口中必填

### 1.2 国际化请求头

```
Accept-Language: zh-CN    # 简体中文
Accept-Language: en-US    # 英文
Accept-Language: zh-TW    # 繁体中文
Accept-Language: ja       # 日文
```

---

## 二、分页参数

### 2.1 分页请求

```
GET /api/v1/user?pageNo=1&pageSize=10
```

### 2.2 分页参数配置类

```java
package com.{company}.{project}.common.config;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

/**
 * 分页配置属性
 * 支持@Value动态配置
 */
@Data
@Component
@ConfigurationProperties(prefix = "page")
public class PageProperties {

    /**
     * 默认页码
     */
    private int defaultPageNo = 1;

    /**
     * 默认每页数量
     */
    private int defaultPageSize = 10;

    /**
     * 最大每页数量
     */
    private int maxPageSize = 100;

    /**
     * 是否启用分页
     */
    private boolean enabled = true;
}
```

### 2.3 分页参数 DTO

```java
package com.{company}.{project}.common.model.request;

import lombok.Data;

/**
 * 分页请求基类
 */
@Data
public class PageRequest {

    /**
     * 页码（从配置读取默认值）
     */
    private Integer pageNo;

    /**
     * 每页数量（从配置读取默认值）
     */
    private Integer pageSize;

    /**
     * 排序字段
     */
    private String sortField;

    /**
     * 排序方向
     */
    private String sortOrder;

    /**
     * 获取页码，使用配置的默认值
     */
    public int getPageNo(int defaultPageNo) {
        return pageNo != null && pageNo > 0 ? pageNo : defaultPageNo;
    }

    /**
     * 获取每页数量，限制最大值
     */
    public int getPageSize(int defaultPageSize, int maxPageSize) {
        if (pageSize == null || pageSize <= 0) {
            return defaultPageSize;
        }
        return Math.min(pageSize, maxPageSize);
    }
}
```

### 2.4 配置文件

```yaml
# 分页配置
page:
  default-page-no: 1        # 默认页码
  default-page-size: 10     # 默认每页数量
  max-page-size: 100        # 最大每页数量
  enabled: true             # 是否启用分页
```

---

## 三、查询参数（GET 请求）

### 3.1 分页参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| pageNo | int | `${page.default-page-no}` | 页码，从 1 开始 |
| pageSize | int | `${page.default-page-size}` | 每页数量，最大 `${page.max-page-size}` |

### 3.2 筛选参数

```
GET /api/v1/user?status=1&keyword=张三
```

### 3.3 排序参数

```
GET /api/v1/user?sortField=createTime&sortOrder=desc
```

| 参数 | 说明 | 可选值 |
|------|------|--------|
| sortField | 排序字段 | 字段名 |
| sortOrder | 排序方向 | `asc`, `desc` |

### 3.4 时间范围

```
GET /api/v1/order?startTime=2024-01-01&endTime=2024-12-31
```

---

## 四、请求体（POST/PUT 请求）

### 4.1 创建请求

```json
POST /api/v1/user
Content-Type: application/json

{
    "username": "zhangsan",
    "phone": "13800138000",
    "email": "zhangsan@example.com",
    "status": 1
}
```

### 4.2 更新请求

```json
PUT /api/v1/user/123
Content-Type: application/json

{
    "username": "zhangsan_new",
    "phone": "13800138001"
}
```

### 4.3 批量操作

```json
POST /api/v1/user/batch-delete
Content-Type: application/json

{
    "ids": [1, 2, 3, 4, 5]
}
```

---

## 五、请求配置

### 5.1 请求配置属性

```java
package com.{company}.{project}.common.config;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

/**
 * 请求配置属性
 */
@Data
@Component
@ConfigurationProperties(prefix = "request")
public class RequestProperties {

    /**
     * 请求体最大大小
     */
    private String maxPayloadSize = "10MB";

    /**
     * 是否启用请求追踪
     */
    private boolean traceEnabled = true;

    /**
     * 请求超时时间（秒）
     */
    private int timeoutSeconds = 30;

    /**
     * 支持的语言列表
     */
    private String[] supportedLanguages = {"zh-CN", "en-US", "zh-TW"};

    /**
     * 默认语言
     */
    private String defaultLanguage = "zh-CN";
}
```

### 5.2 配置文件

```yaml
# 请求配置
request:
  max-payload-size: 10MB
  trace-enabled: true
  timeout-seconds: 30
  supported-languages:
    - zh-CN
    - en-US
    - zh-TW
  default-language: zh-CN
```

---

## 六、使用示例

### 6.1 Controller 使用分页

```java
@RestController
@RequestMapping("/api/v1/user")
@RequiredArgsConstructor
public class UserController {

    private final PageProperties pageProperties;
    private final UserService userService;

    @GetMapping
    public Result<PageResult<User>> list(PageRequest pageRequest) {
        // 使用配置的默认值
        int pageNo = pageRequest.getPageNo(pageProperties.getDefaultPageNo());
        int pageSize = pageRequest.getPageSize(pageProperties.getDefaultPageSize(),
            pageProperties.getMaxPageSize());

        PageResult<User> result = userService.list(pageNo, pageSize);
        return Result.success(result);
    }
}
```

### 6.2 前端请求示例

```javascript
// 分页查询
fetch('/api/v1/user?pageNo=1&pageSize=20', {
  headers: {
    'Content-Type': 'application/json',
    'Accept-Language': 'zh-CN'
  }
})

// 带筛选和排序
fetch('/api/v1/user?status=1&sortField=createTime&sortOrder=desc', {
  headers: {
    'Content-Type': 'application/json',
    'Accept-Language': 'en-US'
  }
})
```

---

## 七、注意事项

1. **Content-Type** - POST/PUT 请求必须设置为 `application/json`
2. **Token 传递** - 放在 Authorization 头，格式 `Bearer {token}`
3. **分页限制** - pageSize 最大值通过配置文件设置，防止一次查询过多数据
4. **时间格式** - 统一使用 `yyyy-MM-dd` 或 `yyyy-MM-dd HH:mm:ss`
5. **国际化** - 通过 `Accept-Language` 头设置语言偏好
6. **动态配置** - 分页默认值、最大值等通过配置文件管理
