# 安全测试检查清单

## 使用说明

本清单用于验证对外接口的安全性，应在代码开发完成后逐项检查。

---

## 1. 输入验证

### 1.1 参数类型校验
- [ ] 所有输入参数都有类型校验
- [ ] 数字参数有范围限制
- [ ] 枚举参数限制在预定义值范围内
- [ ] 日期格式校验

### 1.2 参数长度限制
- [ ] 字符串参数有最大长度限制
- [ ] 数组/集合参数有大小限制
- [ ] 文件上传有大小限制

### 1.3 特殊字符过滤
- [ ] 过滤 SQL 注入字符（`'`, `"`, `;`, `--`, `/*`, `*/`）
- [ ] 过滤 XSS 攻击字符（`<`, `>`, `"`, `'`, `javascript:`, `onerror=`）
- [ ] 过滤路径遍历字符（`../`, `..\`）
- [ ] 过滤 Log4j/Logback 注入字符（`${jndi:}`）

---

## 2. SQL 注入防护

- [ ] 使用参数化查询或 MyBatis `#{}` 占位符
- [ ] 禁止拼接 SQL 语句
- [ ] 对模糊查询进行特殊处理

```java
// 正确示例
@Select("SELECT * FROM user WHERE name = #{name}")
User getByName(String name);

// 错误示例
@Select("SELECT * FROM user WHERE name = '${name}'")
User getByName(String name);
```

---

## 3. XSS 攻击防护

- [ ] 输出时进行 HTML 转义
- [ ] 富文本内容使用白名单过滤
- [ ] 设置 Content-Type 响应头
- [ ] JSON 响应设置 `Content-Type: application/json`

---

## 4. 认证授权（如适用）

### 4.1 认证
- [ ] 敏感接口需要认证
- [ ] Token/Session 有效期验证
- [ ] 登录失败次数限制

### 4.2 授权
- [ ] 接口权限校验
- [ ] 数据权限校验（只能访问自己的数据）
- [ ] 越权访问测试

---

## 5. CSRF 防护（如适用）

- [ ] 表单提交使用 CSRF Token
- [ ] 验证 Referer 请求头
- [ ] SameSite Cookie 属性设置

---

## 6. 敏感信息保护

- [ ] 密码加密存储（BCrypt/Argon2）
- [ ] 日志中不打印敏感信息（密码、Token、身份证号）
- [ ] 响应中不返回敏感字段
- [ ] 异常信息不泄露内部实现

---

## 7. 请求频率限制

- [ ] 对外接口有频率限制
- [ ] 防止暴力破解
- [ ] 防止 CC 攻击

---

## 8. HTTP 安全头

- [ ] `X-Content-Type-Options: nosniff`
- [ ] `X-Frame-Options: DENY/SAMEORIGIN`
- [ ] `X-XSS-Protection: 1; mode=block`
- [ ] `Strict-Transport-Security`（HTTPS）

---

## 9. 文件上传安全（如适用）

- [ ] 文件类型校验（扩展名 + Magic Number）
- [ ] 文件大小限制
- [ ] 文件名重命名（防止路径遍历）
- [ ] 上传目录禁止执行权限
- [ ] 病毒扫描（可选）

---

## 10. 第三方依赖安全

- [ ] 定期更新依赖版本
- [ ] 扫描已知漏洞（CVE）
- [ ] 移除不使用的依赖

---

## 测试用例参考

### SQL 注入测试
```
1' OR '1'='1
1' UNION SELECT * FROM user--
' OR 1=1--
admin'--
```

### XSS 测试
```
<script>alert('xss')</script>
<img src=x onerror=alert('xss')>
<svg onload=alert('xss')>
javascript:alert('xss')
```

### 路径遍历测试
```
../../../etc/passwd
..\..\..\..\windows\system32\drivers\etc\hosts
%2e%2e%2f
```

### 超长输入测试
```
生成 10000+ 字符的字符串
测试所有输入字段
```

---
