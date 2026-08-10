## General

**Turn subtraction into signed addition.** The required value for each date is apples sold minus oranges sold. SQL aggregation works especially naturally with addition, so the query changes the sign of each orange quantity before summing:

- An apples row contributes `sold_num`.
- An oranges row contributes `-sold_num`.

For one date, adding those signed contributions produces exactly `apples - oranges`. This is sometimes called conditional aggregation: a condition decides how each row contributes to an aggregate for its group.

The expression `IF(fruit = 'apples', sold_num, -sold_num)` performs that sign choice. MySQL's `IF` takes a condition, a value to return when true, and a value to return when false. Therefore an apples row remains positive, while every non-apples row becomes negative. Under the problem's contract, the only other fruit category is oranges, so the false branch represents precisely the amount that must be subtracted.

**Form one independent group per day.** `GROUP BY 1` groups rows by the first expression in the `SELECT` list, which is `sale_date`. Each date is therefore processed separately. `SUM(...)` combines only the signed values belonging to that date and gives the result the required alias `diff`.

For example, suppose a date has an apples row with `sold_num = 15` and an oranges row with `sold_num = 16`. The conditional expression produces `15` for the first row and `-16` for the second. Their sum is `-1`, correctly showing that one more orange than apple was sold.

If both quantities are equal, the positive and negative contributions cancel and `diff` is zero. If the orange quantity is zero, its contribution is also zero, so the apple quantity remains as the difference. Negative output is expected and meaningful whenever orange sales exceed apple sales.

**Why grouping is reliable here.** The composite primary key `(sale_date, fruit)` guarantees at most one row for each fruit on each date. Thus a normal complete day has one apple quantity and one orange quantity. The query would also correctly add several rows of the same category if the uniqueness rule were removed, but the stated schema makes the intended daily interpretation unambiguous.

Conditional aggregation avoids needing to place the apple and orange quantities in separate physical columns first. Every input row can be read once, assigned its sign, and added to the accumulator for its date. This is shorter and generally more direct than joining `Sales` to another copy of itself.

**Order the final groups, not the raw rows.** The problem specifically requires increasing `sale_date` order. `ORDER BY 1` refers to the first selected column, again `sale_date`. Because ordering logically happens after grouping, it sorts the one-row-per-date result rather than trying to arrange individual fruit rows before their sums are computed.

Dates use the SQL `date` type, so ascending order is chronological. There is no need to convert them to strings or split them into year, month, and day components. Such conversions could complicate index use and introduce formatting issues without changing the desired order.

Using ordinal `1` in `GROUP BY` and `ORDER BY` is concise MySQL syntax. Reading the query from its `SELECT` list makes the reference clear: selected expression one is `sale_date`. An explicit `GROUP BY sale_date ORDER BY sale_date` would mean the same thing and may be easier to maintain if columns are later reordered, but the stored query is valid as written.

**Follow the relational pipeline.** Conceptually, the database reads each `Sales` row. The `IF` expression maps it to a signed number. Rows with the same `sale_date` enter the same aggregate group. `SUM` reduces every group to one `diff` value. Finally, the resulting date groups are sorted ascending. The query returns only `sale_date` and `diff` because those are the requested output columns.

**Why every result is correct.** Fix a particular date. Partition its rows into apples and oranges. The conditional expression contributes every apple quantity with coefficient positive one and every orange quantity with coefficient negative one. The group's sum is therefore the total apples quantity minus the total oranges quantity, exactly the definition of `diff`. Grouping prevents quantities from other dates from entering that calculation. Every recorded date forms one group, and the final ordering places those correct rows chronologically.

The schema's two-category guarantee is part of this proof. If a third fruit category were possible, the false branch would incorrectly subtract it as though it were oranges. A more defensive general-purpose query would test oranges explicitly, but that additional case is unnecessary under this problem's contract.

**Why a self-join is not needed.** A common first idea is to alias the table as an apple side and an orange side, join matching dates, and subtract their two columns. That works when both rows exist, but it makes row pairing part of the solution. Conditional aggregation instead treats the desired subtraction as a sum of signed rows. It needs only one reference to `Sales` and naturally produces one accumulator per date.

The exact query does not use a `WHERE` clause. It does not need one because both allowed fruit values participate in the calculation. Filtering out either category would destroy the subtraction.

## Complexity detail

Let `R` be the number of rows in `Sales` and `D` the number of distinct sale dates. A standard aggregate plan scans the `R` rows once and maintains a group accumulator for each date, taking expected `O(R)` time with hash aggregation and `O(D)` grouping memory.

The result contains `D` rows and must be ordered by date. If the engine performs an explicit comparison sort, that step costs `O(D log D)` time and `O(D)` working or result space. Together, the usual bound is `O(R + D log D)` time and `O(D)` space, matching the manifest.

As with all SQL, the optimizer chooses the physical execution plan. An index ordered by `sale_date` may let the engine aggregate or emit groups in order and reduce explicit sorting work. A sort-based aggregation may combine grouping and ordering. Conversely, limited memory may cause temporary disk use. The stated complexity captures the conventional in-memory scan, group, and sort strategy exposed by the query.

The `IF` condition, sign negation, and addition are constant work per row. The primary key prevents duplicate date-fruit records but does not eliminate the need to read all `R` rows because every quantity affects its date's result.

## Alternatives and edge cases

- **SUM with CASE WHEN:** `SUM(CASE WHEN fruit = 'apples' THEN sold_num ELSE -sold_num END)` expresses the same signed aggregation in standard SQL style. The stored query uses MySQL's shorter `IF` function.
- **Explicit orange test:** A defensive version can return `-sold_num` only for oranges and zero for any other fruit. That is useful in a broader schema, but the problem guarantees exactly the relevant categories.
- **Self-join by date:** Join an apples alias to an oranges alias and subtract their quantities. It is intuitive, but it references the table twice and can lose dates if one category is missing unless outer joins and null handling are added.
- **Separate filtered subqueries:** Build one apple relation and one orange relation, then join on `sale_date`. This makes the two values visually explicit but is more machinery than conditional aggregation needs.
- **Pivot-style aggregation:** Compute separate conditional sums for apples and oranges and subtract them afterward. It generalizes well when both category totals must also be displayed, but the requested output needs only their difference.
- **Equal daily sales:** Positive and negative contributions cancel, yielding zero rather than a missing row.
- **More oranges than apples:** The result is negative. Applying `ABS` would be wrong because the requested difference is directional.
- **Zero sold quantity:** A zero contributes nothing but its date still belongs to a group and must appear in the result.
- **Only an apples row on a date:** The query returns the apple quantity, effectively subtracting zero. This is sensible even if the dataset does not require missing categories.
- **Only an oranges row on a date:** Its signed contribution produces a negative difference, again behaving as if missing apple sales were zero.
- **Unexpected fruit outside the contract:** The false branch would subtract it. The solution intentionally relies on the schema guarantee that rows describe apples or oranges only.
- **Duplicate category rows outside the contract:** `SUM` would total them correctly by category sign, although their presence would violate the declared composite primary key.
- **Chronological ordering:** Sorting the `date` value directly gives chronological order. Sorting a custom display string could produce a different order and is unnecessary.
- **Ordinal references:** `GROUP BY 1` and `ORDER BY 1` both mean `sale_date` only because it is the first selected expression. Reordering the `SELECT` list would require updating those ordinals.
- **Exact output name:** `AS diff` supplies the required result-column name. Omitting or changing the alias could make an otherwise correct calculation fail the expected schema.
- **No recorded rows:** The aggregate query produces no date groups and therefore an empty result. It does not invent calendar dates absent from `Sales`.
