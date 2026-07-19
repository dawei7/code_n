# Managers with at Least 5 Direct Reports

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 570 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/) |

## Problem Description
### Goal
Given an `Employee` table in which each row's `managerId` identifies that employee's direct manager, find every manager who has at least five direct reports. Employee identifiers are unique, and a null manager identifier means that the employee does not report directly to another employee in the table.

Return the qualifying managers' names in any order. Count only employees whose `managerId` equals the manager's `id`; employees farther down the reporting hierarchy are indirect reports and must not be included in that manager's count.

### Function Contract
**Inputs**

- `Employee(id, name, department, managerId)`: employees and the identifier of each employee's direct manager

**Return value**

- A result grid with one column, `name`, containing every qualifying manager

### Examples
**Example 1**

- Input: manager `John` is referenced by five employee rows
- Output: `John`

**Example 2**

- Input: a manager has only four direct reports
- Output: no rows

**Example 3**

- Input: two managers each have at least five direct reports
- Output: both manager names
