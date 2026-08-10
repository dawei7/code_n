## General

**Treat Queries as the required output population**

The result must contain one row for every pair in `Queries`. Some pairs have a stored net present value and some do not, but missing reference data must not remove the query. This immediately makes `Queries` the preserved left side of the join:

```sql
FROM
    Queries AS q
    LEFT JOIN NPV AS n USING (id, year)
```

A left join emits every left row. When the matching key exists in `NPV`, its columns are attached. When no match exists, SQL still emits the query row and fills columns from the NPV side with `NULL`.

An inner join would be wrong because it would discard queries without a stored value. Starting from NPV would also be wrong because it could emit stored inventory-year pairs nobody requested.

**Both columns form the lookup key**

The schemas define the composite key `(id, year)`. The same inventory ID can have different NPV values in different years. A correct lookup must require equality on both columns.

`USING (id, year)` is concise SQL for joining equal same-named key columns. It is logically equivalent to:

```sql
ON q.id = n.id AND q.year = n.year
```

It also merges each equal key pair into one output column, preventing duplicate `id` and `year` columns in the joined row.

Joining only by `id` could attach a value from the wrong year and could multiply one query into several rows when that ID has multiple stored years. Joining only by `year` would mix unrelated inventories.

**Why the join cannot duplicate a query**

`NPV` has primary key `(id, year)`, so at most one NPV row can match a given query pair. `Queries` also has that primary key, so each requested pair appears at most once. Therefore, the left join produces exactly one result row per Queries row: either one matched row or one unmatched null-extended row.

This uniqueness is what lets the query avoid grouping or deduplication.

**Select the preserved key columns**

The projection begins with:

```sql
SELECT q.*
```

The `Queries` table contains exactly `id` and `year`, so `q.*` returns those two required columns in their table order. It deliberately does not select `n.*`, which would add duplicate key columns and expose the raw nullable NPV field.

Using the explicit list `q.id, q.year` would be equally clear. In this fixed schema, `q.*` has the exact desired key projection.

**Replace a missing lookup with zero**

For a matching NPV row, the selected value should be its `npv`. For an unmatched left-join row, the NPV-side `npv` is `NULL` and must become zero:

```sql
COALESCE(npv, 0) AS npv
```

`COALESCE` returns the first non-null argument. A stored value such as 113 is returned unchanged. A missing-row null falls through to the literal zero.

The alias `AS npv` gives the calculated column the required output name.

A stored NPV value of zero and a missing NPV row both produce zero in the output, which matches the contract. Their internal causes differ, but the requested displayed value is the same.

**Following the sample pairs**

The query pair `(1, 2019)` finds exactly the NPV row with value 113, so `COALESCE` returns 113.

The pair `(7, 2019)` finds an actual stored row whose value is zero, so it returns that zero.

The pair `(7, 2018)` has no matching composite key. The left join still emits ID 7 and year 2018, supplies `NULL` for `npv`, and `COALESCE` converts it to zero.

The NPV row `(11, 2020, 99)` has no corresponding Queries row. Because Queries drives the join, that unrequested row never appears.

**Why no ordering clause is needed**

The contract permits any order. SQL tables have no guaranteed natural row order, so omitting `ORDER BY` is appropriate. Adding an order would not change correctness but would add unnecessary sorting work.

**Why the query is correct**

For each Queries row, the left join preserves its key. Composite-key equality attaches the one matching NPV value if it exists and cannot attach a wrong year or ID. Primary-key uniqueness prevents multiple output rows per query. `COALESCE` returns the stored value when present and zero when absent. Conversely, no row can appear without originating in Queries. These properties establish exactly the required mapping.

## Complexity detail

Let $P$ be the number of NPV rows and $Q$ the number of Queries rows. With a hash join, building and probing keyed structures takes expected $O(P+Q)$ time. With a suitable composite index on NPV, an execution plan may instead scan Queries and perform indexed lookups. Exact physical cost depends on the database optimizer, available indexes, and data distribution.

The manifest states $O(P+Q)$ time and $O(P+Q)$ space for the general hash-based execution model. A hash structure and the $Q$-row result can together occupy linear space. The SQL text itself declares no explicit temporary structure; these are execution-plan resources.

Because no ordering, aggregation, or duplicate elimination is required, the logical query adds no sorting factor.

## Alternatives and edge cases

- **Correlated scalar subquery:** Look up NPV separately for every Queries row and wrap the subquery in `COALESCE`. It is correct but can perform repeated lookups and is less direct than one join.
- **Inner join:** This incorrectly removes requested pairs that have no stored NPV value.
- **Right join from NPV:** It can be arranged to preserve Queries, but reversing the table roles makes the intent harder to read.
- **Join by ID only:** This can retrieve a value from the wrong year or duplicate query rows.
- **Join by year only:** This mixes different inventory IDs from the same year.
- **`IFNULL`:** In MySQL, `IFNULL(npv, 0)` is an equivalent two-argument alternative to `COALESCE` here.
- **Stored zero:** It remains zero; `COALESCE` does not treat zero as missing.
- **Missing pair:** The left join produces null only on the NPV side and the fallback becomes zero.
- **Unrequested NPV row:** It is absent because no preserved Queries row points to it.
- **Any-order contract:** No `ORDER BY` is required, and consumers must not infer a stable natural order.
- **Composite primary keys:** Their uniqueness guarantees at most one match on each side and prevents accidental multiplicative joins.
