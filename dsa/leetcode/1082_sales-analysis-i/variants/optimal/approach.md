## General
**Aggregate at seller grain:** Group `Sales` by `seller_id` and compute `SUM(price)`. The `price` column already stores the sale's total price, so multiplying it by `quantity` would change the stated value and produce an incorrect seller total.

**Compare with one global maximum:** Materialize the grouped totals as `seller_totals`. A scalar subquery computes the maximum of those totals, and the outer query keeps every seller whose total equals it. Equality preserves all ties rather than choosing an arbitrary row.

Every returned seller has the maximum grouped sum by the filter. Every seller attaining that sum satisfies the same equality and is returned, so the result contains exactly all top sellers. The `Product` table is unnecessary because neither product names nor unit prices affect the requested aggregation.

## Complexity detail
Let $R$ be the number of `Sales` rows. Sort-based grouping and deterministic output ordering take $O(R\log R)$ time and up to $O(R)$ execution space. Hash aggregation can make the grouping phase expected $O(R)$; indexes and the optimizer may choose a different physical plan.

## Alternatives and edge cases
- **Dense rank over seller totals:** Rank grouped sums in descending order and keep rank one. It preserves ties but adds a window step when a maximum comparison is sufficient.
- **Correlated seller sum:** Recompute one seller's total for every sale row and deduplicate afterward. It is correct but can rescan `Sales` repeatedly and approach quadratic time.
- **Order and limit one:** `ORDER BY SUM(price) DESC LIMIT 1` discards other sellers tied for first.
- **Multiply by quantity:** It is incorrect because `Sales.price` is already the total price for that sale.
- **Several sales by one seller:** Sum every recorded `price` in that seller's group.
- **Tied maximum:** Return each tied `seller_id` once.
- **Product attributes:** They do not affect total recorded sales price and require no join.
