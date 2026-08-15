# Create a New Column

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2881 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/create-a-new-column/) |

## Problem Description

### Goal

An employee table records each person's `name` and integer `salary`. Extend this DataFrame with a column named `bonus`. For every employee, the value in `bonus` must be exactly twice that row's salary.

Return the resulting DataFrame with the existing employee rows in their original order. Its columns must appear as `name`, `salary`, and then `bonus`; the original names and salaries remain unchanged while the new value is derived independently for each row.

### Function Contract

**Inputs**

- `employees`: A pandas DataFrame with columns `name` and `salary`. Each row represents one employee, and `salary` contains integer values.

Let $n$ be the number of rows in `employees`.

**Return value**

Return the employee DataFrame with a new integer column `bonus`, where each row satisfies `bonus = 2 * salary` and row order is preserved.

### Examples

#### Example 1

- **Input:** `employees = [{"name": "Piper", "salary": 4548}, {"name": "Grace", "salary": 28150}, {"name": "Georgia", "salary": 1103}, {"name": "Willow", "salary": 6593}, {"name": "Finn", "salary": 74576}, {"name": "Thomas", "salary": 24433}]`
- **Output:** `[{"name": "Piper", "salary": 4548, "bonus": 9096}, {"name": "Grace", "salary": 28150, "bonus": 56300}, {"name": "Georgia", "salary": 1103, "bonus": 2206}, {"name": "Willow", "salary": 6593, "bonus": 13186}, {"name": "Finn", "salary": 74576, "bonus": 149152}, {"name": "Thomas", "salary": 24433, "bonus": 48866}]`

#### Example 2

- **Input:** `employees = [{"name": "Ada", "salary": 6000}]`
- **Output:** `[{"name": "Ada", "salary": 6000, "bonus": 12000}]`

#### Example 3

- **Input:** `employees = [{"name": "Lin", "salary": 3200}, {"name": "Sam", "salary": 3200}]`
- **Output:** `[{"name": "Lin", "salary": 3200, "bonus": 6400}, {"name": "Sam", "salary": 3200, "bonus": 6400}]`
