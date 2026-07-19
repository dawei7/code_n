# Range Sum Query 2D - Mutable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 308 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Design, Binary Indexed Tree, Segment Tree, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/range-sum-query-2d-mutable/) |

## Problem Description
### Goal
Construct a mutable range-sum structure from a nonempty rectangular integer matrix. `update(row, column, value)` assigns a new value to one cell, and `sumRegion(row1, col1, row2, col2)` queries the current matrix after all earlier updates.

Return each rectangle's sum including both corner rows and columns, with update calls producing no output. Updates replace rather than add to the old cell value. Support an interleaved operation sequence efficiently without rebuilding all prefix information or scanning every queried cell. The app collects query results in order, while the native `NumMatrix` persists the changing matrix across method calls.

### Function Contract
**Inputs**

- `matrix`: the initial nonempty rectangular integer matrix
- `operations`: ordered commands `["update", row, column, value]` or `["sum", row1, col1, row2, col2]`

**Return value**

The result of every `sum` command in operation order. Updates produce no output.

### Examples
**Example 1**

- Input: the standard 5×5 matrix, then `sum(2,1,4,3)`, `update(3,2,2)`, `sum(2,1,4,3)`
- Output: `[8,10]`

**Example 2**

- Input: `matrix = [[5]], operations = [["sum",0,0,0,0],["update",0,0,-2],["sum",0,0,0,0]]`
- Output: `[5,-2]`

**Example 3**

- Input: `matrix = [[1,2],[3,4]], operations = [["sum",0,0,1,1],["update",0,1,5],["sum",0,1,1,1]]`
- Output: `[10,9]`
