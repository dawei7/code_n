## General

**Join assignments with employee experience**

`Project` tells us which employees work on each project, but it does not store their experience. `Employee` stores `experience_years`, but it does not identify project membership.

The shared `employee_id` connects these facts. The query joins:

```sql
FROM
    Project
    JOIN Employee USING (employee_id)
```

Bare `JOIN` is an inner join. `USING (employee_id)` matches rows whose employee identifiers are equal.

`Project.employee_id` is a foreign key, so each assignment references an existing employee. `Employee.employee_id` is a primary key, so each assignment matches exactly one employee row. The join therefore enriches every project assignment with one experience value without losing or multiplying assignments.

**Group the enriched rows by project**

The query selects:

```sql
SELECT project_id, ...
```

and ends with:

```sql
GROUP BY 1
```

In MySQL, `GROUP BY 1` refers to the first select-list expression, `project_id`. It is equivalent to `GROUP BY project_id`.

Every joined assignment for the same project enters one group. Assignments for different projects remain separate.

The composite primary key `(project_id, employee_id)` guarantees that one employee is not listed twice within the same project. Thus each employee contributes once to that project's average. The same employee may legitimately work on several projects and contributes once to each corresponding group.

**Calculate the arithmetic mean**

Inside each project group:

```sql
AVG(experience_years)
```

computes the sum of all member employees' experience years divided by the number of those employees.

The schema guarantees `experience_years` is not null. Therefore every joined project member contributes to both the numerator and denominator. There is no difference between employee count and non-null experience count.

For experience values three, two, and one, `AVG` computes:

```text
(3 + 2 + 1) / 3 = 2
```

The result is per employee, not weighted by any other property. The `Project` table has one assignment row per employee-project pair, so ordinary `AVG` has exactly the desired weighting.

**Round and name the computed column**

The full aggregate expression is:

```sql
ROUND(AVG(experience_years), 2) AS average_years
```

`ROUND(..., 2)` rounds the numeric average to two digits after the decimal point. This is not truncation; a third decimal digit can increase the second.

The alias `average_years` provides the exact required result-column name.

Rounding must happen after averaging. Rounding each employee's integer experience beforehand would change nothing here, but in general the semantic requirement is the rounded group average, and the query expresses that directly.

**Why the output is correct**

Fix one project identifier `p`. The join produces one row for each employee assigned to `p`, carrying that employee's non-null experience. Grouping collects exactly those rows. `AVG` computes their arithmetic mean, and `ROUND` formats its value to the requested precision. The query emits one row with `p` and that result.

Every output group originates from at least one `Project` row, so projects without assignments are not invented. Every project represented in `Project` creates a group because all foreign-key employee matches exist.

This proves one correct output row for each project in the assignment table.

**Why no extra columns belong in the grouping**

Grouping by `employee_id` would split a project into one row per employee instead of one row per project. Grouping by experience years would split members based on their values.

`project_id` alone defines the requested output grain. `experience_years` belongs only inside the aggregate.

**No order is required**

The result may appear in any order, so there is no `ORDER BY`. A database can return project groups in any plan-dependent order without affecting correctness.

## Complexity detail

Let `R` be the number of rows in `Project` and `E` the number of rows in `Employee`.

SQL physical complexity depends on indexes and the optimizer. A hash join can build employee lookup state and scan assignments in expected `O(E + R)` time. A primary-key index can support one indexed employee lookup per assignment. Grouping may use hashing or sorting.

With sort-based grouping, the assignment-side work can take `O(R log R)` time and `O(R)` working space. Including employee access gives the manifest's conservative `O(E + R log R)` time and `O(E + R)` space.

A hash join plus hash aggregation may run in expected linear time and space proportional to employees plus distinct projects. Declarative SQL does not require one particular physical plan.

The output has one row per distinct project.

## Alternatives and edge cases

- **Explicit ON syntax:** `JOIN Employee ON Project.employee_id = Employee.employee_id` is equivalent and useful when table aliases make ownership clearer.
- **GROUP BY project_id:** Naming the grouping column is equivalent to `GROUP BY 1` and is more robust if select-list order changes.
- **Correlated subquery:** Computing an average separately for every project can repeat work and is less direct than one join and grouping.
- **Pre-aggregate assignments:** There is nothing useful to aggregate before joining because experience values live in `Employee`.
- **One employee on a project:** The average equals that employee's experience, rounded to two digits.
- **Employee on multiple projects:** The join creates one assignment row in each project group, which is correct.
- **Duplicate assignment prevention:** The composite primary key prevents one employee from being counted twice within the same project.
- **Equal experience values:** Every employee still contributes individually; the mean remains that common value.
- **Non-null guarantee:** `AVG` ignores nulls in SQL, but the schema guarantee ensures no project member is silently excluded.
- **Project with no assignment row:** It is absent because `Project` is the assignment relation and drives the query.
- **Rounding:** `ROUND(..., 2)` applies after averaging and gives the requested precision.
- **Any output order:** Omitting `ORDER BY` matches the contract.
- **Positional grouping:** In this MySQL query, one refers to the first selected expression rather than a constant grouping key.
