# Employee Bonus

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 577 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/employee-bonus/) |

## Problem Description
### Goal
Given an `Employee` table and a `Bonus` table keyed by the unique employee identifier `empId`, find every employee whose bonus is less than `1000`. An employee may have no matching row in `Bonus`; that missing bonus also satisfies the requested condition and must not cause the employee to disappear from the result.

Return each qualifying employee's `name` and `bonus` in any order. Preserve `NULL` as the bonus for employees without a bonus record, and exclude a recorded bonus of exactly `1000` because the comparison is strictly less than `1000`.

### Function Contract
**Inputs**

- `Employee(empId, name, supervisor, salary)`: employee details
- `Bonus(empId, bonus)`: optional bonus amounts keyed by employee identifier

**Return value**

- A result grid with columns `name` and `bonus`
- Include employees whose bonus is below 1000 and employees with no matching bonus row; the latter have `NULL` in `bonus`

### Examples
**Example 1**

- Input: an employee has bonus `500`
- Output: that employee's name and `500`

**Example 2**

- Input: an employee has no row in `Bonus`
- Output: that employee's name and `NULL`

**Example 3**

- Input: an employee has bonus `1000`
- Output: no row for that employee
