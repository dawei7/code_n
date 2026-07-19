# Median Employee Salary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 569 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/median-employee-salary/) |

## Problem Description
### Goal
Given an `Employee` table containing each employee's identifier, company, and salary, find the employee row or rows occupying the median salary position within every company. Rank only employees from the same company and order them by salary from lowest to highest.

If a company has an odd number of employees, report its single middle row. If it has an even number, report both central rows whose positions surround the median. Return the original `id`, `company`, and `salary` values for every selected employee rather than returning only a calculated salary average.

### Function Contract
**Inputs**

- `Employee(id, company, salary)`: employee identifiers, company names, and salaries

**Return value**

- A result grid with columns `id`, `company`, and `salary` for each company's median-position employee rows

### Examples
**Example 1**

- Input: company `A` has salaries `10, 20, 30`
- Output: the employee earning `20`

**Example 2**

- Input: company `B` has salaries `5, 15, 25, 35`
- Output: the employees earning `15` and `25`

**Example 3**

- Input: one employee in a company
- Output: that employee
