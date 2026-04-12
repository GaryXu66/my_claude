# Domain 模板（MongoDB）

> **充血模型原则**：简单验证、状态控制、业务规则放在 Domain；复杂流程、跨聚合操作放在 Service

---

## 业务 Domain 类

```java
package com.{company}.{project}.{module}.domain;

import cn.hutool.core.util.ObjectUtil;
import com.{company}.{project}.{module}.enums.StatusEnum;
import lombok.Data;
import org.springframework.data.annotation.Version;
import org.springframework.data.mongodb.core.index.CompoundIndex;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

/**
 * {description}领域模型
 *
 * @author {author}
 * @since {date}
 */
@Data
@Document(collection = "T_{Domain}")
@CompoundIndex(name = "name_status_1", def = "{name: 1, status: 1}")
@CompoundIndex(name = "del_flag_create_time_1", def = "{delFlag: 1, createTime: -1}")
public class {Domain} {

    /**
     * 删除标记常量
     */
    public static final int DEL_FLAG_NORMAL = 0;
    public static final int DEL_FLAG_DELETED = 1;

    /**
     * 乐观锁版本号（防止并发修改冲突）
     * MongoDB 会自动检查版本号，冲突时抛出 OptimisticLockingFailureException
     */
    @Version
    private Long version;

    /**
     * 主键ID（MongoDB ObjectId）
     */
    private String id;

    /**
     * 名称
     */
    @Indexed
    private String name;

    /**
     * 状态
     */
    private StatusEnum status;

    /**
     * 创建人
     */
    private String createBy;

    /**
     * 创建时间
     */
    private LocalDateTime createTime;

    /**
     * 更新人
     */
    private String updateBy;

    /**
     * 更新时间
     */
    private LocalDateTime updateTime;

    /**
     * 删除标记 (0-正常, 1-删除)
     */
    private Integer delFlag;

    /**
     * 启用
     */
    public void enable() {
        this.status = StatusEnum.ENABLED;
        this.updateTime = LocalDateTime.now();
    }

    /**
     * 禁用
     */
    public void disable() {
        this.status = StatusEnum.DISABLED;
        this.updateTime = LocalDateTime.now();
    }

    /**
     * 是否启用
     */
    public boolean isEnabled() {
        return ObjectUtil.equal(this.status, StatusEnum.ENABLED);
    }

    /**
     * 标记删除
     */
    public void markDeleted() {
        this.delFlag = DEL_FLAG_DELETED;
        this.updateTime = LocalDateTime.now();
    }

    /**
     * 是否已删除
     */
    public boolean isDeleted() {
        return ObjectUtil.equal(this.delFlag, DEL_FLAG_DELETED);
    }
}
```

---

## 常用业务方法示例

### 状态控制

```java
public void activate() {
    this.status = StatusEnum.ACTIVE;
    this.updateTime = LocalDateTime.now();
}

public void deactivate() {
    this.status = StatusEnum.INACTIVE;
    this.updateTime = LocalDateTime.now();
}

public boolean isActive() {
    return ObjectUtil.equal(this.status, StatusEnum.ACTIVE);
}
```

### 审核流程

```java
// 审核状态常量
public static final int AUDIT_STATUS_PENDING = 0;
public static final int AUDIT_STATUS_APPROVED = 1;
public static final int AUDIT_STATUS_REJECTED = 2;

public void approve(String auditor) {
    this.auditStatus = AUDIT_STATUS_APPROVED;
    this.auditor = auditor;
    this.auditTime = LocalDateTime.now();
}

public void reject(String auditor, String reason) {
    this.auditStatus = AUDIT_STATUS_REJECTED;
    this.auditor = auditor;
    this.rejectReason = reason;
    this.auditTime = LocalDateTime.now();
}

public boolean isPending() {
    return this.auditStatus == AUDIT_STATUS_PENDING;
}

public boolean isApproved() {
    return this.auditStatus == AUDIT_STATUS_APPROVED;
}
```

### 时间验证

```java
public boolean isExpired() {
    return ObjectUtil.isNotNull(this.expireTime) && LocalDateTime.now().isAfter(this.expireTime);
}

public boolean isValid() {
    LocalDateTime now = LocalDateTime.now();
    return (ObjectUtil.isNull(this.startTime) || now.isAfter(this.startTime))
            && (ObjectUtil.isNull(this.endTime) || now.isBefore(this.endTime));
}
```

---

## 注意事项

1. **使用 @Document** - 指定集合名称，建议格式 `T_{Domain}`
2. **使用 @Indexed** - 定义单字段索引
3. **使用 @CompoundIndex** - 定义复合索引
4. **ID 类型分层设计**
   - Domain 层：`String id`（MongoDB ObjectId）
   - Service/Controller 层：`String id`（业务层统一使用 String）
   - DTO 层：`String id`（响应给前端）
   - 全层统一使用 String 类型，无需转换
5. **索引命名** - `字段名_1`（升序）或 `字段名_-1`（降序）
6. **枚举类型使用规范**
    - Domain 层使用枚举类型（如 `StatusEnum`），提供类型安全和业务方法
    - MongoDB 自动将枚举存储为 Integer（通过 code 值）
    - 需要配置 MongoDB 枚举转换器（见下方配置）
7. **充血模型原则**
    - 简单验证、状态控制、业务规则 → Domain
    - 复杂流程、跨聚合操作 → Service

---

## MongoDB 枚举转换器配置

为了让 MongoDB 正确存储和读取枚举类型，需要添加自定义转换器：

```java
package com.{company}.{project}.common.config;

import com.{company}.{project}.{module}.enums.StatusEnum;
import org.springframework.core.convert.converter.Converter;
import org.springframework.data.convert.ReadingConverter;
import org.springframework.data.convert.WritingConverter;
import org.springframework.data.mongodb.core.convert.MongoCustomConversions;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.Arrays;

/**
 * MongoDB 枚举转换器配置
 *
 * @author {author}
 * @since {date}
 */
@Configuration
public class MongoEnumConverterConfig {

    @Bean
    public MongoCustomConversions customConversions() {
        return new MongoCustomConversions(Arrays.asList(
                new StatusEnumToIntegerConverter(),
                new IntegerToStatusEnumConverter()
        ));
    }

    /**
     * 枚举 → Integer（写入数据库）
     */
    @WritingConverter
    public static class StatusEnumToIntegerConverter implements Converter<StatusEnum, Integer> {
        @Override
        public Integer convert(StatusEnum source) {
            return source.getCode();
        }
    }

    /**
     * Integer → 枚举（从数据库读取）
     */
    @ReadingConverter
    public static class IntegerToStatusEnumConverter implements Converter<Integer, StatusEnum> {
        @Override
        public StatusEnum convert(Integer source) {
            return StatusEnum.of(source);
        }
    }
}
```
