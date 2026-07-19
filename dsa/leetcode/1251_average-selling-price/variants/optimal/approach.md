## General
**Match each sale to its effective price.** Left join `Prices` to `UnitsSold` by `product_id` and require `purchase_date` to fall between `start_date` and `end_date`, inclusively. Non-overlapping intervals ensure that a sale matches at most one price row. The left join preserves price-only products.

**Aggregate revenue and quantity together.** For each product, `price * units` is the revenue contributed by a matched sale. Sum those products for total revenue and sum `units` for total quantity. Dividing the two sums produces a units-weighted average; averaging interval prices directly would incorrectly give every interval equal influence.

**Handle empty products after aggregation.** An unmatched product group has null sums. Use `COALESCE` to turn its quotient into zero, then apply `ROUND(..., 2)` to the final weighted average. Group only by `product_id` so all of a product's price intervals contribute to one output row.

## Complexity detail
With indexes or hash-based join and aggregation, the query processes the $r$ input rows in $O(r)$ logical time and uses $O(r)$ join and grouping state. A database engine may instead choose sort-based or nested-loop physical plans depending on available indexes and statistics.

## Alternatives and edge cases
- **Correlated aggregate per product:** It is correct but may rescan both tables for every product and grow quadratically.
- **Inner join:** It drops products with no sales instead of returning their required zero average.
- **`AVG(price)`:** It averages price intervals rather than weighting prices by sold units.
- **Average of row-level revenue:** `AVG(price * units)` does not divide total revenue by total units and is semantically different.
- **Inclusive boundaries:** Use `BETWEEN` or equivalent `>=` and `<=` comparisons so endpoint sales are retained.
- **No sold units:** Protect the null quotient with `COALESCE` and emit `0`.
