## General
**Identify disqualifying salesperson identifiers**

Join `Orders` to `Company` by `com_id`, keep companies whose name is `RED`, and select distinct `sales_id` values. This relation contains exactly the salespeople who must be excluded.

**Anti-join from the complete salesperson table**

Start from `SalesPerson` so people with no orders remain eligible. Left join the disqualifying identifiers and retain rows where the joined identifier is null.

**Why the result is exact**

A salesperson appears in the disqualifying relation if and only if at least one of that person's orders joins to a company named `RED`. The anti-join removes every such salesperson. Anyone absent from that relation has no `RED` order—including people with no orders at all—and is retained.

**Order only for deterministic local output**

The platform permits any result order. Sorting by name and identifier stabilizes local comparisons without affecting membership.

## Complexity detail
For `S` salespeople, `C` companies, and `O` orders, joining, deduplicating, and anti-joining generally take $O((S + C + O) \log(S + C + O))$ time and linear working space. Suitable indexes can make the joins near-linear.

## Alternatives and edge cases
- **Uncorrelated `NOT IN`:** exclude sales IDs from a subquery of `RED` orders; it is concise when `sales_id` cannot be null.
- **Correlated `NOT EXISTS`:** states the logic directly, but without useful indexes it may rescan orders for every salesperson and take quadratic time.
- **Inner join from salespeople to orders:** incorrectly drops salespeople with no orders.
- **Only non-`RED` orders:** the salesperson qualifies.
- **At least one `RED` order:** disqualifies the salesperson even when other orders are non-`RED`.
- **No orders:** qualifies.
- **Several `RED` orders:** distinct disqualifying IDs prevent duplicate effects.
- **Company matching:** use the company joined by `com_id`, not an order attribute or city.
