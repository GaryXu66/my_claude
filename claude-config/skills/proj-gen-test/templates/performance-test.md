# 性能测试模板

## 测试目的

验证接口在指定负载下的响应时间、并发能力和系统稳定性。

---

## 测试工具

- **JMeter** - 推荐用于复杂的性能测试场景
- **Apache Bench (ab)** - 简单快速的基准测试
- **Gatling** - 高性能负载测试工具

---

## JMeter 测试计划配置

### 基础配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jmeterTestPlan version="1.2" properties="5.0">
  <hashTree>
    <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="性能测试计划">
      <elementProp name="TestPlan.user_defined_variables" elementType="Arguments">
        <collectionProp name="Arguments.arguments">
          <elementProp name="BASE_URL" elementType="Argument">
            <stringProp name="Argument.name">BASE_URL</stringProp>
            <stringProp name="Argument.value">http://localhost:8080</stringProp>
          </elementProp>
          <elementProp name="TARGET_RESPONSE_TIME" elementType="Argument">
            <stringProp name="Argument.name">TARGET_RESPONSE_TIME</stringProp>
            <stringProp name="Argument.value">100</stringProp>
          </elementProp>
        </collectionProp>
      </elementProp>
    </TestPlan>
    <hashTree>
      <!-- 线程组配置 -->
      <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="用户组">
        <stringProp name="ThreadGroup.num_threads">100</stringProp>
        <stringProp name="ThreadGroup.ramp_time">10</stringProp>
        <stringProp name="ThreadGroup.duration">60</stringProp>
      </ThreadGroup>
    </hashTree>
  </hashTree>
</jmeterTestPlan>
```

### HTTP 请求配置

```xml
<HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP请求">
  <stringProp name="HTTPSampler.domain">${BASE_URL}</stringProp>
  <stringProp name="HTTPSampler.path">/api/endpoint</stringProp>
  <stringProp name="HTTPSampler.method">GET</stringProp>
</HTTPSamplerProxy>
```

### 响应断言

```xml
<!-- 响应时间断言 -->
<DurationAssertion guiclass="DurationAssertionGui" testclass="DurationAssertion" testname="响应时间断言">
  <stringProp name="DurationAssertion.duration">${TARGET_RESPONSE_TIME}</stringProp>
</DurationAssertion>

<!-- 响应码断言 -->
<ResponseAssertion guiclass="AssertionGui" testclass="ResponseAssertion" testname="响应码断言">
  <collectionProp name="Asserion.test_strings">
    <stringProp name="49586">200</stringProp>
  </collectionProp>
</ResponseAssertion>
```

---

## Apache Bench 使用示例

```bash
# 基础测试
ab -n 1000 -c 10 http://localhost:8080/api/endpoint

# 参数说明
# -n: 总请求数
# -c: 并发数
# -t: 测试超时时间(秒)
# -p: POST请求体文件
# -T: Content-Type

# POST 请求测试
ab -n 1000 -c 10 -p data.json -T "application/json" http://localhost:8080/api/endpoint

# 带认证头测试
ab -n 1000 -c 10 -H "Authorization: Bearer token123" http://localhost:8080/api/endpoint
```

---

## 性能指标说明

| 指标 | 说明 | 目标值示例 |
|------|------|-----------|
| 响应时间 | 单次请求处理时间 | < 100ms (P95) |
| TPS/QPS | 每秒事务/查询数 | 根据业务需求 |
| 错误率 | 失败请求占比 | < 1% |
| 并发用户数 | 同时在线用户数 | 根据需求 |

---

## 测试场景设计

### 场景1: 响应时间测试

```
目标: 验证单次请求响应时间 < 100ms
方法: 固定并发10，持续1分钟
断言: P95响应时间 < 100ms
```

### 场景2: 并发测试

```
目标: 验证系统支持100并发用户
方法: 并发从10逐步增加到100
断言: 错误率 < 1%
```

### 场景3: 压力测试

```
目标: 找出系统极限承载能力
方法: 并发从100逐步增加到500
断言: 记录系统开始出现大量错误的并发数
```

---

## 测试报告模板

```markdown
# 性能测试报告

## 测试环境
- 服务器配置: CPU/内存/磁盘
- 数据库配置: 版本/连接池
- 测试时间: YYYY-MM-DD HH:mm:ss

## 测试结果

### 场景1: 响应时间测试
| 指标 | 目标 | 实测 | 结果 |
|------|------|------|------|
| P50响应时间 | < 50ms | XXms | 通过/不通过 |
| P95响应时间 | < 100ms | XXms | 通过/不通过 |
| P99响应时间 | < 200ms | XXms | 通过/不通过 |

### 场景2: 并发测试
| 并发数 | TPS | 错误率 | 结果 |
|--------|-----|--------|------|
| 10 | XX | X% | 通过 |
| 50 | XX | X% | 通过 |
| 100 | XX | X% | 通过 |

### 场景3: 压力测试
系统最大并发能力: XXX 用户
瓶颈分析: [CPU/内存/数据库/网络]

## 结论
- [ ] 性能满足需求
- [ ] 存在性能瓶颈，需优化
```

---

## 注意事项

1. **测试数据** - 使用与生产环境相近的数据量
2. **预热** - 正式测试前先运行几分钟预热
3. **资源监控** - 测试时监控 CPU、内存、数据库连接数
4. **网络隔离** - 避免网络波动影响测试结果
5. **多次测试** - 每个场景运行3次取平均值

---

## 测试报告

性能测试完成后，将结果汇总到 [测试报告模板](test-report.md) 中。
