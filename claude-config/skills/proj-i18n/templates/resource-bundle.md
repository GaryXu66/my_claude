# 资源包模板

资源包文件位置：`src/main/resources/i18n/`

**默认语言：** 英文（`message.properties`）

## Key 设计规范

### 命名格式

**格式：** 帕斯卡命名（PascalCase）

```
{模块名}[{业务}][{动作/状态}]
```

- **首字母大写**：使用帕斯卡命名
- **模块前缀**：以模块名开头（如 User、Order、Product）
- **语义清晰**：见名知意

### 命名规则详解

#### 1. 模块名优先原则

**第一部分必须是模块名**，如 `User`、`Order`、`Product`，而不是 `Error`、`Validation` 等通用前缀。

**正确示例：**
```properties
UserErrorNotFound=User not found
UserCreateSuccess=User created successfully
OrderPaymentTimeout=Payment timeout
```

**错误示例：**
```properties
ErrorUserNotFound=User not found        # 错误：不应以 Error 开头
ValidationErrorUsername=Username invalid # 错误：不应以 Validation 开头
```

#### 2. 通用消息例外

只有非常通用、跨模块共享的消息，才允许使用 `Common`、`Validation` 等通用前缀：

| 前缀 | 适用场景 | 示例 |
|------|----------|------|
| `Common*` | 通用操作消息 | CommonSuccess、CommonFailed、CommonLoading |
| `Validation*` | 通用验证错误 | ValidationErrorRequired（字段必填）、ValidationErrorFormat（格式错误） |
| `System*` | 系统级错误 | SystemError、SystemBusy |

#### 3. 完整命名示例

```properties
# ===== 通用消息（Common*、Validation*）=====
CommonSuccess=Operation successful
CommonFailed=Operation failed
ValidationErrorRequired=Field ''{0}'' is required
ValidationErrorEmailFormat=Invalid email format

# ===== 用户模块（User*）=====
UserErrorNotFound=User not found
UserErrorPassword=Password error
UserCreateSuccess=Created successfully
UserDeleteSuccess=Deleted successfully

# ===== 订单模块（Order*）=====
OrderErrorNotFound=Order not found
OrderPaymentTimeout=Payment timeout
OrderCreateSuccess=Order created

# ===== 商品模块（Product*）=====
ProductErrorNotFound=Product not found
ProductInventoryInsufficient=Insufficient inventory
```

**避免：**
```properties
# 无规律、难以维护
Msg1=User not found
Msg2=Password error
ErrUser=User exception
User001=Not found
User002=Password error
```

### 模块划分建议

```
- Common*     # 通用消息
- User*       # 用户模块
- Order*      # 订单模块
- Product*    # 商品模块
- Payment*    # 支付模块
```

### 单复数处理

使用简单的 **`user(s)`** 格式表示复数（推荐方式）：

```properties
# 英文：使用 (s) 表示可能的复数
UserCount={0} user(s)
AppleCount={0} apple(s)
OrderCount={0} order(s)

# 简体中文：不区分单复数
UserCount={0} 个用户
AppleCount={0} 个苹果
OrderCount={0} 个订单

# 繁体中文：不区分单复数
UserCount={0} 個用戶
AppleCount={0} 個蘋果
OrderCount={0} 個訂單
```

---

## 默认资源（英文）

### message.properties

```properties
# ===== Common Messages =====
CommonSuccess=Operation successful
CommonFailed=Operation failed
CommonLoading=Loading...
CommonDeleteSuccess=Delete successful
CommonAddSuccess=Add successful
CommonUpdateSuccess=Update successful
CommonNoData=No data

# ===== User Module =====
UserErrorNotFound=User not found
UserErrorAlreadyExists=User already exists
UserErrorPassword=Password error
UserCreateSuccess=User created successfully
UserDeleteSuccess=User deleted successfully
UserErrorPermissionDenied=Permission denied

# ===== Order Module =====
OrderErrorNotFound=Order not found
OrderPaymentTimeout=Payment timeout
OrderPaymentFailed=Payment failed

# ===== Product Module =====
ProductErrorNotFound=Product not found
ProductInventoryInsufficient=Insufficient inventory
ProductDisabled=Product is out of stock

# ===== Payment Module =====
PaymentAmountInvalid=Invalid payment amount
PaymentMethodNotSupported=Payment method not supported
PaymentTimeout=Payment timeout
```

---

## 中文资源

### message_zh_CN.properties

```properties
# ===== 通用消息（Common*） =====
CommonSuccess=操作成功
CommonFailed=操作失败
CommonLoading=加载中...
CommonDeleteSuccess=删除成功
CommonAddSuccess=新增成功
CommonUpdateSuccess=更新成功
CommonNoData=暂无数据

# ===== 用户模块（User*） =====
UserErrorNotFound=用户不存在
UserErrorAlreadyExists=用户已存在
UserErrorPassword=密码错误
UserCreateSuccess=用户创建成功
UserDeleteSuccess=用户删除成功
UserErrorPermissionDenied=权限不足

# ===== 订单模块（Order*） =====
OrderErrorNotFound=订单不存在
OrderPaymentTimeout=支付超时
OrderPaymentFailed=支付失败

# ===== 商品模块（Product*） =====
ProductErrorNotFound=商品不存在
ProductInventoryInsufficient=库存不足
ProductDisabled=商品已下架

# ===== 支付模块（Payment*） =====
PaymentAmountInvalid=支付金额无效
PaymentMethodNotSupported=不支持该支付方式
PaymentTimeout=支付超时
```

---

## 繁体中文资源

### message_zh_TW.properties

```properties
# ===== 通用消息（Common*） =====
CommonSuccess=操作成功
CommonFailed=操作失敗
CommonLoading=載入中...
CommonDeleteSuccess=刪除成功
CommonAddSuccess=新增成功
CommonUpdateSuccess=更新成功
CommonNoData=暫無資料

# ===== 用戶模組（User*） =====
UserErrorNotFound=用戶不存在
UserErrorAlreadyExists=用戶已存在
UserErrorPassword=密碼錯誤
UserCreateSuccess=用戶創建成功
UserDeleteSuccess=用戶刪除成功
UserErrorPermissionDenied=權限不足

# ===== 訂單模組（Order*） =====
OrderErrorNotFound=訂單不存在
OrderPaymentTimeout=支付超時
OrderPaymentFailed=支付失敗

# ===== 商品模組（Product*） =====
ProductErrorNotFound=商品不存在
ProductInventoryInsufficient=庫存不足
ProductDisabled=商品已下架

# ===== 支付模組（Payment*） =====
PaymentAmountInvalid=支付金額無效
PaymentMethodNotSupported=不支援該支付方式
PaymentTimeout=支付超時
```

---

## 使用说明

### 文件位置

将这些文件保存到项目的资源目录：

```
src/main/resources/
└── i18n/
    ├── message.properties          # 默认（英文）
    ├── message_zh_CN.properties    # 简体中文
    └── message_zh_TW.properties    # 繁体中文
```

### 添加新的语言

1. 复制 `message.properties` 创建新文件，例如 `message_zh_TW.properties`
2. 翻译所有 key 对应的 value
3. 保存文件，确保编码为 UTF-8

### 注意事项

- key 使用帕斯卡命名（PascalCase）
- 在 value 中使用单引号需要转义：`''` 表示一个单引号
- 避免在不同资源包间重复定义同一个 key
- **添加新消息时，必须同时添加到所有语言文件中**



