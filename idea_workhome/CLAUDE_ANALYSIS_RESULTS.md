# Java 微服务项目 - 深度代码分析报告

> 生成时间：2026-03-26 23:17:58
> 项目总数：198
> 分析维度：Controller/Service/Entity 数量、数据库表提取、业务逻辑推断

---

### 3gol

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【3gol】在企业微服务架构中承担业务服务职责。 模块划分为：access2, kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `containing`: 业务数据
  - `t_app_tag`: 应用信息
  - `t_3g_ol_customer`: 业务数据
  - `t_3g_ol_appclient`: 应用信息
  - `t_3g_ec_org`: 组织信息
  - `t_kis_apply`: 应用信息
  - `t_tag_sort`: 业务数据
  - `t_app_config`: 应用信息
  - `query`: 业务数据
  - `t_app_params_define`: 应用信息

---

### YzjJustAuth

- **业务定位**: 面向企业办公场景的认证授权服务
- **核心功能**: 用户认证鉴权
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【YzjJustAuth】在企业微服务架构中承担认证授权职责。 模块划分为：zhyd。 提供统一的用户认证授权能力，支持多端登录、Token 管理、权限校验、会话管理等安全机制，保障系统访问安全。
- **数据库表**:
  - `mica`: 业务数据
  - `2021`: 业务数据
  - `renren`: 业务数据

---

### adware

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 7个 Controller, 8个 Service, 0个 Entity
- **核心业务逻辑**: 【adware】在企业微服务架构中承担业务服务职责。 提供7个 REST 接口供前端和第三方系统调用。 包含8个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `there`: 业务数据
  - `end`: 业务数据
  - `one`: 业务数据
  - `and`: 业务数据
  - `symboltable`: 业务数据
  - `scratch`: 业务数据
  - `the`: 业务数据
  - `start`: 业务数据
  - `different`: 业务数据
  - `this`: 业务数据

---

### ai-faq-service

- **业务定位**: 面向企业办公场景的AI 智能服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 6个 Controller, 10个 Service, 0个 Entity
- **核心业务逻辑**: 【ai-faq-service】在企业微服务架构中承担AI 智能职责。 提供6个 REST 接口供前端和第三方系统调用。 包含10个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 集成大模型能力，提供智能问答、助手服务、自动化处理等 AI 增强功能，支持 MCP 协议与各类 AI 服务对接。
- **数据库表**:
  - `update`: 业务数据

---

### ai-platform-service

- **业务定位**: 面向企业办公场景的AI 智能服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 5个 Controller, 12个 Service, 0个 Entity
- **核心业务逻辑**: 【ai-platform-service】在企业微服务架构中承担AI 智能职责。 提供5个 REST 接口供前端和第三方系统调用。 包含12个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 集成大模型能力，提供智能问答、助手服务、自动化处理等 AI 增强功能，支持 MCP 协议与各类 AI 服务对接。
- **数据库表**:
  - `user`: 用户信息
  - `update`: 业务数据

---

### anonymity-rest

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 0个 Controller, 11个 Service, 6个 Entity
- **核心业务逻辑**: 【anonymity-rest】在企业微服务架构中承担业务服务职责。 包含11个业务服务类，实现核心业务逻辑处理。 设计6个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `report_record`: 报表数据
  - `anonymity_convention`: 业务数据
  - `top_heart_voice`: 业务数据
  - `可能已经被别人的回复更新了`: 业务数据
  - `anonymity_record`: 业务数据
  - `来分页`: 业务数据
  - `network_stat`: 业务数据
  - `anonymity_ban_post_record`: 业务数据

---

### api-gateway

- **业务定位**: 面向企业办公场景的网关服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 1个 Controller, 20个 Service, 0个 Entity
- **核心业务逻辑**: 【api-gateway】在企业微服务架构中承担网关服务职责。 提供1个 REST 接口供前端和第三方系统调用。 包含20个业务服务类，实现核心业务逻辑处理。 模块划分为：springframework, weibo, yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `cache`: 业务数据
  - `the`: 业务数据

---

### apns-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 0个 Controller, 4个 Service, 1个 Entity
- **核心业务逻辑**: 【apns-service】在企业微服务架构中承担业务服务职责。 包含4个业务服务类，实现核心业务逻辑处理。 设计1个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `json`: 业务数据
  - `push_device`: 业务数据

---

### appmanage

- **业务定位**: 面向企业办公场景的应用管理服务
- **核心功能**: REST API 接口, 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 18个 Controller, 30个 Service, 1个 Entity
- **核心业务逻辑**: 【appmanage】在企业微服务架构中承担应用管理职责。 提供18个 REST 接口供前端和第三方系统调用。 包含30个业务服务类，实现核心业务逻辑处理。 设计1个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `t_data_dic`: 业务数据
  - `t_recommend_dushuka`: 业务数据
  - `t_recommend_share_record`: 业务数据
  - `t_user_feedback`: 用户信息
  - `t_company_service`: 业务数据
  - `redis`: 业务数据
  - `t_cust_endyear_info`: 业务数据
  - `t_fp_user`: 用户信息
  - `t_recommend_mobile_record`: 业务数据
  - `t_recommend_voice`: 业务数据

---

### appservice

- **业务定位**: 面向企业办公场景的应用管理服务
- **核心功能**: REST API 接口, 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 47个 Controller, 76个 Service, 5个 Entity
- **核心业务逻辑**: 【appservice】在企业微服务架构中承担应用管理职责。 提供47个 REST 接口供前端和第三方系统调用。 包含76个业务服务类，实现核心业务逻辑处理。 设计5个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `t_data_dic`: 业务数据
  - `t_app_tag`: 应用信息
  - `tableannotation`: 业务数据
  - `redis`: 业务数据
  - `t_appcenter_params_define`: 应用信息
  - `error`: 业务数据
  - `t_app_audit`: 应用信息
  - `mongodb`: 业务数据
  - `jsonobject`: 业务数据
  - `developerinfo`: 业务数据

---

### attendance

- **业务定位**: 面向企业办公场景的考勤管理服务
- **核心功能**: REST API 接口, 业务逻辑处理, 打卡记录管理
- **技术栈**: Spring Boot
- **代码规模**: 58个 Controller, 28个 Service, 0个 Entity
- **核心业务逻辑**: 【attendance】在企业微服务架构中承担考勤管理职责。 提供58个 REST 接口供前端和第三方系统调用。 包含28个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 支撑企业员工考勤管理全流程，包括打卡记录、排班管理、统计分析、异常处理等核心业务场景，与用户服务、组织服务、消息服务等协同工作。
- **数据库表**:
  - `是否接受修改通知`: 业务数据
  - `authtable`: 认证信息
  - `auth`: 认证信息
  - `border`: 业务数据
  - `attmanagervo`: 业务数据
  - `yyyy`: 业务数据
  - `bizattmanager`: 业务数据
  - `col`: 业务数据
  - `row`: 业务数据
  - `api`: 业务数据

---

### attendance-context

- **业务定位**: 面向企业办公场景的考勤管理服务
- **核心功能**: 打卡记录管理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【attendance-context】在企业微服务架构中承担考勤管理职责。 模块划分为：yunzhijia。 支撑企业员工考勤管理全流程，包括打卡记录、排班管理、统计分析、异常处理等核心业务场景，与用户服务、组织服务、消息服务等协同工作。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### attendance-manage

- **业务定位**: 面向企业办公场景的考勤管理服务
- **核心功能**: REST API 接口, 业务逻辑处理, 打卡记录管理
- **技术栈**: Spring Boot
- **代码规模**: 7个 Controller, 27个 Service, 0个 Entity
- **核心业务逻辑**: 【attendance-manage】在企业微服务架构中承担考勤管理职责。 提供7个 REST 接口供前端和第三方系统调用。 包含27个业务服务类，实现核心业务逻辑处理。 模块划分为：dangdang, yunzhijia。 支撑企业员工考勤管理全流程，包括打卡记录、排班管理、统计分析、异常处理等核心业务场景，与用户服务、组织服务、消息服务等协同工作。
- **数据库表**:
  - `toupdate`: 业务数据
  - `update`: 业务数据
  - `version`: 业务数据
  - `attendanceshift`: 考勤记录
  - `begin`: 业务数据

---

### attendance-service

- **业务定位**: 面向企业办公场景的考勤管理服务
- **核心功能**: 业务逻辑处理, 数据持久化, 打卡记录管理
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 0个 Controller, 131个 Service, 54个 Entity
- **核心业务逻辑**: 【attendance-service】在企业微服务架构中承担考勤管理职责。 包含131个业务服务类，实现核心业务逻辑处理。 设计54个数据实体类，映射数据库表结构。 模块划分为：kingdee。 支撑企业员工考勤管理全流程，包括打卡记录、排班管理、统计分析、异常处理等核心业务场景，与用户服务、组织服务、消息服务等协同工作。
- **数据库表**:
  - `attendance_org_cache`: 组织信息
  - `cloud_flow_clear_leave_synced`: 业务数据
  - `attendance_daily_active_network`: 考勤记录
  - `attendance_user_shift`: 用户信息
  - `authtableold`: 认证信息
  - `from`: 业务数据
  - `attendance`: 考勤记录
  - `baidu`: 业务数据
  - `clock_in_vip_network`: 业务数据
  - `att_aid_position`: 业务数据

---

### attendance-signapi

- **业务定位**: 面向企业办公场景的考勤管理服务
- **核心功能**: REST API 接口, 业务逻辑处理, 打卡记录管理
- **技术栈**: Spring Boot
- **代码规模**: 2个 Controller, 6个 Service, 0个 Entity
- **核心业务逻辑**: 【attendance-signapi】在企业微服务架构中承担考勤管理职责。 提供2个 REST 接口供前端和第三方系统调用。 包含6个业务服务类，实现核心业务逻辑处理。 模块划分为：springframework, yunzhijia。 支撑企业员工考勤管理全流程，包括打卡记录、排班管理、统计分析、异常处理等核心业务场景，与用户服务、组织服务、消息服务等协同工作。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### authserver

- **业务定位**: 面向企业办公场景的认证授权服务
- **核心功能**: 业务逻辑处理, 用户认证鉴权
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 8个 Service, 0个 Entity
- **核心业务逻辑**: 【authserver】在企业微服务架构中承担认证授权职责。 包含8个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 提供统一的用户认证授权能力，支持多端登录、Token 管理、权限校验、会话管理等安全机制，保障系统访问安全。
- **数据库表**:
  - `redis`: 业务数据
  - `update`: 业务数据

---

### backend-skill

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 2个 Controller, 1个 Service, 1个 Entity
- **核心业务逻辑**: 【backend-skill】在企业微服务架构中承担业务服务职责。 提供2个 REST 接口供前端和第三方系统调用。 包含1个业务服务类，实现核心业务逻辑处理。 设计1个数据实体类，映射数据库表结构。 模块划分为：example。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `t_user`: 用户信息
  - `public`: 业务数据

---

### base-document

- **业务定位**: 面向企业办公场景的文档管理服务
- **核心功能**: REST API 接口, 业务逻辑处理, 文件上传下载
- **技术栈**: Spring Boot
- **代码规模**: 1个 Controller, 29个 Service, 0个 Entity
- **核心业务逻辑**: 【base-document】在企业微服务架构中承担文档管理职责。 提供1个 REST 接口供前端和第三方系统调用。 包含29个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 提供企业文档全生命周期管理，支持文件上传下载、在线预览、版本控制、权限管理等功能，与云存储服务深度集成。
- **数据库表**:
  - `url`: 业务数据
  - `requesturi`: 业务数据
  - `which`: 业务数据
  - `the`: 业务数据
  - `executable`: 业务数据
  - `storage`: 业务数据
  - `files`: 文件信息

---

### base-mail

- **业务定位**: 面向企业办公场景的邮件服务服务
- **核心功能**: 业务逻辑处理, 消息发送推送
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 6个 Service, 0个 Entity
- **核心业务逻辑**: 【base-mail】在企业微服务架构中承担邮件服务职责。 包含6个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 统一消息发送通道，支持短信、邮件、Push 等多种触达方式，提供模板管理、发送记录、状态回执等完整能力。
- **数据库表**:
  - `emaillastsucmsg`: 消息记录
  - `json`: 业务数据
  - `the`: 业务数据
  - `data`: 业务数据
  - `body`: 业务数据

---

### base-rest

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 0个 Controller, 7个 Service, 1个 Entity
- **核心业务逻辑**: 【base-rest】在企业微服务架构中承担业务服务职责。 包含7个业务服务类，实现核心业务逻辑处理。 设计1个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `guidance`: 业务数据

---

### base-session

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 5个 Service, 0个 Entity
- **核心业务逻辑**: 【base-session】在企业微服务架构中承担业务服务职责。 包含5个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `cas`: 业务数据
  - `subdomain`: 业务数据

---

### base-stakeholder

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 0个 Controller, 100个 Service, 14个 Entity
- **核心业务逻辑**: 【base-stakeholder】在企业微服务架构中承担业务服务职责。 包含100个业务服务类，实现核心业务逻辑处理。 设计14个数据实体类，映射数据库表结构。 模块划分为：kingdee, javatuples。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `tokenexpdate`: Token 信息
  - `user_phone_change_history`: 用户信息
  - `private`: 业务数据
  - `a_p_i_invoke_log`: 日志记录
  - `a_p_i_operate`: 业务数据
  - `from`: 业务数据
  - `thirdparty_m_p_config`: 配置信息
  - `micro_network`: 业务数据
  - `application`: 应用信息
  - `all`: 业务数据

---

### baseaccount

- **业务定位**: 面向企业办公场景的账号管理服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 25个 Service, 0个 Entity
- **核心业务逻辑**: 【baseaccount】在企业微服务架构中承担账号管理职责。 包含25个业务服务类，实现核心业务逻辑处理。 模块划分为：springframework, kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `如果为`: 业务数据
  - `that`: 业务数据
  - `symb`: 业务数据
  - `queue`: 业务数据
  - `extends`: 业务数据
  - `应该也会`: 业务数据
  - `defaultphotoid`: 业务数据
  - `user`: 用户信息
  - `remote`: 业务数据
  - `byte`: 业务数据

---

### baseaccount-api

- **业务定位**: 面向企业办公场景的账号管理服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【baseaccount-api】在企业微服务架构中承担账号管理职责。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### baseaccount-kms-service

- **业务定位**: 面向企业办公场景的账号管理服务
- **核心功能**: REST API 接口, 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 1个 Controller, 10个 Service, 6个 Entity
- **核心业务逻辑**: 【baseaccount-kms-service】在企业微服务架构中承担账号管理职责。 提供1个 REST 接口供前端和第三方系统调用。 包含10个业务服务类，实现核心业务逻辑处理。 设计6个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `t_app_id`: 应用信息
  - `t_app_group`: 群组信息
  - `t_l2_key`: 业务数据
  - `t_l2_domain`: 业务数据
  - `t_group_app`: 群组信息
  - `t_group_key`: 群组信息

---

### baseaccount-service

- **业务定位**: 面向企业办公场景的账号管理服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【baseaccount-service】在企业微服务架构中承担账号管理职责。 模块划分为：weibo, kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `headers`: 业务数据
  - `here`: 业务数据

---

### birthday-rest

- **业务定位**: 面向企业办公场景的生日关怀服务
- **核心功能**: 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 0个 Controller, 7个 Service, 9个 Entity
- **核心业务逻辑**: 【birthday-rest】在企业微服务架构中承担生日关怀职责。 包含7个业务服务类，实现核心业务逻辑处理。 设计9个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `thanks_expression`: 业务数据
  - `push_birthday_wish_failure`: 业务数据
  - `birthday_record`: 业务数据
  - `send_to_birthday_subscription`: 业务数据
  - `thanks`: 业务数据
  - `festival_wishes`: 业务数据
  - `user_extend`: 用户信息
  - `wishes_card`: 业务数据
  - `birthday_user_network_map`: 用户信息

---

### bosspub-boot

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 4个 Controller, 15个 Service, 0个 Entity
- **核心业务逻辑**: 【bosspub-boot】在企业微服务架构中承担业务服务职责。 提供4个 REST 接口供前端和第三方系统调用。 包含15个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `genernatefrom`: 业务数据
  - `update`: 业务数据
  - `from`: 业务数据

---

### camunda-demo

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【camunda-demo】在企业微服务架构中承担业务服务职责。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### carereport-service

- **业务定位**: 面向企业办公场景的报表统计服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 8个 Controller, 14个 Service, 0个 Entity
- **核心业务逻辑**: 【carereport-service】在企业微服务架构中承担报表统计职责。 提供8个 REST 接口供前端和第三方系统调用。 包含14个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `current_timestamp`: 业务数据
  - `cache`: 业务数据
  - `update`: 业务数据

---

### cloudauth

- **业务定位**: 面向企业办公场景的认证授权服务
- **核心功能**: REST API 接口, 业务逻辑处理, 用户认证鉴权
- **技术栈**: Spring Boot
- **代码规模**: 9个 Controller, 13个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudauth】在企业微服务架构中承担认证授权职责。 提供9个 REST 接口供前端和第三方系统调用。 包含13个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 提供统一的用户认证授权能力，支持多端登录、Token 管理、权限校验、会话管理等安全机制，保障系统访问安全。
- **数据库表**:
  - `remove`: 业务数据
  - `success`: 业务数据
  - `add`: 业务数据
  - `addsearchrule`: 业务数据
  - `removesearchrule`: 业务数据
  - `multiple`: 业务数据
  - `describing`: 业务数据
  - `update`: 业务数据

---

### cloudflow-common

- **业务定位**: 面向企业办公场景的流程引擎服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 2个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudflow-common】在企业微服务架构中承担流程引擎职责。 包含2个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee, google, yunzhijia。 内置流程引擎和表单引擎，支持业务流程编排、审批流转、动态表单配置，与企业现有系统无缝集成。
- **数据库表**:
  - `json`: 业务数据
  - `redis`: 业务数据
  - `from`: 业务数据

---

### cloudflow-elastic-job

- **业务定位**: 面向企业办公场景的流程引擎服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudflow-elastic-job】在企业微服务架构中承担流程引擎职责。 模块划分为：weibo, yunzhijia。 内置流程引擎和表单引擎，支持业务流程编排、审批流转、动态表单配置，与企业现有系统无缝集成。
- **数据库表**:
  - `updatestatistic`: 业务数据
  - `server`: 业务数据
  - `outofmemoryerror`: 业务数据
  - `callback`: 业务数据
  - `the`: 业务数据
  - `getupdate`: 业务数据
  - `update`: 业务数据

---

### cloudflow-flowcenter-service

- **业务定位**: 面向企业办公场景的流程引擎服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 17个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudflow-flowcenter-service】在企业微服务架构中承担流程引擎职责。 包含17个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 内置流程引擎和表单引擎，支持业务流程编排、审批流转、动态表单配置，与企业现有系统无缝集成。
- **数据库表**:
  - `new`: 业务数据
  - `update`: 业务数据

---

### cloudflow-form-api

- **业务定位**: 面向企业办公场景的接口服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudflow-form-api】在企业微服务架构中承担接口服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `lusheng`: 业务数据
  - `private`: 业务数据

---

### cloudflow-form-service

- **业务定位**: 面向企业办公场景的流程引擎服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 63个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudflow-form-service】在企业微服务架构中承担流程引擎职责。 包含63个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 内置流程引擎和表单引擎，支持业务流程编排、审批流转、动态表单配置，与企业现有系统无缝集成。
- **数据库表**:
  - `total`: 业务数据
  - `public`: 业务数据
  - `formconstants`: 业务数据
  - `com`: 业务数据
  - `与对应匹配的部门进行包含关系的过滤`: 业务数据
  - `value`: 业务数据
  - `aggreverify2update`: 业务数据
  - `the`: 业务数据
  - `readonly`: 业务数据
  - `2023`: 业务数据

---

### cloudflow-template-service

- **业务定位**: 面向企业办公场景的流程引擎服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 49个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudflow-template-service】在企业微服务架构中承担流程引擎职责。 包含49个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 内置流程引擎和表单引擎，支持业务流程编排、审批流转、动态表单配置，与企业现有系统无缝集成。
- **数据库表**:
  - `set`: 业务数据
  - `otherwise`: 业务数据
  - `setupdatefilevalue`: 文件信息
  - `setelement`: 业务数据
  - `codeupdate`: 业务数据
  - `formtemplate`: 业务数据
  - `formrouter`: 业务数据
  - `list`: 业务数据
  - `error`: 业务数据
  - `getupdate`: 业务数据

---

### cloudflow-workflow-api

- **业务定位**: 面向企业办公场景的接口服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudflow-workflow-api】在企业微服务架构中承担接口服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `20171106`: 业务数据
  - `lusheng`: 业务数据
  - `20201203`: 业务数据

---

### cloudflow-workflow-service

- **业务定位**: 面向企业办公场景的流程引擎服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 197个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudflow-workflow-service】在企业微服务架构中承担流程引擎职责。 包含197个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 内置流程引擎和表单引擎，支持业务流程编排、审批流转、动态表单配置，与企业现有系统无缝集成。
- **数据库表**:
  - `extends`: 业务数据
  - `201804`: 业务数据
  - `多了个参数`: 业务数据
  - `updateact`: 业务数据
  - `askopinionphraseupdate`: 业务数据
  - `error`: 业务数据
  - `20170824`: 业务数据
  - `approveinfoupdate`: 应用信息
  - `from`: 业务数据
  - `20170914`: 业务数据

---

### cloudgroup-web

- **业务定位**: 面向企业办公场景的群组管理服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 2个 Controller, 5个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudgroup-web】在企业微服务架构中承担群组管理职责。 提供2个 REST 接口供前端和第三方系统调用。 包含5个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `jsonobject`: 业务数据
  - `update`: 业务数据
  - `from`: 业务数据

---

### cloudplatform

- **业务定位**: 面向企业办公场景的表单服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 6个 Controller, 11个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudplatform】在企业微服务架构中承担表单服务职责。 提供6个 REST 接口供前端和第三方系统调用。 包含11个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 内置流程引擎和表单引擎，支持业务流程编排、审批流转、动态表单配置，与企业现有系统无缝集成。
- **数据库表**:
  - `ziputils`: 业务数据
  - `jsonarray`: 业务数据
  - `jsonobject`: 业务数据
  - `update`: 业务数据

---

### cloudportal

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 9个 Controller, 28个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudportal】在企业微服务架构中承担业务服务职责。 提供9个 REST 接口供前端和第三方系统调用。 包含28个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `cloudwork`: 业务数据
  - `update`: 业务数据

---

### cloudwork

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 62个 Controller, 1个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudwork】在企业微服务架构中承担业务服务职责。 提供62个 REST 接口供前端和第三方系统调用。 包含1个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `cache`: 业务数据

---

### cloudwork-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 5个 Service, 0个 Entity
- **核心业务逻辑**: 【cloudwork-service】在企业微服务架构中承担业务服务职责。 包含5个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `updates`: 业务数据
  - `jsonobject`: 业务数据
  - `newcard`: 业务数据
  - `update`: 业务数据

---

### collaborative-component

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 6个 Controller, 18个 Service, 0个 Entity
- **核心业务逻辑**: 【collaborative-component】在企业微服务架构中承担业务服务职责。 提供6个 REST 接口供前端和第三方系统调用。 包含18个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `update`: 业务数据

---

### colleague-rest

- **业务定位**: 面向企业办公场景的同事管理服务
- **核心功能**: 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 0个 Controller, 16个 Service, 18个 Entity
- **核心业务逻辑**: 【colleague-rest】在企业微服务架构中承担同事管理职责。 包含16个业务服务类，实现核心业务逻辑处理。 设计18个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `thanks_expression`: 业务数据
  - `role_config`: 配置信息
  - `favors_account`: 账号信息
  - `可能已经被别人的回复更新了`: 业务数据
  - `param`: 业务数据
  - `mention_record`: 业务数据
  - `network_stat`: 业务数据
  - `colleague_circle_visit`: 业务数据
  - `homeconfiginfo`: 配置信息
  - `visit_stat_daily`: 业务数据

---

### comment

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 3个 Controller, 11个 Service, 0个 Entity
- **核心业务逻辑**: 【comment】在企业微服务架构中承担业务服务职责。 提供3个 REST 接口供前端和第三方系统调用。 包含11个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `server`: 业务数据
  - `jsonobject`: 业务数据
  - `cache`: 业务数据
  - `jsonarray`: 业务数据
  - `update`: 业务数据

---

### common

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 1个 Controller, 80个 Service, 1个 Entity
- **核心业务逻辑**: 【common】在企业微服务架构中承担业务服务职责。 提供1个 REST 接口供前端和第三方系统调用。 包含80个业务服务类，实现核心业务逻辑处理。 设计1个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `tableannotation`: 业务数据
  - `queue`: 业务数据
  - `redis`: 业务数据
  - `beans`: 业务数据
  - `city_user_task`: 用户信息
  - `t_3g_appinfo`: 应用信息
  - `json`: 业务数据
  - `common_dao`: 业务数据
  - `t_bd_org`: 组织信息
  - `jsonobject`: 业务数据

---

### common-cache

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【common-cache】在企业微服务架构中承担业务服务职责。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### data-operation-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 8个 Controller, 41个 Service, 0个 Entity
- **核心业务逻辑**: 【data-operation-service】在企业微服务架构中承担业务服务职责。 提供8个 REST 接口供前端和第三方系统调用。 包含41个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `imrecord`: 业务数据
  - `cache`: 业务数据
  - `update`: 业务数据
  - `newdayvisitrecord`: 业务数据

---

### data-processing

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 1个 Controller, 4个 Service, 0个 Entity
- **核心业务逻辑**: 【data-processing】在企业微服务架构中承担业务服务职责。 提供1个 REST 接口供前端和第三方系统调用。 包含4个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `t_cust_auth_info`: 认证信息
  - `redis`: 业务数据
  - `server`: 业务数据

---

### data-rest

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 0个 Controller, 6个 Service, 3个 Entity
- **核心业务逻辑**: 【data-rest】在企业微服务架构中承担业务服务职责。 包含6个业务服务类，实现核心业务逻辑处理。 设计3个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `data_source_mongo`: 业务数据
  - `data_user_visit`: 用户信息
  - `data_query_log`: 日志记录

---

### dbmv

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 4个 Controller, 15个 Service, 24个 Entity
- **核心业务逻辑**: 【dbmv】在企业微服务架构中承担业务服务职责。 提供4个 REST 接口供前端和第三方系统调用。 包含15个业务服务类，实现核心业务逻辑处理。 设计24个数据实体类，映射数据库表结构。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `import_table_task`: 任务信息
  - `prop`: 业务数据
  - `import_task`: 任务信息
  - `data_log`: 日志记录
  - `dto`: 业务数据
  - `export_table_task_status`: 任务信息
  - `如果为`: 业务数据
  - `import_pkg`: 业务数据
  - `implements`: 业务数据
  - `import_db_task`: 任务信息

---

### developerplatform-service

- **业务定位**: 面向企业办公场景的表单服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 10个 Controller, 22个 Service, 0个 Entity
- **核心业务逻辑**: 【developerplatform-service】在企业微服务架构中承担表单服务职责。 提供10个 REST 接口供前端和第三方系统调用。 包含22个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 内置流程引擎和表单引擎，支持业务流程编排、审批流转、动态表单配置，与企业现有系统无缝集成。
- **数据库表**:
  - `app`: 应用信息
  - `update`: 业务数据

---

### doc-convert

- **业务定位**: 面向企业办公场景的文档管理服务
- **核心功能**: REST API 接口, 业务逻辑处理, 文件上传下载
- **技术栈**: Spring Boot
- **代码规模**: 3个 Controller, 1个 Service, 0个 Entity
- **核心业务逻辑**: 【doc-convert】在企业微服务架构中承担文档管理职责。 提供3个 REST 接口供前端和第三方系统调用。 包含1个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 提供企业文档全生命周期管理，支持文件上传下载、在线预览、版本控制、权限管理等功能，与云存储服务深度集成。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### docrest

- **业务定位**: 面向企业办公场景的文档管理服务
- **核心功能**: REST API 接口, 业务逻辑处理, 文件上传下载
- **技术栈**: Spring Boot
- **代码规模**: 33个 Controller, 12个 Service, 0个 Entity
- **核心业务逻辑**: 【docrest】在企业微服务架构中承担文档管理职责。 提供33个 REST 接口供前端和第三方系统调用。 包含12个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 提供企业文档全生命周期管理，支持文件上传下载、在线预览、版本控制、权限管理等功能，与云存储服务深度集成。
- **数据库表**:
  - `format`: 业务数据
  - `redis`: 业务数据
  - `memory`: 业务数据
  - `the`: 业务数据
  - `queue`: 业务数据
  - `sort`: 业务数据
  - `update`: 业务数据

---

### favorite-boot

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 6个 Controller, 19个 Service, 0个 Entity
- **核心业务逻辑**: 【favorite-boot】在企业微服务架构中承担业务服务职责。 提供6个 REST 接口供前端和第三方系统调用。 包含19个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `jsonobject`: 业务数据
  - `update`: 业务数据

---

### fileclean-private

- **业务定位**: 面向企业办公场景的文件管理服务
- **核心功能**: REST API 接口, 业务逻辑处理, 文件上传下载
- **技术栈**: Spring Boot
- **代码规模**: 2个 Controller, 1个 Service, 0个 Entity
- **核心业务逻辑**: 【fileclean-private】在企业微服务架构中承担文件管理职责。 提供2个 REST 接口供前端和第三方系统调用。 包含1个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 提供企业文档全生命周期管理，支持文件上传下载、在线预览、版本控制、权限管理等功能，与云存储服务深度集成。
- **数据库表**:
  - `update`: 业务数据

---

### fileclean-private-hx

- **业务定位**: 面向企业办公场景的文件管理服务
- **核心功能**: REST API 接口, 业务逻辑处理, 文件上传下载
- **技术栈**: Spring Boot
- **代码规模**: 2个 Controller, 3个 Service, 0个 Entity
- **核心业务逻辑**: 【fileclean-private-hx】在企业微服务架构中承担文件管理职责。 提供2个 REST 接口供前端和第三方系统调用。 包含3个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 提供企业文档全生命周期管理，支持文件上传下载、在线预览、版本控制、权限管理等功能，与云存储服务深度集成。
- **数据库表**:
  - `update`: 业务数据

---

### gateway-admin

- **业务定位**: 面向企业办公场景的网关服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 15个 Controller, 6个 Service, 0个 Entity
- **核心业务逻辑**: 【gateway-admin】在企业微服务架构中承担网关服务职责。 提供15个 REST 接口供前端和第三方系统调用。 包含6个业务服务类，实现核心业务逻辑处理。 模块划分为：springframework, yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `update`: 业务数据
  - `one`: 业务数据

---

### group-rest

- **业务定位**: 面向企业办公场景的群组管理服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 2个 Service, 0个 Entity
- **核心业务逻辑**: 【group-rest】在企业微服务架构中承担群组管理职责。 包含2个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `jointype`: 业务数据
  - `groupname`: 群组信息
  - `group`: 群组信息

---

### groupassist

- **业务定位**: 面向企业办公场景的群组管理服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 28个 Controller, 38个 Service, 0个 Entity
- **核心业务逻辑**: 【groupassist】在企业微服务架构中承担群组管理职责。 提供28个 REST 接口供前端和第三方系统调用。 包含38个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `propertykeyconst`: 业务数据
  - `cardid`: 业务数据
  - `personids`: 业务数据
  - `web`: 业务数据
  - `assembledupdate`: 业务数据
  - `修改通知`: 业务数据
  - `remind`: 业务数据
  - `update`: 业务数据

---

### im

- **业务定位**: 面向企业办公场景的即时通讯服务
- **核心功能**: REST API 接口, 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 21个 Controller, 15个 Service, 1个 Entity
- **核心业务逻辑**: 【im】在企业微服务架构中承担即时通讯职责。 提供21个 REST 接口供前端和第三方系统调用。 包含15个业务服务类，实现核心业务逻辑处理。 设计1个数据实体类，映射数据库表结构。 模块划分为：kingdee。 提供 IM 即时通讯能力，支持单聊、群聊、消息推送、已读回执、历史消息等功能，保障企业内外部沟通顺畅。
- **数据库表**:
  - `java`: 业务数据
  - `gettokenbysecurecode`: Token 信息
  - `its`: 业务数据
  - `the`: 业务数据
  - `personal`: 业务数据
  - `heartbeat`: 业务数据
  - `chat_token`: Token 信息

---

### image

- **业务定位**: 面向企业办公场景的即时通讯服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 5个 Controller, 4个 Service, 0个 Entity
- **核心业务逻辑**: 【image】在企业微服务架构中承担即时通讯职责。 提供5个 REST 接口供前端和第三方系统调用。 包含4个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 提供 IM 即时通讯能力，支持单聊、群聊、消息推送、已读回执、历史消息等功能，保障企业内外部沟通顺畅。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### image-service

- **业务定位**: 面向企业办公场景的即时通讯服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 1个 Service, 0个 Entity
- **核心业务逻辑**: 【image-service】在企业微服务架构中承担即时通讯职责。 包含1个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 提供 IM 即时通讯能力，支持单聊、群聊、消息推送、已读回执、历史消息等功能，保障企业内外部沟通顺畅。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### img-convert

- **业务定位**: 面向企业办公场景的即时通讯服务
- **核心功能**: REST API 接口
- **技术栈**: Spring Boot
- **代码规模**: 1个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【img-convert】在企业微服务架构中承担即时通讯职责。 提供1个 REST 接口供前端和第三方系统调用。 模块划分为：yunzhijia。 提供 IM 即时通讯能力，支持单聊、群聊、消息推送、已读回执、历史消息等功能，保障企业内外部沟通顺畅。
- **数据库表**:
  - `cache`: 业务数据
  - `local`: 业务数据

---

### imsdk

- **业务定位**: 面向企业办公场景的即时通讯服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 11个 Controller, 6个 Service, 0个 Entity
- **核心业务逻辑**: 【imsdk】在企业微服务架构中承担即时通讯职责。 提供11个 REST 接口供前端和第三方系统调用。 包含6个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 提供 IM 即时通讯能力，支持单聊、群聊、消息推送、已读回执、历史消息等功能，保障企业内外部沟通顺畅。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### imsdk-service

- **业务定位**: 面向企业办公场景的即时通讯服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 6个 Service, 0个 Entity
- **核心业务逻辑**: 【imsdk-service】在企业微服务架构中承担即时通讯职责。 包含6个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 提供 IM 即时通讯能力，支持单聊、群聊、消息推送、已读回执、历史消息等功能，保障企业内外部沟通顺畅。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### innermanage

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 75个 Controller, 55个 Service, 4个 Entity
- **核心业务逻辑**: 【innermanage】在企业微服务架构中承担业务服务职责。 提供75个 REST 接口供前端和第三方系统调用。 包含55个业务服务类，实现核心业务逻辑处理。 设计4个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `t_base_label_type`: 业务数据
  - `t_cust_auth_info`: 认证信息
  - `redis`: 业务数据
  - `t_appcenter_params_define`: 应用信息
  - `ziputils`: 业务数据
  - `exception`: 业务数据
  - `longname`: 业务数据
  - `query`: 业务数据
  - `t_app_params_define`: 应用信息
  - `t_app_params_value`: 应用信息

---

### intelligentbulletin-web

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 34个 Controller, 66个 Service, 0个 Entity
- **核心业务逻辑**: 【intelligentbulletin-web】在企业微服务架构中承担业务服务职责。 提供34个 REST 接口供前端和第三方系统调用。 包含66个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee, yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `url`: 业务数据
  - `that`: 业务数据
  - `server`: 业务数据
  - `their`: 业务数据
  - `getfrom`: 业务数据
  - `favorite`: 业务数据
  - `from`: 业务数据
  - `other`: 业务数据
  - `update`: 业务数据

---

### invite

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 6个 Controller, 1个 Service, 0个 Entity
- **核心业务逻辑**: 【invite】在企业微服务架构中承担业务服务职责。 提供6个 REST 接口供前端和第三方系统调用。 包含1个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### invite-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 0个 Controller, 15个 Service, 3个 Entity
- **核心业务逻辑**: 【invite-service】在企业微服务架构中承担业务服务职责。 包含15个业务服务类，实现核心业务逻辑处理。 设计3个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `cache`: 业务数据
  - `group_qrcode`: 群组信息
  - `inner_group_qrcode`: 群组信息
  - `qrcode_join_record`: 业务数据

---

### jsonrpc4j

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【jsonrpc4j】在企业微服务架构中承担业务服务职责。 模块划分为：googlecode。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `json`: 业务数据
  - `ioexception`: 业务数据
  - `throwable`: 业务数据
  - `the`: 业务数据

---

### linkcenter

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 21个 Controller, 41个 Service, 0个 Entity
- **核心业务逻辑**: 【linkcenter】在企业微服务架构中承担业务服务职责。 提供21个 REST 接口供前端和第三方系统调用。 包含41个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee, yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `that`: 业务数据
  - `gettable`: 业务数据
  - `genernatefrom`: 业务数据
  - `getfrom`: 业务数据
  - `from`: 业务数据
  - `byte`: 业务数据
  - `for`: 业务数据
  - `update`: 业务数据

---

### linkerp-admin-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 30个 Controller, 39个 Service, 0个 Entity
- **核心业务逻辑**: 【linkerp-admin-service】在企业微服务架构中承担业务服务职责。 提供30个 REST 接口供前端和第三方系统调用。 包含39个业务服务类，实现核心业务逻辑处理。 模块划分为：weibo, yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `rabbitmq`: 业务数据
  - `queue`: 业务数据
  - `method`: 业务数据
  - `update`: 业务数据
  - `更新时间`: 业务数据

---

### linkerp-datasource-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 9个 Controller, 14个 Service, 0个 Entity
- **核心业务逻辑**: 【linkerp-datasource-service】在企业微服务架构中承担业务服务职责。 提供9个 REST 接口供前端和第三方系统调用。 包含14个业务服务类，实现核心业务逻辑处理。 模块划分为：weibo, yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `update`: 业务数据
  - `beanutils`: 业务数据

---

### linkerp-demo

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 3个 Service, 0个 Entity
- **核心业务逻辑**: 【linkerp-demo】在企业微服务架构中承担业务服务职责。 包含3个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### livestream

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 38个 Controller, 87个 Service, 0个 Entity
- **核心业务逻辑**: 【livestream】在企业微服务架构中承担业务服务职责。 提供38个 REST 接口供前端和第三方系统调用。 包含87个业务服务类，实现核心业务逻辑处理。 模块划分为：dangdang, yufu, yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `rfc1779symbols`: 业务数据
  - `ascii`: 业务数据
  - `extensions`: 业务数据
  - `string`: 业务数据
  - `来区分直播和视频会议`: 业务数据
  - `byte`: 业务数据
  - `rfc2253symbols`: 业务数据
  - `var4`: 业务数据
  - `defaultlookup`: 业务数据
  - `var1`: 业务数据

---

### logather

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口
- **技术栈**: Spring Boot
- **代码规模**: 1个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【logather】在企业微服务架构中承担业务服务职责。 提供1个 REST 接口供前端和第三方系统调用。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### manage-v2

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【manage-v2】在企业微服务架构中承担业务服务职责。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `for`: 业务数据
  - `string`: 业务数据
  - `returned`: 业务数据

---

### meeting-rpc-service

- **业务定位**: 面向企业办公场景的会议管理服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 6个 Controller, 17个 Service, 0个 Entity
- **核心业务逻辑**: 【meeting-rpc-service】在企业微服务架构中承担会议管理职责。 提供6个 REST 接口供前端和第三方系统调用。 包含17个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `toupdate`: 业务数据
  - `update`: 业务数据
  - `alive`: 业务数据
  - `garyxu`: 业务数据
  - `join`: 业务数据
  - `fail`: 业务数据

---

### microblog

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 49个 Controller, 1个 Service, 0个 Entity
- **核心业务逻辑**: 【microblog】在企业微服务架构中承担业务服务职责。 提供49个 REST 接口供前端和第三方系统调用。 包含1个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `cache`: 业务数据

---

### microblog-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 0个 Controller, 131个 Service, 15个 Entity
- **核心业务逻辑**: 【microblog-service】在企业微服务架构中承担业务服务职责。 包含131个业务服务类，实现核心业务逻辑处理。 设计15个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `redis`: 业务数据
  - `microblog`: 日志记录
  - `floors_settings`: 设置信息
  - `todo_info`: 业务数据
  - `results`: 业务数据
  - `every`: 业务数据
  - `microblog_topic_app_config`: 日志记录
  - `all`: 业务数据
  - `section_attachment`: 业务数据
  - `the`: 业务数据

---

### miscellanea

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口
- **技术栈**: Spring Boot
- **代码规模**: 8个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【miscellanea】在企业微服务架构中承担业务服务职责。 提供8个 REST 接口供前端和第三方系统调用。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `json`: 业务数据

---

### mongosync

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 9个 Service, 0个 Entity
- **核心业务逻辑**: 【mongosync】在企业微服务架构中承担业务服务职责。 包含9个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `fetchservice`: 业务数据
  - `newupdate`: 业务数据
  - `the`: 业务数据
  - `cache`: 业务数据
  - `update`: 业务数据

---

### msgassist

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口
- **技术栈**: Spring Boot
- **代码规模**: 20个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【msgassist】在企业微服务架构中承担业务服务职责。 提供20个 REST 接口供前端和第三方系统调用。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `propertykeyconst`: 业务数据
  - `data`: 业务数据

---

### msgassist-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 25个 Service, 0个 Entity
- **核心业务逻辑**: 【msgassist-service】在企业微服务架构中承担业务服务职责。 包含25个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee, yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `源语言`: 业务数据
  - `scc`: 业务数据
  - `emoji`: 业务数据
  - `jsonobject`: 业务数据

---

### nacos-console

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 8个 Controller, 2个 Service, 0个 Entity
- **核心业务逻辑**: 【nacos-console】在企业微服务架构中承担业务服务职责。 提供8个 REST 接口供前端和第三方系统调用。 包含2个业务服务类，实现核心业务逻辑处理。 模块划分为：alibaba。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `password`: 业务数据
  - `succeed`: 业务数据
  - `successfully`: 业务数据
  - `user`: 用户信息
  - `header`: 业务数据

---

### newmicroblog-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 0个 Controller, 130个 Service, 15个 Entity
- **核心业务逻辑**: 【newmicroblog-service】在企业微服务架构中承担业务服务职责。 包含130个业务服务类，实现核心业务逻辑处理。 设计15个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `redis`: 业务数据
  - `microblog`: 日志记录
  - `floors_settings`: 设置信息
  - `todo_info`: 业务数据
  - `results`: 业务数据
  - `every`: 业务数据
  - `microblog_topic_app_config`: 日志记录
  - `mongo`: 业务数据
  - `all`: 业务数据
  - `section_attachment`: 业务数据

---

### newtodo

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 46个 Controller, 49个 Service, 0个 Entity
- **核心业务逻辑**: 【newtodo】在企业微服务架构中承担业务服务职责。 提供46个 REST 接口供前端和第三方系统调用。 包含49个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `redis`: 业务数据
  - `dealedtodo`: 业务数据
  - `error`: 业务数据
  - `exception`: 业务数据
  - `t_customer`: 业务数据
  - `personappidcountdao`: 应用信息
  - `dealt`: 业务数据
  - `mongo`: 业务数据
  - `bytes`: 业务数据
  - `delay`: 业务数据

---

### notice-service

- **业务定位**: 面向企业办公场景的通知服务服务
- **核心功能**: 业务逻辑处理, 消息发送推送
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 4个 Service, 0个 Entity
- **核心业务逻辑**: 【notice-service】在企业微服务架构中承担通知服务职责。 包含4个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 统一消息发送通道，支持短信、邮件、Push 等多种触达方式，提供模板管理、发送记录、状态回执等完整能力。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### notice-service-api

- **业务定位**: 面向企业办公场景的通知服务服务
- **核心功能**: 消息发送推送
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【notice-service-api】在企业微服务架构中承担通知服务职责。 模块划分为：yunzhijia。 统一消息发送通道，支持短信、邮件、Push 等多种触达方式，提供模板管理、发送记录、状态回执等完整能力。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### objectstorage-bc

- **业务定位**: 面向企业办公场景的存储服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 3个 Controller, 2个 Service, 0个 Entity
- **核心业务逻辑**: 【objectstorage-bc】在企业微服务架构中承担存储职责。 提供3个 REST 接口供前端和第三方系统调用。 包含2个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### objectstorage-core

- **业务定位**: 面向企业办公场景的存储服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 5个 Service, 0个 Entity
- **核心业务逻辑**: 【objectstorage-core】在企业微服务架构中承担存储职责。 包含5个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `slave`: 业务数据
  - `mongo`: 业务数据
  - `redis`: 业务数据
  - `meta`: 业务数据
  - `historymetatemplate`: 业务数据
  - `multipartuploadmeta`: 业务数据
  - `slaves`: 业务数据
  - `the`: 业务数据
  - `remotefileclient`: 文件信息
  - `stream`: 业务数据

---

### objectstorage-rest

- **业务定位**: 面向企业办公场景的存储服务
- **核心功能**: REST API 接口
- **技术栈**: Spring Boot
- **代码规模**: 10个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【objectstorage-rest】在企业微服务架构中承担存储职责。 提供10个 REST 接口供前端和第三方系统调用。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `_id`: 业务数据
  - `_ids`: 业务数据

---

### objectstorage-sync

- **业务定位**: 面向企业办公场景的存储服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 3个 Controller, 2个 Service, 0个 Entity
- **核心业务逻辑**: 【objectstorage-sync】在企业微服务架构中承担存储职责。 提供3个 REST 接口供前端和第三方系统调用。 包含2个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `std`: 业务数据
  - `queue`: 业务数据

---

### openaccess

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 24个 Controller, 8个 Service, 1个 Entity
- **核心业务逻辑**: 【openaccess】在企业微服务架构中承担业务服务职责。 提供24个 REST 接口供前端和第三方系统调用。 包含8个业务服务类，实现核心业务逻辑处理。 设计1个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `request_record`: 业务数据

---

### openadmin

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 68个 Controller, 58个 Service, 0个 Entity
- **核心业务逻辑**: 【openadmin】在企业微服务架构中承担业务服务职责。 提供68个 REST 接口供前端和第三方系统调用。 包含58个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `orgservice2newsingletable`: 组织信息
  - `extends`: 业务数据
  - `t_cust_auth_info`: 认证信息
  - `redis`: 业务数据
  - `t_bd_exception`: 业务数据
  - `t_bd_org_admin`: 组织信息
  - `t_bd_person_roletag_org`: 组织信息
  - `mongodb`: 业务数据
  - `t_bd_properties`: 业务数据
  - `t_bd_publiccontactproperty`: 业务数据

---

### openai

- **业务定位**: 面向企业办公场景的AI 智能服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【openai】在企业微服务架构中承担AI 智能职责。 模块划分为：gjsm。 集成大模型能力，提供智能问答、助手服务、自动化处理等 AI 增强功能，支持 MCP 协议与各类 AI 服务对接。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### openapi

- **业务定位**: 面向企业办公场景的接口服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 4个 Controller, 15个 Service, 0个 Entity
- **核心业务逻辑**: 【openapi】在企业微服务架构中承担接口服务职责。 提供4个 REST 接口供前端和第三方系统调用。 包含15个业务服务类，实现核心业务逻辑处理。 模块划分为：oauth, kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `t_customer`: 业务数据
  - `cellspacing`: 业务数据
  - `mads`: 业务数据
  - `open`: 业务数据
  - `the`: 业务数据
  - `this`: 业务数据
  - `crontrigger`: 业务数据
  - `cache`: 业务数据

---

### opencloud

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 14个 Controller, 16个 Service, 0个 Entity
- **核心业务逻辑**: 【opencloud】在企业微服务架构中承担业务服务职责。 提供14个 REST 接口供前端和第三方系统调用。 包含16个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `t_base_templet`: 业务数据
  - `that`: 业务数据
  - `t_base_label_type`: 业务数据
  - `t_developer_info`: 业务数据
  - `t_developer_domain`: 业务数据
  - `t_cust_self_app`: 应用信息
  - `t_base_label`: 业务数据
  - `t_product_domain`: 业务数据
  - `jsonobject`: 业务数据
  - `byte`: 业务数据

---

### opencode

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 3个 Controller, 4个 Service, 0个 Entity
- **核心业务逻辑**: 【opencode】在企业微服务架构中承担业务服务职责。 提供3个 REST 接口供前端和第三方系统调用。 包含4个业务服务类，实现核心业务逻辑处理。 模块划分为：yzj。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### opencommon

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【opencommon】在企业微服务架构中承担业务服务职责。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `redis`: 业务数据

---

### opendata-control

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 7个 Controller, 4个 Service, 0个 Entity
- **核心业务逻辑**: 【opendata-control】在企业微服务架构中承担业务服务职责。 提供7个 REST 接口供前端和第三方系统调用。 包含4个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `t_bd_org_history`: 组织信息
  - `opendatadaoimpsingletable`: 业务数据
  - `extends`: 业务数据
  - `t_bd_org_admin`: 组织信息
  - `t_bd_publiccontactproperty`: 业务数据
  - `t_bd_org`: 组织信息

---

### openid

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 3个 Controller, 1个 Service, 0个 Entity
- **核心业务逻辑**: 【openid】在企业微服务架构中承担业务服务职责。 提供3个 REST 接口供前端和第三方系统调用。 包含1个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `t_open_login`: 日志记录
  - `share`: 业务数据
  - `t_open_checkcode`: 业务数据

---

### openimport

- **业务定位**: 面向企业办公场景的即时通讯服务
- **核心功能**: REST API 接口, 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 51个 Controller, 65个 Service, 10个 Entity
- **核心业务逻辑**: 【openimport】在企业微服务架构中承担即时通讯职责。 提供51个 REST 接口供前端和第三方系统调用。 包含65个业务服务类，实现核心业务逻辑处理。 设计10个数据实体类，映射数据库表结构。 模块划分为：kingdee。 提供 IM 即时通讯能力，支持单聊、群聊、消息推送、已读回执、历史消息等功能，保障企业内外部沟通顺畅。
- **数据库表**:
  - `extends`: 业务数据
  - `t_bd_person_parent`: 业务数据
  - `t_cust_auth_info`: 认证信息
  - `t_bd_developerkey`: 业务数据
  - `t_bd_org_admin`: 组织信息
  - `string`: 业务数据
  - `t_bd_properties`: 业务数据
  - `t_bd_publiccontactproperty`: 业务数据
  - `t_bd_industry_org`: 组织信息
  - `t_bd_message`: 业务数据

---

### openorg

- **业务定位**: 面向企业办公场景的组织架构服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 67个 Controller, 107个 Service, 0个 Entity
- **核心业务逻辑**: 【openorg】在企业微服务架构中承担组织架构职责。 提供67个 REST 接口供前端和第三方系统调用。 包含107个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `datacache`: 业务数据
  - `t_bd_busadmin`: 业务数据
  - `t_data_dic`: 业务数据
  - `t_common_template_eid`: 业务数据
  - `t_bd_person_parent`: 业务数据
  - `t_bd_callhangup`: 业务数据
  - `t_cust_auth_info`: 认证信息
  - `redis`: 业务数据
  - `t_bd_sessioninfo_detail`: 会话信息
  - `t_bd_task_removegroup`: 任务信息

---

### opensync

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 5个 Controller, 18个 Service, 0个 Entity
- **核心业务逻辑**: 【opensync】在企业微服务架构中承担业务服务职责。 提供5个 REST 接口供前端和第三方系统调用。 包含18个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `eid`: 业务数据
  - `update`: 业务数据

---

### opentalk

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 5个 Controller, 13个 Service, 0个 Entity
- **核心业务逻辑**: 【opentalk】在企业微服务架构中承担业务服务职责。 提供5个 REST 接口供前端和第三方系统调用。 包含13个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `update`: 业务数据

---

### opentalk-proxy

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 3个 Controller, 10个 Service, 0个 Entity
- **核心业务逻辑**: 【opentalk-proxy】在企业微服务架构中承担业务服务职责。 提供3个 REST 接口供前端和第三方系统调用。 包含10个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `update`: 业务数据

---

### oplogserver

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 1个 Controller, 11个 Service, 0个 Entity
- **核心业务逻辑**: 【oplogserver】在企业微服务架构中承担业务服务职责。 提供1个 REST 接口供前端和第三方系统调用。 包含11个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `check`: 业务数据
  - `redis`: 业务数据

---

### orgunit-rest

- **业务定位**: 面向企业办公场景的组织架构服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 35个 Service, 0个 Entity
- **核心业务逻辑**: 【orgunit-rest】在企业微服务架构中承担组织架构职责。 包含35个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `java`: 业务数据
  - `org`: 组织信息
  - `end`: 业务数据
  - `洪艺榕`: 业务数据
  - `network`: 业务数据
  - `workflow`: 业务数据
  - `admin`: 业务数据
  - `classpath`: 业务数据
  - `database`: 业务数据
  - `redis`: 业务数据

---

### passport-api

- **业务定位**: 面向企业办公场景的通行证服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【passport-api】在企业微服务架构中承担通行证职责。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### passport-service

- **业务定位**: 面向企业办公场景的通行证服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 1个 Controller, 6个 Service, 0个 Entity
- **核心业务逻辑**: 【passport-service】在企业微服务架构中承担通行证职责。 提供1个 REST 接口供前端和第三方系统调用。 包含6个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `mica`: 业务数据
  - `update`: 业务数据

---

### pubacc

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【pubacc】在企业微服务架构中承担业务服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### pubacc-boot

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 19个 Controller, 43个 Service, 0个 Entity
- **核心业务逻辑**: 【pubacc-boot】在企业微服务架构中承担业务服务职责。 提供19个 REST 接口供前端和第三方系统调用。 包含43个业务服务类，实现核心业务逻辑处理。 模块划分为：baidu, yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `pid`: 业务数据
  - `t_customer`: 业务数据
  - `openorg`: 组织信息
  - `server`: 业务数据
  - `being`: 业务数据
  - `current`: 业务数据
  - `excel`: 业务数据
  - `mongo`: 业务数据
  - `rpc`: 业务数据
  - `redis`: 业务数据

---

### ratelimiter4j

- **业务定位**: 面向企业办公场景的即时通讯服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【ratelimiter4j】在企业微服务架构中承担即时通讯职责。 模块划分为：eudemon。 提供 IM 即时通讯能力，支持单聊、群聊、消息推送、已读回执、历史消息等功能，保障企业内外部沟通顺畅。
- **数据库表**:
  - `zookeeper`: 业务数据
  - `system`: 业务数据
  - `jvm`: 业务数据
  - `list`: 业务数据
  - `the`: 业务数据
  - `file`: 文件信息
  - `different`: 业务数据
  - `local`: 业务数据
  - `segments`: 业务数据

---

### redpacket

- **业务定位**: 面向企业办公场景的红包服务
- **核心功能**: REST API 接口
- **技术栈**: Spring Boot
- **代码规模**: 6个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【redpacket】在企业微服务架构中承担红包职责。 提供6个 REST 接口供前端和第三方系统调用。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### sapphire

- **业务定位**: 面向企业办公场景的应用管理服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 28个 Controller, 17个 Service, 0个 Entity
- **核心业务逻辑**: 【sapphire】在企业微服务架构中承担应用管理职责。 提供28个 REST 接口供前端和第三方系统调用。 包含17个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `propertykeyconst`: 业务数据

---

### scc-microservice

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 12个 Controller, 18个 Service, 0个 Entity
- **核心业务逻辑**: 【scc-microservice】在企业微服务架构中承担业务服务职责。 提供12个 REST 接口供前端和第三方系统调用。 包含18个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `服务到期开始时间`: 业务数据
  - `preferences`: 业务数据
  - `private`: 业务数据
  - `update`: 业务数据
  - `task`: 任务信息

---

### searchdata-incrementsync-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 20个 Controller, 39个 Service, 0个 Entity
- **核心业务逻辑**: 【searchdata-incrementsync-service】在企业微服务架构中承担业务服务职责。 提供20个 REST 接口供前端和第三方系统调用。 包含39个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `end`: 业务数据
  - `delay`: 业务数据
  - `lock`: 业务数据
  - `t_usernetwork`: 用户信息
  - `json`: 业务数据
  - `error`: 业务数据
  - `mongodb`: 业务数据
  - `role`: 业务数据
  - `fail`: 业务数据

---

### security-server

- **业务定位**: 面向企业办公场景的安全管理服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 3个 Controller, 8个 Service, 0个 Entity
- **核心业务逻辑**: 【security-server】在企业微服务架构中承担安全管理职责。 提供3个 REST 接口供前端和第三方系统调用。 包含8个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `dictionary`: 业务数据
  - `directory`: 业务数据
  - `update`: 业务数据

---

### securitycenter

- **业务定位**: 面向企业办公场景的安全管理服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 4个 Controller, 8个 Service, 0个 Entity
- **核心业务逻辑**: 【securitycenter】在企业微服务架构中承担安全管理职责。 提供4个 REST 接口供前端和第三方系统调用。 包含8个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### sentinel-dashboard

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 22个 Controller, 2个 Service, 0个 Entity
- **核心业务逻辑**: 【sentinel-dashboard】在企业微服务架构中承担业务服务职责。 提供22个 REST 接口供前端和第三方系统调用。 包含2个业务服务类，实现核心业务逻辑处理。 模块划分为：alibaba。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `cluster`: 业务数据
  - `tree`: 业务数据
  - `gateway`: 业务数据
  - `flow`: 业务数据
  - `provided`: 业务数据
  - `api`: 业务数据
  - `last_fetch`: 业务数据

---

### service-commander

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 8个 Controller, 15个 Service, 12个 Entity
- **核心业务逻辑**: 【service-commander】在企业微服务架构中承担业务服务职责。 提供8个 REST 接口供前端和第三方系统调用。 包含15个业务服务类，实现核心业务逻辑处理。 设计12个数据实体类，映射数据库表结构。 模块划分为：yzj。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `trace_info`: 业务数据
  - `generate_page_log`: 日志记录
  - `ark_project_info`: 业务数据
  - `generate_project_info`: 业务数据
  - `generate_ark_plugin`: 业务数据
  - `flow_remove_rule`: 业务数据
  - `pressure_link_info`: 业务数据
  - `generate_page_info`: 业务数据
  - `pressure_scene_info`: 业务数据
  - `user`: 用户信息

---

### smartatt-clock

- **业务定位**: 面向企业办公场景的打卡服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 20个 Controller, 27个 Service, 0个 Entity
- **核心业务逻辑**: 【smartatt-clock】在企业微服务架构中承担打卡职责。 提供20个 REST 接口供前端和第三方系统调用。 包含27个业务服务类，实现核心业务逻辑处理。 模块划分为：dangdang, yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `attendanceshift`: 考勤记录
  - `toupdate`: 业务数据
  - `update`: 业务数据
  - `fail`: 业务数据

---

### smartatt-sign

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 7个 Controller, 8个 Service, 0个 Entity
- **核心业务逻辑**: 【smartatt-sign】在企业微服务架构中承担业务服务职责。 提供7个 REST 接口供前端和第三方系统调用。 包含8个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `toupdateoninsert`: 业务数据
  - `toupdate`: 业务数据
  - `update`: 业务数据
  - `fail`: 业务数据

---

### sms-service

- **业务定位**: 面向企业办公场景的短信服务服务
- **核心功能**: REST API 接口, 业务逻辑处理, 消息发送推送
- **技术栈**: Spring Boot
- **代码规模**: 2个 Controller, 12个 Service, 0个 Entity
- **核心业务逻辑**: 【sms-service】在企业微服务架构中承担短信服务职责。 提供2个 REST 接口供前端和第三方系统调用。 包含12个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 统一消息发送通道，支持短信、邮件、Push 等多种触达方式，提供模板管理、发送记录、状态回执等完整能力。
- **数据库表**:
  - `update`: 业务数据

---

### smsconfig-service

- **业务定位**: 面向企业办公场景的短信服务服务
- **核心功能**: REST API 接口, 业务逻辑处理, 消息发送推送
- **技术栈**: Spring Boot
- **代码规模**: 5个 Controller, 13个 Service, 0个 Entity
- **核心业务逻辑**: 【smsconfig-service】在企业微服务架构中承担短信服务职责。 提供5个 REST 接口供前端和第三方系统调用。 包含13个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 统一消息发送通道，支持短信、邮件、Push 等多种触达方式，提供模板管理、发送记录、状态回执等完整能力。
- **数据库表**:
  - `update`: 业务数据

---

### smsgateway

- **业务定位**: 面向企业办公场景的短信服务服务
- **核心功能**: REST API 接口, 消息发送推送
- **技术栈**: Spring Boot
- **代码规模**: 22个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【smsgateway】在企业微服务架构中承担短信服务职责。 提供22个 REST 接口供前端和第三方系统调用。 模块划分为：kingdee。 统一消息发送通道，支持短信、邮件、Push 等多种触达方式，提供模板管理、发送记录、状态回执等完整能力。
- **数据库表**:
  - `the`: 业务数据

---

### smsgateway-service

- **业务定位**: 面向企业办公场景的短信服务服务
- **核心功能**: 业务逻辑处理, 消息发送推送
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 63个 Service, 0个 Entity
- **核心业务逻辑**: 【smsgateway-service】在企业微服务架构中承担短信服务职责。 包含63个业务服务类，实现核心业务逻辑处理。 模块划分为：qcloud, kingdee, emay。 统一消息发送通道，支持短信、邮件、Push 等多种触达方式，提供模板管理、发送记录、状态回执等完整能力。
- **数据库表**:
  - `t_open_checkcode`: 业务数据
  - `smsengines`: 短信记录
  - `named`: 业务数据
  - `smsgateway`: 短信记录
  - `mtmessage`: 业务数据
  - `wsdl`: 业务数据
  - `mtrequest`: 业务数据
  - `the`: 业务数据
  - `caching`: 业务数据
  - `morequest`: 业务数据

---

### smsmanage-service

- **业务定位**: 面向企业办公场景的短信服务服务
- **核心功能**: REST API 接口, 业务逻辑处理, 消息发送推送
- **技术栈**: Spring Boot
- **代码规模**: 6个 Controller, 12个 Service, 0个 Entity
- **核心业务逻辑**: 【smsmanage-service】在企业微服务架构中承担短信服务职责。 提供6个 REST 接口供前端和第三方系统调用。 包含12个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 统一消息发送通道，支持短信、邮件、Push 等多种触达方式，提供模板管理、发送记录、状态回执等完整能力。
- **数据库表**:
  - `update`: 业务数据

---

### snsapi

- **业务定位**: 面向企业办公场景的接口服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 12个 Controller, 60个 Service, 0个 Entity
- **核心业务逻辑**: 【snsapi】在企业微服务架构中承担接口服务职责。 提供12个 REST 接口供前端和第三方系统调用。 包含60个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `public`: 业务数据
  - `request`: 业务数据
  - `mxrecords`: 业务数据
  - `参数名`: 业务数据
  - `contacts`: 业务数据
  - `session`: 会话信息
  - `user`: 用户信息
  - `micorblog`: 日志记录
  - `api`: 业务数据
  - `avatar`: 业务数据

---

### space

- **业务定位**: 面向企业办公场景的空间管理服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 89个 Controller, 23个 Service, 0个 Entity
- **核心业务逻辑**: 【space】在企业微服务架构中承担空间管理职责。 提供89个 REST 接口供前端和第三方系统调用。 包含23个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `yzj`: 业务数据
  - `env`: 业务数据
  - `multiple`: 业务数据
  - `the`: 业务数据
  - `property`: 业务数据
  - `jsonobject`: 业务数据
  - `currentnetworkid`: 业务数据
  - `digest`: 业务数据
  - `describing`: 业务数据
  - `avatar`: 业务数据

---

### spring-boot-yzj-llm-starter

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【spring-boot-yzj-llm-starter】在企业微服务架构中承担业务服务职责。 模块划分为：yzj。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### stakeholder-api

- **业务定位**: 面向企业办公场景的接口服务服务
- **核心功能**: 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 0个 Controller, 0个 Service, 1个 Entity
- **核心业务逻辑**: 【stakeholder-api】在企业微服务架构中承担接口服务职责。 设计1个数据实体类，映射数据库表结构。 模块划分为：kingdee, javatuples。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `micro_network`: 业务数据
  - `private`: 业务数据

---

### stakeholder-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 8个 Service, 0个 Entity
- **核心业务逻辑**: 【stakeholder-service】在企业微服务架构中承担业务服务职责。 包含8个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `cache`: 业务数据
  - `user`: 用户信息

---

### statusNotice-rest

- **业务定位**: 面向企业办公场景的通知服务服务
- **核心功能**: REST API 接口, 业务逻辑处理, 消息发送推送
- **技术栈**: Spring Boot
- **代码规模**: 4个 Controller, 3个 Service, 0个 Entity
- **核心业务逻辑**: 【statusNotice-rest】在企业微服务架构中承担通知服务职责。 提供4个 REST 接口供前端和第三方系统调用。 包含3个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 统一消息发送通道，支持短信、邮件、Push 等多种触达方式，提供模板管理、发送记录、状态回执等完整能力。
- **数据库表**:
  - `update`: 业务数据

---

### statusUser-rest

- **业务定位**: 面向企业办公场景的用户管理服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 4个 Controller, 4个 Service, 0个 Entity
- **核心业务逻辑**: 【statusUser-rest】在企业微服务架构中承担用户管理职责。 提供4个 REST 接口供前端和第三方系统调用。 包含4个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 提供统一的用户认证授权能力，支持多端登录、Token 管理、权限校验、会话管理等安全机制，保障系统访问安全。
- **数据库表**:
  - `update`: 业务数据

---

### syncdata

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 1个 Controller, 1个 Service, 0个 Entity
- **核心业务逻辑**: 【syncdata】在企业微服务架构中承担业务服务职责。 提供1个 REST 接口供前端和第三方系统调用。 包含1个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `person`: 业务数据
  - `list`: 业务数据
  - `openimport`: 业务数据
  - `queue`: 业务数据
  - `update`: 业务数据

---

### task-service

- **业务定位**: 面向企业办公场景的任务管理服务
- **核心功能**: 业务逻辑处理, 数据持久化
- **技术栈**: Spring Boot, MyBatis/JPA
- **代码规模**: 0个 Controller, 7个 Service, 2个 Entity
- **核心业务逻辑**: 【task-service】在企业微服务架构中承担任务管理职责。 包含7个业务服务类，实现核心业务逻辑处理。 设计2个数据实体类，映射数据库表结构。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `attribute`: 业务数据
  - `task_new_operate_log`: 日志记录
  - `task_new_no_finish_info`: 任务信息

---

### team-report-service

- **业务定位**: 面向企业办公场景的报表统计服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 8个 Controller, 12个 Service, 0个 Entity
- **核心业务逻辑**: 【team-report-service】在企业微服务架构中承担报表统计职责。 提供8个 REST 接口供前端和第三方系统调用。 包含12个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `t_bd_org_admin`: 组织信息
  - `json`: 业务数据
  - `from`: 业务数据
  - `t_bd_org`: 组织信息
  - `update`: 业务数据

---

### ticket

- **业务定位**: 面向企业办公场景的工单系统服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 9个 Controller, 7个 Service, 0个 Entity
- **核心业务逻辑**: 【ticket】在企业微服务架构中承担工单系统职责。 提供9个 REST 接口供前端和第三方系统调用。 包含7个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `t_customer`: 业务数据
  - `cellspacing`: 业务数据
  - `mads`: 业务数据
  - `the`: 业务数据
  - `crontrigger`: 业务数据

---

### ticket-service

- **业务定位**: 面向企业办公场景的工单系统服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 6个 Service, 0个 Entity
- **核心业务逻辑**: 【ticket-service】在企业微服务架构中承担工单系统职责。 包含6个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee, yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `authorization`: 认证信息
  - `cellspacing`: 业务数据
  - `mads`: 业务数据
  - `the`: 业务数据
  - `crontrigger`: 业务数据

---

### tinyurl-rest

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 3个 Controller, 5个 Service, 0个 Entity
- **核心业务逻辑**: 【tinyurl-rest】在企业微服务架构中承担业务服务职责。 提供3个 REST 接口供前端和第三方系统调用。 包含5个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `redis`: 业务数据
  - `remote`: 业务数据

---

### todo-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 3个 Service, 0个 Entity
- **核心业务逻辑**: 【todo-service】在企业微服务架构中承担业务服务职责。 包含3个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### tool-yzj-nacos-config-center

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 2个 Service, 0个 Entity
- **核心业务逻辑**: 【tool-yzj-nacos-config-center】在企业微服务架构中承担业务服务职责。 包含2个业务服务类，实现核心业务逻辑处理。 模块划分为：yzj。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### usercore-service

- **业务定位**: 面向企业办公场景的用户管理服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 86个 Service, 0个 Entity
- **核心业务逻辑**: 【usercore-service】在企业微服务架构中承担用户管理职责。 包含86个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 提供统一的用户认证授权能力，支持多端登录、Token 管理、权限校验、会话管理等安全机制，保障系统访问安全。
- **数据库表**:
  - `rpc`: 业务数据
  - `t_bd_person_casvirorg`: 组织信息
  - `t_bd_org_admin`: 组织信息
  - `cache`: 业务数据
  - `printftrace`: 业务数据
  - `t_bd_org`: 组织信息
  - `update`: 业务数据
  - `对象进行更新`: 业务数据

---

### version-control

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 8个 Controller, 9个 Service, 0个 Entity
- **核心业务逻辑**: 【version-control】在企业微服务架构中承担业务服务职责。 提供8个 REST 接口供前端和第三方系统调用。 包含9个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `there`: 业务数据
  - `end`: 业务数据
  - `one`: 业务数据
  - `and`: 业务数据
  - `symboltable`: 业务数据
  - `scratch`: 业务数据
  - `the`: 业务数据
  - `start`: 业务数据
  - `different`: 业务数据
  - `this`: 业务数据

---

### voice-robot-assistant

- **业务定位**: 面向企业办公场景的机器人服务
- **核心功能**: 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 20个 Service, 0个 Entity
- **核心业务逻辑**: 【voice-robot-assistant】在企业微服务架构中承担机器人职责。 包含20个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 集成大模型能力，提供智能问答、助手服务、自动化处理等 AI 增强功能，支持 MCP 协议与各类 AI 服务对接。
- **数据库表**:
  - `3gol`: 业务数据
  - `dimension`: 业务数据
  - `cache`: 业务数据
  - `data`: 业务数据
  - `update`: 业务数据

---

### vpn-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 2个 Controller, 3个 Service, 0个 Entity
- **核心业务逻辑**: 【vpn-service】在企业微服务架构中承担业务服务职责。 提供2个 REST 接口供前端和第三方系统调用。 包含3个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### work-wechat-service

- **业务定位**: 面向企业办公场景的即时通讯服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 3个 Controller, 4个 Service, 0个 Entity
- **核心业务逻辑**: 【work-wechat-service】在企业微服务架构中承担即时通讯职责。 提供3个 REST 接口供前端和第三方系统调用。 包含4个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 提供 IM 即时通讯能力，支持单聊、群聊、消息推送、已读回执、历史消息等功能，保障企业内外部沟通顺畅。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### workassistant-ai-agent

- **业务定位**: 面向企业办公场景的AI 智能服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 5个 Controller, 4个 Service, 0个 Entity
- **核心业务逻辑**: 【workassistant-ai-agent】在企业微服务架构中承担AI 智能职责。 提供5个 REST 接口供前端和第三方系统调用。 包含4个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 集成大模型能力，提供智能问答、助手服务、自动化处理等 AI 增强功能，支持 MCP 协议与各类 AI 服务对接。
- **数据库表**:
  - `meeting`: 会议信息
  - `bean`: 业务数据
  - `the`: 业务数据
  - `jsonobject`: 业务数据
  - `发送者id`: 业务数据
  - `response`: 业务数据

---

### workassistant-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 55个 Controller, 103个 Service, 0个 Entity
- **核心业务逻辑**: 【workassistant-service】在企业微服务架构中承担业务服务职责。 提供55个 REST 接口供前端和第三方系统调用。 包含103个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `updates`: 业务数据
  - `decrement`: 业务数据
  - `dispatch`: 业务数据
  - `meetingid`: 会议信息
  - `jsonobject`: 业务数据
  - `meeting`: 会议信息
  - `param`: 业务数据
  - `increment`: 业务数据
  - `work`: 业务数据
  - `result`: 业务数据

---

### workquestionnaire-service

- **业务定位**: 面向企业办公场景的AI 智能服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 5个 Controller, 10个 Service, 0个 Entity
- **核心业务逻辑**: 【workquestionnaire-service】在企业微服务架构中承担AI 智能职责。 提供5个 REST 接口供前端和第三方系统调用。 包含10个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 集成大模型能力，提供智能问答、助手服务、自动化处理等 AI 增强功能，支持 MCP 协议与各类 AI 服务对接。
- **数据库表**:
  - `cache`: 业务数据
  - `update`: 业务数据

---

### workreport

- **业务定位**: 面向企业办公场景的报表统计服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 22个 Controller, 3个 Service, 0个 Entity
- **核心业务逻辑**: 【workreport】在企业微服务架构中承担报表统计职责。 提供22个 REST 接口供前端和第三方系统调用。 包含3个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### workreport-form-service

- **业务定位**: 面向企业办公场景的报表统计服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 1个 Controller, 52个 Service, 0个 Entity
- **核心业务逻辑**: 【workreport-form-service】在企业微服务架构中承担报表统计职责。 提供1个 REST 接口供前端和第三方系统调用。 包含52个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `otherwise`: 业务数据
  - `setupdatefilevalue`: 文件信息
  - `setelement`: 业务数据
  - `workreporttyperecord`: 报表数据
  - `formrouter`: 业务数据
  - `todo`: 业务数据
  - `list`: 业务数据
  - `error`: 业务数据
  - `the`: 业务数据
  - `sync`: 业务数据

---

### wps-server

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 7个 Controller, 8个 Service, 0个 Entity
- **核心业务逻辑**: 【wps-server】在企业微服务架构中承担业务服务职责。 提供7个 REST 接口供前端和第三方系统调用。 包含8个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `meta`: 业务数据
  - `redis`: 业务数据
  - `memory`: 业务数据
  - `wpsservice`: 业务数据

---

### wpsoffice-proxy

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 5个 Controller, 6个 Service, 0个 Entity
- **核心业务逻辑**: 【wpsoffice-proxy】在企业微服务架构中承担业务服务职责。 提供5个 REST 接口供前端和第三方系统调用。 包含6个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `memory`: 业务数据
  - `分组后统计最大count字段`: 业务数据
  - `update`: 业务数据

---

### xeryun-http

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xeryun-http】在企业微服务架构中承担业务服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `within`: 业务数据
  - `input`: 业务数据
  - `buffers`: 业务数据
  - `previous`: 业务数据
  - `search`: 业务数据
  - `the`: 业务数据
  - `dictionary`: 业务数据
  - `map`: 业务数据
  - `this`: 业务数据
  - `another`: 业务数据

---

### xeryun-io

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xeryun-io】在企业微服务架构中承担业务服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `pending`: 业务数据
  - `any`: 业务数据
  - `select`: 业务数据
  - `the`: 业务数据
  - `this`: 业务数据
  - `appout`: 应用信息
  - `update`: 业务数据

---

### xeryun-security

- **业务定位**: 面向企业办公场景的安全管理服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xeryun-security】在企业微服务架构中承担安全管理职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `authexception`: 认证信息
  - `packed`: 业务数据
  - `which`: 业务数据
  - `database`: 业务数据
  - `properties`: 业务数据
  - `the`: 业务数据
  - `threadlocal`: 业务数据
  - `security`: 业务数据
  - `that`: 业务数据

---

### xeryun-server

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xeryun-server】在企业微服务架构中承担业务服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `within`: 业务数据
  - `content`: 业务数据
  - `their`: 业务数据
  - `manager`: 业务数据
  - `localhost`: 业务数据
  - `error`: 业务数据
  - `its`: 业务数据
  - `use`: 业务数据
  - `here`: 业务数据
  - `from`: 业务数据

---

### xeryun-servlet

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xeryun-servlet】在企业微服务架构中承担业务服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `filter`: 业务数据
  - `servlet`: 业务数据
  - `consideration`: 业务数据
  - `status`: 业务数据
  - `web`: 业务数据
  - `getattribute`: 业务数据
  - `the`: 业务数据
  - `javax`: 业务数据
  - `context`: 业务数据
  - `global`: 业务数据

---

### xeryun-servlets

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xeryun-servlets】在企业微服务架构中承担业务服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `conditional`: 业务数据
  - `exec`: 业务数据
  - `them`: 业务数据
  - `request`: 业务数据
  - `place`: 业务数据
  - `printenv`: 业务数据
  - `the`: 业务数据
  - `this`: 业务数据
  - `cgi`: 业务数据
  - `your`: 业务数据

---

### xeryun-spring-boot-starter

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xeryun-spring-boot-starter】在企业微服务架构中承担业务服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `collection`: 业务数据
  - `the`: 业务数据

---

### xeryun-spring-boot-v2-1-starter

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xeryun-spring-boot-v2-1-starter】在企业微服务架构中承担业务服务职责。 模块划分为：springframework, yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `failed`: 业务数据
  - `collection`: 业务数据
  - `the`: 业务数据
  - `default`: 业务数据

---

### xeryun-spring-boot-v2-starter

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xeryun-spring-boot-v2-starter】在企业微服务架构中承担业务服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `collection`: 业务数据
  - `the`: 业务数据

---

### xeryun-util

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xeryun-util】在企业微服务架构中承担业务服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `subdirs`: 业务数据
  - `ascii`: 业务数据
  - `characters`: 业务数据
  - `nested`: 业务数据
  - `its`: 业务数据
  - `input`: 业务数据
  - `use`: 业务数据
  - `byte`: 业务数据
  - `lazylist`: 业务数据
  - `for`: 业务数据

---

### xeryun-webapp

- **业务定位**: 面向企业办公场景的应用管理服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xeryun-webapp】在企业微服务架构中承担应用管理职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `resource`: 业务数据
  - `before`: 业务数据
  - `final`: 业务数据
  - `system`: 业务数据
  - `another`: 业务数据
  - `being`: 业务数据
  - `this`: 业务数据
  - `which`: 业务数据
  - `classloader`: 业务数据
  - `web`: 业务数据

---

### xeryun-websocket-all

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xeryun-websocket-all】在企业微服务架构中承担业务服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `config`: 配置信息
  - `within`: 业务数据
  - `cometd`: 业务数据
  - `getenvironment`: 业务数据
  - `arg3`: 业务数据
  - `endpoint`: 业务数据
  - `server`: 业务数据
  - `metadata`: 业务数据
  - `web`: 业务数据
  - `its`: 业务数据

---

### xeryun-xml

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xeryun-xml】在企业微服务架构中承担业务服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `xml`: 业务数据
  - `the`: 业务数据
  - `different`: 业务数据
  - `this`: 业务数据

---

### xt-common

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xt-common】在企业微服务架构中承担业务服务职责。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `pool`: 业务数据
  - `msg`: 消息记录
  - `last`: 业务数据
  - `newversion`: 业务数据

---

### xt-entry

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xt-entry】在企业微服务架构中承担业务服务职责。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `pool`: 业务数据
  - `memcache`: 业务数据
  - `server`: 业务数据
  - `outofmemoryerror`: 业务数据
  - `disk`: 业务数据
  - `callback`: 业务数据
  - `loader`: 业务数据
  - `memory`: 业务数据
  - `the`: 业务数据

---

### xt-entry-sl

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xt-entry-sl】在企业微服务架构中承担业务服务职责。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `pool`: 业务数据
  - `memcache`: 业务数据
  - `server`: 业务数据
  - `outofmemoryerror`: 业务数据
  - `disk`: 业务数据
  - `callback`: 业务数据
  - `loader`: 业务数据
  - `memory`: 业务数据
  - `the`: 业务数据
  - `cache`: 业务数据

---

### xt-interface

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 10个 Controller, 3个 Service, 0个 Entity
- **核心业务逻辑**: 【xt-interface】在企业微服务架构中承担业务服务职责。 提供10个 REST 接口供前端和第三方系统调用。 包含3个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `config`: 配置信息
  - `update`: 业务数据

---

### xt-lcc-common

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xt-lcc-common】在企业微服务架构中承担业务服务职责。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `version`: 业务数据
  - `servers`: 业务数据
  - `byte`: 业务数据

---

### xt-push

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 2个 Controller, 3个 Service, 0个 Entity
- **核心业务逻辑**: 【xt-push】在企业微服务架构中承担业务服务职责。 提供2个 REST 接口供前端和第三方系统调用。 包含3个业务服务类，实现核心业务逻辑处理。 模块划分为：oppo, kingdee, vivo, harmony, huawei。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `network`: 业务数据
  - `properties`: 业务数据
  - `the`: 业务数据
  - `apns`: 业务数据
  - `cache`: 业务数据
  - `push`: 业务数据

---

### xt-robot

- **业务定位**: 面向企业办公场景的机器人服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 17个 Controller, 22个 Service, 0个 Entity
- **核心业务逻辑**: 【xt-robot】在企业微服务架构中承担机器人职责。 提供17个 REST 接口供前端和第三方系统调用。 包含22个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 集成大模型能力，提供智能问答、助手服务、自动化处理等 AI 增强功能，支持 MCP 协议与各类 AI 服务对接。
- **数据库表**:
  - `interfaces`: 业务数据
  - `assistrobot`: 业务数据
  - `excel`: 业务数据
  - `scc`: 业务数据
  - `remindrobot`: 业务数据
  - `cache`: 业务数据
  - `update`: 业务数据

---

### xt-userinfo

- **业务定位**: 面向企业办公场景的用户管理服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xt-userinfo】在企业微服务架构中承担用户管理职责。 模块划分为：kingdee。 提供统一的用户认证授权能力，支持多端登录、Token 管理、权限校验、会话管理等安全机制，保障系统访问安全。
- **数据库表**:
  - `cache`: 业务数据
  - `redis`: 业务数据
  - `open`: 业务数据

---

### xt-websocket

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【xt-websocket】在企业微服务架构中承担业务服务职责。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `pool`: 业务数据
  - `server`: 业务数据
  - `outofmemoryerror`: 业务数据
  - `callback`: 业务数据
  - `the`: 业务数据

---

### xuntong-ai-agent

- **业务定位**: 面向企业办公场景的AI 智能服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 4个 Controller, 6个 Service, 0个 Entity
- **核心业务逻辑**: 【xuntong-ai-agent】在企业微服务架构中承担AI 智能职责。 提供4个 REST 接口供前端和第三方系统调用。 包含6个业务服务类，实现核心业务逻辑处理。 模块划分为：yzj。 集成大模型能力，提供智能问答、助手服务、自动化处理等 AI 增强功能，支持 MCP 协议与各类 AI 服务对接。
- **数据库表**:
  - `accept`: 业务数据

---

### yzj-crm-common

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【yzj-crm-common】在企业微服务架构中承担业务服务职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `json`: 业务数据
  - `redis`: 业务数据
  - `from`: 业务数据

---

### yzj-mail-server

- **业务定位**: 面向企业办公场景的邮件服务服务
- **核心功能**: REST API 接口, 业务逻辑处理, 消息发送推送
- **技术栈**: Spring Boot
- **代码规模**: 20个 Controller, 27个 Service, 0个 Entity
- **核心业务逻辑**: 【yzj-mail-server】在企业微服务架构中承担邮件服务职责。 提供20个 REST 接口供前端和第三方系统调用。 包含27个业务服务类，实现核心业务逻辑处理。 模块划分为：yzj。 统一消息发送通道，支持短信、邮件、Push 等多种触达方式，提供模板管理、发送记录、状态回执等完整能力。
- **数据库表**:
  - `originemail`: 业务数据
  - `ascii`: 业务数据
  - `server`: 业务数据
  - `inputbuf`: 业务数据
  - `redis`: 业务数据
  - `otheremail`: 业务数据
  - `input`: 业务数据
  - `here`: 业务数据
  - `listinfo`: 业务数据
  - `for`: 业务数据

---

### yzj-mcp-server-spring-boot-starter

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口
- **技术栈**: Spring Boot
- **代码规模**: 1个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【yzj-mcp-server-spring-boot-starter】在企业微服务架构中承担业务服务职责。 提供1个 REST 接口供前端和第三方系统调用。 模块划分为：example。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### yzj-mcp-server-spring-mvc

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【yzj-mcp-server-spring-mvc】在企业微服务架构中承担业务服务职责。 模块划分为：yzj。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `language`: 业务数据
  - `blocking`: 业务数据
  - `users`: 用户信息
  - `one`: 业务数据
  - `mcp`: 业务数据
  - `clients`: 业务数据
  - `the`: 业务数据
  - `stdin`: 业务数据
  - `uri`: 业务数据
  - `for`: 业务数据

---

### yzj-mcp-spring-boot-starter-v1

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口
- **技术栈**: Spring Boot
- **代码规模**: 2个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【yzj-mcp-spring-boot-starter-v1】在企业微服务架构中承担业务服务职责。 提供2个 REST 接口供前端和第三方系统调用。 模块划分为：yzj。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `string`: 业务数据
  - `dto`: 业务数据

---

### yzj-nacos-client

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【yzj-nacos-client】在企业微服务架构中承担业务服务职责。 模块划分为：alibaba。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `nameserver`: 业务数据
  - `servicename`: 业务数据
  - `service`: 业务数据
  - `instance`: 业务数据
  - `system`: 业务数据
  - `multi`: 业务数据
  - `server`: 业务数据
  - `disk`: 业务数据
  - `classpath`: 业务数据
  - `finish`: 业务数据

---

### yzj-space-api

- **业务定位**: 面向企业办公场景的空间管理服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【yzj-space-api】在企业微服务架构中承担空间管理职责。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### yzj-space-manager

- **业务定位**: 面向企业办公场景的空间管理服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 12个 Controller, 16个 Service, 0个 Entity
- **核心业务逻辑**: 【yzj-space-manager】在企业微服务架构中承担空间管理职责。 提供12个 REST 接口供前端和第三方系统调用。 包含16个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `must`: 业务数据
  - `this`: 业务数据

---

### yzj-space-service

- **业务定位**: 面向企业办公场景的空间管理服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 25个 Controller, 173个 Service, 0个 Entity
- **核心业务逻辑**: 【yzj-space-service】在企业微服务架构中承担空间管理职责。 提供25个 REST 接口供前端和第三方系统调用。 包含173个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `redis`: 业务数据
  - `must`: 业务数据
  - `update`: 业务数据

---

### yzj-spring-boot-ai-starter

- **业务定位**: 面向企业办公场景的AI 智能服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 3个 Controller, 2个 Service, 0个 Entity
- **核心业务逻辑**: 【yzj-spring-boot-ai-starter】在企业微服务架构中承担AI 智能职责。 提供3个 REST 接口供前端和第三方系统调用。 包含2个业务服务类，实现核心业务逻辑处理。 模块划分为：yzj。 集成大模型能力，提供智能问答、助手服务、自动化处理等 AI 增强功能，支持 MCP 协议与各类 AI 服务对接。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### yzj-tool-config-center

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【yzj-tool-config-center】在企业微服务架构中承担业务服务职责。 模块划分为：yzj。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### yzj-useragent-tool-common

- **业务定位**: 面向企业办公场景的用户管理服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【yzj-useragent-tool-common】在企业微服务架构中承担用户管理职责。 模块划分为：yzj。 提供统一的用户认证授权能力，支持多端登录、Token 管理、权限校验、会话管理等安全机制，保障系统访问安全。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

### yzj-xeryun-dropwizard-core

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: 业务数据处理
- **技术栈**: Spring Boot
- **代码规模**: 0个 Controller, 0个 Service, 0个 Entity
- **核心业务逻辑**: 【yzj-xeryun-dropwizard-core】在企业微服务架构中承担业务服务职责。 模块划分为：dropwizard, servlet。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `asynchronous`: 业务数据
  - `one`: 业务数据
  - `which`: 业务数据
  - `are`: 业务数据
  - `the`: 业务数据
  - `reporting`: 报表数据
  - `this`: 业务数据
  - `for`: 业务数据

---

### yzjomc-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 11个 Controller, 21个 Service, 0个 Entity
- **核心业务逻辑**: 【yzjomc-service】在企业微服务架构中承担业务服务职责。 提供11个 REST 接口供前端和第三方系统调用。 包含21个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `buildbaseupdate`: 业务数据
  - `getupdate`: 业务数据
  - `update`: 业务数据

---

### yzjsdpc-service

- **业务定位**: 面向企业办公场景的业务服务服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 6个 Controller, 11个 Service, 0个 Entity
- **核心业务逻辑**: 【yzjsdpc-service】在企业微服务架构中承担业务服务职责。 提供6个 REST 接口供前端和第三方系统调用。 包含11个业务服务类，实现核心业务逻辑处理。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**:
  - `cache`: 业务数据
  - `preferences`: 业务数据
  - `jsonobject`: 业务数据

---

### zyy-redpacket-service

- **业务定位**: 面向企业办公场景的红包服务
- **核心功能**: REST API 接口, 业务逻辑处理
- **技术栈**: Spring Boot
- **代码规模**: 3个 Controller, 6个 Service, 0个 Entity
- **核心业务逻辑**: 【zyy-redpacket-service】在企业微服务架构中承担红包职责。 提供3个 REST 接口供前端和第三方系统调用。 包含6个业务服务类，实现核心业务逻辑处理。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力，与其他微服务协同工作，支撑高并发业务场景。
- **数据库表**: 未检测到明显的表结构定义（可能使用外部公共表或通过配置指定）

---

