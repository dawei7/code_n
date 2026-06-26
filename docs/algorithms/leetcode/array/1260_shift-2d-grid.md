# Shift 2D Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1260 |
| Difficulty | Easy |
| Topics | Array, Matrix, Simulation |
| Official Link | [shift-2d-grid](https://leetcode.com/problems/shift-2d-grid/) |

## Problem Description & Examples
### Goal
Shift every value in a matrix to the right by `k` positions, wrapping from the end of a row to the start of the next row and from the last cell to the first cell.

### Function Contract
**Inputs**

- `grid`: `m x n` matrix.
- `k`: number of shifts.

**Return value**

The shifted matrix.

### Examples
**Example 1**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 1`
- Output: `[[9,1,2],[3,4,5],[6,7,8]]`

**Example 2**

- Input: `grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]`, `k = 4`
- Output: `[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]`

**Example 3**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 9`
- Output: `[[1,2,3],[4,5,6],[7,8,9]]`

---

## Underlying Base Algorithm(s)
Index mapping in a flattened matrix.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)` for the returned grid.
