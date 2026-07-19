## General
**Removing duplicate sale pairs first**

Project `sell_date` and `product` through `SELECT DISTINCT`. The resulting relation contains exactly one row for each product that should contribute to one date. After this step, an ordinary row count within a date equals the required distinct-product count, and each product name appears exactly once in the eventual list.

This explicit deduplication also keeps the SQLite app-local query portable: SQLite cannot combine `DISTINCT` with a custom separator in every `GROUP_CONCAT` form.

**Establishing product order before concatenation**

Sort the distinct rows by `sell_date` and then `product`. The rows for each date are therefore contiguous and their product names arrive in lexicographic order. Applying `GROUP_CONCAT(product, ',')` to that ordered input produces the required comma-separated list.

The separate LeetCode-native MySQL artifact can state the same requirement directly as `GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',')`.

**Aggregating one row per date**

Group the ordered distinct relation by `sell_date`. Because each input row now represents a unique product for that date, `COUNT(*)` is exactly `num_sold`. Concatenation includes precisely the same set of rows, so the count and list cannot disagree about duplicates.

Finally, apply `ORDER BY sell_date` to the grouped result. Ordering the products inside each group and ordering the result dates are independent requirements; both must be explicit.

**Why every output row is correct**

For a fixed date $d$, the deduplicated relation contains one and only one row for every product sold on $d$. Counting those rows gives the cardinality of the distinct product set. Concatenating their names after sorting lists every member of that set exactly once in lexicographic order. Grouping creates one result for each represented date, and the final ordering places those dates ascending.

## Complexity detail
Deduplicating $R$ activities requires an $O(R)$ scan under hash-based execution and retains $P$ distinct pairs. Ordering those pairs costs $O(P \log P)$ time, after which grouping and concatenation are linear in $P$. The materialized distinct and ordered data uses $O(P)$ space. Actual database engines may choose equivalent index, hash, or sort plans.

## Alternatives and edge cases
- **Native MySQL distinct concatenation:** Use `COUNT(DISTINCT product)` with `GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',')`. It is concise and is the platform-native artifact, but the exact syntax is not portable to SQLite.
- **Correlated subqueries per date:** Select distinct dates and run separate count and concatenation scans for each one. This is correct but can repeatedly scan `Activities` and grow quadratically with the number of dates.
- **Deduplicate without ordering:** It gives the right count but leaves concatenation order implementation-dependent and therefore does not satisfy the contract.
- **Duplicate activities:** Repeated copies of the same product on the same date contribute one to `num_sold` and one name to `products`.
- **Same product on different dates:** Deduplication is by the pair, so the product contributes independently to each date.
- **One product on a date:** The list contains that name without an extra comma.
- **Unsorted input rows:** Neither output row order nor product-list order may depend on insertion order.
- **Lexicographic comparison:** Product spelling is preserved; ordering follows the database's configured string collation.
- **Output aliases:** The aggregate columns must be named exactly `num_sold` and `products`.
- **Date ordering:** The outer `ORDER BY` is required even though the inner rows were already sorted.
