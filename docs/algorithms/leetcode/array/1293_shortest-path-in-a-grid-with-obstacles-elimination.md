# Shortest Path in a Grid with Obstacles Elimination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1293 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Matrix |
| Official Link | [shortest-path-in-a-grid-with-obstacles-elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) |

## Problem Description & Examples
### Goal
Move from the top-left to the bottom-right of a grid in the fewest steps. You may pass through at most `k` obstacle cells by eliminating them.

### Function Contract
**Inputs**

- `grid`: binary matrix where `1` is an obstacle.
- `k`: maximum number of obstacles that may be removed.

**Return value**

The shortest path length, or `-1` if the target cannot be reached.

### Examples
**Example 1**

- Input: `grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]`, `k = 1`
- Output: `6`

**Example 2**

- Input: `grid = [[0,1,1],[1,1,1],[1,0,0]]`, `k = 1`
- Output: `-1`

**Example 3**

- Input: `grid = [[0,1],[0,0]]`, `k = 0`
- Output: `2`

---

## Underlying Base Algorithm(s)
Breadth-first search with remaining-resource state.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n * (k + 1))`
- **Space Complexity**: `O(m * n * (k + 1))`
