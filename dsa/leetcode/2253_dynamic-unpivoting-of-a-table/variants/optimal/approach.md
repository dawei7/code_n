## General

**Discover the changing store schema**

Query `information_schema.columns` for the current database's `Products`
table, excluding `product_id`. For each remaining column, generate a select
that projects `product_id`, the quoted column name as `store`, and that column
as `price`, while filtering out null prices.

Quote the store string with `QUOTE(column_name)` and escape backticks in the
identifier independently. Concatenate the projections in ordinal column order
with `UNION ALL`. Raising `group_concat_max_len` prevents truncation of the
generated statement.

**Preserve every non-null cell**

Prepare and execute the union. A non-null store cell appears in exactly the
projection generated for its column, producing one required row. A null cell
is rejected by that projection's `IS NOT NULL` filter, and no other projection
can emit it. Therefore the union contains every and only available
product-store combination. `UNION ALL` preserves equal prices from different
products or stores rather than deduplicating them.

## Complexity detail

Let $r$ be the number of cells across the `Products` data rows and store
columns. Since there are at most 30 store columns, metadata discovery is
bounded and the generated projections scan and emit $O(r)$ data in the
standard database model. Time and working/result space are $O(r)$. Exact
execution plans and materialization behavior remain MySQL-engine dependent.

## Alternatives and edge cases

- **Static `UNION ALL`:** It works only for store columns known while writing the procedure and fails when the schema changes.
- **Rescan separately for each product-cell lookup:** This can reconstruct the same rows but repeats table work and can become quadratic.
- **Use `UNION`:** Deduplication is unnecessary and may add sorting work; different source cells are distinct output facts.
- **Keep null prices:** The contract requires unavailable product-store combinations to be omitted entirely.
- **One store:** The generated statement is a single select without a union and remains valid.
- **All-null product row:** That product contributes no output rows.
- **Zero price:** `0` is non-null and must be emitted.
- **Dynamic names:** Quote values and escape identifiers separately so unusual store names remain valid.
