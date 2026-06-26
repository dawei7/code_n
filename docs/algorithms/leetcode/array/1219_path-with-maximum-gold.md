# Path with Maximum Gold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1219 |
| Difficulty | Medium |
| Topics | Array, Backtracking, Matrix |
| Official Link | [path-with-maximum-gold](https://leetcode.com/problems/path-with-maximum-gold/) |

## Problem Description & Examples
### Goal
Starting from any nonzero cell, move up, down, left, or right through nonzero cells without visiting a cell twice. Maximize the total gold collected.

### Function Contract
**Inputs**

- `grid`: matrix where `0` is blocked and positive values are gold amounts.

**Return value**

The maximum gold collectable on one valid path.

### Examples
**Example 1**

- Input: `grid = [[0,6,0],[5,8,7],[0,9,0]]`
- Output: `24`

**Example 2**

- Input: `grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]`
- Output: `28`

**Example 3**

- Input: `grid = [[10]]`
- Output: `10`

---

## Underlying Base Algorithm(s)
Backtracking depth-first search on a grid.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n * 3^g)` in the worst case, where `g` is the count of gold cells.
- **Space Complexity**: `O(g)` recursion depth.
