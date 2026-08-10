## General

**Convert dense rank into a counting question**

The competitive query does not assign a rank column explicitly. Instead, for
each employee, it counts how many distinct salary values in the same department
are greater than that employee's salary. This count is exactly one less than
the salary's descending dense rank.

The mapping is simple: zero greater values means rank one, one greater value
means rank two, and two greater values means rank three. The query therefore
keeps rows whose count is below three. This formulation naturally returns more
than three employees when several people tie at a qualifying salary, which is
required because the limit applies to unique salary values rather than people.

**Join employee rows to department names**

`Employee E INNER JOIN Department D ON E.DepartmentId = D.Id` associates each
employee with the department's display name. The inner join is appropriate for
the stated foreign-key relationship: a valid employee belongs to an existing
department.

The aliases `E` and `D` distinguish the two `Name` columns. The final projection
uses `D.Name AS Department`, `E.Name AS Employee`, and `E.Salary AS Salary`,
which produces the required three-column shape.

**Evaluate the correlated subquery for one employee**

Inside the `WHERE` clause, the unaliased inner `Employee` table is a separate
logical scan from outer alias `E`. `DepartmentId = E.DepartmentId` keeps only
coworkers of the current employee. `Salary > E.Salary` keeps only salary values
strictly greater than the current salary.

The outer references `E.DepartmentId` and `E.Salary` make this subquery
correlated: its result can differ for every outer employee. The department
condition prevents salaries in one department from influencing another. The
strict inequality avoids counting the current employee's own salary level.

**Why `DISTINCT` is essential**

`COUNT(DISTINCT(Salary))` counts higher salary values, not higher-paid rows.
Suppose a department contains three employees earning 100 and one employee
earning 90. For the employee earning 90, only one unique value is greater, so
90 is the second-highest unique salary. Without `DISTINCT`, the count would be
three and the query would wrongly discard that employee.

The extra parentheses in `DISTINCT(Salary)` are accepted MySQL syntax here;
the semantic operation is a distinct count of the `Salary` expression.

**Trace the complete sample logic**

In IT, Max's 90000 has no greater value and passes. Joe and Randy both earn
85000; each sees only 90000 above and passes with count one. Will at 70000 sees
two distinct values, 90000 and 85000, so he passes with count two. Janet at
69000 sees three greater distinct values and fails.

Sales has only two unique salaries. Henry has count zero and Sam has count one,
so both pass. A missing third salary level does not require a placeholder and
does not exclude anyone.

**Why all and only high earners survive**

For any returned employee, the subquery found at most two distinct greater
salaries in the same department. The current salary must therefore be first,
second, or third in descending unique-value order.

For any employee whose salary is in those top three levels, there can be at
most two distinct greater values. The count is below three, so the row passes.
Employees tied on salary see identical greater-value sets and therefore make
the same decision. This establishes exact tie-preserving selection.

**Understand the explicit ordering**

Unlike the optimal variant, this query adds `ORDER by E.DepartmentId,
E.Salary DESC`. The Reference permits any order, so sorting is optional but not
incorrect. It groups result rows by numeric department ID and places higher
salaries first within each department.

The ordering is not fully deterministic for employees tied at the same salary
because no final key such as employee ID is specified. That does not matter to
the stated contract. It also sorts by department ID rather than department
name, which may differ from alphabetical name order.

**Names do not control ranking**

All grouping logic uses `DepartmentId` and salary. Repeated department names
would not merge their employee populations, and employee names have no effect
on ranks. The constraint forbidding duplicate `(name, salary, department)`
triples is compatible with the result but not necessary for the counting
method.

**Know the null assumption**

The intended rows have actual salary and department values. With an outer null
salary, comparisons of the form `Salary > E.Salary` become unknown, the count
can be zero, and the null-salary employee may be admitted. If null salaries
were permitted, the problem would need a defined ordering policy and the query
would require an explicit null filter.

## Complexity detail

Let $n$ be the employee count and $m$ the department count. The source comment
states $O(n^2)$ time, which accurately describes a naive correlated execution:
for every outer employee, scan up to all employees and build a distinct count.
The explicit result sort adds up to $O(n\log n)$ time but does not exceed the
quadratic worst case. Temporary distinct sets and sorting can require $O(n)$
space, agreeing with the source's space comment.

The manifest records $O(n\log n)$ time and $O(n)$ space. That faster bound is
possible when the optimizer decorrelates the query, precomputes departmental
salary levels, or uses a suitable `(DepartmentId, Salary)` index. It is not
forced by the exact correlated SQL. The honest interpretation is plan
dependent: optimized execution can meet the manifest, while straightforward
execution can remain $O(n^2)$.

## Alternatives and edge cases

- **Dense ranking:** `DENSE_RANK()` over each department is the clearest direct expression on window-capable MySQL versions.
- **Precomputed top values:** Deduplicate salaries, select three per department, then join employee rows back to preserve ties.
- **Optimal variant syntax:** The comma join and explicit inner join are logically equivalent once the join predicate is present.
- **Plain row count:** Fails when higher salaries contain ties because top three means three unique values.
- **Strictly greater test:** Preserves the current salary level; using greater-than-or-equal shifts the threshold.
- **Several employees tied third:** Every one has exactly two higher unique values and must be returned.
- **Fewer than three unique levels:** Every employee qualifies.
- **Same salaries across departments:** Correlation by department prevents cross-department interference.
- **Nullable salary:** The stored query may classify it incorrectly; an explicit contract or guard is needed.
- **Optional ordering:** The source sort is allowed but unnecessary and does not order ties deterministically.
