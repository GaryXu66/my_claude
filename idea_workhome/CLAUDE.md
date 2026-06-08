# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 在此代码库中工作时提供指导。

## 代码库概述

这是一个本地仓库，都属于云之家企业协作平台的后端服务。**每一个都是独立的 Java 微服务的单体仓库，每个项目都是独立的 Maven 或 Gradle 工程，无构建层面的父子关系。** 项目按业务域组织，独立部署。

## 构建系统

具体的构建命令，参考每个独立工程目录下的CLAUDE.md。

### 构建前必读 IDEA 配置

**在测试、构建任何工程之前，必须先读取该工程 `.idea` 目录下的配置文件**，获取本地构建环境信息。

需要关注的配置文件：

| 文件 | 关键信息 |
|------|----------|
| `.idea/gradle.xml` | Gradle 安装路径（`gradleHome`）、Gradle JVM 版本、Gradle Distribution 类型 |
| `.idea/misc.xml` | 项目 JDK 版本（`project-jdk-name`）、语言级别（`languageLevel`） |
| `.idea/compiler.xml` | 字节码编译目标级别（`bytecodeTargetLevel`） |
| `.idea/encodings.xml` | 项目文件编码 |

这些配置反映了你在 IDEA 中的本地构建环境设置，构建命令应基于这些配置执行。

## 架构设计参考

**在进行需求分析、架构设计、技术选型、代码开发时，必须参考以下架构设计手册作为方法论和决策依据**：

- `docs/架构设计参考手册-AI优化版.md` - 涵盖架构基础概念、DDD领域驱动设计、架构风格与模式、企业架构设计实战、架构落地技术等完整知识体系，附决策检查清单和组件性能量级参考
- `docs/architecture-doc-images/` - 架构手册配套图片目录（26张架构图）

**使用规则**：
1. **需求分析阶段**：参考手册第三章「需求分析方法论」，使用需求分析模板和二维需求矩阵进行结构化分析
2. **架构设计阶段**：参考手册第六章「DDD领域驱动设计」和第八章「企业架构设计实战」，遵循战略设计→战术设计流程
3. **代码开发阶段**：参考手册第六章的 DDD 分层架构规则（应用层做编排、领域层承载核心逻辑）和附录A的代码实现检查清单
4. **技术选型阶段**：参考手册第七章「架构风格与模式」对比表和附录B「组件性能量级参考」
5. **测试验证阶段**：参考附录A的决策检查清单进行自检，参考附录B的组件性能量级进行容量评估

## 业务领域

本代码库包含 30+ 业务领域，完整业务领域信息，请参阅：
- `工程领域业务说明.md` - 该文档归纳了每个工程项目所属的业务领域，以及一个简短的描述信息
- `工程领域业务说明-完整版.md` - 比较详细的归纳了每个工程的核心业务逻辑、核心业务数据表、架构信息

**重要，当进行需求分析，架构设计，bug排查、代码开发、业务问题等操作之前，都要先参考完整的业务领域信息，找到业务领域后，需要参考该领域所有工程的业务逻辑。如果涉及多个业务领域，则需要把多个领域的信息都关联分析** 梳理完整的业务流程图（业务流程图往往是跨多个业务工程的）
当业务流程跨多个工程时，则需要继续分析关联工程的源码。

## 服务间调用约定

当分析服务间的 HTTP 调用时，URL 格式通常为：
```
http://域名/contextPath/vv/kk?aa
```

**contextPath 匹配规则：**

1. **优先匹配工程名**：contextPath 通常与项目工程名一致
   - 例如：调用 `http://xxx/attendance-service/api/v1/...` 时，优先在 `attendance-service` 工程中查找

2. **查找配置文件**：如果工程名不匹配，则依次遍历工程目录查找配置文件
   - 查找位置：`src/main/resources/application.yml` 或 `application.properties`
   - 配置项：`server.servlet.context-path` 或 `server.context-path`
   - 根据配置文件中的 contextPath 匹配实际的 URL 路径

**示例：**
```yaml
# application.yml
server:
  servlet:
    context-path: /attendance-api  # 实际 contextPath
```

如果 URL 是 `http://xxx/attendance-api/v1/...`，但工程目录名是 `attendance-service`，则需要通过配置文件确认。

## 开发流程

 进入项目目录：
   ```bash
   cd /data/home/heng_xu/work/program/idea_workhome/{项目名}
   ```

## 文档输出规范

**所有生成的方案文档（架构图、设计文档、分析报告等），统一输出到：**

```
/data/home/heng_xu/work/program/idea_workhome/docs/
```

不得输出到其他目录，也不得直接放在 `idea_workhome` 根目录下。

---

## 用户组织领域架构规范

**完整架构图参见**：`用户组织领域架构图.md`

在进行用户组织领域相关的业务代码开发、需求分析、架构设计时，**必须遵循该文件中定义的层级关系**，具体规则如下：

### 层级定义与工程归属

| 层级 | 工程 | 职责边界 |
|------|------|----------|
| 网关层 | `api-gateway`、`openaccess` | 流量入口、路由、鉴权、限流，不承载业务逻辑 |
| 对外开放应用层 | `openorg`、`openadmin`、`openimport`、`openid`、`opendata-control`、`space`、`innermanage` | 对外暴露 REST 接口，编排业务逻辑，调用核心层 |
| 数据同步层 | `opensync`、`syncdata`、`openimport`（Kafka消费端） | 处理第三方系统的增量/全量同步，不直接对外暴露接口 |
| 核心业务层 | `usercore-service`、`passport-service`、`baseaccount-service`、`stakeholder-service`、`orgunit-rest` | 领域核心数据存储与业务规则，仅通过 RPC 对内暴露 |
| 状态通知层 | `statusUser-rest`、`statusNotice-rest` | 用户状态管理与变更广播，单向依赖核心层 |
| 支撑服务层 | `authserver`、`invite-service`、`snsapi` | 通用支撑能力，被多个上层服务复用 |

### 开发时必须遵守的层级规则

1. **禁止跨层调用**：上层可以调用下层，**严禁下层反向调用上层**。
   - ❌ `usercore-service` 不能调用 `openorg`
   - ❌ `baseaccount-service` 不能调用 `openimport`
   - ✅ `openorg` 可以调用 `usercore-service`

2. **新增接口归属判断**：
   - 需要对第三方/外部系统暴露的接口 → 放在**对外开放应用层**（如 `openorg`、`openimport`）
   - 仅供内部服务间调用的接口 → 放在**核心业务层**，以 RPC 形式暴露
   - 第三方数据同步逻辑 → 放在**数据同步层**（`openimport` 或 `opensync`）
   - 用户状态相关变更通知 → 放在**状态通知层**

3. **新增工程归属判断**：新增工程前，先判断其职责属于哪个层级，不得随意创建游离于架构之外的服务。

4. **数据写入路径**：所有用户/组织数据的最终写入必须经过 `usercore-service`，不得绕过核心层直接操作数据库。

5. **认证链路**：对外开放应用层的接口需要 Token 校验时，统一调用 `authserver`，不得自行实现 Token 逻辑。

---

## 全局开发规范

### 依赖使用规范

#### 1. JSON 序列化库

**禁止使用**阿里巴巴的 `fastjson`，**统一使用**云之家内部封装的 `yzj-fastjson`。

```gradle
// ✅ 正确：使用 YZJ FastJSON
api "com.yunzhijia:yzj-fastjson:1.2.83"

// ❌ 错误：禁止使用 Alibaba FastJSON
// api "com.alibaba:fastjson:1.2.83"
```

**原因**：
- 安全考虑：`yzj-fastjson` 是基于 `fastjson` 的安全加固版本
- 统一依赖管理：避免不同项目使用不同版本的 `fastjson` 导致兼容性问题
- 内部组件集成：`yzj-fastjson` 与云之家其他组件深度集成

#### 2. HTTP 客户端 SDK

**禁止使用**原生 `apache httpclient`，**统一使用**云之家内部封装的 `yzj-httpclient` 系列组件。

```gradle
// ✅ 正确：使用 YZJ HttpClient（内部 HTTP 客户端 SDK）
api "com.yunzhijia.component.httpclient:yzj-httpclient:${yzjHttpClientVersion}"
api "com.yunzhijia.component.httpclient:yzj-httpmime:${yzjHttpClientVersion}"
api "com.yunzhijia.component.httpclient:yzj-httpclient-service-manager:${yzjHttpClientVersion}"
api "com.yunzhijia.component.httpclient:yzj-httpasyncclient:${yzjHttpClientVersion}"
api "com.yunzhijia.component.httpclient:yzj-httpclient-cache:${yzjHttpClientVersion}"

// ❌ 错误：禁止直接使用 Apache HttpClient
// api "org.apache.httpcomponents:httpclient:4.5.8"
// api "org.apache.httpcomponents:httpmime:4.5.8"
```

**版本要求**：底层基于 `Apache HttpClient 4.5.8`

**原因**：
- 统一配置管理：`yzj-httpclient` 封装了统一的超时、重试、连接池配置
- 服务治理集成：与云之家服务发现、负载均衡、熔断降级机制集成
- 监控可观测性：内置请求追踪、性能监控、日志记录
- 安全性：内置 SSL 配置、证书校验、敏感信息脱敏

### 代码规范

#### 1. 导入规范

```java
// ✅ 正确
import com.alibaba.fastjson.JSON;  // 实际引用自 yzj-fastjson

// ❌ 错误：不要显式引用 fastjson 包名（即使实际是 yzj-fastjson）
import com.alibaba.fastjson2.JSON;
```

#### 2. JSON 使用示例

```java
// ✅ 正确：使用 yzj-fastjson
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.alibaba.fastjson.JSONArray;

String json = JSON.toJSONString(object);
MyObject obj = JSON.parseObject(json, MyObject.class);
```

#### 3. HttpClient 使用示例

```java
// ✅ 正确：使用 yzj-httpclient
import com.yunzhijia.component.httpclient.HttpClient;
import com.yunzhijia.component.httpclient.HttpRequest;

// 通过服务管理器获取 HttpClient 实例
HttpClient httpClient = HttpClientServiceManager.getInstance().getHttpClient();
```

### 依赖版本管理

各工程应在 `gradle.properties` 或 `build.gradle` 中统一定义依赖版本：

```properties
# build.gradle 示例
yzjFastjsonVersion = "1.2.83"
yzjHttpClientVersion = "4.5.8"
```

### Kafka 配置规范

#### 核心原则

**每个业务模块的 Kafka 配置必须独立，不与 `spring.kafka` 公用**

**原因**：
1. 云之家有多套 Kafka 集群（不同业务域、不同环境）
2. 避免配置耦合，便于后续业务切分和集群迁移
3. 不同业务场景有不同的消费策略（批量大/小、延迟敏感度等）

#### 配置结构规范

```yaml
# ❌ 错误：使用 spring.kafka 公用配置
spring:
  kafka:
    bootstrap-servers: kafka01:9092,kafka02:9092
    consumer:
      auto-offset-reset: latest

业务模块:
  topic: xxx
  group: xxx

# ✅ 正确：业务模块独立配置 Kafka 集群
业务模块:
  # 第一套 Kafka 集群（如：消费上游事件）
  xxx-kafka-bootstrap-servers: kafka01.cluster-a:9092,kafka02.cluster-a:9092
  xxx-consumer-topic: TOPIC_A
  xxx-consumer-group: service-name-xxx-consumer
  xxx-consumer:
    auto-offset-reset: latest
    enable-auto-commit: true
    session-timeout-ms: 120000
    heartbeat-interval-ms: 10000
    max-poll-interval-ms: 1800000
    max-poll-records: 50

  # 第二套 Kafka 集群（如：AI 分析、下游转发）
  yyy-kafka-bootstrap-servers: kafka01.cluster-b:9092,kafka02.cluster-b:9092
  yyy-producer-topic: TOPIC_B
  yyy-consumer-topic: TOPIC_B
  yyy-consumer-group: service-name-yyy-consumer
  yyy-consumer:
    auto-offset-reset: latest
    enable-auto-commit: true
    max-poll-records: 10
```

#### 配置命名规范

| 配置项 | 命名格式 | 示例 |
|--------|----------|------|
| bootstrap-servers | `{业务名}-kafka-bootstrap-servers` | `xt-msg-kafka-bootstrap-servers` |
| consumer topic | `{业务名}-consumer-topic` | `xt-msg-consumer-topic` |
| producer topic | `{业务名}-producer-topic` | `ai-analysis-producer-topic` |
| consumer group | `{业务名}-consumer-group` 或 `{业务名}-topic-group` | `xt-msg-consumer-group` |
| consumer 配置块 | `{业务名}-consumer` | `xt-msg-consumer` |

#### Properties 类规范

```java
@Data
@Component
@ConfigurationProperties(prefix = "业务模块")
public class XxxProperties {

    // 第一套 Kafka 集群
    private String xxxKafkaBootstrapServers;
    private String xxxConsumerTopic;
    private String xxxConsumerGroup;
    private XxxConsumer xxxConsumer = new XxxConsumer();

    // 第二套 Kafka 集群（如有）
    private String yyyKafkaBootstrapServers;
    private String yyyProducerTopic;
    private String yyyConsumerTopic;
    private String yyyConsumerGroup;
    private YyyConsumer yyyConsumer = new YyyConsumer();

    @Data
    public static class XxxConsumer {
        private String autoOffsetReset = "latest";
        private boolean enableAutoCommit = true;
        private int sessionTimeoutMs = 120000;
        private int heartbeatIntervalMs = 10000;
        private int maxPollIntervalMs = 1800000;
        private int maxPollRecords = 50;
    }
}
```

#### KafkaConfig 类规范

```java
@Configuration
@RequiredArgsConstructor
public class XxxKafkaConfig {

    private final XxxProperties properties;

    // 第一套集群 ConsumerFactory
    @Bean
    public ConsumerFactory<String, String> xxxConsumerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(BOOTSTRAP_SERVERS_CONFIG, properties.getXxxKafkaBootstrapServers());
        props.put(GROUP_ID_CONFIG, properties.getXxxConsumerGroup());
        // 其他 consumer 配置...
        return new DefaultKafkaConsumerFactory<>(props);
    }

    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, String> xxxKafkaListenerContainerFactory() {
        ConcurrentKafkaListenerContainerFactory<String, String> factory = new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(xxxConsumerFactory());
        return factory;
    }

    // 第二套集群 ProducerFactory / ConsumerFactory（如有）
    @Bean
    public ProducerFactory<String, String> yyyProducerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(BOOTSTRAP_SERVERS_CONFIG, properties.getYyyKafkaBootstrapServers());
        // 其他 producer 配置...
        return new DefaultKafkaProducerFactory<>(props);
    }
}
```

#### KafkaListener 注解规范

```java
// ❌ 错误：使用默认 containerFactory（会公用 spring.kafka 配置）
@KafkaListener(topics = "xxx", groupId = "xxx")

// ✅ 正确：显式指定业务模块的 containerFactory
@KafkaListener(
    topics = "${业务模块.xxx-consumer-topic}",
    groupId = "${业务模块.xxx-consumer-group}",
    containerFactory = "xxxKafkaListenerContainerFactory"
)
```

### 检查清单

在代码审查（Code Review）时，请检查：

**依赖规范**：
- [ ] 是否使用了 `com.alibaba:fastjson` 而非 `com.yunzhijia:yzj-fastjson`
- [ ] 是否直接使用了 `org.apache.httpcomponents:httpclient`
- [ ] `yzj-fastjson` 版本是否为 `1.2.83`
- [ ] `yzj-httpclient` 版本是否为 `4.5.8`
- [ ] 是否有其他违反开发规范的依赖引用

**Kafka 配置规范**：
- [ ] 是否使用了 `spring.kafka.*` 公用配置（业务模块应独立配置）
- [ ] 业务模块的 Kafka bootstrap-servers 是否独立配置
- [ ] KafkaListener 是否显式指定了 `containerFactory` 参数
- [ ] 配置命名是否符合 `{集群名}-kafka-bootstrap-servers` 等规范
- [ ] 多套 Kafka 集群是否都有独立的 bootstrap-servers 配置

**用户组织领域架构规范**：
- [ ] 新增接口是否放在了正确的层级工程中
- [ ] 是否存在下层调用上层的情况
- [ ] 用户/组织数据写入是否经过 `usercore-service`
- [ ] Token 校验是否统一走 `authserver`
- [ ] 第三方同步逻辑是否放在了 `openimport` 或 `opensync`