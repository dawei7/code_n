## General

**Treat the file as two competing queries, not one program**

The competitive source contains two complete `SELECT` statements placed one
after another without a separating semicolon. They are alternative solutions
to the same problem. They do not form a pipeline, common table expression, or
union. In the expected single-statement submission interface, keeping both in
this form causes a syntax error when the parser reaches the second `SELECT`.

The algorithms should therefore be understood separately. The first builds a
table of department maxima and joins back to employees. The second recomputes
or looks up a maximum through a correlated subquery. A usable submission must
choose exactly one of them.

**First alternative: materialize the maximum relation**

The innermost subquery groups `Employee` by `DepartmentId` and computes
`MAX(Salary) AS Salary`. It yields one row per populated department containing
the department ID and that department's highest salary.

That aggregate is joined with `Department` on matching IDs. The resulting
derived table `d` contains three useful fields: `DepartmentId`, the readable
department name under alias `Department`, and the maximum salary under alias
`Salary`. At this point the query knows each department's threshold but not
which employees attain it.

The outer join connects `Employee e` to `d` with two conditions:
`e.DepartmentId = d.DepartmentId` and `e.Salary = d.Salary`. The first prevents
a salary from one department from qualifying an employee in another. The
second keeps only employees at the computed maximum.

Because the join is equality-based and employee rows are not grouped, every
tie survives. If Jim and Max both earn 90000 in IT, both independently match
the same maximum row and both are returned.

**Second alternative: compare with a correlated maximum**

The second statement first joins every employee with the matching department
to obtain its display name. For each outer employee, the subquery examines
`Employee e` rows whose `e.DepartmentId` equals the current outer
`Employee.DepartmentId`, then returns `MAX(e.Salary)`.

The outer condition uses `Employee.Salary IN (subquery)`. Since this aggregate
subquery returns exactly one value for a populated department, `IN` acts like
equality with that maximum. Any employee whose salary equals it survives;
others are removed.

The correlation is what keeps departments separate. Without the correlated
department predicate, the subquery would compute one global maximum and omit
the leaders of every lower-paying department.

**Trace both forms on the sample**

Grouping creates the maximum rows `(1, 90000)` and `(2, 80000)`. In the first
query, Jim and Max match the first row and Henry matches the second. Joe and
Sam fail the salary part of the join.

In the second query, the correlated maximum seen by each IT employee is 90000,
and the one seen by each Sales employee is 80000. The same three employees
pass. Both approaches therefore produce the Reference's result set when run
individually.

**Why the first query returns exactly all top earners**

Every row returned by the first query matches a grouped maximum row on both
department ID and salary. It cannot belong to the wrong department, and its
salary cannot be below that department's maximum.

Conversely, every employee at a department maximum matches the aggregate row
created for that department. Equality on both join fields succeeds, so the
employee is preserved. This two-field join is the key reason ties are complete
and cross-department salary coincidences are harmless.

**Why the second query has the same result**

For an outer employee, the correlated aggregate considers exactly the rows in
that employee's department. Its single result is the greatest salary in that
set. The outer employee passes if and only if its salary equals that greatest
value. Thus the predicate is precisely the definition of “has the highest
salary in the department.”

**Names and aliases are presentation, not identity**

Both statements join with numeric department IDs and compare numeric salaries.
Department and employee names are selected only for display, so repeated names
do not confuse the grouping or matching logic. The aliases `Department`,
`Employee`, and `Salary` match the requested output headings.

Neither statement has `ORDER BY`, correctly respecting the any-order contract.
A stable-looking plan order is incidental and should never be relied upon.

**Reconcile the source complexity note with real plans**

The source comments state $O(n^2)$ time. That is plausible for the correlated
form if the engine scans the employee table again for every outer employee.
It is not inherent to the first form: grouping once and joining through hash
tables or indexes can avoid repeated full scans. Modern optimizers may also
decorrelate the second form into a grouped join.

Therefore, the manifest's $O(n\log n)$ sort-based bound describes an efficient
execution of the relational task, while the comment describes a pessimistic
naive path. Neither can be guaranteed solely from SQL text.

## Complexity detail

Let $n$ be the number of employees and $m$ the number of departments. The
first alternative can group employees by sorting in $O(n\log n)$ time, then
perform its joins in $O(n + m)$ expected time with suitable hash structures.
Its working storage is $O(n + m)$, reported as $O(n)$ in the manifest's total
input-size convention.

A naive correlated execution of the second alternative may scan up to $n$
employees for each of $n$ outer employees, reaching $O(n^2)$ time. Indexing or
decorrelation can reduce that cost to the same broad class as the first query.
Actual database complexity depends on the chosen physical plan.

## Alternatives and edge cases

- **Submit one alternative only:** The adjacent statements are not valid as one LeetCode SQL answer and must not both remain executable.
- **Derived maximum join:** The first stored query computes each threshold once and makes both join keys explicit.
- **Correlated maximum:** The second is concise but can repeat work on a naive engine.
- **Tuple membership:** Compare `(departmentId, salary)` with grouped maximum pairs, as the optimal variant does.
- **Window ranking:** `DENSE_RANK()` partitioned by department naturally keeps every rank-one tie.
- **Equal maximum salaries:** Return every tied employee rather than selecting one arbitrary name.
- **Same salary across departments:** Department ID must participate in the comparison.
- **Department without employees:** No row is returned because no employee can attain a maximum there.
- **Single employee:** That employee matches the department's own maximum.
- **Repeated display names:** IDs determine relationships; names do not need to be unique.
- **Any order:** Neither alternative needs sorting for presentation.
