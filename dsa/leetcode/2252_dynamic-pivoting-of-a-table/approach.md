## General

**Why this pivot must be dynamic**

The input stores one product-store price per row, but the output needs one product per row and one column per store. Store names can change between test cases, so a fixed query cannot name all output columns in advance.

The procedure first discovers the current stores and builds a SQL query as text. It then prepares and executes that text. This is dynamic SQL: table data determines the query's selected columns.

**Build one conditional aggregate per store**

For store name `S`, the generated fragment has the logical form:

`MAX(CASE WHEN store = 'S' THEN price ELSE NULL END) AS S`.

Within all rows for one product, the `CASE` returns that product's price on the row for store `S` and `NULL` on other-store rows. The primary key `(product_id, store)` guarantees at most one matching price row.

`MAX` ignores nulls and returns the one price when present. If the product is not sold in `S`, every case result is null and the aggregate returns null, exactly as required.

**Discover, deduplicate, and order store expressions**

The first `SELECT` reads `Products` and feeds store values into `STRING_AGG`. `DISTINCT` creates only one expression per store even though many products may be sold there.

`ORDER BY store` inside the aggregation arranges fragments lexicographically by store name. Since those fragments become output columns in that order, the dynamic table satisfies the required lexicographical column ordering.

The resulting comma-separated expression list is assigned to session variable `@sql`.

**Assemble the complete pivot query**

The procedure wraps the generated columns with:

`SELECT product_id, ... FROM Products GROUP BY product_id`.

Grouping creates one result row for every distinct product. Each conditional aggregate independently extracts that product's price for its store column.

The procedure does not add `ORDER BY product_id` because result rows may be returned in any order. Column order, unlike row order, is explicitly constructed lexicographically.

**Execute the generated statement**

`PREPARE stmt FROM @sql` compiles the text as SQL. `EXECUTE stmt` runs the pivot query and returns its result. `DEALLOCATE PREPARE stmt` releases the prepared-statement resource afterward.

`SET group_concat_max_len = 5000` increases the allowed generated-string length so up to thirty store expressions are not truncated.

**Why every output cell is correct**

Fix product `P` and store `S`. Grouping places all rows for `P` together. The `S` case expression is non-null only on row `(P,S)`. If that row exists, its `price` is the aggregate result. If it does not, all values are null and the output cell is null.

Thus, every output cell precisely represents whether and at what price that product is sold in that store.

**Why every required row and column appears**

Every input row has a `product_id`, so grouping creates a row for each product that appears. Every distinct store contributes one generated aggregate expression because `STRING_AGG(DISTINCT ...)` sees it. No non-store column is generated.

The output therefore has exactly one product ID column, exactly one column per live store, and one row per live product.

**Trace the example structure**

Stores are discovered as `LC_Store`, `Nozama`, `Shop`, and `Souq` after lexicographic ordering. Four conditional aggregates are generated.

For product one, the LC_Store and Shop cases see prices one hundred and one hundred ten. The other two cases see only nulls, producing null cells. The same single grouped row logic handles every product.

**Exact identifier assumptions**

The generated text places store names directly after `AS` as column aliases. The solution relies on test-case store names being valid in this generated SQL context. The procedure also embeds store text inside quoted literals for the `CASE` comparison.

## Complexity detail

Let `r` be the number of product-store rows and `s` the number of distinct stores, with `s <= 30`. Discovering stores scans `O(r)` data and orders at most thirty store names. Executing the grouped conditional-aggregation query scans `O(r)` rows and evaluates `s` bounded expressions per row.

Treating the contractual store cap as constant, time is `O(r)`. If `s` were variable, a more explicit bound would include `O(rs + s \log s)`.

Database working space can be `O(r)` for grouping and the result, while the generated statement is `O(s)`. Exact memory and temporary-table use depend on the MySQL execution plan.

## Alternatives and edge cases

- **Static conditional aggregation:** It works only when store names are known ahead of time; this problem changes them by test case.
- **Return rows without pivoting:** That preserves the source shape and fails the required one-column-per-store output.
- **Self-join once per known store:** It is also static and becomes unwieldy as store sets change.
- **Missing product-store pair:** All case values are null, so the pivot cell is null.
- **One store:** The generated query has one dynamic price column.
- **Many products in one store:** `DISTINCT` generates the store column once.
- **Primary-key guarantee:** It ensures at most one non-null price per product-store aggregate.
- **Lexicographical columns:** Ordering belongs inside dynamic expression aggregation; output row ordering is irrelevant.
- **Generated-string length:** Raising `group_concat_max_len` prevents silent truncation of the statement.
- **Prepared-resource cleanup:** `DEALLOCATE PREPARE` releases the statement after execution.
- **Any row order:** No final `ORDER BY product_id` is necessary.
- **Null behavior:** `MAX` ignores nulls but returns null when all values in the group are null.
