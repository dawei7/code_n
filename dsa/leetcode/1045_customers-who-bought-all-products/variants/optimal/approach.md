## General

**Translate “all products” into equal distinct counts**

The `Product` table defines the complete required set. Its `product_key` is a primary key, so each required product appears exactly once.

For one customer, collect the distinct `product_key` values appearing in `Customer`. Because `Customer.product_key` references `Product.product_key`, every counted non-null key belongs to the required product set.

The customer bought every product exactly when the size of this distinct purchased set equals the number of rows in `Product`.

This is a relational-division question expressed through grouping and counting.

**Group rows by customer**

The query selects `customer_id` from `Customer` and uses `GROUP BY 1`.

In MySQL, positional grouping expression `1` refers to the first selected expression, which is `customer_id`. Every row for the same customer is placed in one group.

Writing `GROUP BY customer_id` would be equivalent and more explicit. The exact source uses the concise positional form.

Only IDs that appear in `Customer` form groups. There is no separate customer master table in the schema, so the query cannot report an ID that has no purchase row.

**Why `DISTINCT` is essential**

The `Customer` table may contain duplicate rows. If a customer bought product five and that row appears three times, ordinary `COUNT(product_key)` would count three purchases even though only one distinct product was covered.

`COUNT(DISTINCT product_key)` collapses repeated keys within each customer group. It measures coverage of different products, not transaction-row volume.

Without `DISTINCT`, duplicates could make an incomplete customer's count equal the product total and produce a false positive.

**Count the required products once**

The scalar subquery

`(SELECT COUNT(1) FROM Product)`

returns the number of rows in `Product`. `COUNT(1)` counts every row because the constant one is never null. Since `product_key` is a unique primary key, this row count is also the number of distinct required products.

The subquery does not depend on the current customer group. A database optimizer can evaluate it once and compare the same total against every group.

**Filter groups with `HAVING`**

`WHERE` filters individual rows before grouping. The desired condition depends on an aggregate count for the entire customer group, so it belongs in `HAVING`.

The condition is:

`COUNT(DISTINCT product_key) = total number of products`.

Only groups satisfying that equality produce a selected `customer_id`.

No `ORDER BY` is needed because the source accepts result rows in any order.

**Why equality proves complete coverage**

Let `P` be the set of keys in `Product` and `C_u` the set of distinct product keys bought by customer `u`.

The foreign-key contract gives `C_u \subseteq P` for valid non-null purchases. If `|C_u| = |P|` and one finite set is a subset of the other, then `C_u = P`. The customer bought every required product.

Conversely, if the customer bought all products, `C_u = P` and the counts are equal. The condition is therefore necessary and sufficient.

The subset fact matters. Without referential integrity, a customer could have the right number of distinct keys but include an unknown product while missing a required one. In a less constrained schema, the query should join to `Product` or use a double-`NOT EXISTS` condition.

**Trace the example**

The `Product` table contains keys five and six, so the scalar subquery returns two.

Customer one has distinct purchased keys `{5, 6}`. Its distinct count is two, so it passes.

Customer two has only `{6}`. Its count is one and it fails.

Customer three also has `{5, 6}` and passes.

The output contains IDs one and three.

If customer one had duplicate rows for product five, its distinct count would remain two rather than increasing.

**SQL evaluation at a conceptual level**

Conceptually, the database:

1. Reads `Customer` rows.
2. Forms one group per `customer_id`.
3. Computes the distinct product count in each group.
4. Reads or derives the total row count from `Product`.
5. Keeps groups whose counts match.
6. Projects only `customer_id`.

An optimizer may execute these physical steps in a different order or use indexes and hash aggregation. SQL specifies the result, not one mandatory physical plan.

**Why the query returns one row per customer**

Grouping collapses all purchase rows for a customer into one group. The selected expression is the grouping key itself, so each qualifying customer produces exactly one result row.

An outer `DISTINCT` is unnecessary. Duplicate input rows have already been absorbed by grouping and by the distinct aggregate.

**Empty and null considerations**

`COUNT(DISTINCT product_key)` ignores nulls. A null product key does not establish that any required product was bought, which is appropriate. Primary-key rows in `Product` are non-null by database definition.

If `Product` were empty, the scalar count would be zero. The query would return only customer groups with zero distinct non-null product keys. Since the available domain is purchase rows rather than a separate customer table, it cannot enumerate customers absent from `Customer`. This follows the exact schema and query rather than inventing an external customer population.

## Complexity detail

Let `R` be the number of rows in `Customer` and `Q` the number of rows in `Product`.

The product count requires `O(Q)` row processing without a cached table statistic. Grouping and distinct aggregation can be implemented by sorting customer rows, giving `O(R \log R)` time, or by hashing, giving expected `O(R)` time.

The manifest states the conservative sort-based bound `O(R \log R + Q)`. Group and distinct state can retain up to the purchase keys represented in `R` rows, while product processing uses up to `O(Q)` plan storage depending on the engine. The recorded space bound is `O(R + Q)`.

Actual database performance depends on indexes, optimizer strategy, memory limits, and whether aggregation spills to disk. The relational result remains the same.

## Alternatives and edge cases

- **Double `NOT EXISTS`:** Select customers for whom there does not exist a product lacking a matching purchase row. This expresses universal quantification directly and does not depend on count equality.
- **Cross join then find missing pairs:** Generate every customer-product pair, subtract purchased pairs, and exclude customers with missing rows. It mirrors relational division but can create a very large intermediate table.
- **Join to `Product` before counting:** This is safer if referential integrity is absent or invalid product keys can appear. Under the stated foreign key, it is redundant.
- **Count without `DISTINCT`:** This is incorrect because duplicate `Customer` rows can inflate a customer's coverage.
- **Count distinct products in `Product`:** `COUNT(DISTINCT product_key)` would equal `COUNT(1)` because `product_key` is a primary key, so the simpler row count is sufficient.
- **Duplicate purchase rows:** They collapse inside `COUNT(DISTINCT ...)` and do not affect qualification.
- **Customer missing one product:** Its distinct count is strictly below the product total and it is excluded.
- **Customer buying every product:** Its distinct set equals the required set and it is returned once.
- **Result ordering:** No ordering clause is necessary because any order is accepted.
- **`GROUP BY 1` portability:** Positional grouping is supported by MySQL here, but `GROUP BY customer_id` is clearer and more portable across SQL styles.
- **Null product key:** It is ignored by the distinct count and cannot falsely satisfy a required product.
- **Foreign-key dependence:** Count equality proves set equality only because purchased keys belong to the product set.
- **No customer master table:** The query's candidate IDs come only from `Customer`, which is all the schema makes available.
