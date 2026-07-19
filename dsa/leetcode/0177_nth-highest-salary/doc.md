# Nth Highest Salary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 177 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/nth-highest-salary/) |

## Problem Description
### Goal
The `Employee` table stores employee identifiers and salaries that may repeat. For a positive one-based integer `N`, rank the distinct salary values from highest to lowest and select the value at rank `N`.

Implement the database function `getNthHighestSalary(N)` so it returns that distinct salary, or `NULL` when fewer than `N` different values exist. Duplicate employee salaries occupy one rank rather than several consecutive ranks. The app fixtures provide `N` through a request table while preserving the same result semantics, including $N = 1$ selecting the maximum salary and an empty employee table producing `NULL`.

### Function Contract
**Inputs**

- `Employee(id, salary)`: employee salary rows with possible duplicates
- `N`: positive one-based rank; app fixtures expose it as `Request(N)` while the native MySQL artifact receives a function parameter

**Return value**

The Nth-highest distinct salary as `getNthHighestSalary`, or null when that rank is absent.

### Examples
**Example 1**

- Salaries: `100, 200, 300`; $N = 2$
- Output: `200`

**Example 2**

- Salaries: `100`; $N = 2$
- Output: `null`

**Example 3**

- Salaries: `100, 100, 200`; $N = 2$
- Output: `100`
