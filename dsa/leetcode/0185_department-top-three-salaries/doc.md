# Department Top Three Salaries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 185 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/department-top-three-salaries/) |

## Problem Description
### Goal
The `Employee` table associates each employee and salary with a department, whose display name comes from the `Department` table. Within each department, rank distinct salary values from highest to lowest rather than ranking employee rows individually.

Return `Department`, `Employee`, and `Salary` for every employee whose salary belongs to that department's three highest distinct values, in any order. Tied employees at a qualifying salary must all appear, and ties consume only one salary rank. Departments with fewer than three distinct salaries contribute all their employees, while other departments never influence a local rank.

### Function Contract
**Inputs**

- `Employee(id, name, salary, departmentId)`: employees and salaries
- `Department(id, name)`: department names

**Return value**

Columns `Department`, `Employee`, and `Salary`, including every employee tied at a qualifying salary.

### Examples
**Example 1**

- IT distinct salaries: `90000, 85000, 69000`
- Output: every IT employee earning one of those salaries

**Example 2**

- Sales has only salaries `80000, 60000`
- Output: every Sales employee

**Example 3**

- Four employees tie at the third-highest salary
- Output: all four tied employees
