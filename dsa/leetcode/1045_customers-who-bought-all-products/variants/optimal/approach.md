## General
**Group purchases by customer:** Use `GROUP BY customer_id` so each output candidate is evaluated from all of that customer's purchase rows.

**Count covered products distinctly:** Compute `COUNT(DISTINCT product_key)` within each group. Distinct counting is essential because the source table may repeat the same customer-product pair; duplicates must not inflate catalog coverage.

**Compare with the catalog size:** A scalar subquery obtains `COUNT(*)` from `Product`. Because product keys in `Customer` reference that table, a customer's distinct purchase count equals the catalog count exactly when that customer has every catalog product. Keep only those groups with a matching count, then order by `customer_id` solely to make local output deterministic.

Every returned customer has $Q$ distinct referenced product keys and therefore covers the $Q$-row catalog. Conversely, a customer who bought every catalog product contributes at least one row for each key, so distinct counting produces $Q$ and the group passes the `HAVING` condition.

## Complexity detail
Let $R$ be the number of `Customer` rows and $Q$ the number of `Product` rows. A sort-based grouping and distinct aggregation costs $O(R log R)$ time, while counting the catalog costs $O(Q)$. Grouping, distinct state, input relations, and output sorting require at most $O(R+Q)$ execution space. Database indexes or hash aggregation may improve the physical plan.

## Alternatives and edge cases
- **Double `NOT EXISTS`:** Express relational division by rejecting a customer when any catalog product lacks a matching purchase. It is logically exact but correlated execution can repeatedly scan the purchase table.
- **Cross join and left join:** Form every customer-product requirement, join purchases, and retain customers with no missing pair. This can materialize $O(CQ)$ rows for $C$ customers.
- **Plain `COUNT(product_key)`:** This is incorrect when duplicate purchase rows exist because repeated copies can mimic full coverage.
- **Duplicate purchases:** `COUNT(DISTINCT product_key)` counts a product once for a customer regardless of repetition.
- **One-product catalog:** Every customer appearing with that referenced product qualifies.
- **Incomplete customers:** Missing even one catalog key excludes the customer.
- **Empty purchase table:** No customer identifier is available to report, so the result is empty.
- **Output order:** LeetCode permits any order; ascending order is an implementation-level deterministic choice.
