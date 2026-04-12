# 枚举模板

## StatusEnum（状态枚举）- 通用模板

```java
package com.{company}.{project}.{module}.enums;

import cn.hutool.core.util.ArrayUtil;
import lombok.Getter;
import lombok.AllArgsConstructor;

/**
 * 状态枚举
 *
 * @author {author}
 * @since {date}
 */
@Getter
@AllArgsConstructor
public enum StatusEnum {

    /**
     * 禁用
     */
    DISABLED(0, "禁用"),

    /**
     * 启用
     */
    ENABLED(1, "启用");

    private final Integer code;
    private final String desc;

    /**
     * 根据code获取枚举
     *
     * @param code 状态码
     * @return 状态枚举
     */
    public static StatusEnum of(Integer code) {
        if (code == null) {
            return null;
        }
        return ArrayUtil.firstMatch(values(), item -> item.getCode().equals(code));
    }
}
```

---

## 标准枚举模板

```java
package com.{company}.{project}.{module}.enums;

import cn.hutool.core.util.ArrayUtil;
import lombok.Getter;
import lombok.AllArgsConstructor;

/**
 * {description}枚举
 *
 * @author {author}
 * @since {date}
 */
@Getter
@AllArgsConstructor
public enum {EnumName} {

    {VALUE1}({code1}, "{desc1}"),
    {VALUE2}({code2}, "{desc2}"),
    ;

    private final Integer code;
    private final String desc;

    /**
     * 根据code获取枚举
     *
     * @param code 状态码
     * @return 枚举对象
     */
    public static {EnumName} of(Integer code) {
        if (code == null) {
            return null;
        }
        return ArrayUtil.firstMatch(values(), item -> item.getCode().equals(code));
    }
}
```

---

## 常用枚举示例

```java
// 状态
DISABLE(0, "禁用"), ENABLE(1, "启用")

// 是否
NO(0, "否"), YES(1, "是")

// 审核
PENDING(0, "待审核"), APPROVED(1, "已通过"), REJECTED(2, "已拒绝")
```
