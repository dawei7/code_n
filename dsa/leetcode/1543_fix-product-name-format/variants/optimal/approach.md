## General
**Normalize before forming groups**

Apply `TRIM` before `LOWER` so surrounding whitespace cannot create artificial product variants. Extract the four-digit year and two-digit month from each `sale_date`; in the app-local SQLite query, `strftime('%Y-%m', sale_date)` produces exactly the required representation. These two expressions define the logical group key.

**Aggregate each normalized product-month pair**

Group the rows by both expressions and use `COUNT(*)` to count sales. Grouping by only the product would incorrectly merge different months, while grouping by the original product text would split capitalization and whitespace variants. Because every source row belongs to exactly one normalized pair, the aggregate counts partition all sales without omission or duplication.

**Return the specified deterministic order**

Order by the normalized `product_name` alias and then the formatted `sale_date` alias. The `YYYY-MM` format has fixed-width components, so lexical ascending order is also chronological ascending order. The native MySQL artifact uses `DATE_FORMAT` for the same operation; only the database-specific date formatter differs.

## Complexity detail
For $r$ input rows, normalization and month extraction are constant work per row. A database engine can build the $g$ aggregate groups with a hash table and then sort the result, or use sorting for grouping as well. The portable upper bound is therefore $O(r \log r)$ time. The aggregation state stores one count per distinct group, using $O(g)$ auxiliary space; the engine may also allocate sorting workspace proportional to the data it sorts.

## Alternatives and edge cases
- **Pre-normalized computed columns:** storing an indexed normalized name and month can reduce repeated expression work, but it changes the schema and is unnecessary for this query.
- **Correlated count per sale:** counting matching rows in a subquery can produce the same values, but repeats the scan for many rows and degrades toward $O(r^2)$.
- Leading and trailing whitespace must be removed before grouping; internal spaces remain part of the product name.
- Product names differing only by letter case belong to the same group.
- Sales of one product in different months must remain separate.
- The output month needs a zero-padded two-digit month so lexical and chronological order agree.
- Sorting is by product first, even when that places a later month before an earlier month belonging to another product.
