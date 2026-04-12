# Java 微服务项目核心业务分析报告

> 生成时间：2026-03-26 23:00:55
> 项目总数：198
> 根目录：`/home/heng_xu/work/program/idea_workhome`

## 📁 架构说明

**架构模式**: 独立工程集合（无根 POM / 无父子模块关系）

每个项目都是独立 Maven 工程，按业务域单独构建部署。

---

## 📋 项目详情（核心业务逻辑分析）

> 基于完整源代码分析，每个项目 200-300 字业务描述

### 3gol

⚠️ 未找到有效 Java 源代码

### YzjJustAuth

⚠️ 未找到有效 Java 源代码

### adware

【adware】是面向企业办公场景的上传 + 同步 + 生成服务。 主要提供表单服务等业务处理能力。 系统采用分层架构设计，包含8个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：FileService, IUserNetworkServiceRpc。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担上传职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### ai-faq-service

【ai-faq-service】是面向企业办公场景的下载服务。 主要提供新增, 表单服务等业务处理能力。 系统采用分层架构设计，包含1个 REST 接口, 10个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担下载职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### ai-platform-service

【ai-platform-service】是面向企业办公场景的日程 + 发送 + 同步服务。 核心功能包括：即时通讯, 新增, 组织管理, AI 能力等。 系统采用分层架构设计，包含12个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：XuntongService, AsyncMsgCreateScheduleService。 为企业数字化办公提供稳定可靠的后台服务能力。

### anonymity-rest

【anonymity-rest】是面向企业办公场景的生成服务。 核心功能包括：认证鉴权, 安全审计, 更新, 用户管理等。 系统采用分层架构设计，包含12个业务服务, 6个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：NewsService, UserNetworkService, FileService, MicroblogService。 为企业数字化办公提供稳定可靠的后台服务能力。

### api-gateway

【api-gateway】是面向企业办公场景的同步 + 发送 + 生成服务。 核心功能包括：安全审计, 认证鉴权, 表单服务等。 系统采用分层架构设计，包含1个 REST 接口, 20个业务服务，支持高并发业务场景。 模块划分为：springframework, yunzhijia, weibo。 依赖外部服务：UserService, WebSessionService, OAuth2Service, GatewaySessionService, GatewayAdminService。 为企业数字化办公提供稳定可靠的后台服务能力。

### apns-service

【apns-service】是面向企业办公场景的发送服务。 核心功能包括：安全审计, 删除, 文件处理, 统计分析等。 系统采用分层架构设计，包含4个业务服务, 1个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserService, ApnDataService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### appmanage

【appmanage】是面向企业办公场景的邀请 + 发送 + 分享服务。 核心功能包括：即时通讯, 新增, 认证鉴权, 查询等。 系统采用分层架构设计，包含30个业务服务, 1个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：CompanyServiceService, HomeServiceDao, HomeServiceBiz。 为企业数字化办公提供稳定可靠的后台服务能力。

### appservice

【appservice】是面向企业办公场景的上传 + 发送 + 审核服务。 核心功能包括：AI 能力, 新增, 用户管理, 表单服务等。 系统采用分层架构设计，包含76个业务服务, 4个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：AppOrderService, IMqService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担上传职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### attendance

【attendance】是面向企业办公场景的提醒 + 同步 + 日程服务。 核心功能包括：流程引擎, 新增, 数据导入导出, 表单服务等。 系统采用分层架构设计，包含28个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：ClockInUserService, UserNetworkService, IAttendanceUserShiftService。 支撑企业员工考勤管理全流程，实现打卡记录、统计分析、异常处理等核心业务。

### attendance-context

⚠️ 未找到有效 Java 源代码

### attendance-manage

【attendance-manage】是面向企业办公场景的提醒 + 同步 + 打卡服务。 核心功能包括：新增, 流程引擎, 考勤打卡, 定时提醒等。 系统采用分层架构设计，包含6个 REST 接口, 27个业务服务，支持高并发业务场景。 模块划分为：dangdang, yunzhijia。 依赖外部服务：IPackageManageService。 支撑企业员工考勤管理全流程，实现打卡记录、统计分析、异常处理等核心业务。

### attendance-service

【attendance-service】是面向企业办公场景的提醒 + 同步 + 日程服务。 核心功能包括：考勤打卡, 安全审计, 用户管理, 删除等。 系统采用分层架构设计，包含131个业务服务, 54个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：AttendanceUserNetworkService, CloudFlowLeaveService, EmployeeStatisticsService。 支撑企业员工考勤管理全流程，实现打卡记录、统计分析、异常处理等核心业务。

### attendance-signapi

【attendance-signapi】是面向企业办公场景的应用服务。 核心功能包括：流程引擎, 新增, 通知服务, 表单服务等。 系统采用分层架构设计，包含2个 REST 接口, 6个业务服务，支持高并发业务场景。 模块划分为：springframework, yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担应用职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### authserver

【authserver】是企业微服务架构中的业务服务模块。 核心功能包括：新增, 认证鉴权, 组织管理, 查询等。 系统采用分层架构设计，包含8个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：AppServiceService, Mapper。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担核心业务职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### backend-skill

【backend-skill】是面向企业办公场景的用户服务。 核心功能包括：新增, 更新, 删除, 表单服务等。 系统采用分层架构设计，包含2个 REST 接口, 1个业务服务, 1个数据实体，支持高并发业务场景。 模块划分为：example。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担用户职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### base-document

【base-document】是面向企业办公场景的下载 + 上传 + 生成服务。 核心功能包括：新增, 认证鉴权, 安全审计, 文档处理等。 系统采用分层架构设计，包含29个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserNetworkService, FileService, DownLoadFileHelpService。 为企业数字化办公提供稳定可靠的后台服务能力。

### base-mail

【base-mail】是面向企业办公场景的发送服务。 核心功能包括：新增, AI 能力, 统计分析, 消息推送等。 系统采用分层架构设计，包含6个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：EmailObjectService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### base-rest

【base-rest】是企业微服务架构中的业务服务模块。 核心功能包括：新增, 认证鉴权, AI 能力, 用户管理等。 系统采用分层架构设计，包含7个业务服务, 1个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserService, NewBaseRedisService, OrganizationService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担核心业务职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### base-session

【base-session】是面向企业办公场景的签到 + 发送 + 审核服务。 核心功能包括：即时通讯, 新增, 考勤打卡, 用户管理等。 系统采用分层架构设计，包含5个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserService, AccountService, TribeStatService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担签到职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### base-stakeholder

【base-stakeholder】是面向企业办公场景的提醒 + 同步 + 上传服务。 核心功能包括：新增, 查询, 文件处理, 安全审计等。 系统采用分层架构设计，包含101个业务服务, 14个数据实体，支持高并发业务场景。 模块划分为：kingdee, javatuples。 依赖外部服务：JoinCommunityApplicationService, AccountLogService。 为企业数字化办公提供稳定可靠的后台服务能力。

### baseaccount

【baseaccount】是面向企业办公场景的日程 + 发送 + 同步服务。 核心功能包括：即时通讯, 新增, 查询, 组织管理等。 系统采用分层架构设计，包含27个业务服务，支持高并发业务场景。 模块划分为：kingdee, springframework。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担日程职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### baseaccount-api

⚠️ 未找到有效 Java 源代码

### baseaccount-kms-service

【baseaccount-kms-service】是企业微服务架构中的业务服务模块。 核心功能包括：即时通讯, 新增, 组织管理, 表单服务等。 系统采用分层架构设计，包含1个 REST 接口, 10个业务服务, 6个数据实体，支持高并发业务场景。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担核心业务职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### baseaccount-service

⚠️ 未找到有效 Java 源代码

### birthday-rest

【birthday-rest】是面向企业办公场景的发送服务。 核心功能包括：新增, 认证鉴权, 更新, 用户管理等。 系统采用分层架构设计，包含7个业务服务, 9个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserNetworkService, WishesCardService, NetworkService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### bosspub-boot

【bosspub-boot】是面向企业办公场景的上传 + 发送 + 同步服务。 核心功能包括：新增, 数据同步, 用户管理, 任务管理等。 系统采用分层架构设计，包含2个 REST 接口, 15个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：SendPubaccService, RedisService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担上传职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### camunda-demo

⚠️ 未找到有效 Java 源代码

### carereport-service

【carereport-service】是面向企业办公场景的聊天 + AI + 上传服务。 核心功能包括：AI 能力, 新增, 删除, 表单服务等。 系统采用分层架构设计，包含7个 REST 接口, 14个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：UserCoreService, IReportShowLocalService, IStatisticLocalService。 提供统一认证授权能力，支持多端登录、Token 管理、权限校验等安全机制。

### cloudauth

【cloudauth】是面向企业办公场景的同步 + 应用 + 上传服务。 核心功能包括：新增, 认证鉴权, 安全审计, 文档处理等。 系统采用分层架构设计，包含7个 REST 接口, 13个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：PersonOrgService。 提供统一认证授权能力，支持多端登录、Token 管理、权限校验等安全机制。 该项目在整体架构中承担同步职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### cloudflow-common

【cloudflow-common】是面向企业办公场景的同步 + 发送 + 生成服务。 核心功能包括：认证鉴权, 新增, 表单服务, 文件处理等。 系统采用分层架构设计，包含2个业务服务，支持高并发业务场景。 模块划分为：kingdee, yunzhijia, google。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担同步职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### cloudflow-elastic-job

⚠️ 未找到有效 Java 源代码

### cloudflow-flowcenter-service

【cloudflow-flowcenter-service】是面向企业办公场景的发送 + 提醒 + 同步服务。 核心功能包括：消息推送, AI 能力, 新增, 表单服务等。 系统采用分层架构设计，包含17个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：CountCacheService, TodoCountCacheService。 为企业数字化办公提供稳定可靠的后台服务能力。

### cloudflow-form-api

⚠️ 未找到有效 Java 源代码

### cloudflow-form-service

【cloudflow-form-service】是面向企业办公场景的同步 + 日程 + 下载服务。 核心功能包括：认证鉴权, 组织管理, 安全审计, AI 能力等。 系统采用分层架构设计，包含63个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：NewLeaveService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担同步职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### cloudflow-template-service

【cloudflow-template-service】是面向企业办公场景的同步 + 下载 + 上传服务。 核心功能包括：即时通讯, 新增, 查询, 更新等。 系统采用分层架构设计，包含49个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：PartnerBizRelationLocalService, ScriptBlockLocalService。 为企业数字化办公提供稳定可靠的后台服务能力。

### cloudflow-workflow-api

⚠️ 未找到有效 Java 源代码

### cloudflow-workflow-service

【cloudflow-workflow-service】是面向企业办公场景的提醒 + 同步 + 下载服务。 核心功能包括：即时通讯, 流程引擎, 查询, 新增等。 系统采用分层架构设计，包含197个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：FlowCenterESService, MinePageQueryService, CommentsRegisterService, HandlerTodoCacheService。 为企业数字化办公提供稳定可靠的后台服务能力。

### cloudgroup-web

【cloudgroup-web】是面向企业办公场景的群组 + 上传 + 发送服务。 核心功能包括：即时通讯, 新增, 流程引擎, 认证鉴权等。 系统采用分层架构设计，包含1个 REST 接口, 5个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：RedisService, XunTongService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担群组职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### cloudplatform

【cloudplatform】是面向企业办公场景的上传 + 通讯 + 发送服务。 核心功能包括：审批流程, 即时通讯, 新增, 查询等。 系统采用分层架构设计，包含5个 REST 接口, 11个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：RPCServiceAdapter。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担上传职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### cloudportal

【cloudportal】是面向企业办公场景的应用 + 发送 + 同步服务。 核心功能包括：AI 能力, 新增, 表单服务等。 系统采用分层架构设计，包含9个 REST 接口, 28个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：OrderInfoService, CommonPortalService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担应用职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### cloudwork

【cloudwork】是面向企业办公场景的上传服务。 核心功能包括：即时通讯, 新增, 认证鉴权, 数据导入导出等。 系统采用分层架构设计，包含1个业务服务，支持高并发业务场景。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担上传职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### cloudwork-service

【cloudwork-service】是面向企业办公场景的上传 + 发送服务。 核心功能包括：新增, 查询, AI 能力, 更新等。 系统采用分层架构设计，包含5个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担上传职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### collaborative-component

【collaborative-component】是面向企业办公场景的分享 + 发送 + 同步服务。 核心功能包括：即时通讯, 新增, 数据导入导出, AI 能力等。 系统采用分层架构设计，包含5个 REST 接口, 18个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：XuntongService, RPCServiceAdapter。 为企业数字化办公提供稳定可靠的后台服务能力。

### colleague-rest

【colleague-rest】是面向企业办公场景的同步 + 发送 + 生成服务。 核心功能包括：新增, 认证鉴权, 更新, 用户管理等。 系统采用分层架构设计，包含16个业务服务, 18个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserNetworkService, MicroblogService, NetworkService。 为企业数字化办公提供稳定可靠的后台服务能力。

### comment

【comment】是面向企业办公场景的发送服务。 核心功能包括：云存储, 新增, 更新, 表单服务等。 系统采用分层架构设计，包含1个 REST 接口, 11个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：CollaborativeService, LaudService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### common

【common】是面向企业办公场景的同步 + 分享 + 发送服务。 核心功能包括：新增, 认证鉴权, 流程引擎, 安全审计等。 系统采用分层架构设计，包含85个业务服务, 1个数据实体，支持高并发业务场景。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担同步职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### common-cache

⚠️ 未找到有效 Java 源代码

### data-operation-service

【data-operation-service】是面向企业办公场景的同步 + 通讯 + AI服务。 核心功能包括：即时通讯, 组织管理, AI 能力, 用户管理等。 系统采用分层架构设计，包含7个 REST 接口, 41个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：UserCoreService, AppService。 提供统一认证授权能力，支持多端登录、Token 管理、权限校验等安全机制。

### data-processing

【data-processing】是面向企业办公场景的日程服务。 核心功能包括：即时通讯, 新增, 流程引擎, 定时提醒等。 系统采用分层架构设计，包含4个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：NetWorkService, CustInfoAuthService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担日程职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### data-rest

【data-rest】是面向企业办公场景的发送 + 同步服务。 核心功能包括：新增, 认证鉴权, 更新, 用户管理等。 系统采用分层架构设计，包含6个业务服务, 3个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：DataQueryService, RedisService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### dbmv

【dbmv】是面向企业办公场景的应用服务。 核心功能包括：即时通讯, 新增, AI 能力, 更新等。 系统采用分层架构设计，包含4个 REST 接口, 15个业务服务, 24个数据实体，支持高并发业务场景。 模块划分为：yunzhijia。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担应用职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### developerplatform-service

【developerplatform-service】是面向企业办公场景的同步 + 日志 + 应用服务。 核心功能包括：新增, 认证鉴权, AI 能力, 更新等。 系统采用分层架构设计，包含9个 REST 接口, 22个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：MsgCardService, ICloudAppService, CloudMiniAppService。 提供统一认证授权能力，支持多端登录、Token 管理、权限校验等安全机制。

### doc-convert

【doc-convert】是面向企业办公场景的WPS 办公 + 同步 + 日程服务。 核心功能包括：即时通讯, 新增, 文档处理, 表单服务等。 系统采用分层架构设计，包含1个 REST 接口, 1个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：CacheFileService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担WPS 办公职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### docrest

【docrest】是面向企业办公场景的同步 + 通讯 + 下载服务。 核心功能包括：即时通讯, 新增, 查询, 安全审计等。 系统采用分层架构设计，包含4个 REST 接口, 12个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：DocBoxService。 提供企业文档全生命周期管理，支持上传下载、在线预览、权限控制等功能。 该项目在整体架构中承担同步职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### favorite-boot

【favorite-boot】是面向企业办公场景的群组 + 同步 + 日程服务。 核心功能包括：即时通讯, 新增, 组织管理, 文档处理等。 系统采用分层架构设计，包含6个 REST 接口, 19个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：FavoriteAuthService, FileService, WeChatService, MsgassistMsgService。 支撑企业员工考勤管理全流程，实现打卡记录、统计分析、异常处理等核心业务。

### fileclean-private

【fileclean-private】是面向企业办公场景的文件 + 发送 + 同步服务。 核心功能包括：安全审计, 文档处理, 数据同步, 删除等。 系统采用分层架构设计，包含1个 REST 接口, 1个业务服务，支持高并发业务场景。 模块划分为：kingdee。 提供企业文档全生命周期管理，支持上传下载、在线预览、权限控制等功能。 该项目在整体架构中承担文件职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### fileclean-private-hx

【fileclean-private-hx】是面向企业办公场景的文件 + 下载 + 发送服务。 核心功能包括：即时通讯, 安全审计, 文档处理, 删除等。 系统采用分层架构设计，包含1个 REST 接口, 3个业务服务，支持高并发业务场景。 模块划分为：kingdee。 提供企业文档全生命周期管理，支持上传下载、在线预览、权限控制等功能。 该项目在整体架构中承担文件职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### gateway-admin

【gateway-admin】是面向企业办公场景的群组 + 同步 + 日志服务。 核心功能包括：新增, 认证鉴权, 组织管理, 安全审计等。 系统采用分层架构设计，包含15个 REST 接口, 7个业务服务，支持高并发业务场景。 模块划分为：springframework, yunzhijia。 依赖外部服务：GatewayServiceDao。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担群组职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### group-rest

【group-rest】是面向企业办公场景的发送服务。 核心功能包括：即时通讯, 新增, 认证鉴权, 组织管理等。 系统采用分层架构设计，包含2个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserService, MicroblogDataService, MicroblogSyncEsServiceImpl, UserNetworkService, SearchUserService。 为企业数字化办公提供稳定可靠的后台服务能力。

### groupassist

【groupassist】是面向企业办公场景的群组 + 提醒 + 同步服务。 核心功能包括：AI 能力, 新增, 删除, 表单服务等。 系统采用分层架构设计，包含17个 REST 接口, 39个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserCoreService, IStatisticLocalService, RecommendService, GroupNoticeService。 为企业数字化办公提供稳定可靠的后台服务能力。

### im

【im】是面向企业办公场景的上传 + 分享 + 发送服务。 核心功能包括：用户管理, 新增, 组织管理, 表单服务等。 系统采用分层架构设计，包含15个业务服务, 1个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserNetworkService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担上传职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### image

【image】是企业微服务架构中的业务服务模块。 核心功能包括：新增, 安全审计, 表单服务等。 系统采用分层架构设计，包含4个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：ImageProcessService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担核心业务职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### image-service

【image-service】是企业微服务架构中的业务服务模块。 系统采用分层架构设计，包含1个业务服务，支持高并发业务场景。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担核心业务职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### img-convert

⚠️ 未找到有效 Java 源代码

### imsdk

【imsdk】是面向企业办公场景的上传 + 下载 + 发送服务。 核心功能包括：即时通讯, 新增, 任务管理, 组织管理等。 系统采用分层架构设计，包含6个业务服务，支持高并发业务场景。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担上传职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### imsdk-service

【imsdk-service】是面向企业办公场景的上传 + 发送服务。 核心功能包括：即时通讯, 新增, 认证鉴权, 组织管理等。 系统采用分层架构设计，包含6个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：LightappConfigureService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担上传职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### innermanage

【innermanage】是面向企业办公场景的同步 + 下载 + 上传服务。 核心功能包括：即时通讯, 新增, 查询, 数据导入导出等。 系统采用分层架构设计，包含2个 REST 接口, 56个业务服务, 4个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：IYZJPersonParentService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担同步职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### intelligentbulletin-web

【intelligentbulletin-web】是面向企业办公场景的提醒 + 同步 + 通讯服务。 核心功能包括：新增, 查询, 文档处理, AI 能力等。 系统采用分层架构设计，包含33个 REST 接口, 66个业务服务，支持高并发业务场景。 模块划分为：kingdee, yunzhijia。 依赖外部服务：GlobalPrimaryService, DocRecycleBinService, PermissionService。 为企业数字化办公提供稳定可靠的后台服务能力。

### invite

【invite】是面向企业办公场景的发送服务。 核心功能包括：即时通讯, 新增, 认证鉴权, 组织管理等。 系统采用分层架构设计，包含1个业务服务，支持高并发业务场景。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### invite-service

【invite-service】是面向企业办公场景的邀请 + 分享 + 同步服务。 核心功能包括：即时通讯, 新增, 认证鉴权, 流程引擎等。 系统采用分层架构设计，包含15个业务服务, 3个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserNetworkService, AccountService, NetworkService, InvitationService。 为企业数字化办公提供稳定可靠的后台服务能力。

### jsonrpc4j

⚠️ 未找到有效 Java 源代码

### linkcenter

【linkcenter】是面向企业办公场景的提醒 + 同步 + 日志服务。 核心功能包括：新增, 流程引擎, 更新, 用户管理等。 系统采用分层架构设计，包含20个 REST 接口, 42个业务服务，支持高并发业务场景。 模块划分为：kingdee, yunzhijia。 依赖外部服务：SystemExtendFormService, ReimbursementService。 为企业数字化办公提供稳定可靠的后台服务能力。

### linkerp-admin-service

【linkerp-admin-service】是面向企业办公场景的同步 + 日志 + 通讯服务。 核心功能包括：即时通讯, 新增, 安全审计, 文档处理等。 系统采用分层架构设计，包含29个 REST 接口, 39个业务服务，支持高并发业务场景。 模块划分为：yunzhijia, weibo。 依赖外部服务：PayPackageService, BusinessDataNewMapper。 提供 IM 即时通讯能力，支持单聊、群聊、消息推送、已读回执等功能。

### linkerp-datasource-service

【linkerp-datasource-service】是面向企业办公场景的同步 + 日志 + 日程服务。 核心功能包括：即时通讯, 新增, 考勤打卡, 更新等。 系统采用分层架构设计，包含9个 REST 接口, 14个业务服务，支持高并发业务场景。 模块划分为：yunzhijia, weibo。 提供统一认证授权能力，支持多端登录、Token 管理、权限校验等安全机制。 该项目在整体架构中承担同步职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### linkerp-demo

【linkerp-demo】是面向企业办公场景的生成服务。 核心功能包括：统计分析, 新增, 认证鉴权, 表单服务等。 系统采用分层架构设计，包含3个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：EncryptDataService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担生成职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### livestream

【livestream】是面向企业办公场景的会议 + 同步 + 日志服务。 主要提供认证鉴权, 表单服务等业务处理能力。 系统采用分层架构设计，包含36个 REST 接口, 87个业务服务，支持高并发业务场景。 模块划分为：dangdang, yunzhijia, yufu。 依赖外部服务：TencentMeetingSuperAdminService。 支持会议全生命周期管理，包括预约、通知、参会、纪要等核心场景。

### logather

⚠️ 未找到有效 Java 源代码

### manage-v2

⚠️ 未找到有效 Java 源代码

### meeting-rpc-service

【meeting-rpc-service】是面向企业办公场景的邀请 + 分享 + 发送服务。 核心功能包括：新增, 组织管理, 更新, 会议管理等。 系统采用分层架构设计，包含2个 REST 接口, 17个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：PushService, JoinMeetingService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担邀请职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### microblog

【microblog】是面向企业办公场景的上传 + 邀请服务。 核心功能包括：即时通讯, 新增, 文件处理, 表单服务等。 系统采用分层架构设计，包含1个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserService, UserNetworkService, GroupService, SnsUserService, GroupMemberService。 为企业数字化办公提供稳定可靠的后台服务能力。

### microblog-service

【microblog-service】是面向企业办公场景的提醒 + 同步 + 下载服务。 核心功能包括：即时通讯, 新增, 安全审计, AI 能力等。 系统采用分层架构设计，包含131个业务服务, 15个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：PrivateMessageService, JoinCommunityApplicationService, NewsService, UserPrivateMessageThreadService。 为企业数字化办公提供稳定可靠的后台服务能力。

### miscellanea

⚠️ 未找到有效 Java 源代码

### mongosync

【mongosync】是面向企业办公场景的日程 + 发送 + 同步服务。 核心功能包括：即时通讯, 新增, 安全审计, AI 能力等。 系统采用分层架构设计，包含9个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：FormInstNotProcessFullSyncService, ESAutoBalanceService。 为企业数字化办公提供稳定可靠的后台服务能力。

### msgassist

⚠️ 未找到有效 Java 源代码

### msgassist-service

【msgassist-service】是面向企业办公场景的同步 + 上传 + 邀请服务。 核心功能包括：即时通讯, 组织管理, AI 能力, 更新等。 系统采用分层架构设计，包含25个业务服务，支持高并发业务场景。 模块划分为：kingdee, yunzhijia。 依赖外部服务：MsgMarkService, FileService, INetworkServiceRpc, IUserNetworkServiceRpc。 为企业数字化办公提供稳定可靠的后台服务能力。

### nacos-console

【nacos-console】是面向企业办公场景的空间 + 用户服务。 核心功能包括：新增, 认证鉴权, 查询, 安全审计等。 系统采用分层架构设计，包含7个 REST 接口, 2个业务服务，支持高并发业务场景。 模块划分为：alibaba。 依赖外部服务：PermissionPersistService, RolePersistService, NacosUserDetailsServiceImpl, UserPersistService。 为企业数字化办公提供稳定可靠的后台服务能力。

### newmicroblog-service

【newmicroblog-service】是面向企业办公场景的提醒 + 同步 + 下载服务。 核心功能包括：即时通讯, 新增, 安全审计, AI 能力等。 系统采用分层架构设计，包含130个业务服务, 15个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：PrivateMessageService, JoinCommunityApplicationService, NewsService, UserPrivateMessageThreadService。 为企业数字化办公提供稳定可靠的后台服务能力。

### newtodo

【newtodo】是面向企业办公场景的群组 + 同步 + 通讯服务。 核心功能包括：即时通讯, 查询, 表单服务等。 系统采用分层架构设计，包含13个 REST 接口, 50个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：SystemDataCorrelationService, TaskDateMarkService, IMqService, IOrderTodoAppService。 提供企业文档全生命周期管理，支持上传下载、在线预览、权限控制等功能。

### notice-service

【notice-service】是面向企业办公场景的发送服务。 核心功能包括：新增, 查询, 组织管理, 认证鉴权等。 系统采用分层架构设计，包含4个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：UserCoreService, OpenOrgService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### notice-service-api

⚠️ 未找到有效 Java 源代码

### objectstorage-bc

【objectstorage-bc】是面向企业办公场景的文件服务。 核心功能包括：即时通讯, 组织管理, 文档处理, 更新等。 系统采用分层架构设计，包含1个 REST 接口, 2个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：MetaService。 提供企业文档全生命周期管理，支持上传下载、在线预览、权限控制等功能。 该项目在整体架构中承担文件职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### objectstorage-core

【objectstorage-core】是面向企业办公场景的上传 + 同步 + 发送服务。 核心功能包括：文档处理, 文件处理, 表单服务等。 系统采用分层架构设计，包含5个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：DeletedMetaService, MetaCacheService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担上传职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### objectstorage-rest

⚠️ 未找到有效 Java 源代码

### objectstorage-sync

【objectstorage-sync】是面向企业办公场景的文件 + 同步服务。 核心功能包括：即时通讯, 任务管理, 数据同步, 表单服务等。 系统采用分层架构设计，包含1个 REST 接口, 2个业务服务，支持高并发业务场景。 模块划分为：kingdee。 提供企业文档全生命周期管理，支持上传下载、在线预览、权限控制等功能。 该项目在整体架构中承担文件职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### openaccess

【openaccess】是面向企业办公场景的邀请 + 发送 + 提醒服务。 核心功能包括：新增, 认证鉴权, 流程引擎, 安全审计等。 系统采用分层架构设计，包含8个业务服务, 1个数据实体，支持高并发业务场景。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担邀请职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### openadmin

【openadmin】是面向企业办公场景的群组 + 同步 + 下载服务。 核心功能包括：新增, 更新, 组织管理, 表单服务等。 系统采用分层架构设计，包含3个 REST 接口, 58个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：IYZJRoleShareService, IYZJBusAdminService, IYZJAddressBookExtendFieldService。 为企业数字化办公提供稳定可靠的后台服务能力。

### openai

⚠️ 未找到有效 Java 源代码

### openapi

【openapi】是面向企业办公场景的同步 + 上传 + 生成服务。 核心功能包括：新增, 安全审计, 用户管理, 表单服务等。 系统采用分层架构设计，包含15个业务服务，支持高并发业务场景。 模块划分为：kingdee, oauth。 依赖外部服务：IOpenTokenFacadeService, ContextService, OpenAdminService。 提供统一认证授权能力，支持多端登录、Token 管理、权限校验等安全机制。

### opencloud

【opencloud】是面向企业办公场景的上传 + 下载 + 发送服务。 主要提供删除, 表单服务等业务处理能力。 系统采用分层架构设计，包含1个 REST 接口, 16个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserBaseService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担上传职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### opencode

【opencode】是企业微服务架构中的业务服务模块。 核心功能包括：即时通讯, 新增, 表单服务等。 系统采用分层架构设计，包含4个业务服务，支持高并发业务场景。 模块划分为：yzj。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担核心业务职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### opencommon

⚠️ 未找到有效 Java 源代码

### opendata-control

【opendata-control】是面向企业办公场景的发送服务。 核心功能包括：即时通讯, 新增, 查询, 认证鉴权等。 系统采用分层架构设计，包含4个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：IYZJOrgService, IYZJOrgAdminService, IOSSUserNetworkService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### openid

【openid】是面向企业办公场景的发送 + 同步服务。 核心功能包括：即时通讯, 流程引擎, 认证鉴权, 查询等。 系统采用分层架构设计，包含1个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：IUserExtendService, YZJUserNetworkServiceAdapter。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### openimport

【openimport】是面向企业办公场景的同步 + 下载 + 邀请服务。 核心功能包括：AI 能力, 新增, 删除, 表单服务等。 系统采用分层架构设计，包含1个 REST 接口, 66个业务服务, 10个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：IYZJUserGroupService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担同步职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### openorg

【openorg】是面向企业办公场景的提醒 + 同步 + 邀请服务。 核心功能包括：组织管理, 更新, 删除, 邀请分享等。 系统采用分层架构设计，包含108个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：IAddressNewCacheService, YZJOrgSearchRuleService, HidePhoneServiceV2。 为企业数字化办公提供稳定可靠的后台服务能力。

### opensync

【opensync】是面向企业办公场景的日程 + 发送 + 提醒服务。 核心功能包括：即时通讯, 新增, 组织管理, 安全审计等。 系统采用分层架构设计，包含1个 REST 接口, 18个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：IOrgAdminService, IUniversalService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担日程职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### opentalk

【opentalk】是面向企业办公场景的发送服务。 核心功能包括：新增, 删除, 表单服务等。 系统采用分层架构设计，包含13个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：TalkServiceImpl。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### opentalk-proxy

【opentalk-proxy】是面向企业办公场景的发送服务。 核心功能包括：新增, 删除, 表单服务等。 系统采用分层架构设计，包含10个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：SimpleNotifyRecordServiceImpl, CompanyService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### oplogserver

【oplogserver】是面向企业办公场景的发送 + 生成服务。 核心功能包括：新增, 组织管理, AI 能力, 更新等。 系统采用分层架构设计，包含11个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：KafkaService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### orgunit-rest

【orgunit-rest】是面向企业办公场景的提醒 + 同步 + 下载服务。 核心功能包括：即时通讯, 新增, 更新, 用户管理等。 系统采用分层架构设计，包含35个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：DomainRelationService, JoinCommunityApplicationService, UserNetworkService。 为企业数字化办公提供稳定可靠的后台服务能力。

### passport-api

⚠️ 未找到有效 Java 源代码

### passport-service

【passport-service】是面向企业办公场景的日程 + 同步服务。 核心功能包括：新增, 认证鉴权, 安全审计, AI 能力等。 系统采用分层架构设计，包含6个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：IAuthWeComChildAppService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担日程职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### pubacc

⚠️ 未找到有效 Java 源代码

### pubacc-boot

【pubacc-boot】是面向企业办公场景的群组 + 空间 + 同步服务。 核心功能包括：即时通讯, 新增, 查询, 组织管理等。 系统采用分层架构设计，包含18个 REST 接口, 43个业务服务，支持高并发业务场景。 模块划分为：yunzhijia, baidu。 依赖外部服务：LinkSpaceService, PubaccMessageService。 集成大模型能力，提供智能问答、助手服务、自动化处理等 AI 增强功能。

### ratelimiter4j

⚠️ 未找到有效 Java 源代码

### redpacket

⚠️ 未找到有效 Java 源代码

### sapphire

【sapphire】是面向企业办公场景的上传服务。 核心功能包括：查询, 文档处理, 文件处理, 消息推送等。 系统采用分层架构设计，包含17个业务服务，支持高并发业务场景。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担上传职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### scc-microservice

【scc-microservice】是面向企业办公场景的同步 + 日程 + 应用服务。 核心功能包括：新增, 更新, 任务管理, 统计分析等。 系统采用分层架构设计，包含11个 REST 接口, 18个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：SiteControlService, SendMsgService。 内置流程引擎和表单引擎，支持业务流程编排和动态表单配置。

### searchdata-incrementsync-service

【searchdata-incrementsync-service】是面向企业办公场景的群组 + 组织 + 同步服务。 核心功能包括：即时通讯, 新增, 安全审计, 表单服务等。 系统采用分层架构设计，包含20个 REST 接口, 39个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：XtRobotIndexService, GroupUserIndexService, PubaccMessageService。 提供 IM 即时通讯能力，支持单聊、群聊、消息推送、已读回执等功能。

### security-server

【security-server】是面向企业办公场景的安全 + 发送 + 同步服务。 核心功能包括：新增, 安全审计, AI 能力, 更新等。 系统采用分层架构设计，包含1个 REST 接口, 8个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：SecurityLogService, NotifyService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担安全职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### securitycenter

【securitycenter】是面向企业办公场景的发送服务。 核心功能包括：新增, 用户管理, 删除, 任务管理等。 系统采用分层架构设计，包含8个业务服务，支持高并发业务场景。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### sentinel-dashboard

【sentinel-dashboard】是面向企业办公场景的流程 + 应用 + 认证服务。 核心功能包括：新增, 认证鉴权, 流程引擎, 安全审计等。 系统采用分层架构设计，包含17个 REST 接口, 2个业务服务，支持高并发业务场景。 模块划分为：alibaba。 依赖外部服务：ClusterConfigService。 提供统一认证授权能力，支持多端登录、Token 管理、权限校验等安全机制。

### service-commander

【service-commander】是面向企业办公场景的发送 + 生成 + 用户服务。 核心功能包括：新增, 流程引擎, 认证鉴权, 安全审计等。 系统采用分层架构设计，包含8个 REST 接口, 15个业务服务, 12个数据实体，支持高并发业务场景。 模块划分为：yzj。 依赖外部服务：IKubernetesService, FlowRemoveRuleService。 为企业数字化办公提供稳定可靠的后台服务能力。

### smartatt-clock

【smartatt-clock】是面向企业办公场景的任务 + 提醒 + 日志服务。 核心功能包括：即时通讯, 流程引擎, 认证鉴权, 新增等。 系统采用分层架构设计，包含19个 REST 接口, 27个业务服务，支持高并发业务场景。 模块划分为：dangdang, yunzhijia。 依赖外部服务：AttendanceTransferMappingService, RobotFeignService, AttendanceTransferService。 支撑企业员工考勤管理全流程，实现打卡记录、统计分析、异常处理等核心业务。

### smartatt-sign

【smartatt-sign】是面向企业办公场景的签到 + 打卡服务。 核心功能包括：即时通讯, 新增, 考勤打卡, 统计分析等。 系统采用分层架构设计，包含7个 REST 接口, 8个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：ExcepSignService, SignConfigService。 支撑企业员工考勤管理全流程，实现打卡记录、统计分析、异常处理等核心业务。

### sms-service

【sms-service】是面向企业办公场景的发送 + 同步服务。 核心功能包括：新增, 更新, 统计分析, 消息推送等。 系统采用分层架构设计，包含12个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：SMSReportService, SMSRecvRptService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### smsconfig-service

【smsconfig-service】是面向企业办公场景的发送 + 同步服务。 核心功能包括：新增, 安全审计, 更新, 删除等。 系统采用分层架构设计，包含13个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：SMSCustomService, SMSSccTrafficService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### smsgateway

⚠️ 未找到有效 Java 源代码

### smsgateway-service

【smsgateway-service】是面向企业办公场景的发送 + 生成服务。 核心功能包括：新增, 查询, 更新, 任务管理等。 系统采用分层架构设计，包含63个业务服务，支持高并发业务场景。 模块划分为：emay, kingdee, qcloud。 依赖外部服务：EnvMobileCtrlService, SMSServiceUnitRateService。 为企业数字化办公提供稳定可靠的后台服务能力。

### smsmanage-service

【smsmanage-service】是面向企业办公场景的发送 + 同步服务。 核心功能包括：新增, 更新, 任务管理, 通知服务等。 系统采用分层架构设计，包含12个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：SMSStatService, SMSServiceTypeTemplateDAO。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### snsapi

【snsapi】是面向企业办公场景的同步 + 打卡 + 上传服务。 核心功能包括：用户管理, 认证鉴权, 表单服务等。 系统采用分层架构设计，包含60个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：PrivateMessageService, JoinCommunityApplicationService, NewsService, UserPrivateMessageThreadService, AttendanceMachineHelperService。 支撑企业员工考勤管理全流程，实现打卡记录、统计分析、异常处理等核心业务。

### space

【space】是面向企业办公场景的同步 + 上传 + 邀请服务。 核心功能包括：新增, 数据导入导出, 更新, 用户管理等。 系统采用分层架构设计，包含23个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：JoinCommunityApplicationService, UserNetworkService, NetworkBaseService, IWecomCloudHubService, NetworkService。 为企业数字化办公提供稳定可靠的后台服务能力。

### spring-boot-yzj-llm-starter

⚠️ 未找到有效 Java 源代码

### stakeholder-api

⚠️ 未找到有效 Java 源代码

### stakeholder-service

【stakeholder-service】是面向企业办公场景的同步服务。 核心功能包括：即时通讯, 新增, 更新, 用户管理等。 系统采用分层架构设计，包含8个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：NewNetworkService, NewUserService, NewAccountService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担同步职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### statusNotice-rest

【statusNotice-rest】是面向企业办公场景的日程 + 发送 + 同步服务。 核心功能包括：新增, 定时提醒, 更新, 数据同步等。 系统采用分层架构设计，包含3个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：AsyncDealService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担日程职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### statusUser-rest

【statusUser-rest】是面向企业办公场景的发送 + 同步服务。 核心功能包括：即时通讯, 新增, 更新, 用户管理等。 系统采用分层架构设计，包含4个业务服务，支持高并发业务场景。 模块划分为：kingdee。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### syncdata

【syncdata】是企业微服务架构中的业务服务模块。 核心功能包括：即时通讯, 新增, 数据导入导出, 文档处理等。 系统采用分层架构设计，包含1个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：ShareImportService, WpsSyncService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担核心业务职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### task-service

【task-service】是面向企业办公场景的提醒 + 生成服务。 核心功能包括：新增, 流程引擎, 安全审计, 定时提醒等。 系统采用分层架构设计，包含7个业务服务, 2个数据实体，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：PrivateMessageService, UserNetworkService, MicroblogService, TaskMsgPushService。 为企业数字化办公提供稳定可靠的后台服务能力。

### team-report-service

【team-report-service】是面向企业办公场景的同步 + 日志 + 报表服务。 核心功能包括：即时通讯, 新增, 查询, 组织管理等。 系统采用分层架构设计，包含5个 REST 接口, 12个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：ISumUserService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担同步职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### ticket

【ticket】是面向企业办公场景的发送 + 生成服务。 核心功能包括：认证鉴权, 组织管理, 表单服务等。 系统采用分层架构设计，包含7个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：IContextService, IOpenOrgService, ILightAppService, IOpenCloudService, IAuthorizationService。 为企业数字化办公提供稳定可靠的后台服务能力。

### ticket-service

【ticket-service】是面向企业办公场景的发送 + 生成服务。 核心功能包括：认证鉴权, 组织管理, 表单服务等。 系统采用分层架构设计，包含6个业务服务，支持高并发业务场景。 模块划分为：kingdee, yunzhijia。 依赖外部服务：IOpenOrgService, ILightAppService, IOpenCloudService, IAuthorizationService, IOpenAdminService。 为企业数字化办公提供稳定可靠的后台服务能力。

### tinyurl-rest

【tinyurl-rest】是面向企业办公场景的生成服务。 核心功能包括：新增, 删除, 表单服务等。 系统采用分层架构设计，包含1个 REST 接口, 5个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：HashIdService, BlackListService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担生成职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### todo-service

【todo-service】是面向企业办公场景的发送 + 生成服务。 核心功能包括：新增, 查询, 组织管理, 更新等。 系统采用分层架构设计，包含3个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserService, ApplicationService, UserNetworkService, TodoConfigureService。 为企业数字化办公提供稳定可靠的后台服务能力。

### tool-yzj-nacos-config-center

【tool-yzj-nacos-config-center】是企业微服务架构中的业务服务模块。 主要提供表单服务等业务处理能力。 系统采用分层架构设计，包含2个业务服务，支持高并发业务场景。 模块划分为：yzj。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担核心业务职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### usercore-service

【usercore-service】是面向企业办公场景的分享 + 发送 + 同步服务。 核心功能包括：即时通讯, 新增, 用户管理, 删除等。 系统采用分层架构设计，包含86个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：YZJHidePhoneTypeServiceRepository。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担分享职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### version-control

【version-control】是企业微服务架构中的业务服务模块。 主要提供表单服务等业务处理能力。 系统采用分层架构设计，包含9个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserBaseService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担核心业务职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### voice-robot-assistant

【voice-robot-assistant】是面向企业办公场景的下载 + 日程 + 发送服务。 核心功能包括：统计分析, 消息推送, 即时通讯, 表单服务等。 系统采用分层架构设计，包含20个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：IntentDetectService, KnowledgeInfoService。 为企业数字化办公提供稳定可靠的后台服务能力。

### vpn-service

【vpn-service】是企业微服务架构中的业务服务模块。 核心功能包括：即时通讯, 认证鉴权, 查询, 表单服务等。 系统采用分层架构设计，包含3个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：VpnService, DataStatisticsService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担核心业务职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### work-wechat-service

【work-wechat-service】是面向企业办公场景的聊天 + 应用 + 上传服务。 核心功能包括：即时通讯, 新增, 认证鉴权, 组织管理等。 系统采用分层架构设计，包含2个 REST 接口, 4个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：OpenOrgService。 提供统一认证授权能力，支持多端登录、Token 管理、权限校验等安全机制。 该项目在整体架构中承担聊天职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### workassistant-ai-agent

【workassistant-ai-agent】是面向企业办公场景的发送 + 用户服务。 核心功能包括：即时通讯, 新增, 查询, AI 能力等。 系统采用分层架构设计，包含5个 REST 接口, 4个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：MeetingServiceRpcAccessor。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担发送职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### workassistant-service

【workassistant-service】是面向企业办公场景的通知 + 日程 + 短信服务。 核心功能包括：即时通讯, 新增, AI 能力, 更新等。 系统采用分层架构设计，包含48个 REST 接口, 104个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：CommonCommentService。 统一消息发送通道，支持短信、邮件、Push 等多种触达方式，保障消息及时送达。

### workquestionnaire-service

【workquestionnaire-service】是面向企业办公场景的聊天 + AI + 上传服务。 核心功能包括：即时通讯, 新增, 文档处理, AI 能力等。 系统采用分层架构设计，包含4个 REST 接口, 10个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：UserCoreService, IStatisticLocalService。 提供统一认证授权能力，支持多端登录、Token 管理、权限校验等安全机制。

### workreport

【workreport】是面向企业办公场景的提醒服务。 核心功能包括：新增, 查询, 流程引擎, 数据导入导出等。 系统采用分层架构设计，包含3个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：WorkReportService, WorkReportBasicService, LightappConfigureService, WorkReportUserPermissionService, TreeOrgInfoService。 为企业数字化办公提供稳定可靠的后台服务能力。

### workreport-form-service

【workreport-form-service】是面向企业办公场景的提醒 + 同步 + 日程服务。 核心功能包括：认证鉴权, 组织管理, 安全审计, AI 能力等。 系统采用分层架构设计，包含1个 REST 接口, 52个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：FreeflowService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担提醒职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### wps-server

【wps-server】是面向企业办公场景的WPS 办公 + 同步 + 下载服务。 核心功能包括：文档处理, 新增, 认证鉴权, 表单服务等。 系统采用分层架构设计，包含6个 REST 接口, 8个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：WpsService, WWOWpsService。 提供企业文档全生命周期管理，支持上传下载、在线预览、权限控制等功能。 该项目在整体架构中承担WPS 办公职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### wpsoffice-proxy

【wpsoffice-proxy】是面向企业办公场景的下载 + 同步服务。 核心功能包括：新增, 查询, 文档处理, 更新等。 系统采用分层架构设计，包含2个 REST 接口, 6个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：WpsRequestService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担下载职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### xeryun-http

⚠️ 未找到有效 Java 源代码

### xeryun-io

⚠️ 未找到有效 Java 源代码

### xeryun-security

⚠️ 未找到有效 Java 源代码

### xeryun-server

⚠️ 未找到有效 Java 源代码

### xeryun-servlet

⚠️ 未找到有效 Java 源代码

### xeryun-servlets

⚠️ 未找到有效 Java 源代码

### xeryun-spring-boot-starter

⚠️ 未找到有效 Java 源代码

### xeryun-spring-boot-v2-1-starter

⚠️ 未找到有效 Java 源代码

### xeryun-spring-boot-v2-starter

⚠️ 未找到有效 Java 源代码

### xeryun-util

⚠️ 未找到有效 Java 源代码

### xeryun-webapp

⚠️ 未找到有效 Java 源代码

### xeryun-websocket-all

⚠️ 未找到有效 Java 源代码

### xeryun-xml

⚠️ 未找到有效 Java 源代码

### xt-common

⚠️ 未找到有效 Java 源代码

### xt-entry

⚠️ 未找到有效 Java 源代码

### xt-entry-sl

⚠️ 未找到有效 Java 源代码

### xt-interface

【xt-interface】是面向企业办公场景的机器人 + 发送 + 群组服务。 核心功能包括：即时通讯, 新增, 流程引擎, 组织管理等。 系统采用分层架构设计，包含9个 REST 接口, 3个业务服务，支持高并发业务场景。 模块划分为：kingdee。 集成大模型能力，提供智能问答、助手服务、自动化处理等 AI 增强功能。 该项目在整体架构中承担机器人职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### xt-lcc-common

⚠️ 未找到有效 Java 源代码

### xt-push

【xt-push】是面向企业办公场景的日程 + 发送 + 同步服务。 核心功能包括：即时通讯, 删除, 消息推送, 通知服务等。 系统采用分层架构设计，包含3个业务服务，支持高并发业务场景。 模块划分为：kingdee, harmony, huawei, vivo, oppo。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担日程职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### xt-robot

【xt-robot】是面向企业办公场景的群组 + 提醒 + 同步服务。 核心功能包括：即时通讯, 新增, 查询, AI 能力等。 系统采用分层架构设计，包含16个 REST 接口, 22个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：FeatureService。 集成大模型能力，提供智能问答、助手服务、自动化处理等 AI 增强功能。 该项目在整体架构中承担群组职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### xt-userinfo

⚠️ 未找到有效 Java 源代码

### xt-websocket

⚠️ 未找到有效 Java 源代码

### xuntong-ai-agent

【xuntong-ai-agent】是面向企业办公场景的搜索 + 同步服务。 核心功能包括：新增, 认证鉴权, 文档处理, 用户管理等。 系统采用分层架构设计，包含4个 REST 接口, 6个业务服务，支持高并发业务场景。 模块划分为：yzj。 依赖外部服务：NaturalLanguageRecognitionService, AISearchService。 为企业数字化办公提供稳定可靠的后台服务能力。

### yzj-crm-common

⚠️ 未找到有效 Java 源代码

### yzj-mail-server

【yzj-mail-server】是面向企业办公场景的同步 + 日程 + 下载服务。 核心功能包括：更新, 删除, 数据同步, 表单服务等。 系统采用分层架构设计，包含17个 REST 接口, 27个业务服务，支持高并发业务场景。 模块划分为：yzj。 依赖外部服务：ExchangeServiceFactory, OriginEmailService, FileService。 提供企业文档全生命周期管理，支持上传下载、在线预览、权限控制等功能。

### yzj-mcp-server-spring-boot-starter

⚠️ 未找到有效 Java 源代码

### yzj-mcp-server-spring-mvc

⚠️ 未找到有效 Java 源代码

### yzj-mcp-spring-boot-starter-v1

⚠️ 未找到有效 Java 源代码

### yzj-nacos-client

⚠️ 未找到有效 Java 源代码

### yzj-space-api

⚠️ 未找到有效 Java 源代码

### yzj-space-manager

【yzj-space-manager】是面向企业办公场景的组织 + 日志 + 用户服务。 核心功能包括：审批流程, 新增, 认证鉴权, 查询等。 系统采用分层架构设计，包含10个 REST 接口, 16个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：UserService。 提供统一认证授权能力，支持多端登录、Token 管理、权限校验等安全机制。 该项目在整体架构中承担组织职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### yzj-space-service

【yzj-space-service】是面向企业办公场景的空间 + 同步 + 日志服务。 核心功能包括：云存储, 流程引擎, 认证鉴权, 新增等。 系统采用分层架构设计，包含18个 REST 接口, 213个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：UserNotifyService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担空间职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### yzj-spring-boot-ai-starter

【yzj-spring-boot-ai-starter】是面向企业办公场景的聊天 + 应用 + 发送服务。 核心功能包括：AI 能力, 即时通讯, 表单服务等。 系统采用分层架构设计，包含3个 REST 接口, 2个业务服务，支持高并发业务场景。 模块划分为：yzj。 提供 IM 即时通讯能力，支持单聊、群聊、消息推送、已读回执等功能。 该项目在整体架构中承担聊天职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

### yzj-tool-config-center

⚠️ 未找到有效 Java 源代码

### yzj-useragent-tool-common

⚠️ 未找到有效 Java 源代码

### yzj-xeryun-dropwizard-core

⚠️ 未找到有效 Java 源代码

### yzjomc-service

【yzjomc-service】是面向企业办公场景的上传 + 发送 + 生成服务。 主要提供查询, 表单服务等业务处理能力。 系统采用分层架构设计，包含9个 REST 接口, 21个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：YzjAppServiceHttpAdapter, CqServiceHttpAdapter, YzjCmcServiceRPCAdapter, OrderItemService。 为企业数字化办公提供稳定可靠的后台服务能力。

### yzjsdpc-service

【yzjsdpc-service】是面向企业办公场景的上传 + 发送 + 生成服务。 核心功能包括：更新, 删除, 统计分析, 消息推送等。 系统采用分层架构设计，包含4个 REST 接口, 11个业务服务，支持高并发业务场景。 模块划分为：yunzhijia。 依赖外部服务：DeliveryOrderService, ServiceInstanceService, CustomerServiceRpcAdapter。 为企业数字化办公提供稳定可靠的后台服务能力。

### zyy-redpacket-service

【zyy-redpacket-service】是面向企业办公场景的红包服务。 核心功能包括：即时通讯, 新增, 用户管理, 任务管理等。 系统采用分层架构设计，包含2个 REST 接口, 6个业务服务，支持高并发业务场景。 模块划分为：kingdee。 依赖外部服务：UserService, UserNetworkService。 为企业数字化办公提供稳定可靠的后台服务能力。 该项目在整体架构中承担红包职责，与其他微服务协同工作，共同支撑企业级应用的高可用、高并发需求。

