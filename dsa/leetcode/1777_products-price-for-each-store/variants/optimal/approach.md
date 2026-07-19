## General
**Form one group per product**

Group the source rows by `product_id`. Every output row then corresponds to exactly one product, regardless of the order in which that product's store records appeared.

**Route each store into its own aggregate**

For column `store1`, a `CASE` expression returns `price` only when `store = 'store1'` and returns `NULL` otherwise. `MAX` ignores those `NULL` values. Because the primary key permits at most one row for a given product and store, the remaining value is exactly the desired price rather than a maximum chosen among duplicates. Apply the same conditional aggregate to `"store2"` and `"store3"`.

**Preserve missing prices as NULL**

If a product has no row for one store, every value supplied to that store's aggregate is `NULL`, so the aggregate result is also `NULL`. This distinguishes an unavailable product-store pair from any actual stored price. Ordering by `product_id` is optional for LeetCode but makes the app-local output deterministic.

## Complexity detail
A hash-aggregation plan examines each of the $R$ source rows once, giving $O(R)$ logical time. It keeps three fixed aggregate slots for each of the $P$ product groups, so its auxiliary grouping state is $O(P)$. A database may choose a sort-based physical plan with different implementation costs.

## Alternatives and edge cases
- **Three correlated subqueries:** Look up each store separately for every product. This is correct with suitable indexes but can repeatedly scan the source table without them.
- **Database-specific `PIVOT`:** Some SQL systems provide a pivot operator, but conditional aggregation works in both MySQL and the app-local SQLite runtime.
- A product can be absent from one or two stores; those result cells must be `NULL`.
- Input row order has no effect on the grouped result.
- The composite primary key guarantees that no store column combines multiple prices for the same product.
- A product represented by only one source row must still appear exactly once.
