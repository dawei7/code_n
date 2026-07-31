## General

**Discover and quote the dynamic columns**

The store set is data, not fixed schema, so a static query cannot name every
output column. Aggregate the distinct store names into a comma-separated list
of conditional expressions. For each store, generate
`MAX(CASE WHEN store = <quoted value> THEN price END)` and alias it with the
escaped store name. Ordering inside `GROUP_CONCAT` establishes the required
lexicographical column order.

`QUOTE(store)` safely creates the SQL string literal used by the condition,
while doubling identifier backticks protects the generated alias. Increasing
`group_concat_max_len` prevents the expression list from being truncated.

**Execute one grouped pivot**

Concatenate the generated expressions into a query that groups `Products` by
`product_id`, then prepare and execute it. The primary key guarantees at most
one matching price per product and store, so `MAX` returns that price.
For an absent pair, every condition result is `NULL`, and `MAX` remains
`NULL`. Thus every generated cell has the required value.

## Complexity detail

Let $r$ be the number of `Products` rows. The number of stores is capped at
30, so distinct-store discovery, expression construction, conditional
aggregation, and result materialization are linear in $r$ under the standard
database model: $O(r)$ time and $O(r)$ working/result space. Exact constants,
indexes, grouping strategy, and materialization remain MySQL-engine dependent.

## Alternatives and edge cases

- **Static conditional aggregation:** It works only for store names known while writing the query and cannot satisfy the dynamic schema contract.
- **Rescan once per product:** Building each product row with correlated scans is correct but can require quadratic work in the number of input rows.
- **Omit column ordering:** Store discovery order is not guaranteed and can violate the required lexicographical schema.
- **Use store text without quoting:** Quotes or backticks in data can break the generated statement; quote values and escape identifiers separately.
- **Missing product-store pair:** Conditional aggregation naturally returns `NULL`.
- **One store:** The generated query contains one store column and still groups products correctly.
- **Different product coverage:** Every discovered store becomes a column even when only one product uses it.
- **Any row order:** The procedure need not add an `ORDER BY product_id`.
