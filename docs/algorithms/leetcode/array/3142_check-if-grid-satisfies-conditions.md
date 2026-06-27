# Check if Grid Satisfies Conditions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3142 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [check-if-grid-satisfies-conditions](https://leetcode.com/problems/check-if-grid-satisfies-conditions/) |

## Problem Description & Examples
### Goal
Determine if a 2D grid of integers adheres to two specific structural rules: every cell must be equal to the cell directly below it (if one exists), and every cell must be different from the cell immediately to its right (if one exists).

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the matrix.

**Return value**

- `bool`: Returns `True` if the grid satisfies both conditions, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = [[1,0,2],[1,0,2]]`
- Output: `True`

**Example 2**

- Input: `grid = [[1,1,1],[0,0,0]]`
- Output: `False`

**Example 3**

- Input: `grid = [[1],[2],[3]]`
- Output: `False`

---

## Underlying Base Algorithm(s)
The solution utilizes a linear scan (nested iteration) over the grid dimensions. By checking the vertical adjacency condition `grid[r][c] == grid[r+1][c]` and the horizontal adjacency condition `grid[r][c] != grid[r][c+1]`, we can validate the grid properties in a single pass.

---

## Complexity Analysis
- **Time Complexity**: `O(R * C)`, where `R` is the number of rows and `C` is the number of columns, as we visit each cell at most once.
- **Space Complexity**: `O(1)`, as we perform the validation in-place without allocating extra data structures.
