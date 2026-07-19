# Employees With Missing Information

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1965 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/employees-with-missing-information/) |

## Problem Description
### Goal
The `Employees` table associates an employee ID with a name, while the
`Salaries` table associates an employee ID with a salary. Each table contains
at most one row for a given employee ID.

An employee has missing information when their ID appears in exactly one of
the two tables: a row found only in `Employees` lacks salary information, and
a row found only in `Salaries` lacks a name. Report every such employee ID in
ascending numeric order.

### Function Contract
**Inputs**

- `Employees(employee_id, name)`: $E$ rows with unique `employee_id` values.
- `Salaries(employee_id, salary)`: $S$ rows with unique `employee_id` values.

**Return value**

- A table with one column, `employee_id`.
- Include IDs present in exactly one input table.
- Order rows by `employee_id` ascending.

### Examples
**Example 1**

`Employees` contains IDs 2, 4, and 5; `Salaries` contains IDs 1, 4, and 5.

- Output rows: `(1)` and `(2)`, in that order.

**Example 2**

Both tables contain exactly IDs 3 and 8.

- Output: no rows.

**Example 3**

`Employees` contains ID 7 and `Salaries` is empty.

- Output row: `(7)`.
