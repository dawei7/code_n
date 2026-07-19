# Find Cumulative Salary of an Employee

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 579 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-cumulative-salary-of-an-employee/) |

## Problem Description
### Goal
Given monthly salary rows for multiple employees, calculate a three-month cumulative salary for each employee and recorded month. The value for month `M` is that employee's salary in calendar months `M`, $M - 1$, and $M - 2$; when one of those months has no row, it contributes nothing rather than being replaced by an older recorded month.

Exclude the latest recorded month for each employee from the result. Return `Id`, `Month`, and the cumulative value as `Salary`, ordering rows first by `Id` in ascending order and then by `Month` in descending order. An employee with only one recorded month therefore contributes no output row.

### Function Contract
**Inputs**

- `Employee(Id, Month, Salary)`: one salary record per employee and month

**Return value**

- Columns `Id`, `Month`, and `Salary`, where `Salary` is the sum over months from `Month - 2` through `Month` for the same employee
- Exclude each employee's greatest recorded month
- Order rows by `Id` ascending and then `Month` descending

### Examples
**Example 1**

- Input: employee 1 has salaries `20`, `30`, `40`, and `60` in months 1 through 4
- Output: months 3, 2, and 1 with cumulative salaries `90`, `50`, and `20`; month 4 is excluded

**Example 2**

- Input: one employee has records only in months 1 and 4
- Output: month 1 with only its own salary; month 4 is excluded

**Example 3**

- Input: an employee has a single salary row
- Output: no rows for that employee
