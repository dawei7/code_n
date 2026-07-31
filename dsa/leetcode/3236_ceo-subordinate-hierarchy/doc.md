# CEO Subordinate Hierarchy

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3236 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/ceo-subordinate-hierarchy/) |

## Problem Description

### Goal

The `Employees` table stores an organization's reporting hierarchy. Every employee has a unique identifier, name, salary, and manager identifier; the CEO is the row whose `manager_id` is `NULL`.

Return every direct and indirect subordinate of the CEO. For each subordinate, report the employee's identifier and name, the number of reporting edges from the CEO, and the subordinate's salary minus the CEO's salary. Direct reports are at level $1$, their reports are at level $2$, and the pattern continues through any depth.

Order the result by hierarchy level ascending and then subordinate identifier ascending. Do not include the CEO in the output.

### Function Contract

**Inputs**

The `Employees` table contains:

- `employee_id`: The unique integer employee identifier.
- `employee_name`: The employee's name.
- `manager_id`: The identifier of the direct manager, or `NULL` for the CEO.
- `salary`: The employee's integer salary.

Let $e$ be the number of employee rows.

**Return value**

Return columns `subordinate_id`, `subordinate_name`, `hierarchy_level`, and `salary_difference`, ordered by level and then subordinate ID, both ascending.

### Examples

**Example 1**

If Alice is the CEO, Bob and Charlie report to Alice, David and Eve report to Bob, Frank and Grace report to Charlie, and Helen reports to Eve, the result assigns levels $1$, $2$, and $3$ respectively. Each salary difference is computed against Alice's salary, not against the employee's immediate manager.
