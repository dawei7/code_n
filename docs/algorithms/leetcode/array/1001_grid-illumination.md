# Grid Illumination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1001 |
| Difficulty | Hard |
| Topics | Array, Hash Table |
| Official Link | [grid-illumination](https://leetcode.com/problems/grid-illumination/) |

## Problem Description & Examples
### Goal
On an `n x n` grid, lamps illuminate their row, column, and both diagonals. For each query cell, report whether it is illuminated, then switch off any lamps in that cell or its eight neighboring cells.

### Function Contract
**Inputs**

- `n`: int grid size
- `lamps`: List[List[int]] lamp coordinates
- `queries`: List[List[int]] queried coordinates

**Return value**

List[int] - `1` for illuminated query cells, otherwise `0`

### Examples
**Example 1**

- Input: `n = 5, lamps = [[0, 0], [4, 4]], queries = [[1, 1], [1, 0]]`
- Output: `[1, 0]`

**Example 2**

- Input: `n = 5, lamps = [[0, 0], [4, 4]], queries = [[1, 1], [1, 1]]`
- Output: `[1, 1]`

**Example 3**

- Input: `n = 3, lamps = [[0, 0], [1, 1]], queries = [[1, 1], [2, 2]]`
- Output: `[1, 0]`

---

## Underlying Base Algorithm(s)
Hash maps for row, column, and diagonal illumination counts.

---

## Complexity Analysis
- **Time Complexity**: `O(l + q)` for `l` lamps and `q` queries
- **Space Complexity**: `O(l)`
