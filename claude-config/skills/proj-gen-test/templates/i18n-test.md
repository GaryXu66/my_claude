# 国际化测试补充用例

本文档提供国际化测试的补充用例，**不生成独立的测试类**，而是补充到现有的测试中。

---

## 检测条件

满足以下任一条件即认为项目配置了国际化：

1. `src/main/resources/i18n/` 目录存在
2. `application.yml` 中配置了 `spring.messages.basename=i18n/message`
3. 项目中存在 `I18nConfig` 相关配置类
4. 代码中使用了 `I18n` 工具类

---

## Controller 集成测试补充用例

补充到 `integration-test.md` 的 `{Entity}ControllerIntegrationTest` 类中：

### 中文响应测试

```java
@Test
@DisplayName("查询详情 - 不存在（中文）")
void getDetail_NotFound_Chinese() throws Exception {
    mockMvc.perform(get(BASE_URL + "/999999")
            .header("Accept-Language", "zh-CN"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.code").value("user.not.found"))
            .andExpect(jsonPath("$.message").value(containsString("用户不存在")));
}
```

### 英文响应测试

```java
@Test
@DisplayName("查询详情 - 不存在（英文）")
void getDetail_NotFound_English() throws Exception {
    mockMvc.perform(get(BASE_URL + "/999999")
            .header("Accept-Language", "en"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.code").value("user.not.found"))
            .andExpect(jsonPath("$.message").value(containsString("User not found")));
}
```

### 繁体中文响应测试

```java
@Test
@DisplayName("查询详情 - 不存在（繁体中文）")
void getDetail_NotFound_TraditionalChinese() throws Exception {
    mockMvc.perform(get(BASE_URL + "/999999")
            .header("Accept-Language", "zh-TW"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.code").value("user.not.found"))
            .andExpect(jsonPath("$.message").value(containsString("用戶不存在")));
}
```

### 默认语言测试（无请求头）

```java
@Test
@DisplayName("查询详情 - 不存在（默认语言）")
void getDetail_NotFound_Default() throws Exception {
    mockMvc.perform(get(BASE_URL + "/999999"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.code").value("user.not.found"))
            .andExpect(jsonPath("$.message").value(containsString("User not found"))); // 默认英文
}
```

### 参数校验国际化测试

```java
@Test
@DisplayName("创建 - 参数校验失败（中文）")
void create_ValidationFail_Chinese() throws Exception {
    {Entity}CreateRequest request = new {Entity}CreateRequest();
    // name 为空，触发校验

    mockMvc.perform(post(BASE_URL)
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request))
            .header("Accept-Language", "zh-CN"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.code").value("common.param.invalid"))
            .andExpect(jsonPath("$.message").value(containsString("不能为空")));
}

@Test
@DisplayName("创建 - 参数校验失败（英文）")
void create_ValidationFail_English() throws Exception {
    {Entity}CreateRequest request = new {Entity}CreateRequest();
    // name 为空，触发校验

    mockMvc.perform(post(BASE_URL)
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request))
            .header("Accept-Language", "en"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.code").value("common.param.invalid"))
            .andExpect(jsonPath("$.message").value(containsString("is required")));
}
```

---

## Service 单元测试补充用例

补充到 `service-test.md` 的 `{Entity}ServiceTest` 类中：

### 需要新增的依赖

```java
import com.example.common.I18n;
import org.springframework.context.i18n.LocaleContextHolder;
import java.util.Locale;
```

### 中文消息测试

```java
@Test
@DisplayName("根据ID查询 - 不存在（中文消息）")
void getDetail_NotFound_ChineseMessage() {
    // Given
    LocaleContextHolder.setLocale(Locale.SIMPLIFIED_CHINESE);
    when({entity}Mapper.selectById(1L)).thenReturn(null);

    // When & Then
    assertThatThrownBy(() -> {entity}Service.getDetail(1L))
            .isInstanceOf(BusinessException.class)
            .hasMessageContaining("用户不存在");
}
```

### 英文消息测试

```java
@Test
@DisplayName("根据ID查询 - 不存在（英文消息）")
void getDetail_NotFound_EnglishMessage() {
    // Given
    LocaleContextHolder.setLocale(Locale.ENGLISH);
    when({entity}Mapper.selectById(1L)).thenReturn(null);

    // When & Then
    assertThatThrownBy(() -> {entity}Service.getDetail(1L))
            .isInstanceOf(BusinessException.class)
            .hasMessageContaining("User not found");
}
```

### 使用 I18n 工具类测试（推荐）

```java
@Test
@DisplayName("根据ID查询 - 不存在（使用I18n工具类）")
void getDetail_NotFound_WithI18n() {
    // Given
    when({entity}Mapper.selectById(1L)).thenReturn(null);

    // When & Then
    assertThatThrownBy(() -> {entity}Service.getDetail(1L))
            .isInstanceOf(BusinessException.class)
            .hasMessageContaining(I18n.userErrorNotFound());
}
```

### 清理 Locale（建议添加到 @AfterEach）

```java
@AfterEach
void tearDown() {
    LocaleContextHolder.resetLocaleContext();
}
```

---

## I18n 工具类单元测试

```java
package com.example.common.util;

import com.example.common.I18n;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.context.i18n.LocaleContextHolder;
import org.springframework.test.context.ActiveProfiles;

import java.util.Locale;

import static org.assertj.core.api.Assertions.assertThat;

/**
 * I18n 工具类测试
 */
@DisplayName("I18n 工具类测试")
@ActiveProfiles("test")
class I18nTest {

    @AfterEach
    void tearDown() {
        LocaleContextHolder.resetLocaleContext();
    }

    @Test
    @DisplayName("获取成功消息 - 默认英文")
    void testCommonSuccess_Default() {
        String message = I18n.commonSuccess();
        assertThat(message).isEqualTo("Success");
    }

    @Test
    @DisplayName("获取成功消息 - 中文")
    void testCommonSuccess_Chinese() {
        LocaleContextHolder.setLocale(Locale.SIMPLIFIED_CHINESE);
        String message = I18n.commonSuccess();
        assertThat(message).isEqualTo("成功");
    }

    @Test
    @DisplayName("获取带参数的消息 - 英文")
    void testGetMessageWithArgs_English() {
        String message = I18n.validationErrorAgeInvalid(18, 100);
        assertThat(message).isEqualTo("Age must be between 18 and 100");
    }

    @Test
    @DisplayName("获取带参数的消息 - 中文")
    void testGetMessageWithArgs_Chinese() {
        LocaleContextHolder.setLocale(Locale.SIMPLIFIED_CHINESE);
        String message = I18n.validationErrorAgeInvalid(18, 100);
        assertThat(message).isEqualTo("年龄必须在18到100之间");
    }

    @Test
    @DisplayName("获取用户不存在消息 - 繁体中文")
    void testUserNotFound_TraditionalChinese() {
        LocaleContextHolder.setLocale(Locale.TRADITIONAL_CHINESE);
        String message = I18n.userErrorNotFound();
        assertThat(message).isEqualTo("用戶不存在");
    }

    @Test
    @DisplayName("测试复数 - 英文")
    void testPlural_English() {
        String message = I18n.userCount(5);
        assertThat(message).isEqualTo("5 user(s)");
    }

    @Test
    @DisplayName("测试复数 - 中文")
    void testPlural_Chinese() {
        LocaleContextHolder.setLocale(Locale.SIMPLIFIED_CHINESE);
        String message = I18n.userCount(5);
        assertThat(message).isEqualTo("5 个用户");
    }
}
```

---

## 国际化测试覆盖要求

| 测试项 | 说明 | 必需 | 补充位置 |
|--------|------|------|----------|
| 中文响应 | 验证中文消息正确显示 | 是 | Controller 集成测试 |
| 英文响应 | 验证英文消息正确显示 | 是 | Controller 集成测试 |
| 繁体中文响应 | 验证繁体中文消息正确显示 | 可选 | Controller 集成测试 |
| 默认语言 | 无请求头时使用英文 | 是 | Controller 集成测试 |
| 参数校验消息 | 验证参数校验的多语言提示 | 是 | Controller 集成测试 |
| 异常消息 | 验证业务异常的多语言消息 | 是 | Service 单元测试 |
| I18n 工具类 | 测试国际化工具类方法 | 是 | 单独测试类 |

---

## 支持的语言列表

根据项目配置的 i18n 资源包文件，测试对应语言：

| Locale | 语言 | Accept-Language 值 | 资源包文件 |
|--------|------|-------------------|-----------|
| en | 英文（默认） | en | message.properties |
| zh_CN | 简体中文 | zh-CN | message_zh_CN.properties |
| zh_TW | 繁体中文 | zh-TW | message_zh_TW.properties |

---

## 常用语义化错误码映射

测试时使用对应的错误码和预期消息：

```properties
# 通用消息（Common*）
common.success=成功 / Success
common.failed=操作失败 / Operation failed
common.param.invalid=参数错误 / Parameter error
common.resource.not.found=资源不存在 / Resource not found

# 用户模块（User*）
UserErrorNotFound=用户不存在 / User not found
UserErrorAlreadyExists=用户已存在 / User already exists
UserErrorUsernameRequired=用户名不能为空 / Username is required
UserErrorPasswordRequired=密码不能为空 / Password is required
UserCreateSuccess=创建成功 / Create successful
UserUpdateSuccess=更新成功 / Update successful
UserDeleteSuccess=删除成功 / Delete successful

# 验证消息（Validation*）
ValidationErrorRequired=字段 ''{0}'' 不能为空 / Field ''{0}'' is required
ValidationErrorAgeInvalid=年龄必须在{0}到{1}之间 / Age must be between {0} and {1}
```

---

## MockMvc 请求头设置方式

```java
// 方式1：通过 header() 方法
.header("Accept-Language", "zh-CN")

// 方式2：通过 locale() 方法
.locale(Locale.SIMPLIFIED_CHINESE)

// 方式3：同时设置
.header("Accept-Language", "en")
.locale(Locale.ENGLISH)
```

---

## 常用断言模式

### 验证响应消息

```java
// 精确匹配
.andExpect(jsonPath("$.message").value("用户不存在"))

// 包含匹配
.andExpect(jsonPath("$.message").value(containsString("用户")))

// 正则匹配
.andExpect(jsonPath("$.message").value(matchesPattern(".+用户.+")))
```

### 验证异常消息

```java
// 精确匹配
.hasMessage("用户不存在")

// 包含匹配
.hasMessageContaining("用户")

// 以指定字符串开头/结尾
.hasMessageStartingWith("用户")
.hasMessageEndingWith("存在")
```

---

## 生成建议

1. **检测到国际化配置时**，在生成 Controller 集成测试时自动添加国际化测试用例
2. **每个接口**至少添加一个中文和一个英文的测试用例
3. **参数校验失败**场景必须添加多语言测试
4. **Service 单元测试**中的异常场景添加多语言消息验证
5. **生成 I18nTest.java** 单独测试 I18n 工具类的所有方法

---

## 测试执行顺序建议

1. 先生成基础测试用例（CRUD）
2. 再补充国际化测试用例
3. 确保每个关键接口都有中英文测试覆盖
4. 最后生成 I18n 工具类的单元测试
