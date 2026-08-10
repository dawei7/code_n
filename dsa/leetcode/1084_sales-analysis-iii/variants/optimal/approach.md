## General

**Turn “only during the period” into a condition over every sale**

The important word in the requirement is “only.” A product qualifies when it has at least one sale and every one of its sales happened from January 1, 2019 through March 31, 2019, with both dates included. Looking only for a sale inside that period is insufficient. A product sold once in February and once in April has an in-period row, but it must still be rejected because of the April row.

This naturally suggests grouping all sales of one product together and asking a universal question about the group: does every row satisfy the date condition? SQL does not need a separate universal-quantifier operator. The query converts the condition on each row into a numeric value and then compares the count of successful rows with the count of all rows.

**Attach the requested product name**

The result needs both `product_id` and `product_name`, while `Sales` contains only the identifier. The inner `JOIN Product USING (product_id)` connects every sale to its product record. The foreign-key relationship says that a sale’s product identifier refers to `Product.product_id`, and that column is the primary key, so each sale joins to exactly one product row. Consequently, the join neither loses a valid sale nor multiplies it into several copies.

An inner join also has a useful semantic effect here: products with no sales create no joined rows and therefore create no group. Such a product cannot qualify as a product “sold” exclusively in the target quarter, because it was not sold at all.

**Make one group per product**

`GROUP BY 1` uses the first selected expression, `product_id`, as the grouping key. All joined sale rows for the same product are therefore examined together, and at most one output row is produced for that product. The selected `product_name` is well defined because one primary-key value identifies one Product row and therefore one name. This is a MySQL convenience based on functional dependence; writing `GROUP BY product_id, product_name` would make the same relationship more explicit.

There is no need for `DISTINCT`. Grouping already collapses every qualifying product’s sale records into a single result row. Repeated sales remain separate while the condition is checked, which is correct, but they do not create repeated result rows.

**Count how many rows pass the inclusive date test**

For each joined row, MySQL evaluates:

`sale_date BETWEEN '2019-01-01' AND '2019-03-31'`

`BETWEEN` is inclusive at both ends. A sale on January 1 contributes true, and a sale on March 31 also contributes true. In a numeric aggregate, MySQL treats true as `1` and false as `0`. Therefore, `SUM(...)` is exactly the number of that product’s sales that lie inside the requested quarter.

At the same time, `COUNT(1)` counts every row in the product’s group. The constant `1` is never null, so every joined sale is counted. The `HAVING` condition keeps the group precisely when:

`COUNT(1) = SUM(date_is_in_the_quarter)`

If a product has six sales and all six are in the quarter, both sides equal six. If even one sale is before January 1 or after March 31, the sum is at most five while the count is still six, and equality fails. Thus equality proves that no outside sale exists.

The grouping step also supplies the existence requirement. A `HAVING` condition is evaluated only for a group that was formed from at least one joined sale row. The query therefore does not accidentally accept a product with zero sales through a vacuous “all zero sales are in range” argument.

**Why duplicates and input order do not matter**

The `Sales` table may contain duplicate rows. A duplicate in-range row adds one to both `COUNT(1)` and the boolean sum, so it preserves equality. A duplicate outside-range row adds one only to the count, so it correctly causes inequality. The test depends only on whether every row passes, not on the order in which rows are stored or read.

The database may return qualifying rows in any order because the problem permits any result order and the query has no `ORDER BY`. Omitting an unnecessary sort avoids imposing work that the contract does not request.

## Complexity detail

Let $P$ be the number of Product rows and $R$ the number of Sales rows. The package records the required time bound as $O(P + R\log R)$ and the required space bound as $O(P + R)$.

The exact physical plan is chosen by MySQL, so SQL complexity describes a reasonable implementation rather than forcing one algorithm. The database first relates Sales rows to Product rows. With a primary-key index on `Product.product_id`, each lookup can be efficient; alternatively, a hash join can process the two relations in linear expected time.

The joined rows must then be grouped by product identifier. A sort-based aggregation may sort $R$ sale rows, giving $O(R\log R)$ time, and then scan them once. Reading or preparing Product information contributes $O(P)$, which yields the stated $O(P + R\log R)$ bound. A hash aggregation can often reduce the expected grouping time to $O(R)$, but the manifest’s sort-based bound remains a safe general description.

Materializing join and grouping state can require $O(P + R)$ space in a conservative plan. A streaming plan over rows already ordered by product may use less working memory, while a hash plan usually keeps one aggregate state per represented product. The output itself contains at most $P$ rows. The query’s logical result is independent of which legal plan the optimizer selects.

## Alternatives and edge cases

- **Filter in `WHERE` only:** Writing a date predicate before grouping is wrong for this requirement because it removes outside-quarter sales before the query can notice them. The February and April product would appear to have only its February row and would be accepted incorrectly.
- **Minimum and maximum sale dates:** A group can qualify when `MIN(sale_date) >= '2019-01-01'` and `MAX(sale_date) <= '2019-03-31'`. This is correct for nonempty groups, but the count-versus-sum formulation mirrors the “every row passes” logic more directly.
- **Conditional minimum:** Aggregating a boolean with `MIN(sale_date BETWEEN ... ) = 1` also expresses that every row is true. It is concise, but readers must know how MySQL converts booleans to numbers.
- **Correlated `NOT EXISTS`:** Start from products with an in-range sale, then reject any product for which an outside-range sale exists. This can perform well with a suitable index, but it requires two logically separate existence checks.
- **Products with no sales:** The inner join produces no group, so they are excluded. This is necessary because the requested product must actually have been sold in the period.
- **Boundary dates:** January 1 and March 31 are valid because `BETWEEN` includes both endpoints. December 31 and April 1 are outside and make the product fail.
- **Duplicate sale rows:** Duplicates do not change the universal conclusion. Each duplicate is counted consistently as either another passing row or another failing row.
- **Many in-range sales:** The requirement does not limit the number of sales. Five, fifty, or five hundred in-range records all qualify as long as there is no outside record.
- **Result ordering:** No ordering is guaranteed without `ORDER BY`, but that is acceptable because the contract explicitly permits any order.
