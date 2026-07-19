# Swap Sex of Employees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 627 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/swap-sex-of-employees/) |

## Problem Description
### Goal
Given a `Salary` table whose `sex` column contains only `m` or `f`, swap every value in that column: change each `m` to `f` and each `f` to `m`.

Perform the mutation with a single `UPDATE` statement, without a `SELECT` statement or an intermediate temporary table. Leave every employee's `id`, `name`, and `salary` unchanged, and do not add, remove, or reorder rows; only the two allowed `sex` values are exchanged in place.

### Function Contract
**Inputs**

- `Salary(id, name, sex, salary)`: employee rows whose `sex` value is either `m` or `f`

**Return value**

- The `Salary` table is mutated in place
- Every `m` is replaced by `f` and every `f` by `m`
- IDs, names, salaries, and row count remain unchanged

### Examples
**Example 1**

- Input rows: `(A, m)`, `(B, f)`, `(C, m)`
- Final rows: `(A, f)`, `(B, m)`, `(C, f)`

**Example 2**

- Input: one employee with `sex = f`
- Final value: `m`
