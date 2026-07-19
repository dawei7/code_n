# Employees Whose Manager Left the Company

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1978 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/employees-whose-manager-left-the-company/) |

## Problem Description
### Goal
The `Employees` table stores each current employee's ID, name, manager ID, and
salary. Employees without a manager have `NULL` as `manager_id`. When a
manager leaves the company, that manager's row is deleted, but current reports
retain the departed manager's ID in their own rows.

Report current employees whose salary is strictly below `30000` and whose
non-null manager ID no longer identifies any current employee. Return their
IDs in ascending order.

### Function Contract
**Inputs**

- `Employees(employee_id, name, manager_id, salary)`: $R$ current employee
  rows.
- `employee_id` is the primary key.
- `manager_id` is either `NULL`, an existing employee ID, or the former ID of
  a manager whose row has been removed.

**Return value**

- A one-column table named `employee_id`.
- Include only employees with `salary < 30000`, a non-null manager ID, and no
  matching manager row.
- Order rows by `employee_id` ascending.

### Examples
**Example 1**

In the public sample, employee 1 earns below the threshold but manager 11
still exists. Employee 11 earns below the threshold and references absent
manager 6.

- Output row: `(11)`.

**Example 2**

An employee earns `29999` and references manager ID 9, which is absent.

- Output: that employee's ID.

**Example 3**

An employee earns exactly `30000` and references an absent manager.

- Output: no rows because the salary condition is strict.

### Required Complexity
- **Time:** $O(R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

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

#### Complexity detail

With an index or hash table on the primary key, the database scans $R$
employees and performs one constant expected-time manager lookup per row,
giving $O(R)$ expected time. The table index, join state, and result may use
$O(R)$ space. A particular database engine may select another physical plan
while preserving the query result.

#### Alternatives and edge cases

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

</details>
