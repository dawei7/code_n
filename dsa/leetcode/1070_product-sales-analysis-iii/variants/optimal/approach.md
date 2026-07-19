## General
**Find one first year per product:** Group `Sales` by `product_id` and compute `MIN(year)`. This relation contains the earliest year for every product represented in the table.

**Join the minimum back to sale rows:** Match the grouped relation to `Sales` on both `product_id` and `year`. Matching only the product would retain later years; matching both conditions selects exactly the required first-year entries.

**Preserve ties rather than rank one row:** The join returns every sale sharing the minimum year. Project the sale's year as `first_year` together with its quantity and price. Ordering by product and the composite sale key is included solely for deterministic fixtures.

Every joined row has a year equal to its product's grouped minimum, so it belongs in the result. Conversely, every sale in a product's first year satisfies both join conditions and is retained, including any additional row tied on that year.

## Complexity detail
A sort-based grouped minimum over $R$ rows and deterministic result ordering take $O(R\log R)$ time and up to $O(R)$ execution space. A hash aggregate and hash join may run in expected $O(R)$ time before output ordering; indexes can produce other physical plans.

## Alternatives and edge cases
- **Correlated minimum:** Compare each sale's year with a subquery computing its product's minimum. It is concise but can rescan all $R$ rows for each sale, taking $O(R^2)$ time without an index.
- **Dense rank:** `DENSE_RANK()` partitioned by product and ordered by year preserves all first-year ties, but may sort the full input and requires an outer filter.
- **Row number:** Keeping only `ROW_NUMBER() = 1` is incorrect when a product has several sales in its earliest year.
- **Single sale for a product:** It is necessarily a first-year row.
- **Several first-year sales:** Every tied row is returned with its own quantity and price.
- **Later price change:** Later-year rows are omitted even if their price or quantity differs.
- **Composite sale key:** Reusing a `sale_id` in a different year does not merge the rows.
