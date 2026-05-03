# 全局开发规范

## 执行构建命令前必读 IDEA 配置

**在对任何工程执行 Maven、Gradle、Java 命令之前，必须先读取该工程 `.idea` 目录下的配置文件**，根据本地 IDEA 配置来确定实际使用的工具路径和版本，然后再执行对应命令。

### 需要读取的配置文件

| 文件 | 关键信息 |
|------|----------|
| `.idea/gradle.xml` | Gradle 安装路径（`gradleHome`）、Gradle JVM 版本、Gradle Distribution 类型 |
| `.idea/misc.xml` | 项目 JDK 版本（`project-jdk-name`）、语言级别（`languageLevel`） |
| `.idea/compiler.xml` | 字节码编译目标级别（`bytecodeTargetLevel`） |
| `.idea/maven.xml` | Maven 安装路径（`mavenHome`）、Maven JVM 配置 |

### 执行规则

1. **读取配置**：进入工程目录后，先读取 `.idea/` 下相关配置文件
2. **确定 JDK**：从 `misc.xml` 的 `project-jdk-name` 获取 JDK 版本，找到本地对应的 JDK 路径
3. **确定构建工具路径**：
   - Gradle 工程：从 `gradle.xml` 的 `gradleHome` 获取 Gradle 安装路径，使用该路径下的 gradle 可执行文件，或使用工程自带的 `gradlew`
   - Maven 工程：从 `maven.xml` 的 `mavenHome` 获取 Maven 安装路径，使用该路径下的 `mvn` 可执行文件
4. **执行命令**：基于上述配置执行构建、测试、编译等命令

### 示例

```bash
# 读取配置后，使用本地 IDEA 配置的 JDK 和 Gradle 执行
JAVA_HOME=/path/from/idea/config /path/from/idea/gradleHome/bin/gradle build

# 或使用 gradlew（推荐，gradlew 会使用 gradle-wrapper.properties 中指定的版本）
JAVA_HOME=/path/from/idea/config ./gradlew build
```
