# DAO 模板（MongoDB）

> **设计原则**：直接使用 MongoTemplate，不过度抽象

---

## DAO 接口

```java
package com.{company}.{project}.{module}.dao;

import com.{company}.{project}.{module}.domain.{Domain};
import com.{company}.{project}.{module}.enums.StatusEnum;
import org.springframework.data.mongodb.core.query.Query;

import java.util.List;

/**
 * {description} DAO
 *
 * @author {author}
 * @since {date}
 */
public interface {Domain}Dao {

    /**
     * 根据ID查询
     *
     * @param id 主键ID
     * @return {description}
     */
    {Domain} findById(String id);

    /**
     * 根据名称查找
     *
     * @param name 名称
     * @return {description}
     */
    {Domain} findByName(String name);

    /**
     * 根据查询条件查询列表
     *
     * @param query 查询条件
     * @return {description}列表
     */
    List<{Domain}> find(Query query);

    /**
     * 统计数量
     *
     * @param query 查询条件
     * @return 数量
     */
    long count(Query query);

    /**
     * 保存
     *
     * @param domain {description}
     */
    void save({Domain} domain);

    /**
     * 批量更新删除标记（逻辑删除）
     *
     * @param ids ID列表
     * @return 更新的文档数量
     */
    long batchUpdateDeleted(List<String> ids);

    /**
     * 根据ID列表批量查询
     *
     * @param ids ID列表
     * @return {description}列表
     */
    List<{Domain}> listByIds(List<String> ids);

    /**
     * 根据状态查询
     *
     * @param status 状态枚举
     * @return {description}列表
     */
    List<{Domain}> listByStatus(StatusEnum status);
}
```

---

## DAO 实现

```java
package com.{company}.{project}.{module}.dao.impl;

import cn.hutool.core.collection.CollUtil;
import com.{company}.{project}.{module}.dao.{Domain}Dao;
import com.{company}.{project}.{module}.domain.{Domain};
import com.{company}.{project}.{module}.enums.StatusEnum;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.core.query.Update;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * {description} DAO 实现
 *
 * @author {author}
 * @since {date}
 */
@Repository
public class {Domain}DaoImpl implements {Domain}Dao {

    private final MongoTemplate mongoTemplate;

    public {Domain}DaoImpl(MongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }

    @Override
    public {Domain} findById(String id) {
        Query query = new Query();
        Criteria criteria = Criteria.where("_id").is(id)
                .and("delFlag").is(0);
        query.addCriteria(criteria);
        return mongoTemplate.findOne(query, {Domain}.class);
    }

    @Override
    public {Domain} findByName(String name) {
        Query query = new Query();
        Criteria criteria = Criteria.where("name").is(name)
                .and("delFlag").is(0);
        query.addCriteria(criteria);
        return mongoTemplate.findOne(query, {Domain}.class);
    }

    @Override
    public List<{Domain}> listByIds(List<String> ids) {
        // 防御性编程：空列表直接返回空结果
        if (CollUtil.isEmpty(ids)) {
            return CollUtil.newArrayList();
        }

        Query query = new Query();
        Criteria criteria = Criteria.where("_id").in(ids)
                .and("delFlag").is(0);
        query.addCriteria(criteria);
        return mongoTemplate.find(query, {Domain}.class);
    }

    @Override
    public List<{Domain}> listByStatus(StatusEnum status) {
        Query query = new Query();
        Criteria criteria = Criteria.where("status").is(status)
                .and("delFlag").is(0);
        query.addCriteria(criteria);
        return mongoTemplate.find(query, {Domain}.class);
    }

    @Override
    public List<{Domain}> find(Query query) {
        return mongoTemplate.find(query, {Domain}.class);
    }

    @Override
    public long count(Query query) {
        return mongoTemplate.count(query, {Domain}.class);
    }

    @Override
    public void save({Domain} domain) {
        mongoTemplate.save(domain);
    }

    @Override
    public long batchUpdateDeleted(List<String> ids) {
        // 防御性编程：空列表直接返回 0
        if (CollUtil.isEmpty(ids)) {
            return 0;
        }

        Query query = new Query(Criteria.where("_id").in(ids)
                .and("delFlag").is(0));

        Update update = new Update()
                .set("delFlag", {Domain}.DEL_FLAG_DELETED)
                .set("updateTime", java.time.LocalDateTime.now());

        return mongoTemplate.updateMulti(query, update, {Domain}.class).getModifiedCount();
    }
}
```

---

## 注意事项

1. **使用构造器注入** - 替代 `@Autowired`，更安全
2. **@Repository 注解** - 标记为 Spring Bean
3. **Query + Criteria** - 构建查询条件
4. **逻辑删除** - 查询条件默认加 `delFlag = 0`
5. **ID 类型** - MongoDB 使用 String 类型 ID
6. **Hutool 工具使用**
   - 集合判空：`CollUtil.isEmpty(list)` / `CollUtil.isNotEmpty(list)`
   - 创建集合：`CollUtil.newArrayList()`
   - 防御性编程：所有集合参数都应判空，避免 NPE
