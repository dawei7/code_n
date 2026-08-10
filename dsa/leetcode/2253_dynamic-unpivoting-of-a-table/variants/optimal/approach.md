## General

**Why column discovery is necessary**

The source table has one row per product and one price column per store. Store column names change between test cases, so a static query cannot write one branch for each store in advance.

The procedure queries database metadata to discover every current store column, generates a `SELECT` for each, joins those branches with `UNION`, then prepares and executes the resulting SQL.

**Read store columns from `information_schema`**

The CTE `t` selects `column_name` from `information_schema.columns` with three filters:

- `table_schema = DATABASE()` restricts metadata to the active database;
- `table_name = 'Products'` restricts it to the source table;
- `column_name != 'product_id'` excludes the identifier column.

Every remaining column is a store-price column by the supplied schema. There is at least one, so the generated query is nonempty.

**Generate one long-form projection per store**

For a discovered column named `S`, the generated branch has this logical form:

`SELECT product_id, 'S' store, S price FROM Products WHERE S IS NOT NULL`.

It transforms each non-null cell of column `S` into a row:

- the existing product ID;
- the literal store name `S`;
- that cell's price.

The `WHERE` clause omits null cells, which represent products not sold in that store.

**Combine all store branches**

`STRING_AGG` concatenates branch strings with separator `' UNION '` and assigns the result to `@sql`. Executing the combined query stacks the long-form rows from every store.

The exact procedure uses `UNION` rather than `UNION ALL`. The source primary key makes `product_id` unique, and different branches emit different store literals, so generated rows should already be distinct. `UNION` may perform unnecessary duplicate elimination, but it preserves correct results.

No ordering clause is needed because the result may be returned in any order. Metadata column order therefore also does not affect correctness.

**Execute and clean up**

`PREPARE stmt FROM @sql` compiles the generated union query, `EXECUTE stmt` returns its result, and `DEALLOCATE PREPARE stmt` releases it.

`SET group_concat_max_len = 5000` provides enough room for up to thirty generated branches without truncating the SQL text.

**Why every emitted row is valid**

Every branch emits rows only where its source store column is non-null. Such a cell means that product is sold at that store for the selected price. The branch labels the row with exactly that column's name.

Therefore, every output triple describes a real available product-store-price cell.

**Why every required cell becomes a row**

Take any non-null store-price cell. Its column is discovered by the metadata CTE. The corresponding generated branch scans the product's row, passes the `IS NOT NULL` predicate, and emits its product ID, store name, and price.

Null cells fail the predicate and emit nothing. Hence, output rows correspond one-to-one with non-null store cells.

**Trace the example conceptually**

Columns LC_Store, Nozama, Shop, and Souq produce four branches. Product one passes the LC_Store and Shop branches but fails the other two null predicates, so exactly its two available-store rows appear.

Product two and three are treated independently by the same column branches.

**Exact identifier behavior**

The generated SQL inserts `column_name` as an identifier in the select list and predicate and as a quoted string literal for `store`. The solution relies on the provided store column names being valid in this dynamic SQL context.

## Complexity detail

Let `r` be the number of product rows and `s` the number of store columns, with `1 <= s <= 30`. Metadata discovery processes `O(s)` columns. The generated union contains `s` branches, each scanning `r` rows, for `O(rs)` logical row work.

Because `s` is capped at thirty, the manifest simplifies this to `O(r)` with a bounded constant. `UNION` duplicate elimination can add sorting or hashing over emitted rows, depending on the optimizer.

The generated statement uses `O(s)` text. Database working and result space can reach `O(rs)` emitted rows, simplified to `O(r)` under the fixed store cap.

## Alternatives and edge cases

- **Static `UNION ALL` branches:** Simpler when store columns are fixed, but invalid when names change dynamically.
- **Application-side unpivoting:** It moves transformation outside SQL and does not implement the requested stored procedure.
- **Use `UNION ALL` dynamically:** It would be sufficient and may avoid deduplication because generated triples are inherently distinct; the exact solution uses `UNION`.
- **Null price:** The branch predicate omits that product-store combination entirely.
- **Zero price:** Zero is not null and is correctly emitted.
- **One store column:** The generated statement contains one select and no meaningful separator.
- **Maximum thirty stores:** Increasing `group_concat_max_len` protects the longer generated text.
- **Product unavailable everywhere:** Its row emits no long-form result.
- **Any result order:** Neither metadata ordering nor a final `ORDER BY` is required.
- **Active database filter:** It avoids accidentally discovering a same-named table in another schema.
- **Exclude `product_id`:** Treating it as a store would create invalid rows; the metadata predicate prevents that.
- **Prepared-resource cleanup:** The statement is explicitly deallocated after execution.
- **Generated identifier safety:** Store names come from actual metadata column identifiers and are inserted unquoted into the dynamic statement. The source relies on the supplied schema using names valid in that position.
