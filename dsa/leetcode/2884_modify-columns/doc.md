# Modify Columns

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2884 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/modify-columns/) |

## Problem Description

### Goal

A company stores each employee's `name` and integer `salary` in a DataFrame. The company plans to give every employee a pay rise by replacing each salary with twice its current value.

Modify the `salary` column for all rows and return the resulting DataFrame. Keep the original `name`, preserve employee order, and retain the two-column schema `name`, `salary`; only the salary values change, with every new value equal to two times the corresponding input salary.

### Function Contract

**Inputs**

- `employees`: A pandas DataFrame with object column `name` and integer column `salary`.

Let $n$ be the number of employee rows.

**Return value**

Return the employee DataFrame with every `salary` replaced by twice its original value, while names, columns, and row order remain unchanged.

### Examples

**Example 1**

- Input: `employees = [{"name": "Jack", "salary": 19666}, {"name": "Piper", "salary": 74754}, {"name": "Mia", "salary": 62509}, {"name": "Ulysses", "salary": 54866}]`
- Output: `[{"name": "Jack", "salary": 39332}, {"name": "Piper", "salary": 149508}, {"name": "Mia", "salary": 125018}, {"name": "Ulysses", "salary": 109732}]`

**Example 2**

- Input: `employees = [{"name": "Ada", "salary": 1}]`
- Output: `[{"name": "Ada", "salary": 2}]`

**Example 3**

- Input: `employees = [{"name": "Lin", "salary": 3200}, {"name": "Sam", "salary": 3200}]`
- Output: `[{"name": "Lin", "salary": 6400}, {"name": "Sam", "salary": 6400}]`
