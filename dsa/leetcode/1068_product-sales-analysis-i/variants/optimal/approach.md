## General

**Identify which table owns each requested column**

The output needs `product_name`, `year`, and `price` for every row in `Sales`.

`year` and `price` are already stored in `Sales`. The readable `product_name` is stored in `Product`. Both tables share `product_id`:

- `Sales.product_id` is a foreign key referencing `Product.product_id`.
- `Product.product_id` is a primary key, so at most one product row matches any product identifier.

This is a direct relational join problem. Each sale row must be paired with its one referenced product row so the result can combine sales facts with the product name.

**Use an inner join on the common key**

The query's source is:

```sql
FROM
    Sales
    JOIN Product USING (product_id)
```

In MySQL, bare `JOIN` means `INNER JOIN`. Only row pairs whose `product_id` values are equal survive.

`USING (product_id)` is concise syntax for an equality join when both tables use the same column name. It corresponds to:

```sql
Sales.product_id = Product.product_id
```

and exposes the join key as one merged output column rather than two separately named copies.

The foreign-key contract guarantees that every `Sales` row references an existing product. Therefore, no sale is lost through the inner join.

The primary-key contract on `Product.product_id` guarantees exactly one matching product row for a referenced identifier. Therefore, the join does not multiply one sale into several result rows.

Together, those constraints establish a one-to-one relationship from each sale row to its joined result row, even though one product can appear in many different sales.

**Project only the required attributes**

The select list is:

```sql
SELECT product_name, year, price
```

`product_name` exists only in `Product`, while `year` and `price` exist only in `Sales`, so these unqualified names are unambiguous.

Other columns are intentionally omitted:

- `sale_id` identifies the source sale but is not requested.
- `product_id` performs the join but is not requested in the output.
- `quantity` does not affect the requested per-unit price and year.

Projection does not merge equal rows. If two distinct sales happen to have the same product name, year, and price, SQL returns two identical-looking result rows because there is no `DISTINCT`. That is correct: the requirement asks for one result for each `sale_id`, even though `sale_id` itself is not displayed.

Adding `DISTINCT` would be a semantic bug because it could collapse separate sales into one row.

**Why the join result is correct**

Take any row `s` in `Sales`. Its foreign-key value identifies one product row `p`. The join condition matches `s` with `p`, and product-key uniqueness prevents any second product match. The projection returns `p.product_name` together with `s.year` and `s.price`. Thus the query emits the exact requested information for `s` once.

Conversely, every joined row contains a real `Sales` row and its matching `Product` row because this is an inner equality join. The projection cannot invent a sale or a product name. Therefore every output row is justified by one sale.

Applying this reasoning to all sales proves both completeness and soundness.

**No ordering clause is needed**

The problem permits the result in any order. The query correctly omits `ORDER BY`.

Without `ORDER BY`, a database may return rows in any physical-plan-dependent order. The order can change with indexes, statistics, or execution plans and must not be treated as guaranteed. Since the evaluator compares the result as an unordered relation, no sorting work is semantically required.

**Why Product rows without sales disappear**

A product may exist in `Product` without a corresponding `Sales` row. Because `Sales` is joined only through matching rows and the query begins from the join relation, such a product produces no result.

This is correct because the output is defined per sale, not per catalog product. A left join from `Product` would introduce products without sales and null year or price values, which the problem does not request.

## Complexity detail

Let `R` be the number of rows in `Sales` and `P` the number of rows in `Product`.

SQL complexity depends on the database engine, indexes, statistics, and chosen physical join algorithm. The declarative query specifies the result, not one mandated execution strategy.

With a hash join, the engine can build a hash table for one input and scan the other, giving expected `O(P + R)` time and `O(P)` or `O(R)` working space. With an index on the product primary key, it can scan sales and perform indexed product lookups, commonly costing approximately `O(R log P)` after index availability. A sort-merge plan can require sorting unsorted inputs.

The manifest records `O(P + R log R)` time and `O(P + R)` space as a conservative abstract bound for reading product data and ordering or indexing sales-side work. The exact physical cost is engine-dependent, but the query performs only one key join and one projection.

The result itself contains `R` rows under the foreign-key and primary-key guarantees, so output materialization necessarily requires space proportional to `R` outside streaming execution.

## Alternatives and edge cases

- **Explicit ON syntax:** `JOIN Product ON Sales.product_id = Product.product_id` is semantically equivalent and can be clearer when key names differ or table aliases are used.
- **Correlated scalar subquery:** Looking up the product name separately for each sale can produce the same result, but it is less direct and may lead to repeated index probes.
- **Left join:** It is unnecessary because every sale has a valid product foreign key. Starting from products with a left join could also introduce catalog rows with no sale.
- **DISTINCT:** Do not add it. Separate sale rows may project to identical visible values and must remain separate.
- **Product with many sales:** The product name appears once for each matching sale, preserving the required per-sale grain.
- **Product with no sales:** It contributes no row because the output is driven by `Sales`.
- **Same product and year across sales:** Each sale remains a separate joined row, even when all selected values are identical.
- **Composite Sales primary key:** Uniqueness of `(sale_id, year)` identifies sale records but is not needed as a join key; `product_id` is the relational link to `Product`.
- **Per-unit price:** The query selects `price` directly and does not multiply it by `quantity`.
- **Any result order:** Omitting `ORDER BY` is correct and avoids implying an unsupported ordering contract.
- **USING column behavior:** `USING (product_id)` requires the same key name in both tables and merges that key in the joined namespace.
- **Null key concerns:** The foreign-key description supplies referenced product identifiers. Under the stated schema, every sale has its corresponding product.
