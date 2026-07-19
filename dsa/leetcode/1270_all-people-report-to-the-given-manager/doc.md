# All People Report to the Given Manager

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1270 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/all-people-report-to-the-given-manager/) |

## Problem Description

### Goal

The `Employees` table describes a small company's reporting hierarchy. Each row gives one employee's unique identifier and name together with the identifier of that employee's direct manager. The company head has `employee_id = 1`; that row reports to itself.

Find the identifiers of all employees whose chain of direct managers eventually reaches the company head, whether they report to the head directly or through other managers. Do not include the head. A reporting chain contains at most three managers, and employees belonging to a separate self-managed hierarchy must be excluded. Return the qualifying identifiers in any order without duplicates.

### Function Contract

**Inputs**

- `Employees(employee_id, employee_name, manager_id)`: one row per employee, with `employee_id` unique and `manager_id` naming the direct manager.
- Let $n$ be the number of rows in `Employees`.

**Return value**

- Return a one-column table named `employee_id` containing every non-head employee who reports directly or indirectly to employee `1`.

### Examples

**Example 1**

- Input: employees `2` and `77` report to `1`, employee `4` reports to `2`, employee `7` reports to `4`, and a separate hierarchy is rooted at self-managed employee `3`.
- Output: employee identifiers `2`, `4`, `7`, and `77` in any order.

**Example 2**

- Input: the table contains only the head row `(1, "Boss", 1)`.
- Output: an empty result.

**Example 3**

- Input: `2 -> 1`, `3 -> 2`, and `4 -> 3`.
- Output: employee identifiers `2`, `3`, and `4`.
