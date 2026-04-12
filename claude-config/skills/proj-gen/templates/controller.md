# Controller 模板

> **规范要点**：
> 1. Controller 只做参数校验和响应包装，业务逻辑放在 Service 层
> 2. 写操作必须添加 `@ApiLog`，请求参数使用 `@Validated`，统一返回 `Result<T>`
> 3. 使用 `@RequiredArgsConstructor`，异常由全局处理器统一处理

**示例对比**：

❌ **错误示例**（业务逻辑泄露到 Controller）：
```java
@PutMapping("/{id}")
public Result<Void> update(@PathVariable String id, @RequestBody {Domain}UpdateRequest request) {
    // 错误：业务逻辑应该在 Service 层
    if (request.getName() == null || request.getName().isEmpty()) {
        throw new BusinessException("Name cannot be empty");
    }

    {Domain} domain = {domain}Dao.findById(id);
    domain.setName(request.getName());
    // 错误：直接操作 DAO
    {domain}Dao.save(domain);

    return Result.success();
}
```

✅ **正确示例**（只做参数校验和响应包装）：
```java
@PutMapping("/{id}")
public Result<Void> update(@PathVariable String id, @RequestBody @Validated {Domain}UpdateRequest request) {
    // ✅ 参数校验由 @Validated 完成
    // ✅ 业务逻辑委托给 Service
    {domain}Service.update(id, request);
    // ✅ 只包装响应
    return Result.success();
}
```

## Web端 Controller

```java
package com.{company}.{project}.{module}.controller;

import com.{company}.{project}.common.annotation.ApiLog;
import com.{company}.{project}.common.core.Result;
import com.{company}.{project}.{module}.model.request.*;
import com.{company}.{project}.{module}.model.response.{Domain}Response;
import com.{company}.{project}.{module}.service.{Domain}Service;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.Page;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import org.springframework.security.access.prepost.PreAuthorize;

import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import java.util.List;
import java.util.stream.Collectors;

/**
 * {description}控制器
 *
 * @author {author}
 * @since {date}
 */
@Slf4j
@Api(tags = "{description} Management", description = "Provides CRUD APIs for {description}")
@RestController
@RequestMapping("/{project}/web/v1/{module}")
@RequiredArgsConstructor
public class {Domain}Controller {

    private final {Domain}Service {domain}Service;

    /**
     * 分页查询{description}
     */
    @ApiOperation(value = "Page query for {description}", notes = "分页查询{description}")
    @GetMapping("/page")
    @PreAuthorize("hasAuthority('{module}:query')")
    public Result<Page<{Domain}Response>> page(@Validated {Domain}QueryRequest request) {
        Page<{Domain}Response> result = {domain}Service.pageQuery(request);
        return Result.success(result);
    }
    /**
     * 获取{description}详情
     */
    @ApiOperation(value = "Get {description} detail", notes = "获取{description}详情")
    @GetMapping("/{id}")
    @PreAuthorize("hasAuthority('{module}:query')")
    public Result<{Domain}Response> detail(@PathVariable String id) {
        {Domain}Response result = {domain}Service.getDetail(id);
        return Result.success(result);
    }

    /**
     * 创建{description}
     */
    @ApiOperation(value = "Create {description}", notes = "创建{description}")
    @ApiLog("Create {description}")
    @PostMapping
    @PreAuthorize("hasAuthority('{module}:create')")
    public Result<String> create(@RequestBody @Validated {Domain}CreateRequest request) {
        String id = {domain}Service.create(request);
        return Result.success(id);
    }

    /**
     * 更新{description}
     */
    @ApiOperation(value = "Update {description}", notes = "更新{description}")
    @ApiLog("Update {description}")
    @PutMapping("/{id}")
    @PreAuthorize("hasAuthority('{module}:update')")
    public Result<Void> update(
            @PathVariable String id,
            @RequestBody @Validated {Domain}UpdateRequest request) {
        {domain}Service.update(id, request);
        return Result.success();
    }

    /**
     * 删除{description}
     */
    @ApiOperation(value = "Delete {description}", notes = "删除{description}")
    @ApiLog("Delete {description}")
    @DeleteMapping("/{id}")
    @PreAuthorize("hasAuthority('{module}:delete')")
    public Result<Void> delete(@PathVariable String id) {
        {domain}Service.deleteById(id);
        return Result.success();
    }

    /**
     * 批量删除{description}
     */
    @ApiOperation(value = "Batch delete {description}", notes = "批量删除{description}")
    @ApiLog("Batch delete {description}")
    @PostMapping("/batch-delete")
    @PreAuthorize("hasAuthority('{module}:delete')")
    public Result<Void> batchDelete(
            @RequestBody @NotEmpty(message = "ID列表不能为空") @Size(max = 1000, message = "批量删除最多支持1000条") List<@NotNull String> ids) {

        // 参数去重
        List<String> uniqueIds = ids.stream().distinct().collect(Collectors.toList());

        {domain}Service.batchDelete(uniqueIds);
        return Result.success();
    }

    /**
     * 启用/禁用{description}
     */
    @ApiOperation(value = "Enable/Disable {description}", notes = "启用/禁用{description}")
    @ApiLog("Enable/Disable {description}")
    @PutMapping("/{id}/status")
    @PreAuthorize("hasAuthority('{module}:update')")
    public Result<Void> updateStatus(@PathVariable String id,
            @RequestParam @NotNull(message = "状态不能为空") Integer status) {
        {domain}Service.updateStatus(id, status);
        return Result.success();
    }
}
```

---

## App端 Controller (移动端)

```java
package com.{company}.{project}.api.controller;

import com.{company}.{project}.common.core.Result;
import com.{company}.{project}.{module}.model.request.*;
import com.{company}.{project}.{module}.model.response.{Domain}Response;
import com.{company}.{project}.{module}.service.{Domain}Service;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * {description}移动端控制器
 *
 * @author {author}
 * @since {date}
 */
@Slf4j
@Api(tags = "{description}", description = "Provides query APIs for {description}")
@RestController
@RequestMapping("/{project}/api/v1/{module}")
@RequiredArgsConstructor
public class {Domain}AppController {

    private final {Domain}Service {domain}Service;

    /**
     * 获取{description}列表
     */
    @ApiOperation(value = "Get {description} list", notes = "获取{description}列表")
    @GetMapping("/list")
    public Result<List<{Domain}Response>> list(@Validated {Domain}QueryRequest request) {
        List<{Domain}Response> result = {domain}Service.list(request);
        return Result.success(result);
    }
    /**
     * 获取{description}详情
     */
    @ApiOperation(value = "Get {description} detail", notes = "获取{description}详情")
    @GetMapping("/{id}")
    public Result<{Domain}Response> detail(@PathVariable String id) {
        {Domain}Response result = {domain}Service.getDetail(id);
        return Result.success(result);
    }

}
```