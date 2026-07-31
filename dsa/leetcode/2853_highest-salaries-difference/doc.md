# Highest Salaries Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2853 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/highest-salaries-difference/) |

## Problem Description

### Goal

The `Salaries` table records an employee name, the employee's department, and a salary. The pair `(emp_name, department)` uniquely identifies a row. The data contains at least one employee in `Engineering` and at least one employee in `Marketing`.

Find the highest salary in each of those two departments. Return the absolute difference between the two maxima in a single-row result table.

### Function Contract

**Inputs**

- `Salaries(emp_name, department, salary)`: `emp_name` and `department` are strings, `salary` is an integer, and `(emp_name, department)` is the composite primary key.

Let $S$ be the number of rows in `Salaries`.

**Return value**

Return one row with one column named `salary_difference`. Its value is the absolute difference between the maximum `Marketing` salary and the maximum `Engineering` salary.

### Examples

**Example 1**

- Input: Engineering salaries include `50000`, `45000`, `85000`, `102000`, `44000`, and `32000`; Marketing salaries include `30000`, `34000`, `42000`, and `53000`.
- Output: `salary_difference = 49000`
- Explanation: The departmental maxima are `102000` and `53000`, whose absolute difference is `49000`.
