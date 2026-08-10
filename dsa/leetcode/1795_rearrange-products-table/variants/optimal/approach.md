## General

**Convert a wide row into several narrow rows**

The input uses a wide representation: one product row has separate `store1`, `store2`, and `store3` price columns. The requested output uses a long representation: every available product-store combination gets its own row with columns `product_id`, `store`, and `price`.

Each source row can therefore generate zero to three output rows:

- `(product_id, 'store1', store1)` when `store1` is not null;
- `(product_id, 'store2', store2)` when `store2` is not null;
- `(product_id, 'store3', store3)` when `store3` is not null.

The protected SQL expresses these three fixed transformations as three `SELECT` branches.

**One branch per store column**

The first branch selects the source `product_id`, the string literal `'store1'` under alias `store`, and the value of column `store1` under alias `price`. Its `WHERE store1 IS NOT NULL` filter removes products unavailable in that store.

The second and third branches repeat the same structure for `store2` and `store3`. The literal store label is essential: after the three price columns are stacked into one `price` column, that label records which original column supplied the value.

All branches return the same number of columns in the same semantic order. SQL set operators combine columns by position, so this structural agreement is required.

**Why null checks belong in each branch**

A null price means the product is unavailable at that store and must not produce an output row. Filtering independently lets one product appear for its available stores while disappearing only from the unavailable branch.

For product 1 in the example, `store1 = 70` passes the first filter, `store2 = null` fails the second, and `store3 = 80` passes the third. The output consequently includes `(1, 'store1', 70)` and `(1, 'store3', 80)` but no store2 row.

The predicate must use `IS NOT NULL`. SQL null represents unknown or missing information and does not compare normally; expressions such as `store1 != NULL` evaluate to unknown rather than true and would not implement the intended test.

**Combine the branches with `UNION`**

The exact solution places `UNION` between the three query results. `UNION` applies set semantics and removes duplicate rows.

Under the table contract, duplicate elimination is not needed for logical correctness. `product_id` is unique in the source, and each branch uses a different literal store name. Even if two stores charge the same numerical price, their `store` fields differ, so the output triples remain distinct. `UNION ALL` would therefore produce the same valid rows under these guarantees and can avoid distinct-processing work.

Nevertheless, plain `UNION` is the operator used by the protected source. The explanation and complexity account for that exact behavior.

**Column names in the combined result**

The first branch explicitly aliases the literal as `store` and the source price as `price`. In a SQL union, result-column names are generally taken from the first `SELECT`. The later branches use the same aliases as well, keeping the intent clear.

The output order is unspecified because the query has no `ORDER BY` and the problem accepts any order. `UNION` is free to reorder rows while eliminating duplicates; that does not affect correctness.

**Following the example completely**

For product 0, all three price columns are non-null. It contributes three rows: store1 with 95, store2 with 100, and store3 with 105.

For product 1, store2 is null. The store2 branch filters that product out, while the other two branches contribute prices 70 and 80. Across both products, the union contains five rows, exactly matching the requested long-form table.

**Why the query is correct**

Take any row emitted by the query. It comes from exactly one store branch, whose filter proves the corresponding source price is non-null. Its product ID, literal store label, and price are copied into the required three-column form, so every emitted row represents a real available product-store combination.

Conversely, take any non-null price cell in the source table. It belongs to one of the three named store columns. That column's branch scans the product row, passes its non-null filter, and emits the corresponding triple. Thus no required combination is omitted.

The store literals distinguish branches and the primary key distinguishes products, so combining the results does not conflate different required rows. These two directions prove the rearranged table is complete and accurate.

## Complexity detail

Let $R$ be the number of product rows and $K$ the number of non-null store-price cells in the output, where $0\leq K\leq3R$. The query has three full-table branches. Because three is a fixed constant, their total scan work is $O(R)$.

Plain `UNION` performs duplicate elimination. With hash-based set processing, this adds expected $O(K)$ time and $O(K)$ working space. Since $K\leq3R$, expected total time remains $O(R)$ and space is $O(K)$, matching the manifest.

SQL does not prescribe the physical plan. An engine using sorting for `UNION` distinct may spend $O(K\log K)$ time, and indexes or optimizer rewrites can change scan details. The manifest represents the standard logical/hash-based cost model.

## Alternatives and edge cases

- **`UNION ALL`:** The source primary key and distinct store literals guarantee no duplicate triples, so this avoids unnecessary distinct elimination while returning the same rows.
- **Native `UNPIVOT`:** Engines that support it can express wide-to-long conversion directly, but MySQL compatibility and null behavior must be checked.
- **JSON or dynamic SQL unpivoting:** Useful for a dynamic number of store columns, but unnecessary for the fixed three-column schema.
- **Application-side transformation:** It moves simple relational work out of the database and transfers a wider result than needed.
- **Omit null filters:** This would emit forbidden rows for stores where a product is unavailable.
- **Compare with `NULL` using equality:** `= NULL` and `!= NULL` do not behave as ordinary Boolean comparisons; `IS NOT NULL` is required.
- **Same price in multiple stores:** Both rows must remain because their `store` labels differ.
- **All three prices present:** One source row expands into exactly three output rows.
- **Only one price present:** Only that store's branch emits a row for the product.
- **All prices null:** The product emits no rows, exactly as the availability rule requires.
- **Unique product IDs:** The primary key prevents duplicate source rows for one product.
- **Any result order:** Without `ORDER BY`, row order is intentionally unspecified and accepted.
- **Fixed store schema:** The three explicit branches must be updated if the table later gains another store column.
- **Output-sensitive storage:** Distinct processing can retain up to $K$ triples even though the source scans are linear.
- **Source table unchanged:** The query only projects and filters data; it performs no updates.
