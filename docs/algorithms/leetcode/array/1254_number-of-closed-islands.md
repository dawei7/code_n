# Number of Closed Islands

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1254 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Official Link | [number-of-closed-islands](https://leetcode.com/problems/number-of-closed-islands/) |

## Problem Description & Examples
### Goal
Count islands of `0` cells that are completely surrounded by `1` cells and do not touch the grid border.

### Function Contract
**Inputs**

- `grid`: matrix where `0` is land and `1` is water.

**Return value**

The number of closed land islands.

### Examples
**Example 1**

- Input: `grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[1,1,1],[1,0,1],[1,1,1]]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Flood fill / depth-first search.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)` recursion depth in the worst case.
