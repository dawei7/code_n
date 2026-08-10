## General

**Rank orders independently for each customer**

The requested limit is not three rows for the whole table. It is at most three rows for every customer who has placed an order. That makes this a grouped top-$k$ query: orders must first be separated by `customer_id`, then ranked from newest to oldest inside each customer's group.

The common table expression named `T` performs exactly that preparation. It joins `Orders` with `Customers` through `JOIN Customers USING (customer_id)`, so each order row gains the corresponding customer name. Because this is an inner join, a customer with no order does not create a result row. That matches a report whose rows represent actual orders.

The query selects every joined column temporarily because the outer query will need the customer's name and identifier as well as the order's identifier and date. The `cost` column survives inside `T` but is intentionally not projected by the final `SELECT`.

**Why ROW_NUMBER is the right window function**

`ROW_NUMBER() OVER (...)` assigns consecutive integers one, two, three, and so on to rows without collapsing them. Its `PARTITION BY customer_id` clause restarts the numbering whenever the customer changes. Therefore, every customer has a private ranking sequence rather than competing with every other customer.

Within a partition, `ORDER BY order_date DESC` places the most recent date first. Rank one is the newest order, rank two is the next newest, and rank three is the third newest.

The statement guarantees that a customer has at most one order on any date. Consequently, two orders belonging to the same customer cannot tie on `order_date`. No additional order-id tiebreaker is required to make the top three deterministic.

`ROW_NUMBER` is preferable to `RANK` for expressing a fixed row count. If date ties were possible, `RANK` could assign the same rank to multiple rows and `rk <= 3` might return more than three orders. The no-duplicate-date guarantee prevents ambiguity here, but `ROW_NUMBER` still states the intended row limit directly.

**Filter only after ranking**

The outer query applies `WHERE rk <= 3`. Filtering must happen after the window value has been computed. If rows were limited globally before partitioned ranking, orders of one customer could consume positions needed by another customer.

A customer with at least three orders contributes exactly the rows ranked one through three. A customer with one or two orders contributes all available rows, because all their ranks are at most three. This handles the “less than three” rule without a separate count or conditional branch.

For Winston in the example, the dates sort as August 3, July 31, July 15, and June 10. Their ranks are one through four in that order. The filter retains the first three and removes only June 10. Annabelle has ranks one and two, so neither row is removed.

**Project the required schema**

The outer `SELECT` renames `name` to `customer_name` and emits exactly four columns: `customer_name`, `customer_id`, `order_id`, and `order_date`. Neither the helper rank nor `cost` appears in the returned relation.

This separation is useful: the inner relation can contain columns needed for computation, while the public result contains only the contract's columns.

**Apply presentation ordering after choosing rows**

`ORDER BY 1, 2, 4 DESC` uses select-list positions. Position one is `customer_name` and position two is `customer_id`; both default to ascending order. Position four is `order_date` and is explicitly descending.

Thus names are grouped alphabetically. If two distinct customers share a name, the lower customer identifier appears first. Within one customer, newer returned orders appear before older ones.

The ranking order and final display order serve different purposes. The window order decides which rows survive; the final order arranges those surviving rows for output. Both use descending dates within a customer, but the final order additionally groups by name and identifier.

**Why the result is correct**

Fix any customer. Partitioning ensures that only this customer's orders receive ranks in the customer's sequence. Descending date order and the one-order-per-day guarantee imply that the row with rank $r$ is exactly that customer's $r$-th newest order.

Keeping precisely ranks at most three therefore keeps all orders when the customer has fewer than three and exactly the three newest otherwise. Since the argument holds independently for every partition, the union of retained rows is exactly the requested result. Joining supplies the correct name, projection supplies the required columns, and the final ordering satisfies all three output sort keys.

## Complexity detail

Let $M$ be the number of order rows, $C$ the number of customer rows, and $R$ the number of returned rows. Here $R \le 3C$.

Logically, the join reads the participating relations. A typical indexed or hash join costs about $O(M+C)$. Computing `ROW_NUMBER` requires orders to be available by customer and descending date. Without a matching index, sorting is bounded by $O(M\log M)$ time. Filtering and projection are linear in the ranked or returned rows.

The final `ORDER BY` may sort $R$ rows, costing $O(R\log R)$ without a usable ordering. Database complexity is plan-dependent: indexes, join algorithms, temporary tables, and the optimizer can change physical costs. The manifest's `O(m\log m + c)` summarizes the dominant ranking sort plus customer processing, but a conservative unindexed account also includes the final $O(R\log R)$ output sort.

Materializing ranks or sorting orders can require $O(M)$ working space, while the result itself uses $O(R)$ rows. The manifest's $O(M)$ space captures the dominant intermediate storage. A database may spill that storage to disk rather than keep it all in memory.

## Alternatives and edge cases

- **Correlated count:** Count, for each order, how many newer orders the same customer has and retain counts below three. It can be correct but is often more expensive and harder to read than a window rank.
- **RANK or DENSE_RANK:** These can return more than three rows when ranking values tie; `ROW_NUMBER` expresses a row limit directly.
- **Global LIMIT 3:** It returns only three orders overall and is therefore wrong for a per-customer requirement.
- **Customers with no orders:** The inner join omits them because there is no order row to report.
- **One or two orders:** Their ranks all satisfy `rk <= 3`, so every order is returned.
- **Exactly three orders:** All three survive without special handling.
- **More than three orders:** Only ranks one, two, and three survive.
- **Duplicate customer names:** The secondary ascending `customer_id` key gives the required deterministic grouping.
- **Same-day orders:** The contract excludes two orders by one customer on the same date, so date alone totally orders each partition.
- **Unused cost:** It participates in the intermediate wildcard row but is omitted from the final projection.
- **Positional ordering:** `ORDER BY 1, 2, 4 DESC` is concise but depends on select-column order; spelling out column names would be more robust to projection changes.
- **General most recent n:** Replace the literal three in the rank filter with the desired positive limit; the partitioning and ranking logic remains unchanged.
