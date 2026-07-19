## General
**Attach experience to assignments:** Inner-join `Project` with `Employee` on `employee_id`. The foreign-key relationship gives each assignment exactly one non-null experience value.

**Aggregate at project grain:** Group the joined rows by `project_id` and apply `AVG(experience_years)`. The composite project key prevents the same employee from appearing twice within one project's assignments.

**Round the reported average:** Apply `ROUND` with precision two and alias the value as `average_years`. Employee names are not selected because they neither identify the output group nor affect the average. Ascending project order only stabilizes local fixtures.

Every joined experience value belongs to the project from its assignment and contributes once to that project's average. Conversely, every assignment has a matching employee row, so no assigned employee is omitted from the corresponding group.

## Complexity detail
A hash join can build an $E$-employee lookup and process all $R$ assignments in expected $O(E+R)$ time. Sort-based grouping and deterministic output ordering can add $O(R\log R)$ time, with up to $O(E+R)$ execution space. Indexes and the optimizer may choose different physical plans.

## Alternatives and edge cases
- **Correlated average:** Compute a project average in a scalar subquery for each assignment and deduplicate projects. It can repeatedly rescan assignments and take quadratic time.
- **Average employee identifiers:** It is incorrect; the aggregate must use `experience_years` after the employee join.
- **Group by employee:** That answers one row per employee rather than one row per project.
- **Single employee project:** Its average equals that employee's experience, formatted to two decimals.
- **Employee on several projects:** The experience value contributes once to each project assignment.
- **Non-terminating decimal:** `ROUND(..., 2)` produces the required two-decimal result.
- **Names:** Duplicate or different names have no effect because `employee_id` is the join key.
