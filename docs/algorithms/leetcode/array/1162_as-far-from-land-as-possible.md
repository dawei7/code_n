# As Far from Land as Possible

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1162 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Breadth-First Search, Matrix |
| Official Link | [as-far-from-land-as-possible](https://leetcode.com/problems/as-far-from-land-as-possible/) |

## Problem Description & Examples
### Goal
In a square grid of water (`0`) and land (`1`), find the water cell whose Manhattan distance to the nearest land cell is as large as possible.

### Function Contract
**Inputs**

- `grid`: an `n x n` matrix of `0` and `1`.

**Return value**

The maximum distance from a water cell to its nearest land cell, or `-1` if the grid has no water or no land.

### Examples
**Example 1**

- Input: `grid = [[1,0,1],[0,0,0],[1,0,1]]`
- Output: `2`

**Example 2**

- Input: `grid = [[1,0,0],[0,0,0],[0,0,0]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1,1],[1,1]]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Multi-source breadth-first search.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)` for the queue in the worst case.
