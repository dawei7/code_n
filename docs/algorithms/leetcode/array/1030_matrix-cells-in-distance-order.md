# Matrix Cells in Distance Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1030 |
| Difficulty | Easy |
| Topics | Array, Math, Geometry, Sorting, Matrix |
| Official Link | [matrix-cells-in-distance-order](https://leetcode.com/problems/matrix-cells-in-distance-order/) |

## Problem Description & Examples
### Goal
Return all coordinates in a `rows x cols` matrix ordered by their Manhattan distance from a given center cell.

### Function Contract
**Inputs**

- `rows`: int
- `cols`: int
- `rCenter`: int
- `cCenter`: int

**Return value**

List[List[int]] - all matrix coordinates in nondecreasing distance order

### Examples
**Example 1**

- Input: `rows = 1, cols = 2, rCenter = 0, cCenter = 0`
- Output: `[[0, 0], [0, 1]]`

**Example 2**

- Input: `rows = 2, cols = 2, rCenter = 0, cCenter = 1`
- Output: `[[0, 1], [0, 0], [1, 1], [1, 0]]`

**Example 3**

- Input: `rows = 2, cols = 3, rCenter = 1, cCenter = 2`
- Output: `[[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]`

---

## Underlying Base Algorithm(s)
Coordinate enumeration sorted by Manhattan distance.

---

## Complexity Analysis
- **Time Complexity**: `O(rows * cols * log(rows * cols))`
- **Space Complexity**: `O(rows * cols)` for the output
