## General

**Reduce every order to its maximum and average quantity.** One order spans several product rows. The common table expression `t` groups by `order_id` and calculates the two statistics needed by the definition:

- `MAX(quantity) AS max_quantity` is the largest single-product quantity in that order.
- `SUM(quantity) / COUNT(1) AS avg_quantity` is total quantity divided by its number of product rows.

The composite primary key guarantees one row per different product within an order, so `COUNT(1)` is exactly the number of different products required by the average definition.

**Translate “greater than every average” into one threshold.** An order maximum is strictly greater than the average of every order exactly when it is greater than the largest average among all orders. The scalar subquery

`SELECT MAX(avg_quantity) FROM t`

computes that single global threshold.

The outer `WHERE max_quantity > threshold` then keeps precisely the imbalanced orders. The strict greater-than operator is important: equality with the largest average does not satisfy “strictly greater.”

**Why including the order itself needs no special case.** The threshold is taken from every row of `t`, including the candidate order’s own average. A maximum quantity is always at least its own average, but it must be strictly greater than the global maximum average to qualify.

**Trace the sample threshold.** The order averages are approximately 12.33, 5.5, 14.33, 5, and 9. Their maximum is about 14.33. Order one’s maximum 15 exceeds it, and order three’s maximum 20 exceeds it. Order two’s maximum eight may exceed several averages, but it does not exceed every average because 14.33 is larger, so it is excluded.

**One-product orders.** If an order contains one product row, its maximum equals its average. It could still qualify only if that quantity is strictly greater than the averages of all orders including its own—but strict comparison with its own equal average makes that impossible whenever its average is the global threshold it helps define. More generally, no single-row order can have max strictly greater than its own average, so it can never be imbalanced under the “including itself” rule.

**Numerical division behavior.** In MySQL, `SUM(quantity) / COUNT(1)` performs non-integer division and retains fractional averages. This matters for values such as 37 divided by three. Using integer division would lower thresholds and could incorrectly include orders.

**Why a scalar maximum is sufficient.** If `max_quantity` exceeds the largest average, it necessarily exceeds every smaller or equal average. Conversely, if it fails to exceed the largest, then at least the order attaining that largest average disproves the “every order” condition. This establishes exact equivalence.

**Row preservation.** The CTE produces one row per order. The outer query selects only `order_id` and has no join that could duplicate it. Each qualifying order therefore appears once.

**Any output order is allowed.** No `ORDER BY` appears, so SQL may return qualifying identifiers in any physical order, exactly as permitted.
Group aggregation computes each order’s statistics from all and only its product rows. The scalar subquery finds the greatest average across those summaries. The outer strict comparison is equivalent to being greater than every average. Thus every returned identifier is imbalanced, and every imbalanced order passes the filter.

## Complexity detail

Let `R` be the number of product rows and `G` the number of orders. Grouping scans `R` rows and maintains `G` aggregates. The maximum subquery and outer filter scan the `G` summaries. With hash aggregation, logical time is `O(R + G) = O(R)`; engine choices may instead sort groups.

The grouped CTE requires `O(G)` logical working storage. The output can contain up to `G` identifiers.

## Alternatives and edge cases

- **Compare with `ALL`:** SQL can express `max_quantity > ALL (subquery of averages)`, but the maximum threshold is usually clearer.
- **Window maximum:** Compute per-order statistics and a global maximum average with a window function, then filter in an outer query.
- **Strict equality:** An order whose maximum equals the largest average must be excluded.
- **Fractional average:** Ordinary division preserves the exact decimal comparison; integer truncation would be wrong.
- **One order only:** It qualifies only if its maximum is strictly greater than its own average, which requires at least two unequal product quantities.
- **One product in an order:** Maximum equals average, so that order cannot exceed its own average.
- **Several orders share maximum average:** The scalar threshold remains that shared value, and candidates must exceed it.
- **Several products with equal maximum:** `MAX` needs only the value, not how many rows attain it.
- **Composite primary key:** It makes row count equal the number of different products within each order.
- **Any-order result:** Omitting `ORDER BY` is intentional.
- **Nonempty table assumption:** Each CTE order has at least one row, so `COUNT(1)` is positive.
- **No duplicate output:** One grouped summary row produces at most one selected identifier.
