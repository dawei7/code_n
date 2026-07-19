# Second Highest Salary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 176 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/second-highest-salary/) |

## Problem Description
### Goal
The `Employee` table contains identifiers and salary values, and several employees may share the same salary. Determine the second-highest distinct salary represented in the table, ranking salary values rather than individual employee rows.

Return exactly one row with one column named `SecondHighestSalary`. When at least two distinct salaries exist, the column contains the value immediately below the maximum; duplicate rows at either salary do not change its rank. When the table has fewer than two distinct salary values, including when it is empty, return `NULL` in that single result row instead of returning no rows.

### Function Contract
**Inputs**

- `Employee(id, salary)`: employee rows whose salary values may repeat

**Return value**

Exactly one column named `SecondHighestSalary` and one row containing the requested salary or null.

### Examples
**Example 1**

- Salaries: `100, 200, 300`
- Output: `200`

**Example 2**

- Salaries: `100`
- Output: `null`

**Example 3**

- Salaries: `100, 100, 200`
- Output: `100`
