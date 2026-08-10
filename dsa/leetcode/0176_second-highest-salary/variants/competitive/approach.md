## General

**First alternative: remove the maximum and aggregate again**

The competitive file's first query contains two nested maximum operations.
The deepest subquery:

`SELECT MAX(Salary) FROM Employee`

returns the highest salary. The middle aggregate scans employees whose salary
is not that value:

`SELECT MAX(Salary) FROM Employee WHERE Salary NOT IN (...)`.

Among all values below the maximum, their maximum is exactly the second-highest
distinct salary. Repeated maximum rows are all excluded by value, and duplicate
rows at the second salary do not matter because `MAX` returns their shared
value once.

**Why the aggregate returns null when needed**

SQL aggregate `MAX` over an empty qualifying set returns `NULL` while still
producing one aggregate row.

If all employees have the same salary, excluding the maximum leaves no
candidate. The middle `MAX` is null. If the table is empty, the inner maximum
is also null and no row qualifies; the aggregate still yields null.

The outer scalar `SELECT (...) SecondHighestSalary` preserves a single row and
assigns the required alias. This outer layer is redundant for row-count
purposes because the middle aggregate already returns one row, but it does not
change the value.

**Why distinctness is implicit in the first alternative**

The query never writes `DISTINCT`. It does not need to: all occurrences equal
to the global maximum are filtered out, and taking `MAX` of the remainder
chooses the next lower value regardless of how many employees share it.

For salaries `[300,300,200,200,100]`, the inner maximum is 300. Filtering
removes both 300 rows. The maximum remaining salary is 200.

**Second alternative: group, order, and offset**

After the comment `# or`, the file includes another query:

`SELECT Salary FROM Employee GROUP BY Salary ORDER BY Salary DESC LIMIT 1,1`.

`GROUP BY Salary` creates one group per salary value, playing the same
deduplication role as `DISTINCT`. Descending order ranks the groups. MySQL
`LIMIT 1,1` skips the highest group and takes the next one.

Wrapping this query as a scalar expression makes an empty offset result become
`NULL`, and the alias again names the output column correctly.

Both alternatives compute the same result on ordinary non-null salary data,
but they use different relational plans.

**Material packaging defect**

The exact `solution.sql` contains both complete `SELECT` statements separated
by a semicolon, with a MySQL hash comment between them. A typical LeetCode-style
judge expects one statement and one result set.

Depending on the execution harness, multiple statements may be rejected,
disabled for security, or produce two result sets when only one is expected.
Therefore the file is not a clean single-query submission as stored. One
alternative must be selected and the other removed or kept outside the
executable solution.

This issue is independent of whether each individual query is logically
correct.

**`NOT IN` and null semantics**

SQL comparisons involving null use three-valued logic. If the global maximum
subquery yields null, `Salary NOT IN (NULL)` is unknown for every row, leaving
an empty candidate set; the aggregate then returns null, which is appropriate
for an empty table.

If actual salary rows may be null, `MAX` ignores them. The intended classic
dataset treats salaries as numeric values, but a production query should state
whether null salary rows are excluded. Using
`Salary < (SELECT MAX(Salary) ...)` communicates the below-maximum condition
more directly than `NOT IN` for a single scalar.

**Why the first alternative is sound**

If at least two distinct numeric salary levels exist, removing every row at
the greatest level leaves a nonempty set. Its maximum is below the original
maximum and no other lower salary exceeds it, so it is second highest.

If fewer than two levels exist, the remaining set is empty and `MAX` yields the
required null. The alias and scalar outer select produce exactly the desired
one-column schema.

## Complexity detail

Let $n$ be the employee count. The nested-aggregate alternative may scan
`Employee` twice, which is $O(n)$ total asymptotic row work and constant
aggregate state in a straightforward plan. A salary index can improve access.

The group-and-order alternative may require $O(n)$ grouping work, $O(u\log u)$
sorting time, and $O(u)$ state for $u$ distinct salaries.

Thus the manifest's $O(n)$ time and $O(1)$ space plausibly describe the first
aggregate plan, not every engine or the second query. Physical SQL cost remains
optimizer- and index-dependent.

## Alternatives and edge cases

- **Keep only the nested `MAX` query:** It is the cleaner choice from this file for linear scan and constant aggregate state.
- **Keep only the grouped offset query:** Also correct in MySQL, but may require sorting distinct groups.
- **`DENSE_RANK`:** Assign rank two to the second distinct salary with a window function.
- **One salary level:** Both scalar alternatives yield null.
- **Duplicate highest salaries:** The first query removes all of them by value.
- **Duplicate second salaries:** `MAX` or grouping still returns one scalar value.
- **Empty table:** Aggregate semantics produce null.
- **Multiple statements:** The exact file should not submit both alternatives to a single-statement judge.
- **Hash comments:** `#` is MySQL-specific comment syntax.
- **Nullable salaries:** Explicit filtering may be needed if the data contract permits them.
