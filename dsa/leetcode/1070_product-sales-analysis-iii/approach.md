## General

**Separate finding the first year from returning its sales**

For each product, the query must first discover its minimum `year`. It must then return every original sale row for that product in that year.

These are deliberately two steps. Aggregating to `MIN(year)` alone loses `quantity` and `price` because those values belong to individual sale rows. Joining or filtering the original table by the per-product minimum restores the full first-year rows.

The phrase "all sales entries" matters. A product can have multiple sales in its earliest year. The query must retain every one rather than choose an arbitrary row or combine their quantities.

**Compute one earliest-year key per product**

The inner query is:

```sql
SELECT
    product_id,
    MIN(year) AS year
FROM Sales
GROUP BY product_id
```

`GROUP BY product_id` creates one group from all sale rows for each product.

Within each group, `MIN(year)` returns the smallest year value. The subquery therefore produces one pair:

```text
(product_id, earliest year)
```

for every product appearing in `Sales`.

The alias `AS year` makes the second column's role compatible with the outer tuple comparison. The alias is not the final output name; the outer query later renames the original sale year to `first_year`.

No `quantity` or `price` appears in this grouped result. Selecting either without aggregation would not identify which source row it came from, especially when several rows share the earliest year.

**Filter original rows with a composite membership test**

The outer condition is:

```sql
WHERE
    (product_id, year) IN (
        ...
    )
```

`(product_id, year)` is a row-value expression. A sale row passes when its two-column pair equals one of the product-and-minimum-year pairs returned by the subquery.

Matching both columns is essential:

- Matching only `year` could retain a later sale for one product merely because that year is the first year of another product.
- Matching only `product_id` would retain every year for that product.

The composite pair expresses exactly the desired relation: this sale's year equals the minimum year for this same product.

**Return all matching source rows**

The select list is:

```sql
SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM Sales
```

These values come from the original `Sales` row, not from an arbitrary grouped row.

`year AS first_year` gives the requested output column name while preserving the actual earliest-year value.

`quantity` and `price` remain at sale-row grain. If two sale records for one product share its first year, both satisfy the same tuple membership condition and both are returned with their own quantities and prices.

There is no `DISTINCT` and no outer `GROUP BY`. Either could collapse or combine source entries, violating the requirement to return all first-year sales.

**A concrete multiple-row example**

Suppose product 100 has these sale rows:

```text
year 2008, quantity 10, price 5000
year 2008, quantity 4,  price 4800
year 2009, quantity 12, price 5000
```

The subquery returns `(100, 2008)` once. Both 2008 rows match that pair and appear in the result. The 2009 row does not.

The query does not assume that price or quantity is constant within a year. It correctly preserves the values from each matching record.

**Why the query is correct**

For any product `p`, the inner group computes `y`, the minimum year among all rows for `p`. An outer row for `p` passes exactly when its year equals `y`. Therefore every returned row is a sale from `p`'s first year.

Every sale from that first year has pair `(p, y)`, which appears in the subquery, so it passes. Thus no first-year row is omitted.

The argument holds independently for every product, proving that the result contains all and only the requested sales entries.

**Why an aggregate-only query would be insufficient**

A tempting query might group by product and select `MIN(year)` together with quantity and price. Standard SQL either rejects ungrouped quantity and price or, under permissive modes, returns values from an indeterminate row. It would also return only one row per product and lose additional sales in the same first year.

The inner aggregate plus outer filter avoids both problems by using aggregation only to identify keys and reading details from the original rows.

**No ordering is necessary**

The output may be in any order, so the query omits `ORDER BY`. Database row order is not guaranteed without it, but that has no effect on correctness here.

## Complexity detail

Let `R` be the number of rows in `Sales` and `G` the number of distinct products.

The physical cost is database-plan-dependent. A sort-based grouping of `Sales` by product takes `O(R log R)` time, after which the engine can materialize or hash the `G` minimum-year pairs and scan or semijoin the outer sales rows. Working space can be `O(R)` for sorting and intermediate data.

A hash aggregation plus hash semijoin can run in expected `O(R)` time with `O(G)` state. An index ordered by `(product_id, year)` may permit still different access paths.

The manifest states `O(R log R)` time and `O(R)` space, corresponding to the conservative sort-based execution. The declarative SQL does not force one physical algorithm, so actual plans may improve on it.

Output size can itself be `O(R)` when every sale for each product occurs in that product's only year.

## Alternatives and edge cases

- **Join with the aggregate subquery:** Compute `(product_id, MIN(year))` and inner-join it to `Sales` on both product and year. This is semantically equivalent and often makes the two-step logic explicit.
- **Window function:** Compute `MIN(year) OVER (PARTITION BY product_id)` for each row, then filter where `year` equals that window value. This preserves all ties but may require a derived table because window aliases are not normally available directly in `WHERE`.
- **Correlated subquery:** Filter with `year = (SELECT MIN(year) ... WHERE product_id = outer.product_id)`. Optimizers may decorrelate it, but the grouped key set is often clearer.
- **ROW_NUMBER:** Using `ROW_NUMBER() = 1` would keep only one row when several sales share the first year. A minimum-year filter or `DENSE_RANK() = 1` is required to preserve all ties.
- **One sale for a product:** Its year is automatically the minimum and the row is returned.
- **Several first-year sales:** Every row with the minimum year is returned independently.
- **Later sale with identical quantity and price:** It is rejected because the composite key includes year.
- **Same earliest year across products:** Matching also includes product identifier, so groups cannot interfere.
- **No Product table:** This problem requires only `Sales`; product metadata is irrelevant.
- **No DISTINCT:** Identical-looking projected rows may represent different sales and must not be collapsed.
- **Alias first_year:** Only the output column name changes; filtering still uses the source `year`.
- **Any order:** Omitting `ORDER BY` matches the contract.
- **Composite row IN support:** MySQL supports row-value membership for the two-column comparison used by the exact query.
