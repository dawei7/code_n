## General
**Join each report to the current manager row**

Left-join `Employees` to itself. The left alias represents the employee being
tested, while the right alias represents the possible current manager whose
`employee_id` equals the employee's `manager_id`.

Filter the left row to salaries strictly below `30000` and non-null manager
references. Then require the joined manager's primary key to be `NULL`. A
matching current manager produces a non-null right-side ID and is rejected;
an unmatched non-null reference represents precisely a manager who left.
Finally, order the qualifying employee IDs.

**Why the null checks distinguish departed managers**

A left join preserves every report even when no manager row matches. For a
non-null `manager_id`, a null joined primary key can arise only from absence of
that referenced employee, since primary keys themselves are never null. The
explicit `employee.manager_id IS NOT NULL` condition prevents employees who
legitimately have no manager from being mistaken for reports of departed
managers.

## Complexity detail
With an index or hash table on the primary key, the database scans $R$
employees and performs one constant expected-time manager lookup per row,
giving $O(R)$ expected time. The table index, join state, and result may use
$O(R)$ space. A particular database engine may select another physical plan
while preserving the query result.

## Alternatives and edge cases
- **Correlated `NOT EXISTS`:** Check manager absence for every qualifying
  employee. With primary-key lookups this can be equally efficient, though the
  left anti-join makes the relationship visible in one join.
- **`NOT IN` subquery:** This is concise because `employee_id` is non-null, but
  `NOT EXISTS` or an anti-join is less vulnerable to null-related surprises if
  a schema changes.
- **Compare every possible manager:** A Cartesian self-join followed by
  grouping can establish absence but takes $O(R^2)$ time.
- Salary `30000` does not qualify because the condition is strictly less.
- A null `manager_id` means the employee has no manager, not that a manager
  left.
- A low-salary employee whose manager still has a row must not appear.
- The manager's own salary and manager relationship are irrelevant to whether
  the report qualifies.
