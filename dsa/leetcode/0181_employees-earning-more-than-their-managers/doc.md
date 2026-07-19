# Employees Earning More Than Their Managers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 181 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/employees-earning-more-than-their-managers/) |

## Problem Description
### Goal
The `Employee` table stores each employee's identifier, name, salary, and an optional `managerId` that references another row in the same table. Compare each employee who has a recorded manager with that manager's salary.

Return one column named `Employee` containing the names of qualifying employees in any order. Employees earning the same amount as their manager do not qualify, and top-level employees with no manager have no comparison and must be excluded. Manager status does not otherwise affect eligibility: a manager may also qualify relative to their own manager.

### Function Contract
**Inputs**

- `Employee(id, name, salary, managerId)`: employees and their optional manager reference into the same table

**Return value**

One column named `Employee` containing each qualifying employee name.

### Examples
**Example 1**

Joe earns `70000` while manager Sam earns `60000`; Joe is returned.

**Example 2**

An employee earning exactly the manager's salary is not returned.

**Example 3**

Top-level employees with null managerId are not returned.
