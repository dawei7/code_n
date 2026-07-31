# Analyze Organization Hierarchy

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3482 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/analyze-organization-hierarchy/) |

## Problem Description

### Goal

The `Employees` table describes a rooted organizational hierarchy. Each row identifies an employee, their salary and department, and the employee who directly manages them. The single top-level manager, or CEO, has a `NULL` manager.

Produce one result row for every employee, including the CEO. Report the employee's hierarchy level with the CEO at level 1, the number of direct and indirect reports below that employee, and the salary budget controlled by that employee. A controlled budget includes the employee's own salary and the salaries of every descendant in their reporting subtree.

Order the result by level ascending, then budget descending within a level, and finally employee name ascending when both preceding keys tie.

### Function Contract

**Inputs**

The `Employees` table contains:

- `employee_id`: The unique integer identifier for an employee.
- `employee_name`: The employee's name.
- `manager_id`: The identifier of the employee's direct manager, or `NULL` for the CEO.
- `salary`: The employee's salary.
- `department`: The employee's department.

Let $n$ be the number of employee rows. The manager references form one rooted hierarchy headed by the CEO.

**Return value**

Return columns `employee_id`, `employee_name`, `level`, `team_size`, and `budget` in the required order. `team_size` excludes the employee, while `budget` includes the employee.

### Examples

**Example**

For a company led by Alice, Bob and Charlie are level-2 employees because they report directly to her. Reports below Bob or Charlie contribute to those managers' team sizes and budgets and also to Alice's company-wide totals.

If Alice's hierarchy contains nine other employees whose salaries total 72,500 and Alice earns 12,000, her result row has `level = 1`, `team_size = 9`, and `budget = 84500`. Rows on the same level are placed by decreasing budget, with employee name breaking a remaining tie.
