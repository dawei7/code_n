## General

**Turn a one-based rank into a row offset**

The requested rank `N` begins at one: the highest distinct salary has rank one,
the next distinct level has rank two, and so on. MySQL offset positions begin
at zero.

The function therefore executes `SET N = N - 1`. After that assignment, `N`
is the number of distinct salary rows to skip in descending order.

For an original request of two, the stored offset becomes one. Skipping the
single highest distinct salary exposes the second highest.

**Remove employee-level duplicates before ranking**

The inner query selects `DISTINCT salary`. This collapses employees with the
same salary into one rank level.

Without `DISTINCT`, two employees earning the maximum could occupy the first
two ordered rows and cause rank two to return the maximum again. The task ranks
salary values, not employee records.

`ORDER BY salary DESC` then places the largest distinct value first, followed
by the second largest and so forth.

**Select exactly the requested row**

`LIMIT 1 OFFSET N` asks for one row after skipping `N` rows. Since `N` has
already been decremented, this row corresponds to the original one-based rank.

Inside a stored MySQL routine, a local parameter or variable can be used as the
limit offset. The positive-rank contract ensures the decremented value is
nonnegative.

The ordering must occur before the offset is meaningful. Without `ORDER BY`,
row position is unspecified and would not represent salary rank.

**Use scalar subqueries to produce null**

The distinct ordered query is nested inside:

`SELECT (SELECT ...)`.

The innermost query returns at most one salary. If the requested offset exists,
its scalar value is selected. If fewer than the original `N` distinct salaries
exist, the inner scalar subquery has no row and evaluates to SQL `NULL`.

The enclosing `SELECT` still produces one scalar row. The stored function's
`RETURN (...)` then returns that integer or null.

This matters because a bare row query with an out-of-range offset would return
an empty table, while the function contract needs a scalar null.

**Trace a normal request**

With distinct salaries 100, 200, 300 and original `N = 2`, the function changes
`N` to one. Descending order is 300, 200, 100. The query skips 300, takes 200,
and returns it.

If salaries are `[500,500,300,200]` and `N = 2`, distinctness first produces
500, 300, 200. The offset still returns 300. Duplicate employees at 500 do not
consume extra ranks.

For `N = 1`, the offset becomes zero, so no row is skipped and the maximum
distinct salary is returned.

**Trace a missing rank**

If only salary 100 exists and the request is two, the function skips its one
distinct ordered row. No row remains. The scalar subquery evaluates to null,
which the function returns.

The same applies to an empty employee table for any positive rank.

**Why the result has the correct dense rank**

After `DISTINCT`, every salary level appears once. Descending order means
exactly `N - 1` greater distinct values precede the row at offset `N - 1`.
Therefore the selected value has dense descending rank `N`.

If no such row exists, there are fewer than `N` distinct salary levels, exactly
the condition requiring null.

**Function name determines the output label**

The database function is named `getNthHighestSalary`. Native evaluation calls
that function with `N`; the displayed result column may include the call text,
such as `getNthHighestSalary(2)`, even though the inner scalar query does not
write an alias.

**Dialect and null considerations**

The source uses MySQL stored-function and `LIMIT ... OFFSET` syntax. Other
engines use different function bodies or window functions.

If actual salary values can be SQL null, `DISTINCT` retains a null group and
MySQL places it after numeric salaries in descending order. Classic challenge
data treats salaries as numeric values; a production contract should explicitly
decide whether to exclude null with `WHERE salary IS NOT NULL`.

## Complexity detail

Let $n$ be the employee count and $u$ the number of distinct salaries. A
straightforward plan deduplicates rows and sorts $u$ values in
$O(n+u\log u)$ time, which is $O(n\log n)$ worst case.

Materializing or sorting distinct salaries can use $O(u)=O(n)$ working space.
These bounds match the manifest. A descending salary index and optimizer
support may reduce physical work, but query text alone does not guarantee that
plan.

## Alternatives and edge cases

- **`DENSE_RANK`:** Assign descending dense ranks and select rank `N`; it directly states the ranking intent.
- **Correlated greater-count:** A salary has rank `N` when exactly `N - 1` distinct salaries are greater, but naive execution is quadratic.
- **Repeated maximum:** `DISTINCT` gives it only rank one.
- **`N = 1`:** Zero offset returns the maximum salary.
- **Too-large `N`:** The scalar subquery returns null.
- **Empty table:** Also returns null.
- **One-based conversion:** Decrement exactly once before applying the offset.
- **Ordering:** Descending order is essential to rank highest first.
- **Nullable salaries:** Define or filter their policy if the schema permits them.
- **MySQL routine syntax:** Porting requires adapting the function declaration and limit-variable form.
