# Replace Employee ID With The Unique Identifier

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1378 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/) |

## Problem Description

### Goal

The `Employees` table stores each employee's internal `id` and `name`. A second table, `EmployeeUNI`, optionally associates an internal employee `id` with a `unique_id`. Not every employee necessarily has an entry in that mapping table.

Produce one row for every employee, showing the employee's `unique_id` and `name`. When an employee has no matching mapping, return `NULL` for `unique_id`. The result rows may be returned in any order.

### Function Contract

**Inputs**

- `Employees(id, name)`: $E$ employee rows keyed by internal `id`.
- `EmployeeUNI(id, unique_id)`: $U$ optional mappings from internal IDs to unique identifiers.

**Return value**

- A relation with columns `unique_id` and `name`, containing every employee exactly once and using `NULL` when no unique identifier exists.

### Examples

**Example 1**

- Input: `Employees = [[1,"Alice"],[7,"Bob"],[11,"Meir"],[90,"Winston"],[3,"Jonathan"]], EmployeeUNI = [[3,1],[11,2],[90,3]]`
- Output: `[[null,"Alice"],[1,"Jonathan"],[null,"Bob"],[2,"Meir"],[3,"Winston"]]`

**Example 2**

- Input: `Employees = [[5,"Ada"],[8,"Lin"]], EmployeeUNI = [[5,105],[8,108]]`
- Output: `[[105,"Ada"],[108,"Lin"]]`

**Example 3**

- Input: `Employees = [[4,"Solo"],[9,"Mapped"]], EmployeeUNI = [[9,109]]`
- Output: `[[null,"Solo"],[109,"Mapped"]]`
