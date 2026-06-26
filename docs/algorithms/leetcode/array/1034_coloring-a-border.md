# Coloring A Border

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1034 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Official Link | [coloring-a-border](https://leetcode.com/problems/coloring-a-border/) |

## Problem Description & Examples
### Goal
Starting from a cell in a grid, find its connected component of equal-colored cells. Recolor only the border cells of that component.

### Function Contract
**Inputs**

- `grid`: List[List[int]]
- `row`: int starting row
- `col`: int starting column
- `color`: int new border color

**Return value**

List[List[int]] - updated grid

### Examples
**Example 1**

- Input: `grid = [[1,1],[1,2]], row = 0, col = 0, color = 3`
- Output: `[[3,3],[3,2]]`

**Example 2**

- Input: `grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3`
- Output: `[[1,3,3],[2,3,3]]`

**Example 3**

- Input: `grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2`
- Output: `[[2,2,2],[2,1,2],[2,2,2]]`

---

## Underlying Base Algorithm(s)
DFS component traversal with border detection.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)` worst-case visited/recursion space
