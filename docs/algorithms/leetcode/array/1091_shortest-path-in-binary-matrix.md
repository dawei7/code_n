# Shortest Path in Binary Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1091 |
| Difficulty | Medium |
| Topics | Array, Breadth-First Search, Matrix |
| Official Link | [shortest-path-in-binary-matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) |

## Problem Description & Examples
### Goal
In a square binary grid, find the length of the shortest clear path from the top-left cell to the bottom-right cell. A path may move in any of the eight neighboring directions, and it may only step on cells containing `0`.

### Function Contract
**Inputs**

- `grid`: an `n x n` matrix of `0` and `1` values.

**Return value**

The number of cells in the shortest valid path, or `-1` if no path exists.

### Examples
**Example 1**

- Input: `grid = [[0,1],[1,0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[0,0,0],[1,1,0],[1,1,0]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1,0,0],[1,1,0],[1,1,0]]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Breadth-first search on an unweighted grid graph.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)` for the BFS queue in the worst case.
