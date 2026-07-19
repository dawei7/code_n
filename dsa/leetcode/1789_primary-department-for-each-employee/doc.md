# Primary Department for Each Employee

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/primary-department-for-each-employee/) |
| Frontend ID | 1789 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Employee` table records the departments to which each employee belongs. An employee may have several rows, one for each department. For a multi-department employee, exactly one membership is identified as primary by `primary_flag = 'Y'`; other memberships use `'N'`.

An employee who belongs to only one department has no separate choice to make, so that sole row keeps `primary_flag = 'N'` even though its department must be reported as primary.

Return each employee's identifier together with the correct primary department: use the explicitly flagged department for employees with several memberships, and use the only department for employees with one membership. Result rows may appear in any order.

### Function Contract

**Input**

- `Employee(employee_id, department_id, primary_flag)`: membership rows whose composite primary key is `(employee_id, department_id)`.
- `primary_flag` is either `'Y'` or `'N'`. A multi-department employee has one `'Y'` row; a single-department employee's only row is `'N'`.

Let $R$ be the number of membership rows and $M$ the number of distinct employees.

**Return value**

- Return columns `employee_id` and `department_id`, with exactly one row per employee containing that employee's primary department.
- Result order is unrestricted.

### Examples

**Example 1**

- Input: `Employee = [[1,1,"N"],[2,1,"Y"],[2,2,"N"],[3,3,"N"],[4,2,"N"],[4,3,"Y"],[4,4,"N"]]`
- Output: `[[1,1],[2,1],[3,3],[4,3]]`

Employees `1` and `3` use their only departments; employees `2` and `4` use their `'Y'` rows.

**Example 2**

- Input: `Employee = [[7,42,"N"]]`
- Output: `[[7,42]]`

A sole membership is reported despite its `'N'` flag.

**Example 3**

- Input: `Employee = [[5,90,"N"],[5,3,"Y"],[5,40,"N"]]`
- Output: `[[5,3]]`

The primary department is selected by the flag, not by the smallest or largest identifier.
