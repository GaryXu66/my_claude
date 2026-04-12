# DTO 模板

> **规范要点**：
> 1. DTO 必须实现 `Serializable` 并声明 `serialVersionUID`
> 2. 必填字段添加校验注解（`@NotNull`/`@NotBlank`/`@NotEmpty`）+ 中文消息
> 3. 所有字段添加 `@ApiModelProperty` 注解和 Javadoc 注释
> 4. UpdateRequest 所有字段可选，CreateRequest 必填字段加校验
> 5. **状态字段使用 Integer**：DTO 层使用 Integer 便于前端传递，Service 层负责转换为枚举

## CreateRequest

```java
package com.{company}.{project}.{module}.model.request;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import javax.validation.constraints.*;
import lombok.Data;
import java.io.Serializable;

/**
 * {description}创建请求
 *
 * @author {author}
 * @since {date}
 */
@Data
@ApiModel(description = "{description}创建请求")
public class {Domain}CreateRequest implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 名称
     */
    @NotBlank(message = "Name cannot be blank")
    @Size(max = 100, message = "Name length cannot exceed 100")
    @ApiModelProperty(value = "Name", required = true, example = "Example Name")
    private String name;

    /**
     * 状态 (1-启用, 0-禁用)
     */
    @ApiModelProperty(value = "Status (1-Enabled, 0-Disabled)", defaultValue = "1", example = "1")
    private Integer status = 1;
}
```

---

## UpdateRequest

```java
package com.{company}.{project}.{module}.model.request;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import java.io.Serializable;

/**
 * {description}更新请求
 *
 * @author {author}
 * @since {date}
 */
@Data
@ApiModel(description = "{description}更新请求")
public class {Domain}UpdateRequest implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 名称
     */
    @ApiModelProperty(value = "Name")
    private String name;

    /**
     * 状态 (1-启用, 0-禁用)
     */
    @ApiModelProperty(value = "Status (1-Enabled, 0-Disabled)")
    private Integer status;
}
```

---

## QueryRequest

```java
package com.{company}.{project}.{module}.model.request;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import javax.validation.constraints.Max;
import javax.validation.constraints.Min;
import java.io.Serializable;

/**
 * {description}查询请求
 *
 * @author {author}
 * @since {date}
 */
@Data
@ApiModel(description = "{description}查询请求")
public class {Domain}QueryRequest implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 页码
     */
    @Min(value = 1, message = "页码至少为1")
    @ApiModelProperty(value = "Page number", defaultValue = "1")
    private int pageNo = 1;
    /**
     * 每页数量
     */
    @Min(value = 1, message = "每页数量至少为1")
    @Max(value = 500, message = "每页数量不能超过500")
    @ApiModelProperty(value = "Page size", defaultValue = "10")
    private int pageSize = 10;

    /**
     * 关键词
     */
    @ApiModelProperty(value = "Keyword")
    private String keyword;

    /**
     * 状态 (1-启用, 0-禁用)
     */
    @ApiModelProperty(value = "Status (1-Enabled, 0-Disabled)")
    private Integer status;
}
```

---

## Response

```java
package com.{company}.{project}.{module}.model.response;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import java.io.Serializable;
import java.time.LocalDateTime;

/**
 * {description}响应
 *
 * @author {author}
 * @since {date}
 */
@Data
@ApiModel(description = "{description}响应")
public class {Domain}Response implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 主键ID
     */
    @ApiModelProperty(value = "Primary key ID", example = "507f1f77bcf86cd799439011")
    private String id;

    /**
     * 名称
     */
    @ApiModelProperty(value = "Name", example = "Example Name")
    private String name;

    /**
     * 状态码 (1-启用, 0-禁用)
     * 注：响应中使用 Integer 类型，前端便于判断
     */
    @ApiModelProperty(value = "Status code (1-Enabled, 0-Disabled)", example = "1")
    private Integer status;

    /**
     * 创建时间
     */
    @ApiModelProperty(value = "Create time", example = "2026-01-29T10:00:00")
    private LocalDateTime createTime;

    /**
     * 更新时间
     */
    @ApiModelProperty(value = "Update time", example = "2026-01-29T10:00:00")
    private LocalDateTime updateTime;
}
```

---

## 注意事项

1. **必填字段** - CreateRequest使用 `@NotNull` / `@NotBlank` / `@NotEmpty`
2. **可选字段** - UpdateRequest 所有字段都是可选的
3. **长度限制** - 字符串使用 `@Size`，与数据库字段长度一致
4. **错误消息** - 必须提供中文错误消息
5. **触发校验** - Controller 必须使用 `@Validated` 触发校验
