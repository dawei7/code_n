## General

**Give the employee table two roles**

Each row contains both an employee's data and the ID of another row representing
that employee's manager. To compare their salaries, the query joins `Employee`
to itself.

Alias `e1` is the employee being evaluated. Alias `e2` is that employee's
manager. The aliases are necessary because otherwise references such as
`salary` and `id` would be ambiguous between the two uses of the same table.

The join condition:

`e1.managerId = e2.id`

connects each employee row to the unique manager row named by its foreign-key
value. `e2.id` is a primary key, so at most one manager row matches.

No assumption is made that a manager's row appears before or after a
subordinate's row. Relational matching uses identifier equality, so physical
table order is irrelevant.

**Why an inner join is appropriate**

Employees with no manager have `managerId = NULL`. SQL equality with null is
not true, so those rows do not match `e2`.

That exclusion is correct. A top-level employee without a manager cannot
satisfy “earns more than their manager,” because there is no manager salary to
compare.

If a non-null `managerId` referred to no existing row, an inner join would
exclude it for the same reason. The expected relational data normally maintains
the reference, but the query remains semantically sensible.

**Apply the salary comparison after matching**

The `WHERE` clause keeps a joined employee-manager pair only when:

`e1.salary > e2.salary`.

The operator is strictly greater. Equal salaries do not qualify, and a lower
employee salary does not qualify.

Matching first is important conceptually. Comparing an employee with every
other employee would create unrelated salary pairs; the ID join restricts the
comparison to the one designated manager.

**Project only the employee's name**

The output selects `e1.name` and aliases it as `Employee`. It must use the
employee alias, not `e2.name`, because the requested person is the subordinate
whose salary passed the comparison.

The output does not include salary or identifiers. The alias supplies the exact
column name required by the contract.

No `DISTINCT` is needed. `e1.id` is unique, and each employee can match at most
one manager primary-key row. If two different employees share the same name
and both qualify, returning two rows is relationally correct because the task
asks for employees, not unique name strings.

**Trace the sample**

Joe's row has `managerId = 3`, which joins to Sam. Joe earns 70,000 and Sam
earns 60,000, so the strict comparison is true and Joe's name is returned.

Henry's `managerId = 4` joins to Max. Henry earns 80,000 while Max earns
90,000, so Henry is filtered out.

Sam and Max have null manager IDs. Neither produces a joined pair, so neither
is compared or returned.

**Why the query is sound and complete**

Every output row comes from an `e1` row joined to the row whose primary key
equals its `managerId`. The salary predicate proves that employee earns more
than that manager, so every output is sound.

Conversely, any employee who has a manager and earns more has a corresponding
`e2` primary-key row satisfying the join and comparison. The query therefore
returns that employee's name, proving completeness.

**NULL salary behavior**

The schema types salaries as integers but does not explicitly state
`NOT NULL`. If either salary is null, `e1.salary > e2.salary` evaluates to
unknown and the row is excluded. This is SQL's standard behavior; a production
specification should state whether missing salaries can qualify under some
custom policy.

**Output order**

The Reference allows any order, so no `ORDER BY` appears. Physical row order is
not guaranteed and should not be inferred from IDs or join execution.

## Complexity detail

Let $n$ be the number of employees. With the primary-key index on `e2.id`, an
engine can scan employees and probe each manager in roughly $O(n\log n)$ worst
case for tree-index lookups, or near $O(n)$ with hashing or index assumptions.

A hash self-join can use $O(n)$ working space, matching the manifest's broad
$O(n)$ time and space. Actual SQL cost depends on indexes, statistics, and the
optimizer; the query text does not force one physical algorithm.

## Alternatives and edge cases

- **Correlated scalar subquery:** Fetch the manager salary for each employee and compare it; clear but may repeat lookup work.
- **Left join:** A later manager-salary predicate removes null matches, making it effectively inner; direct inner join better states intent.
- **Cartesian product plus `WHERE`:** Logically equivalent when both join and salary predicates are present, but explicit join syntax is clearer.
- **No manager:** The employee is excluded.
- **Equal salary:** Strict `>` correctly excludes it.
- **Several employees with one manager:** Each qualifying employee produces its own row.
- **Duplicate employee names:** They can legitimately appear multiple times because IDs identify employees.
- **Broken manager reference:** Inner join produces no output for that row.
- **Null salary:** The comparison is unknown and does not qualify.
- **Any order:** No sorting clause is required.
