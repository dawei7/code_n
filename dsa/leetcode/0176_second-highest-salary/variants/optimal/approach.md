## General

**Rank distinct salary values**

The word **distinct** changes the problem. If the highest salary appears for
several employees, those rows still represent only one salary level. The
second output must be the next lower value, not the second employee row after
sorting.

The inner query first selects `DISTINCT salary`, collapsing all equal salary
values into one row. It then orders those values from largest to smallest.

After these two relational operations, row zero is the highest distinct salary
and row one is the second highest.

**Use MySQL offset-and-count syntax**

`LIMIT 1, 1` is MySQL's comma form:

`LIMIT offset, row_count`.

The first one skips one row—the highest salary. The second one requests at most
one row after that skip. It is equivalent to `LIMIT 1 OFFSET 1`.

For salaries 100, 200, and 300, the ordered distinct inner rows are 300, 200,
100. Skipping one and taking one yields 200.

For salaries 300, 300, and 200, `DISTINCT` produces 300 and 200 before the
limit. The result is again 200 rather than another 300.

**Wrap the result as a scalar subquery**

The outer query selects:

`(inner query) AS SecondHighestSalary`.

A scalar subquery used as an expression has special empty-result behavior. If
it returns one row, that row's value becomes the expression. If it returns no
rows, the expression evaluates to SQL `NULL`.

This is how the source meets the “exactly one row” requirement. Writing only
the inner `SELECT DISTINCT ... LIMIT 1,1` would return an empty result table
when fewer than two distinct salaries exist. Wrapping it causes the outer
`SELECT`—which has no `FROM` clause—to emit one row whose expression is null.

The alias gives that one column the exact required name
`SecondHighestSalary`.

**Trace the missing-answer case**

For a table containing only salary 100, the distinct ordered set has one row.
The offset skips it, leaving no row for the inner query. The scalar subquery
therefore evaluates to `NULL`, and the outer query returns:

`SecondHighestSalary = NULL`.

The same logic handles an empty `Employee` table: no second value exists, so
the inner result is empty and the scalar expression is null.

This is different from the text `"null"` and from zero. SQL `NULL` is the
database marker for an absent value.

**Why every returned non-null value is correct**

`DISTINCT` ensures each salary level appears once. Descending order places
exactly one distinct value—the maximum—before the desired one. The offset
removes that maximum, and the row-count limit selects the greatest remaining
value.

Therefore any non-null returned salary is lower than the maximum and at least
as large as every other lower distinct salary: it is exactly second highest.
If no such value exists, scalar empty-result semantics produce null.

**Ordering is internal, not an output-order promise**

`ORDER BY salary DESC` determines which row the offset selects inside the
subquery. It is logically necessary even though the outer result has only one
row.

Without this ordering, “second” would depend on an unspecified physical row
order and would have no connection to salary rank.

**Consider SQL null salary values**

The local schema calls `salary` an integer but does not explicitly state a
`NOT NULL` constraint. `DISTINCT` can retain one null value, and MySQL sorts
null after numeric values in descending order.

The classic challenge data normally treats employee salaries as actual numeric
values. If nullable salaries were allowed, the desired policy should be stated:
most interpretations would exclude them with `WHERE salary IS NOT NULL` before
ranking. The selected source does not add that unstated rule.

**Dialect dependency**

The comma form of `LIMIT` is MySQL syntax, matching the template comment.
Other database engines may prefer `OFFSET ... FETCH`, `LIMIT ... OFFSET`, or a
window function.

## Complexity detail

Let $n$ be the employee-row count and $u$ the number of distinct salaries.
Without a supporting salary index, deduplication and descending ordering can
require $O(n)$ input processing plus $O(u\log u)$ sorting time and $O(u)$
working space.

With a suitable index, an optimizer may scan distinct salary keys in descending
order and stop early, changing the physical cost. The manifest's $O(n)$ time
and $O(1)$ space are therefore not guaranteed by the query text; database
complexity depends on indexes and the selected execution plan.

## Alternatives and edge cases

- **Maximum below the maximum:** Select `MAX(salary)` where salary is less than the global `MAX(salary)`. This naturally returns one null aggregate row when no candidate exists.
- **`DENSE_RANK`:** Rank distinct salary levels and select rank two; portable across modern SQL engines but may require similar sorting.
- **`IFNULL` wrapper:** Can turn an empty scalar result into null explicitly, though a scalar subquery already does so.
- **Duplicate maximum:** `DISTINCT` prevents it from occupying both rank positions.
- **One distinct salary:** The inner query is empty after offset and the outer row contains null.
- **Empty table:** Produces the same one-row null result.
- **Column alias:** Must be exactly `SecondHighestSalary`.
- **Descending order:** Required before applying the offset.
- **Nullable salary:** A production query should define whether nulls are excluded.
- **Physical cost:** Indexes and optimizer strategy determine whether an explicit sort is needed.
