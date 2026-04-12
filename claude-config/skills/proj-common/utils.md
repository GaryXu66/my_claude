# 工具类

## AssertUtils 断言工具

```java
package com.{company}.{project}.common.utils;

import com.{company}.{project}.common.core.ErrorCode;
import com.{company}.{project}.common.exception.BizException;

/**
 * 断言工具类
 * <p>
 * 阿里巴巴Java开发手册规范说明：
 * 1. 工具类如果为静态方法调用，需要私有化构造函数
 * 2. 判断相等使用Objects.equals，避免空指针
 * 3. 集合判断使用工具类isEmpty，禁止size()==0
 * </p>
 */
public final class AssertUtils {

    /**
     * 私有构造函数，防止实例化
     */
    private AssertUtils() {
        throw new UnsupportedOperationException("Utility class cannot be instantiated");
    }

    /**
     * 断言对象非空
     *
     * @param obj        待校验对象
     * @param errorCode  错误码
     */
    public static void notNull(Object obj, ErrorCode errorCode) {
        if (obj == null) {
            throw new BizException(errorCode);
        }
    }

    /**
     * 断言对象非空（自定义消息）
     *
     * @param obj        待校验对象
     * @param errorCode  错误码
     * @param message    错误信息
     */
    public static void notNull(Object obj, ErrorCode errorCode, String message) {
        if (obj == null) {
            throw new BizException(errorCode, message);
        }
    }

    /**
     * 断言条件为真
     *
     * @param condition  待校验条件
     * @param errorCode  错误码
     */
    public static void isTrue(boolean condition, ErrorCode errorCode) {
        if (!condition) {
            throw new BizException(errorCode);
        }
    }

    /**
     * 断言条件为真（自定义消息）
     *
     * @param condition  待校验条件
     * @param errorCode  错误码
     * @param message    错误信息
     */
    public static void isTrue(boolean condition, ErrorCode errorCode, String message) {
        if (!condition) {
            throw new BizException(errorCode, message);
        }
    }

    /**
     * 断言字符串非空
     *
     * @param str        待校验字符串
     * @param errorCode  错误码
     */
    public static void notEmpty(String str, ErrorCode errorCode) {
        if (str == null || str.trim().isEmpty()) {
            throw new BizException(errorCode);
        }
    }
}
```

---

## RedisUtils Redis工具类

```java
package com.{company}.{project}.common.utils;

import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Component;
import java.util.concurrent.TimeUnit;

/**
 * Redis工具类
 * <p>
 * 阿里巴巴Java开发手册规范说明：
 * 1. Redis key设置过期时间，避免内存溢出
 * 2. 合理设置过期时间加随机值，防止缓存雪崩
 * 3. 大批量key查询使用pipeline，减少网络IO
 * </p>
 */
@Component
@RequiredArgsConstructor
public class RedisUtils {

    private final StringRedisTemplate redisTemplate;

    /**
     * 设置键值对
     *
     * @param key   键
     * @param value 值
     */
    public void set(String key, String value) {
        redisTemplate.opsForValue().set(key, value);
    }

    /**
     * 设置键值对（带过期时间）
     *
     * @param key     键
     * @param value   值
     * @param timeout 过期时间（秒）
     */
    public void set(String key, String value, long timeout) {
        redisTemplate.opsForValue().set(key, value, timeout, TimeUnit.SECONDS);
    }

    /**
     * 获取值
     *
     * @param key 键
     * @return 值
     */
    public String get(String key) {
        return redisTemplate.opsForValue().get(key);
    }

    /**
     * 删除键
     *
     * @param key 键
     * @return 是否删除成功
     */
    public Boolean delete(String key) {
        return redisTemplate.delete(key);
    }

    /**
     * 判断键是否存在
     *
     * @param key 键
     * @return 是否存在
     */
    public Boolean hasKey(String key) {
        return redisTemplate.hasKey(key);
    }

    /**
     * 设置过期时间
     *
     * @param key     键
     * @param timeout 过期时间（秒）
     * @return 是否设置成功
     */
    public Boolean expire(String key, long timeout) {
        return redisTemplate.expire(key, timeout, TimeUnit.SECONDS);
    }

    /**
     * 自增计数
     *
     * @param key 键
     * @return 自增后的值
     */
    public Long increment(String key) {
        return redisTemplate.opsForValue().increment(key);
    }

    /**
     * 自增计数（指定步长）
     *
     * @param key   键
     * @param delta 步长
     * @return 自增后的值
     */
    public Long increment(String key, long delta) {
        return redisTemplate.opsForValue().increment(key, delta);
    }

    /**
     * 获取过期时间（秒）
     *
     * @param key 键
     * @return 过期时间（-1表示永不过期，-2表示键不存在）
     */
    public Long getExpire(String key) {
        return redisTemplate.getExpire(key, TimeUnit.SECONDS);
    }
}
```

---

## RedisKeys Redis Key 常量

```java
package com.{company}.{project}.common.constant;

/**
 * Redis Key 常量
 */
public class RedisKeys {

    private static final String PREFIX = "{project}:";

    // ========== 用户相关 ==========
    public static final String USER_TOKEN = PREFIX + "user:token:";
    public static final String USER_INFO = PREFIX + "user:info:";

    // ========== 验证码 ==========
    public static final String CAPTCHA = PREFIX + "captcha:";
    public static final String SMS_CODE = PREFIX + "sms:code:";

    // ========== 限流 ==========
    public static final String RATE_LIMIT = PREFIX + "rate:limit:";
}
```

---

```
