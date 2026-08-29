## General

**Understand what “top three unique salaries” counts**

An employee is a high earner when the employee's salary is one of the three
largest distinct salary values in that employee's department. The word
“unique” changes the ranking rule. If two employees both earn 85000, that value
occupies one salary level, not two positions. Both employees must receive the
same effective rank.

A convenient way to determine the rank of a salary $s$ is to ask how many
distinct salaries in the same department are strictly greater than $s$. If
that count is zero, $s$ is the highest unique salary. If it is one, $s$ is the
second-highest; if it is two, $s$ is the third-highest. Therefore, the employee
qualifies exactly when the count is less than three.

**Build each employee's department context**

The outer query reads `Employee` and `Department` with comma-style join syntax.
The condition `Employee.DepartmentId = Department.Id` turns that Cartesian
product into an inner equijoin. It associates every employee with the readable
department name required in the result.

Modern SQL usually writes this as an explicit `INNER JOIN ... ON ...`. The two
forms have the same relational meaning here, but explicit join syntax makes it
harder to forget the matching condition and accidentally create every possible
employee-department pair.

**Correlate the count with the current employee**

For each outer `Employee` row, the subquery scans another logical copy of the
employee table named `e2`. Its first predicate, `e2.Salary > Employee.Salary`,
keeps only salaries strictly greater than the current salary. Its second
predicate, `Employee.DepartmentId = e2.DepartmentId`, restricts the comparison
to the current employee's own department.

Both predicates are indispensable. Replacing `>` with `>=` would count the
current salary level and shift every rank by one. Omitting the department
condition would compare against the whole company and incorrectly suppress
leaders in departments whose salaries are lower than another department's.

**Count values rather than employees**

The aggregate is `COUNT(DISTINCT e2.Salary)`. `DISTINCT` ensures that several
higher-paid employees with the same salary contribute only one higher salary
level. Without it, ties above the current employee would consume multiple
positions and could wrongly push a true top-three salary out of the result.

For example, suppose three coworkers all earn 90000 and another earns 85000.
Only one distinct salary is greater than 85000, so 85000 is the second unique
salary and must qualify. A plain row count would report three greater rows and
incorrectly reject it.

**Apply the threshold**

The outer condition keeps the employee when the correlated count is `< 3`.
Counts zero, one, and two correspond to unique-salary ranks one, two, and
three. A count of three means at least three distinct salary values are higher,
so the current value is fourth or lower and must be excluded.

This count-based definition also handles departments with fewer than three
unique salaries. Every salary in such a department has fewer than three levels
above it, so every employee qualifies, exactly as the sample's two-person Sales
department demonstrates.

**Trace the IT department**

IT has distinct salaries 90000, 85000, 70000, and 69000. Max at 90000 has zero
greater distinct values. Joe and Randy at 85000 each see only 90000 above them,
so both have count one. Will at 70000 sees 90000 and 85000, giving count two.
Janet at 69000 sees three greater values and is rejected.

The result therefore includes four IT employees even though only three unique
salary levels qualify. This is not an off-by-one error; ties expand the number
of employee rows while preserving exactly three salary levels.

**Why the filter is exact**

If an employee is returned, fewer than three distinct salaries in that
department are greater. The employee's salary can therefore be no lower than
the third-highest distinct value, so it is in the required set.

Conversely, if a salary is among the department's top three distinct values,
at most two distinct values can be greater. The subquery returns zero, one, or
two, the `< 3` condition succeeds, and every employee at that salary is
returned. The reasoning covers both ordinary rows and ties.

**Projection and source guarantees**

The query projects the department name as `Department`, the employee name as
`Employee`, and the salary as `Salary`. Relationships and comparisons use IDs
and numeric salaries, so duplicate department names would not mix groups. The
Reference also rules out two rows with the exact same name, salary, and
department, though this algorithm does not need that promise for ranking.

No `ORDER BY` appears because any result order is accepted. A database's
observed scan order is not contractual.

**Nullable values would require an explicit policy**

The intended data treats employees as having a department and salary. If an
outer salary were `NULL`, every `e2.Salary > Employee.Salary` comparison would
be unknown, the count would be zero, and the row could incorrectly qualify.
Similarly, an employee with no matching department is removed by the inner
join. If nullable salary or department references were legal, the query would
need guards and the problem would need to define their ranking semantics.

## Complexity detail

Let $n$ be the number of employees and $m$ the number of departments. Read
literally, the correlated subquery may inspect up to $n$ rows for each of $n$
outer employees, giving $O(n^2)$ time. Maintaining each `DISTINCT` count may
also require a temporary set or sort. This is a material qualification: the
exact source does not itself guarantee the manifest's $O(n\log n)$ time.

A capable optimizer can decorrelate the predicate, precompute salary levels,
or exploit an index on `(DepartmentId, Salary)`. Such a plan can sort or rank
once in $O(n\log n)$ time and use $O(n + m)$ working space, conventionally
reported as the manifest's $O(n)$ space. Actual SQL complexity depends on the
engine and plan; $O(n\log n)$ is the intended optimized bound, while $O(n^2)$
remains possible for naive correlated execution.

## Alternatives and edge cases

- **`DENSE_RANK()` window function:** Partition by department, order salary descending, and retain ranks at most three; this directly models unique salary levels.
- **Distinct salary table:** Deduplicate department-salary pairs, choose the top three per department, then join back to all employees so ties survive.
- **Pandas dense rank:** The local editorial uses descending dense rank within each department and filters values at most three.
- **Plain `COUNT(*)`:** Incorrect when several higher-paid employees share a salary because it ranks people instead of unique salary values.
- **Strict comparison:** Use `>`; `>=` would count the current salary level and cause an off-by-one error.
- **Ties at any qualifying level:** Return every tied employee.
- **Fewer than three unique salaries:** Return every employee in that department.
- **Same salary in different departments:** The correlation must include `DepartmentId`.
- **Nullable salary:** The stored comparison does not define a safe null ranking and may admit nulls incorrectly.
- **Any order:** No output sorting is required.
