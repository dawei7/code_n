## General

The query must total ordered units per product, but only for February 2020, then keep products whose total reaches at least 100. It also needs the product name, which lives in a separate table.

The exact SQL follows the logical sequence:

1. join orders to product metadata;
2. filter rows to the target month;
3. group the surviving rows by product;
4. sum units within each group; and
5. filter aggregate groups with `HAVING`.

**Joining orders to names**

`Orders AS o JOIN Products AS p ON o.product_id = p.product_id` is an inner join.

Each order's foreign-key identifier matches the unique primary-key row in `Products`, attaching exactly one `product_name`. Products with no February order do not need to appear, so the inner join is appropriate.

Duplicate rows are allowed in `Orders`. They represent separate input rows and each contributes its `unit` value to the total. The query does not use `DISTINCT`, so it does not incorrectly discard them.

**Filtering February 2020 before aggregation**

`WHERE DATE_FORMAT(order_date, '%Y-%m') = '2020-02'` keeps exactly dates whose year and month are February 2020.

Filtering occurs before `GROUP BY`, so January and March units never enter the product sums. This is critical: aggregating all dates first and filtering later would compute lifetime totals rather than the requested period.

Formatting includes the year, preventing February from another year from entering the result.

**Grouping by product identity**

`GROUP BY o.product_id` creates one group for every product with at least one surviving February order.

The selected `product_name` is functionally determined by `product_id` because `Products.product_id` is a primary key and the join attaches one product row. MySQL can therefore associate the unique name with the group.

In SQL modes or database systems requiring every nonaggregated selected column to appear explicitly, grouping by both `o.product_id` and `p.product_name` would be more portable.

**Summing units**

`SUM(unit) AS unit` adds every February `unit` value in the current product group. The alias reuses the required output column name.

For product 1 in the example, the February rows contain 60 and 70, so the aggregate is 130. Product 5 has two February rows of 50, so equality at 100 qualifies.

**Why `HAVING` is used**

`HAVING unit >= 100` filters groups after their sums have been computed. `WHERE` cannot directly test `SUM(unit)` because row filtering happens before aggregation.

The alias `unit` refers to the selected aggregate in MySQL. The comparison is inclusive, matching “at least 100.”

Products with February totals below 100 are removed. Products with no February rows never form a group in the first place.

**Why the output is correct**

Every row reaching grouping is a February 2020 order connected to its unique product. Grouping places all and only those rows for one product together. `SUM` computes its exact period units, and `HAVING` retains exactly totals at least 100.

The selected name comes from the matching product row, so every output pair contains the correct name and total. The task allows any row order, and the exact query correctly omits `ORDER BY`.

**Index-friendly date filtering**

Although `DATE_FORMAT` is logically correct, wrapping `order_date` in a function is often non-sargable. A normal index on `order_date` may not support a direct range seek.

The equivalent half-open predicate:

`order_date >= '2020-02-01' AND order_date < '2020-03-01'`

is typically more index-friendly and safely includes every February date without calculating the month's last day.

## Complexity detail

Let $p$ be the number of product rows, $o$ the number of order rows, and $k$ the number of product groups surviving the month filter.

With a hash or indexed join, product lookup and order scanning can take expected $O(p+o)$ time. Hash aggregation maintains up to $k$ group totals in expected $O(o)$ additional work.

The exact query has no result ordering, so an ideal hash plan does not inherently require $O(k\log k)$ sorting. A sort-based grouping plan can cost $O(o\log o)$, while the manifest's $O(p+o+k\log k)$ is a conservative plan-style description rather than a forced logical cost.

Working space can be $O(p+k)$ for join lookup and group state, matching the manifest. Database plans, indexes, and materialization choices affect actual costs.

The `DATE_FORMAT` predicate may require scanning all orders even when only a small fraction belong to February.

## Alternatives and edge cases

- **Half-open date range:** It expresses the same month and can use an ordinary date index more effectively.
- **Conditional aggregation:** Group all orders and sum a `CASE` only for February, but extra logic is needed to exclude zero-total or absent-period products.
- **Correlated subquery per product:** It is valid but may repeatedly scan `Orders` without good indexing.
- **Exactly 100 units:** The inclusive `>=` condition retains the product.
- **Duplicate order rows:** Every row contributes because duplicates are explicitly allowed.
- **No February orders:** The product has no group and does not appear.
- **Orders in February of another year:** The `%Y-%m` comparison excludes them.
- **Several orders on one date:** All their units are summed; no daily deduplication is required.
- **Functional dependency:** Grouping by product ID identifies one name under the primary-key join, but explicit name grouping is more portable.
- **Aggregate alias in `HAVING`:** MySQL permits `unit` there; other dialects may require repeating `SUM(o.unit)`.
- **Any-order output:** No final sort is necessary, so consumers must not assume incidental order.
