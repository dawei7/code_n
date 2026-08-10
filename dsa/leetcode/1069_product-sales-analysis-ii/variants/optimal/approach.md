## General

**Match the requested output grain**

The requested result has one row for every distinct `product_id` that appears in `Sales`. For each such product, all `quantity` values from its sale rows must be added.

This is exactly a grouping aggregation:

- `product_id` identifies the group.
- `SUM(quantity)` reduces all rows in that group to one total.

No information from `Product` is needed. The output does not ask for `product_name`, and products with no sale rows should not create a group. Reading or joining `Product` would add work without contributing any result value.

**Select the group key and aggregate**

The exact query begins:

```sql
SELECT product_id, SUM(quantity) AS total_quantity
FROM Sales
```

`product_id` is preserved as the identifier of each result group.

`SUM(quantity)` adds the quantities across every row in that group. It does not add prices, sale identifiers, or distinct quantity values. If a product has quantities ten and twelve in two sale rows, the aggregate is 22.

The alias:

```sql
AS total_quantity
```

gives the computed column the exact output name required by the contract. Without the alias, the database would expose an implementation-dependent expression label such as `SUM(quantity)`.

**Group by the first selected expression**

The final clause is:

```sql
GROUP BY 1
```

In MySQL, an integer in `GROUP BY` can refer to a select-list position. Position one is `product_id`, so this is equivalent to:

```sql
GROUP BY product_id
```

All sale rows with the same product identifier enter one group. Different product identifiers enter different groups.

The positional form is concise but depends on select-list order. If another expression were inserted before `product_id`, `GROUP BY 1` would silently refer to the new first expression. Writing the column name explicitly is often clearer in maintained code, but the exact query is correct as written.

**Why no join is required**

The schema also provides `Product`, but both required inputs to the result already live in `Sales`:

- The grouping identifier is `Sales.product_id`.
- The measure being summed is `Sales.quantity`.

A join to `Product` would match every sale with metadata that is then discarded. Product-key uniqueness would prevent accidental multiplication, but the join would still be logically redundant.

More importantly, starting from `Product` and using an outer join could produce a row for a product with no sales. The stated output grain is each product identifier occurring in `Sales`, so those catalog-only products should be absent.

**Why the query returns exactly one correct row per sold product**

Fix any product identifier `p` appearing in `Sales`. The grouping clause places every and only row with `product_id = p` into one group. `SUM(quantity)` adds the quantity from each row of that group, so the computed value equals the total quantity sold for `p`. The select list emits `p` and that total as one row.

Every output group originates from at least one sale row because grouping is performed directly on `Sales`. Thus the query cannot invent a product with no sale.

Different identifiers cannot be combined because they have different group keys. The result is therefore sound, complete, and at the required one-row-per-sold-product grain.

**Why sale year and unit price do not belong in the grouping**

The total is requested across every sale record for a product, regardless of year or price. Adding `year` to `GROUP BY` would split one product into separate annual totals. Adding `price` would split it again whenever prices differ.

Neither column belongs in the select list because non-aggregated selected columns must describe the group as a whole. `product_id` is the only requested grouping dimension.

**No DISTINCT inside SUM**

The correct expression is `SUM(quantity)`, not `SUM(DISTINCT quantity)`. If two separate sale rows both have quantity ten, both contribute ten units and the total must include 20. A distinct aggregate would incorrectly count the numeric value only once.

Similarly, a top-level `DISTINCT` is unnecessary because `GROUP BY` already produces one row for each distinct product identifier.

**No output order is promised**

The problem accepts any order, so there is no `ORDER BY`. Grouping implementations may output product groups in hash order, key order, or another plan-dependent order. None is guaranteed without an explicit ordering clause, and none is required here.

## Complexity detail

Let `R` be the number of rows in `Sales` and `G` the number of distinct product identifiers.

Physical complexity depends on the database engine and plan. A hash aggregation can scan all rows once, maintaining one running sum per product, for expected `O(R)` time and `O(G)` working space.

A sort-based aggregation first orders rows by `product_id` and then reduces consecutive groups. Without a useful index, that commonly takes `O(R log R)` time and up to `O(R)` working space. An existing index ordered by `product_id` can reduce or eliminate explicit sorting.

The manifest states `O(R log R)` time and `O(R)` space, matching the conservative sort-based plan. A hash-capable optimizer may execute the same declarative query more efficiently on a particular database.

The result contains `G` rows, so materializing the output itself uses `O(G)` space.

## Alternatives and edge cases

- **Explicit group name:** `GROUP BY product_id` is equivalent to `GROUP BY 1` and is more robust when the select-list order changes.
- **Window sum plus DISTINCT:** A window function could attach the total to every sale row and a later deduplication could keep one per product. It is more complicated and creates unnecessary intermediate repetition.
- **Correlated subquery:** Computing one sum for every distinct product can repeat scans or index lookups. Direct grouping expresses the task more efficiently.
- **Join to Product:** It is redundant because no product metadata is requested and can only add work.
- **Product with one sale:** Its one quantity is also its group sum.
- **Product with many years:** Every year contributes to the same product group because year is not a grouping dimension.
- **Repeated equal quantities:** Every row contributes; `SUM` must not use `DISTINCT`.
- **Product with no Sales row:** No group is created, which matches the requested sales-driven result.
- **Multiple unit prices:** Price does not alter the number of units sold and is deliberately ignored.
- **Composite sale key:** The primary key distinguishes records, but aggregation needs only `product_id` and `quantity`.
- **Output alias:** `total_quantity` is required even though it is not a stored source column.
- **Any row order:** Omitting `ORDER BY` is correct.
- **Positional grouping caution:** `GROUP BY 1` refers to the first select expression, not the numeric constant one in this MySQL context.
