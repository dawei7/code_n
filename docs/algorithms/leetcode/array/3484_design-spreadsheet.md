# Design Spreadsheet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3484 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Design, Matrix |
| Official Link | [design-spreadsheet](https://leetcode.com/problems/design-spreadsheet/) |

## Problem Description & Examples
### Goal
Design a spreadsheet system that supports setting values in specific cells (identified by row and column) and evaluating formulas. Formulas can involve simple arithmetic or references to other cells (e.g., "A1:B2" representing a range sum). The system must handle dynamic updates where changing a cell's value automatically propagates to any dependent formulas.

### Function Contract
**Inputs**

- `rows`: Integer representing the number of rows.
- `cols`: Integer representing the number of columns.
- `operations`: A list of commands, where each command is either `set(r, c, val)`, `get(r, c)`, or `sum(r, c, r1, c1, r2, c2)`.

**Return value**

- A list of integers representing the results of all `get` and `sum` operations.

### Examples
**Example 1**

- Input: `rows=3, cols=3, ops=[set(1, 1, 5), get(1, 1)]`
- Output: `[5]`

**Example 2**

- Input: `rows=3, cols=3, ops=[set(1, 1, 1), set(1, 2, 2), sum(2, 2, 1, 1, 1, 2)]`
- Output: `[3]`

**Example 3**

- Input: `rows=3, cols=3, ops=[set(1, 1, 1), sum(1, 2, 1, 1, 1, 1), set(1, 1, 2), get(1, 2)]`
- Output: `[1, 2]`

---

## Underlying Base Algorithm(s)
The system utilizes a **Directed Acyclic Graph (DAG)** to track cell dependencies. Each cell maintains a list of formulas that depend on it. When a cell's value is updated, we perform a topological update or re-evaluation of dependent cells. A **Hash Map** is used to store current cell values and their associated formula definitions.

---

## Complexity Analysis
- **Time Complexity**: `O(K * (N + M))` where `K` is the number of operations, `N` is the number of cells in a range, and `M` is the number of dependencies.
- **Space Complexity**: `O(R * C + D)` where `R*C` is the grid size and `D` is the total number of dependencies stored.
