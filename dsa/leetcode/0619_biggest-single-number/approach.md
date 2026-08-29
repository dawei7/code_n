## General

**“Single” describes frequency, not mathematical uniqueness.** A number qualifies only if it occurs in exactly one input row. The largest distinct value is not necessarily a single number: a very large number that appears twice must be rejected. The query therefore calculates occurrence counts before it calculates the maximum.

**The inner query forms one group per value.** `GROUP BY 1` groups by the first selected expression, which is `num`. All rows with the same number enter the same group. `COUNT(1)` counts the rows in that group because the literal `1` is non-null for every row.

The condition

`HAVING COUNT(1) = 1`

retains only groups containing exactly one row. `HAVING` is the correct clause because the count does not exist until after grouping. A `WHERE` condition cannot filter on an aggregate count at the same query level.

For input `8, 8, 3, 3, 1, 4, 5, 6`, the groups for `8` and `3` have count 2 and are removed. The groups for `1`, `4`, `5`, and `6` each have count 1, so the derived table `t` contains those four values.

**The outer aggregate chooses the largest survivor.** `SELECT MAX(num) AS num FROM (...) AS t` computes the maximum over the filtered set. The alias preserves the required output column name `num`.

The two levels solve two different questions:

1. inner grouping asks, “Which values occur exactly once?”
2. outer `MAX` asks, “Which of those qualifying values is greatest?”

Combining these concepts in the wrong order would fail. Taking `MAX(num)` from the original table and then checking its frequency would return no smaller answer when the largest value is duplicated, even though a lower single number might exist.

**Why the query returns one row even when nothing qualifies.** An aggregate query without `GROUP BY` returns one aggregate row over its entire input. If the derived table is empty, SQL defines `MAX` over that empty set as `NULL`. This exactly matches the requirement to report null when no single number exists. Using `ORDER BY num DESC LIMIT 1` on the derived table would instead return zero rows unless extra handling were added.

**Why the answer is correct.** Every value entering `t` has a group count of one, so every candidate is a single number. Every single number has exactly one source row, so its group passes the `HAVING` condition and enters `t`. Thus `t` contains all and only the single numbers. If it is nonempty, `MAX` returns its greatest member, which is the requested answer. If it is empty, there is no single number and `MAX` returns the required `NULL`. These two cases cover every input.

**Understand the ordinal syntax.** `GROUP BY 1` means “group by the first select-list item,” not “put every row into the constant group 1.” MySQL resolves that ordinal to `num` here. Writing `GROUP BY num` is more explicit and resilient if the select list changes, but the exact source is valid.

The same is true of `COUNT(1)` versus `COUNT(*)` in this schema. Both count rows, including a row whose `num` might be null, because neither depends on `num` being non-null. `COUNT(num)` would ignore null values and therefore has different behavior if nulls are permitted.

## Complexity detail

Let $R$ be the number of rows in `MyNumbers` and $U$ the number of distinct values. A sort-based grouping plan orders the rows by `num`, costing $O(R\log R)$ time, and then scans the groups. A hash aggregation can achieve expected $O(R)$ time. The outer `MAX` scans at most $U$ qualifying group rows, which is dominated by the grouping cost. The manifest's conservative, engine-independent time bound is $O(R\log R)$.

A hash grouping table can store one count for each distinct number, using $O(U)$ space and therefore $O(R)$ in the worst case. A sort-based engine similarly uses temporary sorting storage up to linear size, possibly spilling it to disk. The outer maximum needs only one running value, so it adds $O(1)$ working state. These observations match the manifest's $O(R)$ space bound.

The final result size is always exactly one row. That output size does not change even when every input number is single, because the outer aggregate reduces all qualifying groups to one value.

## Alternatives and edge cases

- **Sort descending and test counts:** Group values with their counts, sort qualifying groups by `num DESC`, and take the first. This can find the same value but needs special handling to return one `NULL` row when no group qualifies.
- **Correlated frequency subquery:** Filter each row where a subquery counts one matching value, then take `MAX`. It is readable but can repeat work without effective optimization.
- **Window count:** Attach `COUNT(*) OVER (PARTITION BY num)` to every row, filter count 1, and aggregate the maximum. This avoids a grouped derived table but usually carries more repeated rows through the plan.
- **All values duplicated:** The inner query is empty, and outer `MAX` correctly returns one row containing `NULL`.
- **Exactly one row:** Its group count is one, so that value is returned.
- **Negative numbers:** `MAX` still means the greatest numeric value; for example, `-2` is greater than `-7`.
- **Largest raw value duplicated:** It is removed before `MAX`, allowing a smaller qualifying value to win.
- **Many copies of one value:** Its group still occupies one aggregate entry and fails because its count is greater than one.
- **Null input value:** The statement describes integers but does not explicitly state nullability. `COUNT(1)` would treat one null row as a size-one group, while outer `MAX(num)` ignores null and returns `NULL`; this is indistinguishable from no qualifying numeric value. If null semantics mattered, they should be specified explicitly.
- **`GROUP BY 1` maintainability:** It is concise but positional. `GROUP BY num` communicates intent more directly and cannot silently change meaning after select-list reordering.
