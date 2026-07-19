## General
**Join order facts to their monetary value**

Each `Orders` row contains quantity but not price, so join it to `Product` by `product_id` and compute `quantity * price`. Join `Customers` as well so the grouped result can return the required identity and name.

Restrict orders with the half-open interval from `2020-06-01` through, but not including, `2020-08-01`. This includes every possible June and July timestamp while excluding May and August without relying on month-extraction functions.

**Aggregate both months in one grouped pass**

Group by customer identity. One conditional sum assigns rows before `2020-07-01` to June; a second assigns rows on or after that boundary to July. Because the earlier `WHERE` clause already limits rows to the two-month window, those branches cover exactly the two required months.

The `HAVING` clause requires both conditional totals to be at least 100. This is different from requiring their combined total to be 200: a customer with 199 in June and 1 in July must fail. Grouping also ensures that many orders or products still yield only one output row per customer.

**Why the filters preserve boundary semantics**

The lower bound includes `2020-06-01`; the July split includes `2020-07-01`; and the upper bound excludes `2020-08-01`. Every qualifying order enters exactly one conditional sum. Multiplying before summing correctly handles both multi-unit orders and several orders that together reach the threshold.

## Complexity detail
With ordinary database indexes or hash joins, reading the three relations and joining relevant keys is linear in their row counts; grouping may require sorting the $O$ relevant order rows, yielding the conservative bound $O(C+P+O\log O)$. Hash aggregation can reduce the expected grouping work to linear time.

The joins and grouped customer totals may retain data proportional to the input relations, so the stated working-space bound is $O(C+P+O)$. Physical indexes and query-planner choices can change constants without changing the relational strategy.

## Alternatives and edge cases
- **Two monthly aggregates joined together:** compute qualifying June and July customer sets separately, then intersect them. This is correct but duplicates the join and grouping structure.
- **Correlated monthly subqueries:** calculate each customer's two totals with subqueries. It is readable for small data but can repeatedly rescan orders and products for every customer.
- **Combined two-month threshold:** requiring total spending of 200 is incorrect because each month must independently reach 100.
- **Exact threshold:** `>= 100`, not `> 100`, includes customers spending exactly 100.
- **Several orders:** sum all qualifying order values within each month before comparing.
- **Quantity:** spending is `quantity * price`, not merely the sum of product prices.
- **Missing month:** a customer with no order in either June or July fails that month's threshold.
- **Outside dates:** May and August orders never contribute.
- **Month boundaries:** June 30 belongs to June, July 1 belongs to July, and August 1 is excluded.
- **Duplicate names:** group by `customer_id` as well as `name`; distinct customers sharing a name remain separate.
