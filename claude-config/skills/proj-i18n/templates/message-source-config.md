# MessageSource 配置模板

## Java 配置类

### MessageSource 配置

```java
package com.{company}.{project}.common.config;

import org.springframework.context.MessageSource;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.support.ResourceBundleMessageSource;

/**
 * 全球化(国际化)配置
 */
@Configuration
public class I18nConfig {

    /**
     * 配置 MessageSource Bean
     * 负责加载和解析多语言资源包
     */
    @Bean
    public MessageSource messageSource() {
        ResourceBundleMessageSource messageSource = new ResourceBundleMessageSource();
        messageSource.setBasename("i18n/message");
        messageSource.setDefaultEncoding("UTF-8");
        messageSource.setCacheSeconds(3600);
        messageSource.setFallbackToSystemLocale(false);
        return messageSource;
    }
}
```

---

## I18n 类自动生成

通过 Gradle 任务自动从 properties 文件生成 I18n 类，每个 key 生成无参和带参两个方法，实现 IDE 自动补全。

### Gradle 配置

在 `build.gradle` 中添加：

```groovy
plugins {
    id 'java'
    // 使用 buildSrc 或自定义任务生成常量类
}

// 自动生成 I18n 工具类的任务
task generateI18n {
    def propsDir = file("src/main/resources/i18n")
    def outputDir = file("src/main/java/com/{company}/{project}/common")
    def outputFile = new File(outputDir, "I18n.java")

    inputs.dir propsDir
    outputs.file outputFile

    doFirst {
        if (!outputDir.exists()) {
            outputDir.mkdirs()
        }

        // 读取默认资源文件（message.properties）
        def propsFile = new File(propsDir, "message.properties")
        if (!propsFile.exists()) {
            throw new FileNotFoundException("未找到资源文件: ${propsFile.absolutePath}")
        }

        def props = new Properties()
        propsFile.withReader("UTF-8") { reader ->
            props.load(reader)
        }

        // 生成 Java 类
        def writer = new OutputStreamWriter(new FileOutputStream(outputFile), "UTF-8")
        writer.write '''package com.{company}.{project}.common;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.MessageSource;
import org.springframework.context.i18n.LocaleContextHolder;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;

/**
 * 国际化工具类
 * 自动生成，请勿手动修改
 * 生成时间：''' + new Date().toString() + '''
 */
@Component
public class I18n {

    @Autowired
    private MessageSource messageSource;

'''
        // 按key排序后生成方法（每个key生成两个版本）
        props.keySet().sort().each { key ->
            def value = props.getProperty(key)
            // 方法名：首字母小写（PascalCase -> camelCase）
            def methodName = key.substring(0, 1).toLowerCase() + key.substring(1)
            // 无参版本
            writer.write "    /** ${value} */\n"
            writer.write "    public static String ${methodName}() {\n"
            writer.write "        return get(\"${key}\");\n"
            writer.write "    }\n\n"
            // 带参版本
            writer.write "    /** ${value} (带参数) */\n"
            writer.write "    public static String ${methodName}(Object... args) {\n"
            writer.write "        return get(\"${key}\", args);\n"
            writer.write "    }\n\n"
        }

        writer.write '''    /**
     * 获取消息（内部使用）
     */
    private static String get(String key) {
        return Holder.getMessage(key);
    }

    /**
     * 获取带参消息（内部使用）
     */
    private static String get(String key, Object[] args) {
        return Holder.getMessage(key, args);
    }

    /**
     * 内部Holder，用于静态方法访问Spring Bean
     */
    @Component
    static class Holder {
        private static Holder instance;

        @Autowired
        private MessageSource messageSource;

        @PostConstruct
        public void init() {
            instance = this;
        }

        static String getMessage(String key) {
            return getMessage(key, null);
        }

        static String getMessage(String key, Object[] args) {
            return instance.messageSource.getMessage(key, args, key, LocaleContextHolder.getLocale());
        }
    }
}
'''
        writer.close()
    }
}

// 编译前先生成I18n类
compileJava.dependsOn generateI18n

// 清理时删除生成的文件
clean {
    delete file("src/main/java/com/{company}/{project}/common/I18n.java")
}
```

### 生成的 I18n 类

```java
package com.{company}.{project}.common;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.MessageSource;
import org.springframework.context.i18n.LocaleContextHolder;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;

/**
 * 国际化工具类
 * 自动生成，请勿手动修改
 * 生成时间：Mon Jan 01 10:00:00 CST 2026
 */
@Component
public class I18n {

    @Autowired
    private MessageSource messageSource;

    /** 操作成功 */
    public static String commonSuccess() {
        return get("CommonSuccess");
    }

    /** 操作成功 (带参数) */
    public static String commonSuccess(Object... args) {
        return get("CommonSuccess", args);
    }

    /** 操作失败 */
    public static String commonFailed() {
        return get("CommonFailed");
    }

    /** 操作失败 (带参数) */
    public static String commonFailed(Object... args) {
        return get("CommonFailed", args);
    }

    /** 用户不存在 */
    public static String userErrorNotFound() {
        return get("UserErrorNotFound");
    }

    /** 用户不存在 (带参数) */
    public static String userErrorNotFound(Object... args) {
        return get("UserErrorNotFound", args);
    }

    // ... 其他方法

    /**
     * 获取消息（内部使用）
     */
    private static String get(String key) {
        return Holder.getMessage(key);
    }

    /**
     * 获取带参消息（内部使用）
     */
    private static String get(String key, Object[] args) {
        return Holder.getMessage(key, args);
    }

    /**
     * 内部Holder，用于静态方法访问Spring Bean
     */
    @Component
    static class Holder {
        private static Holder instance;

        @Autowired
        private MessageSource messageSource;

        @PostConstruct
        public void init() {
            instance = this;
        }

        static String getMessage(String key) {
            return getMessage(key, null);
        }

        static String getMessage(String key, Object[] args) {
            return instance.messageSource.getMessage(key, args, key, LocaleContextHolder.getLocale());
        }
    }
}
```

### 运行方式

```bash
# 手动执行生成任务
.\gradlew.bat generateI18n

# 或在编译时自动执行
.\gradlew.bat compileJava
```

---

## 使用示例

### 基本用法

```java
// 无参消息
String msg = I18n.commonSuccess();
// 输出: Operation successful

// 带参数消息
String errorMsg = I18n.validationErrorAgeInvalid(18, 100);
// 输出: Age must be between 18 and 100
```

### 在 Controller 中使用

```java
package com.{company}.{project}.user.controller;

import com.{company}.{project}.common.core.Result;
import com.{company}.{project}.common.I18n;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/users")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/{id}")
    public Result<UserVO> getUserById(@PathVariable Long id) {
        UserVO user = userService.getDetail(id);
        return Result.success(I18n.commonSuccess(), user);
    }

    @GetMapping
    public Result<List<UserVO>> listUsers() {
        List<UserVO> users = userService.list();
        return Result.success(I18n.commonSuccess(), users);
    }
}
```

### 在 Service 中使用

```java
import com.{company}.{project}.common.I18n;

@Service
public class UserService {

    public void createUser(CreateUserRequest request) {
        if (request.getName() == null || request.getName().isEmpty()) {
            String errorMsg = I18n.userErrorUsernameRequired();
            throw new BizException(ErrorCode.USER_USERNAME_EMPTY, errorMsg);
        }
        // 业务逻辑...
    }

    public void validateAge(int age) {
        if (age < 18 || age > 100) {
            // 带参数消息：直接传参
            String errorMsg = I18n.validationErrorAgeInvalid(18, 100);
            throw new BizException(ErrorCode.PARAM_ERROR, errorMsg);
        }
    }
}
```

---

## 常见问题排查

### Q1: 消息不显示，显示的是 key 值

**原因：** 资源包配置路径错误，或 key 不存在

**解决：**
```java
// 检查配置
messageSource.setBasename("i18n/message");  // 正确：目录/基础名

// 检查文件位置
src/main/resources/i18n/message.properties  // 正确位置
```

### Q2: 异步调用时消息获取失败

**原因：** ThreadLocal 中的 Locale 在异步线程中丢失

**解决：** 配置 TaskDecorator 自动传递上下文

```java
@Configuration
@EnableAsync
public class AsyncConfig implements AsyncConfigurer {

    @Override
    public Executor getAsyncExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);
        executor.setMaxPoolSize(10);
        executor.setQueueCapacity(25);
        executor.setThreadNamePrefix("async-");
        executor.setTaskDecorator(new LocaleAwareTaskDecorator());
        executor.initialize();
        return executor;
    }

    /**
     * 装饰器：在主线程和子线程之间传递 Locale 和请求上下文
     */
    static class LocaleAwareTaskDecorator implements TaskDecorator {

        @Override
        public Runnable decorate(Runnable runnable) {
            RequestAttributes parentRequestAttributes = RequestContextHolder.getRequestAttributes();
            Locale parentLocale = LocaleContextHolder.getLocale();

            return () -> {
                try {
                    if (parentRequestAttributes != null) {
                        RequestContextHolder.setRequestAttributes(parentRequestAttributes);
                    }
                    LocaleContextHolder.setLocale(parentLocale);
                    runnable.run();
                } finally {
                    RequestContextHolder.resetRequestAttributes();
                    LocaleContextHolder.resetLocaleContext();
                }
            };
        }
    }
}
```

**使用：**
```java
@Async
public void sendWelcomeEmail() {
    // 直接使用，无需手动传递 Locale
    String msg = I18n.welcomeMessage();
}
```

**注意：** 如果使用自定义线程池（如 `@Async("taskExecutor")`），需确保该线程池也设置了 `TaskDecorator`。



