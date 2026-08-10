## General

**Turn each order into a zero-or-one indicator**

An order is immediate exactly when `customer_pref_delivery_date = order_date`.

For aggregation, it is useful to translate that Boolean fact into a number:

- immediate order becomes 1;
- scheduled order becomes 0.

The MySQL expression `IF(customer_pref_delivery_date = order_date, 1, 0)` performs this translation for every row.

Once rows are indicators, counting immediate orders is just summing them.

**Group by the date being reported**

The requested result has one row for each unique `order_date`. The clause `GROUP BY order_date` partitions all deliveries according to that column.

Every aggregate in the `SELECT` list is evaluated separately within one date's group:

- `SUM(IF(...))` is the number of immediate orders on that date;
- `COUNT(*)` is the total number of orders on that date.

No customer grouping is involved. The same customer may order on several dates, and each row contributes to its own order-date group.

**Compute a percentage rather than a fraction**

For a group with $I$ immediate orders and $T$ total orders, the desired value is:

$$
100\cdot\frac{I}{T}.
$$

The query writes `100 * SUM(...) / COUNT(*)`.

Multiplying by 100 converts the proportion into percentage points. Without that factor, two immediate orders out of three would produce approximately 0.67 rather than 66.67.

Every emitted group has at least one row, so `COUNT(*)` is positive and division by zero cannot occur.

**Round only after calculating the ratio**

`ROUND(expression, 2)` rounds the completed percentage to two decimal places.

For two immediate orders among three total orders:

$$
100\cdot\frac{2}{3}=66.666\ldots,
$$

which rounds to 66.67.

Rounding the numerator or fraction prematurely could lose accuracy. The query aggregates first, divides second, and rounds last.

**Why `SUM(IF(...))` handles every date uniformly**

If every order on a date is immediate, every indicator is one. The sum equals the count, so the percentage is 100.

If none is immediate, every indicator is zero. The sum is zero, so the percentage is zero.

Mixed dates fall naturally between those extremes. No separate branch is needed for all-immediate or all-scheduled groups.

**Trace one example date**

Suppose 2019-08-01 has three rows with preferred dates corresponding to scheduled, immediate, and immediate.

The `IF` values are 0, 1, and 1. Their sum is two, while `COUNT(*)` is three.

The inner percentage expression yields $100\cdot2/3$, and `ROUND` produces 66.67. The output row pairs that number with 2019-08-01.

**The selected alias defines the output schema**

The rounded expression is named `immediate_percentage` with `AS immediate_percentage`.

This is not only cosmetic. The challenge expects the result columns to be `order_date` and `immediate_percentage`.

The original table is not modified; a SQL query constructs a derived result relation.

**Order the final grouped rows**

`ORDER BY order_date` runs after grouping and aggregation. MySQL uses ascending order by default, matching the required earliest-to-latest output.

The ordering belongs after `GROUP BY` because the result must order one row per date, not individual delivery records before aggregation.

**Why delivery and customer identifiers are irrelevant**

`delivery_id` uniquely identifies a row, but the calculation counts all rows with `COUNT(*)` and does not need to deduplicate them.

`customer_id` also has no role because the problem asks for the percentage of orders, not the percentage of customers who placed an immediate order.

Adding either identifier to the grouping would incorrectly split one date into smaller result rows.

**Logical execution flow**

A helpful conceptual order for this query is:

1. read every row from `Delivery`;
2. partition rows by `order_date`;
3. evaluate immediate indicators within each partition;
4. compute the sum, count, percentage, and rounding for the partition;
5. name the calculated column;
6. sort the result partitions by date.

SQL is declarative, so the database optimizer may implement these steps differently, but this logical model proves what result is requested.


Within a fixed date group, the conditional expression contributes one exactly for every immediate order and zero for every scheduled order. Its sum is therefore the exact immediate-order count.

Dividing that count by the total group row count and multiplying by 100 gives the exact percentage. Rounding gives the required precision. Since grouping creates exactly one row for every distinct order date and ordering sorts those rows ascending, the complete result is correct.

## Complexity detail

Let $R$ be the number of delivery rows and $D$ the number of distinct order dates. The database must scan $R$ rows. Grouping and final ordering are commonly bounded by $O(R\log R)$ time without assuming a favorable index or hash aggregation plan.

Aggregation state and grouped result rows can use $O(R)$ space in the worst case, with a tighter logical group-state bound of $O(D)$. Actual database execution may use indexes, hashing, sorting, temporary tables, or disk spill.

## Alternatives and edge cases

- **Average the Boolean condition:** In MySQL, `100 * AVG(condition)` can express the same indicator ratio, but the explicit sum and count are easier to derive.
- **Conditional `COUNT`:** Counting only immediate rows also works if null behavior is handled carefully.
- **Correlated subquery per date:** Correct but needlessly repeats work.
- **Group by customer:** Incorrect because the requested denominator is orders on each date.
- **All immediate:** The ratio is one and the percentage is 100.00.
- **All scheduled:** The numerator is zero and the percentage is 0.00.
- **One order on a date:** Its percentage is either 100.00 or 0.00.
- **Repeating customers:** Each delivery row still counts independently.
- **Rounding:** Apply it after division, not to intermediate counts.
- **Ascending dates:** The explicit `ORDER BY` makes output deterministic by date.
- **Nonempty groups:** `COUNT(*)` cannot be zero for a produced date.
- **SQL execution plans:** Indexes may improve physical performance without changing the query's logical result.
