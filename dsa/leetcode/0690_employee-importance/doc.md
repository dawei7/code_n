# Employee Importance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 690 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Tree, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/employee-importance/) |

## Problem Description
### Goal
Each employee record contains a unique identifier, an importance value, and the identifiers of that employee's direct subordinates. Given the collection of employee records and one requested `id`, consider the complete reporting hierarchy beginning at that employee.

Return the total importance of the requested employee together with all direct and indirect subordinates. Count each employee in that hierarchy once, follow subordinate identifiers through as many levels as necessary, and do not include managers or employees outside the requested employee's descendant structure.

### Function Contract
**Inputs**

- `employees`: employee records with fields `id`, `importance`, and `subordinates`; local cases encode the platform objects as JSON records
- `id`: the employee ID whose complete subordinate hierarchy should be totaled

**Return value**

- The sum of importance values for the requested employee and all reachable subordinates

### Examples
**Example 1**

- Input: `employees = [{id:1, importance:5, subordinates:[2,3]}, {id:2, importance:3, subordinates:[]}, {id:3, importance:3, subordinates:[]}], id = 1`
- Output: `11`

**Example 2**

- Input: `employees = [{id:1, importance:2, subordinates:[2]}, {id:2, importance:4, subordinates:[]}], id = 2`
- Output: `4`

**Example 3**

- Input: `employees = [{id:1, importance:-5, subordinates:[2]}, {id:2, importance:2, subordinates:[]}], id = 1`
- Output: `-3`
