## General

The query reduces all order rows for one customer to one aggregate row, computes the four required metrics, filters customers with `HAVING`, and orders the survivors.

The logical stages are:

1. group rows by `customer_id`;
2. count total, peak-hour, and rated orders while averaging non-null ratings;
3. keep groups satisfying every eligibility rule;
4. sort the result by displayed average rating and then customer ID.

**One group per customer**

`GROUP BY customer_id` collects all orders made by the same customer. Every selected expression that is not the grouping key is an aggregate over that customer's rows.

`COUNT(1) total_orders` counts every order row, regardless of whether `order_rating` is null. This is the correct denominator for both the peak-hour ratio and rating-completion ratio.

The alias `total_orders` is reused in the MySQL `HAVING` clause.

**Recognizing peak-hour orders**

`TIME(order_timestamp)` extracts only the time-of-day portion of each timestamp.

The query tests two inclusive intervals:

- `'11:00:00'` through `'14:00:00'`;
- `'18:00:00'` through `'21:00:00'`.

MySQL `BETWEEN` includes both endpoints. An order at exactly 14:00:00 or 21:00:00 is counted as peak, while one second later is not.

Each comparison produces Boolean zero or one. The `OR` is one when either interval contains the time. Summing that expression therefore counts peak-hour orders.

The displayed percentage is:

`ROUND(SUM(peak_condition) / COUNT(1) * 100)`.

Because `ROUND` has no second argument, it rounds to a whole percentage point.

For four peak orders among four total rows, the expression produces 100. For two among three, it displays 67 after rounding $66.666\ldots$.

**Average rating over rated orders only**

`AVG(order_rating)` ignores null values in MySQL. It divides the sum of available ratings by the number of non-null ratings, not by `total_orders`.

The output expression:

`ROUND(AVG(order_rating), 2) average_rating`

rounds that rated-order average to two decimal places.

For ratings $5,4,5,\text{NULL}$, the average is:

$$
\frac{5+4+5}{3}=4.666\ldots,
$$

which displays as 4.67.

**Counting rating completion**

The expression:

`order_rating IS NOT NULL`

is one for a rated order and zero for an unrated order. Its sum counts rated rows.

The condition:

`SUM(order_rating IS NOT NULL) / total_orders >= 0.5`

therefore requires at least half of all customer orders to have a rating. This ratio is not rounded in the exact source.

An alternative count would be `COUNT(order_rating)` because that aggregate also ignores nulls, but the Boolean sum makes the criterion explicit.

**Applying all four filters**

Aggregate predicates belong in `HAVING` because they are evaluated after grouping. The source requires:

- `total_orders >= 3`;
- `peak_hour_percentage >= 60`;
- `average_rating >= 4.0`;
- rated-order count divided by total count at least $0.5$.

The conditions are connected by `AND`, so failing any one excludes the customer.

MySQL permits select-list aliases such as `total_orders`, `peak_hour_percentage`, and `average_rating` inside `HAVING`. This is why the query does not repeat those aggregate expressions.

**Important rounding behavior in the exact source**

The local function contract says eligibility thresholds should be applied to exact aggregate values and rounding should be used for displayed columns. The checked-in SQL instead filters the rounded aliases for two criteria:

- `peak_hour_percentage` has already been rounded to zero decimal places;
- `average_rating` has already been rounded to two decimal places.

This can admit a customer whose exact metric is just below the threshold but whose displayed value rounds up.

For example, 25 peak orders out of 42 total are approximately $59.5238\%$. The displayed percentage rounds to 60, so the exact source passes `peak_hour_percentage >= 60` even though the exact ratio is below 60%.

Likewise, a sufficiently large rated-order set can have an exact average just below 4.0 that rounds to 4.00 and passes the alias condition.

This is a genuine source/contract discrepancy. A contract-exact filter would compare unrounded expressions in `HAVING`, such as:

`SUM(peak_condition) / COUNT(1) >= 0.60`

and:

`AVG(order_rating) >= 4.0`,

while retaining rounded expressions only in `SELECT`. This document describes the checked-in source faithfully rather than claiming it applies exact thresholds.

**Ordering the result**

`ORDER BY average_rating DESC, customer_id DESC` first places larger displayed average ratings earlier. When two customers have the same rounded average, the larger customer ID appears first.

The peak percentage and total-order count do not participate in tie-breaking.

**Why each output row has the required data**

Grouping guarantees one result row per retained customer. The select list emits exactly:

- customer ID;
- total order count;
- rounded peak-hour percentage;
- rounded average over rated orders.

Every metric is computed from the same customer group, and `HAVING` removes groups failing the source's four conditions.

## Complexity detail

Let $R$ be the number of order rows and $C$ the number of distinct customers.

Logically, the database must inspect all $R$ rows, extract each time, and update one customer's aggregate state. A hash aggregation can do this in expected $O(R)$ time and $O(C)$ grouping space. A sort-based aggregation may require $O(R\log R)$ time and additional row-ordering storage.

Sorting at most $C$ qualifying aggregate rows for the final `ORDER BY` costs $O(C\log C)$ time and $O(C)$ sorting space.

The manifest's conservative bound `O(R log R + C log C)` and `O(R + C)` space allows for sort-based grouping and sorting. Actual execution depends on the MySQL optimizer, available indexes, memory limits, and whether temporary tables spill to disk; SQL text alone does not force one physical plan.

Calling `TIME` and evaluating the Boolean interval conditions are constant work per row under the fixed timestamp representation.

## Alternatives and edge cases

- **Conditional aggregation with `CASE`:** `SUM(CASE WHEN peak_condition THEN 1 ELSE 0 END)` is more portable across SQL dialects. MySQL permits summing Boolean expressions directly.
- **Filter exact metrics:** To match the local contract strictly, compare the unrounded peak ratio and raw `AVG(order_rating)` in `HAVING`, then round only for output.
- **Use `COUNT(order_rating)`:** This counts rated rows because `COUNT(column)` ignores nulls and can replace `SUM(order_rating IS NOT NULL)`.
- **Inclusive interval endpoints:** `BETWEEN` counts orders exactly at 11:00, 14:00, 18:00, and 21:00.
- **Unrated orders:** They count toward total orders and peak percentage but are excluded automatically from `AVG(order_rating)`.
- **No rated orders:** `AVG` is null and the rating-completion ratio is zero, so the customer cannot pass all conditions.
- **Exactly half rated:** The `>= 0.5` comparison includes a customer with exactly 50% rated orders.
- **Exactly three orders:** The `>= 3` condition includes the threshold boundary.
- **Rounded peak false positive:** An exact percentage below 60 can round to 60 and pass the checked-in alias filter.
- **Ordering ties:** Equal rounded averages are ordered by descending `customer_id`, not by raw average or peak percentage.
