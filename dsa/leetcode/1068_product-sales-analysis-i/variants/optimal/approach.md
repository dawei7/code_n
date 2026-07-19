## General
**Join through the foreign key:** Inner-join `Sales` to `Product` where their `product_id` values are equal. The foreign-key guarantee ensures every sale obtains exactly one product name, while products having no sale naturally produce no row.

**Project only requested data:** Select `Product.product_name`, `Sales.year`, and `Sales.price`. Neither `quantity` nor `sale_id` belongs in the result, and no aggregation is needed because the requested grain is one row per sale.

**Stabilize local output:** Order by `sale_id` and `year`, the sale key, so fixtures are deterministic. This does not alter which rows or columns are returned; LeetCode permits any order.

For each sale, the join's matching product row supplies its unique name, proving every emitted row is correct. Conversely, referential integrity provides a matching product for every sale, so the inner join cannot omit a required sale row.

## Complexity detail
A hash join can build a $P$-row product lookup and probe it for all $R$ sales in expected $O(P+R)$ time and $O(P)$ space. The deterministic local ordering can sort $R$ output rows in $O(R\log R)$ time and $O(R)$ execution space, yielding the stated bounds. Physical indexes and database plans may change constants or the chosen join algorithm.

## Alternatives and edge cases
- **Correlated product lookup:** A scalar subquery can fetch the name for each sale, but without an index it may rescan all $P$ products for each of $R$ rows.
- **Left join:** Referential integrity makes it equivalent for valid data, but an inner join states that every output row must have a real product match.
- **Group by product:** It is incorrect because the output must retain every sale rather than combine a product's years or prices.
- **Unused product:** A product with no sales does not appear.
- **Repeated product:** Multiple sales of one product each produce an output row.
- **Composite sale key:** The same `sale_id` may occur in different years; those rows remain separate.
- **Quantity:** It describes units sold but does not change the requested per-unit `price` projection.
