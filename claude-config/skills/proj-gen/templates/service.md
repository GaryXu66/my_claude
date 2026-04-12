# Service 模板

> **规范要点**：
> 1. 使用返回值进行流程控制，捕获异常时必须记录日志或重新抛出
> 2. 业务异常统一使用 `BusinessException`，在方法入口和出口处记录日志
> 3. 使用批量查询或 JOIN 避免 N+1 问题，超过 500 条数据时分批处理
> 4. 批量写操作必须添加 `@Transactional` 注解

## Service 接口

```java
package com.{company}.{project}.{module}.service;

import com.{company}.{project}.{module}.domain.{Domain};
import com.{company}.{project}.{module}.enums.StatusEnum;
import com.{company}.{project}.{module}.model.request.*;
import com.{company}.{project}.{module}.model.response.{Domain}Response;
import org.springframework.data.domain.Page;
import java.util.List;

/**
 * {description}服务接口
 *
 * @author {author}
 * @since {date}
 */
public interface {Domain}Service {

    /**
     * 创建{description}
     *
     * @param request 创建请求
     * @return 主键ID
     * @throws com.{company}.{project}.common.exception.BusinessException 创建失败时抛出
     */
    String create({Domain}CreateRequest request);

    /**
     * 更新{description}
     *
     * @param id      主键ID
     * @param request 更新请求
     * @throws com.{company}.{project}.common.exception.BusinessException 更新失败时抛出
     */
    void update(String id, {Domain}UpdateRequest request);

    /**
     * 删除{description}
     *
     * @param id 主键ID
     * @throws com.{company}.{project}.common.exception.BusinessException 删除失败时抛出
     */
    void deleteById(String id);

    /**
     * 获取{description}详情
     *
     * @param id 主键ID
     * @return {description}详情信息
     * @throws com.{company}.{project}.common.exception.BusinessException 数据不存在时抛出
     */
    {Domain}Response getDetail(String id);

    /**
     * 列表查询{description}
     *
     * @param request 查询请求
     * @return {description}列表
     */
    List<{Domain}Response> list({Domain}QueryRequest request);

    /**
     * 分页查询{description}
     *
     * @param request 查询请求
     * @return 分页结果
     */
    Page<{Domain}Response> pageQuery({Domain}QueryRequest request);

    /**
     * 更新状态
     *
     * @param id 主键ID
     * @param status 状态值(1-启用, 0-禁用)
     */
    void updateStatus(String id, Integer status);

    /**
     * 批量删除
     *
     * @param ids ID列表
     */
    void batchDelete(List<String> ids);
}
```

---

## Service 实现类

```java
package com.{company}.{project}.{module}.service.impl;

import cn.hutool.core.bean.BeanUtil;
import cn.hutool.core.collection.CollUtil;
import cn.hutool.core.util.ObjectUtil;
import cn.hutool.core.util.StrUtil;
import com.{company}.{project}.common.core.ErrorCode;
import com.{company}.{project}.common.exception.BusinessException;
// import com.{company}.{project}.common.security.LoginUser;
// import com.{company}.{project}.common.security.LoginUserHolder;  // 需从 proj-common 获取
import com.{company}.{project}.{module}.dao.{Domain}Dao;
import com.{company}.{project}.{module}.domain.{Domain};
import com.{company}.{project}.{module}.enums.StatusEnum;
import com.{company}.{project}.{module}.model.request.*;
import com.{company}.{project}.{module}.model.response.{Domain}Response;
import com.{company}.{project}.{module}.service.{Domain}Service;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.stream.Collectors;

/**
 * {description}服务实现类
 *
 * @author {author}
 * @since {date}
 */
@Slf4j
@Service
@RequiredArgsConstructor
public class {Domain}ServiceImpl implements {Domain}Service {

    private final {Domain}Dao {domain}Dao;

    @Override
    @Transactional(rollbackFor = Exception.class)
    public String create({Domain}CreateRequest request) {
        log.info("[{Domain}Service.create] Create {description}, request={}", request);

        // LoginUser loginUser = LoginUserHolder.get();  // 需从 proj-common 获取
        String currentUsername = "system";  // 默认值，实际应从登录上下文获取

        {Domain} domain = BeanUtil.copyProperties(request, {Domain}.class);

        // 设置默认状态：如果 request 中 status 为 null，默认设置为启用
        if (ObjectUtil.isNull(domain.getStatus())) {
            domain.setStatus(StatusEnum.ENABLED);
        }

        domain.setCreateBy(currentUsername);
        domain.setCreateTime(LocalDateTime.now());
        domain.setDelFlag({Domain}.DEL_FLAG_NORMAL);

        {domain}Dao.save(domain);

        String domainId = domain.getId();
        log.info("[{Domain}Service.create] {description} created successfully, id={}", domainId);
        return domainId;
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void update(String id, {Domain}UpdateRequest request) {
        log.info("[{Domain}Service.update] Update {description}, id={}, request={}", id, request);

        {Domain} domain = {domain}Dao.findById(id);
        if (ObjectUtil.isNull(domain)) {
            log.warn("[{Domain}Service.update] {description} does not exist, id={}", id);
            throw new BusinessException(ErrorCode.DATA_NOT_EXIST);
        }

        // LoginUser loginUser = LoginUserHolder.get();  // 需从 proj-common 获取
        String currentUsername = "system";  // 默认值，实际应从登录上下文获取

        BeanUtil.copyProperties(request, domain);
        domain.setUpdateBy(currentUsername);
        domain.setUpdateTime(LocalDateTime.now());

        {domain}Dao.save(domain);

        log.info("[{Domain}Service.update] {description} updated successfully, id={}", id);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void deleteById(String id) {
        log.info("[{Domain}Service.deleteById] Delete {description}, id={}", id);

        {Domain} domain = {domain}Dao.findById(id);
        if (ObjectUtil.isNull(domain)) {
            log.warn("[{Domain}Service.deleteById] {description} does not exist, id={}", id);
            throw new BusinessException(ErrorCode.DATA_NOT_EXIST);
        }

        // 调用 Domain 层方法标记删除（充血模型）
        domain.markDeleted();
        {domain}Dao.save(domain);

        log.info("[{Domain}Service.deleteById] {description} deleted successfully, id={}", id);
    }

    @Override
    public {Domain}Response getDetail(String id) {
        log.info("[{Domain}Service.getDetail] Get {description} detail, id={}", id);

        {Domain} domain = {domain}Dao.findById(id);
        if (ObjectUtil.isNull(domain)) {
            log.warn("[{Domain}Service.getDetail] {description} does not exist, id={}", id);
            throw new BusinessException(ErrorCode.DATA_NOT_EXIST);
        }

        return convertToResponse(domain);
    }

    @Override
    public List<{Domain}Response> list({Domain}QueryRequest request) {
        log.info("[{Domain}Service.list] Query {description} list, request={}", request);

        Query query = buildQuery(request);
        query.with(Sort.by(Sort.Direction.DESC, "createTime"));

        // 限制返回数量：最多返回 1000 条数据
        query.limit(1000);

        List<{Domain}> list = {domain}Dao.find(query);

        return CollUtil.isEmpty(list) ? CollUtil.newArrayList() :
                list.stream()
                    .map(this::convertToResponse)
                    .collect(Collectors.toList());
    }

    @Override
    public Page<{Domain}Response> pageQuery({Domain}QueryRequest request) {
        log.info("[{Domain}Service.pageQuery] Page query {description}, request={}", request);

        Query query = buildQuery(request);
        long total = {domain}Dao.count(query);

        // 如果没有数据，直接返回空结果
        if (total == 0) {
            return new PageImpl<>(CollUtil.newArrayList(),
                PageRequest.of(0, request.getPageSize()), 0);
        }

        // 分页参数校验：pageNo 至少为 1，pageSize 范围 1-500
        int pageNo = Math.max(request.getPageNo(), 1);
        int pageSize = Math.min(Math.max(request.getPageSize(), 1), 500);

        // 计算总页数
        int totalPages = (int) Math.ceil((double) total / pageSize);

        // ⚠️ 性能优化：限制最大页码，禁止深度分页（skip > 10000 性能极差）
        int maxPageNo = 100;  // 最多查询第 100 页（10,000 条记录）

        // ✅ 修复：优先级 - 先检查业务边界
        int actualPageNo = pageNo;

        // 业务边界：页码不能超过总页数
        if (pageNo > totalPages) {
            log.warn("[{Domain}Service.pageQuery] Page number exceeds total pages, pageNo={}, totalPages={}",
                pageNo, totalPages);
            return new PageImpl<>(CollUtil.newArrayList(),
                PageRequest.of(pageNo - 1, pageSize), total);
        }

        // 性能保护：如果总页数超过限制，也要限制
        if (totalPages > maxPageNo) {
            actualPageNo = Math.min(pageNo, maxPageNo);
        }

        Pageable pageable = PageRequest.of(
                actualPageNo - 1,  // Spring Data MongoDB 的页码从 0 开始
                pageSize,
                Sort.by(Sort.Direction.DESC, "createTime", "_id")  // ⚠️ 稳定性优化：添加 _id 保证排序稳定
        );

        query.with(pageable);
        List<{Domain}> list = {domain}Dao.find(query);

        List<{Domain}Response> responseList = CollUtil.isEmpty(list) ? CollUtil.newArrayList() :
                list.stream()
                    .map(this::convertToResponse)
                    .collect(Collectors.toList());

        return new PageImpl<>(responseList, pageable, total);
    }

    /**
     * 构建查询条件
     *
     * @param request 查询请求
     * @return Query
     */
    private Query buildQuery({Domain}QueryRequest request) {
        Query query = new Query();
        Criteria criteria = Criteria.where("delFlag").is(0);

        if (StrUtil.isNotBlank(request.getKeyword())) {
            // 限制长度并转义正则特殊字符，防止正则注入攻击
            String keyword = StrUtil.sub(request.getKeyword(), 0, 50);
            String escapedKeyword = java.util.regex.Pattern.quote(keyword);
            criteria.and("name").regex(escapedKeyword, "i");
        }

        if (ObjectUtil.isNotNull(request.getStatus())) {
            criteria.and("status").is(request.getStatus());
        }

        query.addCriteria(criteria);
        return query;
    }

    /**
     * 转换为响应对象
     *
     * @param domain 领域对象
     * @return 响应对象
     */
    private {Domain}Response convertToResponse({Domain} domain) {
        return BeanUtil.copyProperties(domain, {Domain}Response.class);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void updateStatus(String id, Integer status) {
        log.info("[{Domain}Service.updateStatus] Update {description} status, id={}, status={}", id, status);

        // 枚举转换和校验
        StatusEnum statusEnum = StatusEnum.of(status);
        if (statusEnum == null) {
            throw new BusinessException(ErrorCode.INVALID_PARAM, "Invalid status value");
        }

        {Domain} domain = {domain}Dao.findById(id);
        if (ObjectUtil.isNull(domain)) {
            log.warn("[{Domain}Service.updateStatus] {description} does not exist, id={}", id);
            throw new BusinessException(ErrorCode.DATA_NOT_EXIST);
        }

        // 状态转换校验：已删除的记录不能修改状态
        if (domain.isDeleted()) {
            log.warn("[{Domain}Service.updateStatus] Cannot modify deleted {description}, id={}", id);
            throw new BusinessException(ErrorCode.INVALID_PARAM, "已删除的记录不能修改状态");
        }

        String currentUsername = "system";  // Default value, should get from login context

        domain.setStatus(statusEnum);
        domain.setUpdateBy(currentUsername);
        domain.setUpdateTime(LocalDateTime.now());

        {domain}Dao.save(domain);

        log.info("[{Domain}Service.updateStatus] {description} status updated successfully, id={}", id);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void batchDelete(List<String> ids) {
        log.info("[{Domain}Service.batchDelete] Batch delete {description}, ids={}", ids);

        if (CollUtil.isEmpty(ids)) {
            return;
        }

        // 批量删除：使用 DAO 层的批量更新方法
        int batchSize = 500;
        int successCount = 0;

        for (int i = 0; i < ids.size(); i += batchSize) {
            int end = Math.min(i + batchSize, ids.size());
            List<String> batchIds = ids.subList(i, end);

            // 调用 DAO 层批量更新方法
            long modifiedCount = {domain}Dao.batchUpdateDeleted(batchIds);
            successCount += modifiedCount;
        }

        log.info("[{Domain}Service.batchDelete] Batch delete completed, total={}, success={}",
            ids.size(), successCount);

        // 如果全部失败，抛出异常
        if (successCount == 0) {
            throw new BusinessException(ErrorCode.OPERATION_FAILED,
                "批量删除失败，所有ID均不存在或已删除");
        }
    }

}
```

---

## 注意事项

1. **日志规范** - 方法入口和出口都要记录日志，格式：`[类名.方法名] 操作描述, 参数={}`
2. **空值检查** - 查询结果为空时抛出 `BusinessException(ErrorCode.DATA_NOT_EXIST)`
3. **Hutool 工具使用**
   - 对象判空：`ObjectUtil.isNull(obj)` / `ObjectUtil.isNotNull(obj)`
   - 字符串判空：`StrUtil.isNotBlank(str)` / `StrUtil.isBlank(str)`
   - 集合判空：`CollUtil.isEmpty(list)` / `CollUtil.isNotEmpty(list)`
   - 对象复制：`BeanUtil.copyProperties(source, Target.class)`
4. **N+1 问题** - 使用批量查询或 JOIN 避免循环内查询数据库
5. **批量操作** - 超过 500 条数据必须分批处理
6. **事务控制** - 批量写操作添加 `@Transactional`
7. **分页查询** - 分页参数使用 `Math.max()` 校验，确保至少为 1
