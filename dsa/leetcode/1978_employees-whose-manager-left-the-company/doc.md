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
