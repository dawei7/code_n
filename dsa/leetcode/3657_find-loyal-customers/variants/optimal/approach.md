## General

**Reduce all loyalty criteria to one customer-level group**

Every condition describes a customer across all of their transaction rows:

- A count of purchase transactions.
- A count or proportion of refund transactions.
- The span from the earliest transaction date to the latest.

These are aggregate properties, so the query groups rows by `customer_id` and evaluates one completed group per customer. No transaction amount is involved in the loyalty definition, and the unique `transaction_id` is only row identity; neither needs to appear in the result or filters.

The source writes

`GROUP BY 1`.

In MySQL, ordinal one refers to the first selected expression, `customer_id`. This is equivalent to `GROUP BY customer_id`. The explicit column name would be easier to maintain, but the positional form has the intended behavior here.

**Count refunds with a MySQL Boolean sum**

The expression

`transaction_type = 'refund'`

evaluates to one for a refund row and zero for a purchase row in MySQL numeric context. Therefore

`SUM(transaction_type = 'refund')`

is the number of refunds in a customer’s group.

`COUNT(1)` counts every transaction row, regardless of type. Since the schema guarantees that `transaction_type` is either `'purchase'` or `'refund'`, the total count is

`T = P + R`,

where `P` is purchases and `R` is refunds.

MySQL’s `/` operator performs division rather than integer truncation in this expression, so

`SUM(transaction_type = 'refund') / COUNT(1)`

is the refund fraction `R / T`. The condition uses strict inequality:

`R / T < 0.2`.

A customer at exactly twenty percent does not qualify.

**Why `COUNT(1) >= 3` still enforces three purchases**

The statement asks for at least three purchases, but the source’s first condition is

`COUNT(1) >= 3`,

which counts purchases and refunds together. Viewed in isolation, that would not be the requested test. However, it appears in conjunction with the strict refund-rate condition, and together the two conditions are equivalent to the intended purchase minimum plus refund-rate requirement.

Assume the source conditions hold. Then `T >= 3` and

`R / T < 0.2`.

The purchase count is `P = T - R`, so

`P > 0.8T`.

Since `T >= 3`, this gives `P > 2.4`. Purchase counts are integers, so `P >= 3`.

Conversely, if a customer has at least three purchases and satisfies the refund-rate condition, then `T = P + R >= 3`, so the source’s total-count condition also holds.

Thus no customer with fewer than three purchases can pass the complete `HAVING` clause under the guaranteed two transaction types. The query is semantically correct, although writing

`SUM(transaction_type = 'purchase') >= 3`

would express the requirement more directly and remain correct even if new transaction types were later introduced.

**Measure activity using the date endpoints**

The earliest transaction is `MIN(transaction_date)` and the latest is `MAX(transaction_date)`. MySQL’s

`DATEDIFF(later_date, earlier_date)`

returns the number of day boundaries between the two dates. The source requires

`DATEDIFF(MAX(transaction_date), MIN(transaction_date)) >= 30`.

This matches an active span of at least 30 days. A customer whose first transaction is January 1 and last transaction is January 31 has a difference of 30 and qualifies on this dimension.

The calculation includes all transaction types. The statement says the customer must “have been active” for the period, not that purchases alone must span it, so refunds are valid endpoints as transaction activity.

Only the minimum and maximum dates matter. The customer does not need a transaction on every intermediate day.

**Use `HAVING` rather than `WHERE`**

`WHERE` filters individual rows before grouping. Applying transaction-type or date filters there would remove rows from counts and endpoints and change the meaning of the metrics.

`HAVING` filters after aggregates have been computed for each customer. All three source conditions depend on complete groups:

- `COUNT(1) >= 3`.
- Refund count divided by total count is below `0.2`.
- Latest date minus earliest date is at least 30 days.

Placing them in `HAVING` preserves every customer transaction while calculating the metrics and then removes customers whose complete histories do not qualify.

**Return only the required identity and order it**

The result needs only `customer_id`. The source does not expose the intermediate counts, rate, or date span.

`ORDER BY 1` again refers to the first selected expression. The default order is ascending, so this is equivalent to

`ORDER BY customer_id ASC`.

Grouping already produces one row per customer, but SQL does not guarantee group output order. The explicit `ORDER BY` is necessary for the requested ascending result.

**Trace the example**

Customer 101 has four purchases, no refunds, and activity from January 5 through February 20. The total count is four, refund fraction is zero, and `DATEDIFF` is 46, so all conditions pass.

Customer 102 has five total transactions and therefore passes the raw count. Its two refunds give `2 / 5 = 0.4`, failing the strict rate condition.

Customer 103 has three purchases and no refunds, but January 1 through January 3 spans only two days, so the date condition fails.

Customer 104 has five purchases and one refund. Its refund fraction is `1 / 6`, approximately `0.1667`, below `0.2`, and its activity span is 73 days. It qualifies.

Sorting the two surviving identifiers yields 101 followed by 104.

**Why one aggregation pass contains all needed information**

For each customer, the database needs only constant-sized aggregate state: total row count, refund count, minimum date, and maximum date. Each transaction row updates those values once.

After grouping, every loyalty decision can be made from that state. No self-join, correlated subquery, or transaction-level ranking is required. This makes grouped aggregation the natural optimal logical plan.

## Complexity detail

Let `N` be the number of transaction rows and `C` the number of distinct customers.

With hash aggregation, scanning and updating customer groups takes expected `O(N)` time and `O(C)` group-state space. Sorting at most `C` qualifying output rows by `customer_id` costs `O(C log C)` time.

A database may instead choose sort-based grouping, especially depending on indexes and memory. Sorting the input for grouping can cost `O(N log N)` time and use up to `O(N)` temporary space. The manifest’s `O(N log N + C log C)` time and `O(N + C)` space are conservative plan-level bounds.

If an index begins with `customer_id`, the database may stream groups in index order and reduce both grouping and final-order work. SQL complexity is physical-plan dependent; the query expresses one logical scan, aggregation, filter, and ordering stage.

The aggregate state per customer is constant-sized. The `amount` and `transaction_id` values do not need to be retained for this result.

## Alternatives and edge cases

- **Count purchases explicitly:** `SUM(transaction_type = 'purchase') >= 3` states the requirement directly and is more robust if transaction types ever expand. Under the current two-type guarantee and refund filter, it is equivalent to the source’s conjunction.
- **Conditional `CASE` expressions:** `SUM(CASE WHEN transaction_type = 'refund' THEN 1 ELSE 0 END)` is more portable than MySQL Boolean arithmetic.
- **Correlated subqueries:** Separately querying counts and dates for every customer can repeatedly scan the table. One grouped aggregation computes all metrics together.
- **Filter refunds in `WHERE`:** Removing refund rows before grouping would force every observed refund rate to zero and corrupt total counts and date endpoints.
- **Exactly three total transactions:** To pass a refund rate below twenty percent, all three must be purchases; one refund would make the rate one-third.
- **Exactly twenty-percent refunds:** The customer is excluded because the rule and source both use strict `< 0.2`.
- **No refunds:** The refund sum is zero and the rate is zero, so the rate condition passes.
- **Fewer than three purchases:** Such a customer cannot satisfy both `COUNT(1) >= 3` and a refund rate below twenty percent under the two-type schema.
- **Transactions on one date:** `DATEDIFF` is zero regardless of transaction count, so the activity criterion fails.
- **Exactly 30 days apart:** The customer passes the activity condition because the query uses `>= 30`.
- **Refund extends the activity span:** It counts as activity because endpoints are taken over all transaction rows.
- **Repeated transaction dates:** They are counted as separate transactions but do not independently increase the min-to-max date span.
- **Transaction amount:** Purchase and refund amounts do not affect any criterion and are correctly ignored.
- **Ordinal column references:** `GROUP BY 1` and `ORDER BY 1` are valid MySQL shorthand but less self-documenting than naming `customer_id`.
- **Potential nulls:** The reference presents valid transaction types and dates. If nulls were allowed, Boolean sums, `MIN`, and `MAX` would need an explicit null policy.
- **Ascending result order:** `ORDER BY 1` defaults to ascending; adding `DESC` would contradict the requirement.
