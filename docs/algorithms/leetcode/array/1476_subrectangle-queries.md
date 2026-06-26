# Subrectangle Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1476 |
| Difficulty | Medium |
| Topics | Array, Design, Matrix |
| Official Link | [subrectangle-queries](https://leetcode.com/problems/subrectangle-queries/) |

## Problem Description & Examples
### Goal
Design a matrix wrapper that can set every value in a subrectangle and retrieve the current value of a single cell.

### Function Contract
**Inputs**

- Constructor input: `rectangle`, the initial matrix.
- `updateSubrectangle(row1, col1, row2, col2, newValue)`: updates all cells in that inclusive subrectangle.
- `getValue(row, col)`: returns one current cell value.

**Return value**

Updates mutate the stored rectangle; queries return the visible value at the requested cell.

### Examples
**Example 1**

- Input: `SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]); getValue(0,2); updateSubrectangle(0,0,3,2,5); getValue(0,2)`
- Output: `[1,5]`

**Example 2**

- Input: `SubrectangleQueries([[1,1],[2,2]]); updateSubrectangle(0,0,0,0,7); getValue(0,0); getValue(1,1)`
- Output: `[7,2]`

**Example 3**

- Input: `SubrectangleQueries([[3]]); getValue(0,0); updateSubrectangle(0,0,0,0,9); getValue(0,0)`
- Output: `[3,9]`

---

## Underlying Base Algorithm(s)
Either apply each update directly to the matrix, or store updates lazily and answer queries by checking the most recent covering update. The direct approach is simple and fast enough for modest dimensions.

---

## Complexity Analysis
- **Time Complexity**: `O(area)` per direct update and `O(1)` per query.
- **Space Complexity**: `O(1)` extra beyond the stored matrix.
