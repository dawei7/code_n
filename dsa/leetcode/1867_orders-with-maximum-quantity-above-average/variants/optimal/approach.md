## General
**Reduce each order to the two statistics that matter**

Group `OrdersDetails` by `order_id`. For each group, compute `AVG(quantity)` and `MAX(quantity)`. This produces one compact row per order: its comparison threshold contribution and its candidate maximum. No product-level distinction is relevant after these aggregates have been calculated.

**Turn “every order” into one global threshold**

An order maximum must exceed every per-order average. A value exceeds every member of a finite set exactly when it exceeds that set's maximum, so compute `MAX(average_quantity)` over the grouped rows. This preserves the strict comparison: a maximum equal to the largest average must still be rejected.

**Filter the same grouped relation**

Select each grouped `order_id` whose `maximum_quantity` is greater than the global threshold. Every returned row therefore beats every order average. Conversely, any order satisfying the original condition beats their maximum and passes the filter. Since the grouped relation contains one row per order, the result cannot contain duplicates.

## Complexity detail
A hash aggregation reads the $R$ detail rows once and maintains an average accumulator and maximum for each of the $G$ orders. Scanning the resulting $G$ rows to find the largest average and filter candidates adds $O(G)$ time. Because $G \le R$, total time is $O(R)$. The grouped state and result relation use $O(G)$ space. A physical database plan may instead sort by `order_id`, which can add sorting cost when no suitable access path exists; the required bound describes the direct hash-grouping strategy.

## Alternatives and edge cases
- **Window functions over grouped rows:** `MAX(AVG(quantity)) OVER ()` can attach the global threshold to every order in one expression, but it requires a dialect with the needed window support.
- **Repeat the grouped subquery:** Computing order aggregates once for candidates and again for the threshold is logically correct, but it performs avoidable duplicate work.
- **Correlated rescans:** Recomputing an order's maximum for every detail row is correct after `DISTINCT`, yet it can degrade to $O(R^2)$ work without an index-aware optimizer.
- **Strict equality:** An order whose maximum equals the largest average is excluded because the predicate is `>`, not `>=`.
- **Single-product orders:** Their maximum equals their own average, so they cannot qualify when their average is the global maximum.
- **Fractional averages:** Compare numeric aggregate values directly; do not truncate or round them before filtering.
- **Several qualifying orders:** Return all of them, each exactly once.
- **Output order:** No `ORDER BY` is required.
