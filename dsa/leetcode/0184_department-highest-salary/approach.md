## General

**Separate the problem into a threshold and the rows meeting it**

For each department, the query must first determine one value: the greatest
salary among that department's employees. It must then return every employee
whose salary equals that value. These are distinct operations because an
aggregate such as `MAX(salary)` produces the maximum value but does not by
itself preserve all employee rows tied at that maximum.

The stored query expresses the two operations with a grouped subquery followed
by a tuple-membership filter. This is especially important for ties. Selecting
an arbitrary employee beside `MAX(salary)` could lose another employee who has
the same top salary.

**Compute one maximum per department**

The inner query reads `Employee`, groups rows by `departmentId`, and selects
the group key together with `MAX(salary)`. Its conceptual result contains
pairs of the form:

`(department ID, that department's maximum salary)`

`GROUP BY 1` means “group by the first expression in this select list,” which
is `departmentId`. The positional syntax is valid MySQL, though spelling out
`GROUP BY departmentId` would be easier to maintain if the select-list order
later changed.

For the example, department 1 produces `(1, 90000)` and department 2 produces
`(2, 80000)`. There is one pair per department represented in `Employee`.

**Join employees to their department names**

The outer query joins `Employee AS e` to `Department AS d` using
`e.departmentId = d.id`. This converts the numeric foreign key into the human
readable department name required by the output.

An inner join is appropriate. The Reference says `departmentId` refers to the
department table, so every valid employee has a matching department. A
department with no employees contributes no employee row and therefore should
not appear in a result about highest-paid employees.

**Match both department and salary together**

The filter tests whether `(d.id, salary)` belongs to the subquery's set of
maximum pairs. Comparing a pair rather than salary alone is essential. A
salary of 90000 might be the maximum in IT but an ordinary salary in another
department whose maximum is higher. Pair membership requires the salary to be
maximal for this employee's own department.

Although `salary` is unqualified in the stored query, it is unambiguous because
only `Employee` supplies that column in the outer join. Writing `e.salary`
would make the ownership more explicit without changing the result.

**Trace the example and preserve ties**

The maximum-pair set is `{(1, 90000), (2, 80000)}`. Joe's pair `(1, 70000)`
is absent, while Jim's `(1, 90000)` is present. Henry's `(2, 80000)` is
present, and Sam's `(2, 60000)` is absent. Max has the same qualifying pair as
Jim, so Max is also retained.

This shows why the result can contain multiple rows for one department. The
question asks for employees who have the highest salary, not for exactly one
representative per department. Grouping happens only inside the threshold
subquery; the outer employee rows remain separate.

**Why every returned employee is valid**

If an employee is returned, that employee's `(department, salary)` pair
matches a pair emitted by the grouped subquery. The second component of the
emitted pair is the maximum salary for the first component, so the employee's
salary is the department maximum.

Conversely, take any employee tied at the maximum in a department. The inner
group for that department emits exactly that employee's department ID and
salary. The tuple membership test therefore succeeds, and the join supplies
the department name. No top-paid employee can be lost, including ties.

**Project the requested three columns**

The query returns `d.name`, `e.name`, and `salary`, with aliases `department`
and `employee` for the first two. The Reference displays `Department`,
`Employee`, and `Salary`. MySQL treats identifiers without case sensitivity in
ordinary query resolution, but some clients preserve the alias's display
case. Exact presentation-sensitive consumers may prefer aliases whose letter
case exactly matches the Reference.

Employee or department names need not be unique for the reasoning to work.
All matching is based on primary and foreign keys; names are projected only
after the qualifying rows are identified.

**Result order and numeric boundaries**

No `ORDER BY` is included because any order is accepted. Negative, zero, or
equal salaries would not require a different algorithm: `MAX` and equality
still identify the greatest value within each group. A single-employee
department naturally returns that employee because its only salary is also
its maximum.

## Complexity detail

Let $n$ be the number of employee rows and $m$ the number of departments. A
sort-based grouping step costs $O(n\log n)$ time and can use $O(n)$ working
space. Joining employees to departments and testing the maximum pairs can be
implemented with hashes in $O(n + m)$ expected additional time. The dominant
bound is therefore $O(n\log n)$ time with $O(n + m)$ working space, commonly
reported as the manifest's $O(n)$ space when departments are bounded by or
included in input size $n$.

A database optimizer may instead use hash aggregation, indexes, or transform
tuple membership into joins, giving expected linear behavior on favorable
plans. SQL states the relational computation rather than prescribing one
physical algorithm, so actual cost depends on indexes, statistics, and engine.

## Alternatives and edge cases

- **Join to a derived maximum table:** Group `(departmentId, MAX(salary))`, then join employees on both fields; equivalent and often more explicit than tuple `IN`.
- **Correlated maximum subquery:** Compare each salary with its department's maximum; concise, but a naive plan can repeat scans.
- **Window function:** Use `DENSE_RANK()` or `MAX() OVER (PARTITION BY departmentId)` and keep top rows; clear tie handling on engines supporting windows.
- **Pandas transform:** The local editorial joins names, broadcasts each group's maximum with `transform('max')`, and filters equal salaries.
- **Tied maximum:** Return every tied employee, never an arbitrary single row.
- **One employee in a department:** That employee is automatically highest.
- **Department with no employees:** Produce no row because there is no employee to report.
- **Duplicate names:** Keys, not names, determine membership, so identical display names remain distinct employee rows.
- **Positional grouping:** `GROUP BY 1` depends on select order; explicit grouping is safer during maintenance.
- **Any order:** The absence of `ORDER BY` is intentional.
