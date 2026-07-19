# Coloring A Border

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1034 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/coloring-a-border/) |

## Problem Description

### Goal

You are given an $m\times n$ integer matrix `grid` and integers `row`, `col`, and `color`. Each grid value is the color of that square.

Two squares are adjacent when they share a side in one of the four directions. Squares with the same color belong to one connected component when a path of such adjacent, same-colored squares joins them.

A square on a component's border either lies on the first or last row or column of the grid, or has at least one adjacent square that is not in the component. Recolor only the border of the connected component containing `grid[row][col]` with `color`, then return the final grid.

### Function Contract

**Inputs**

- `grid`: an $m\times n$ color matrix, where $1 \le m,n \le 50$ and every value is between $1$ and $1000$.
- `row` and `col`: a valid starting coordinate in `grid`.
- `color`: the new border color, between $1$ and $1000$.
- Let $P$ be the number of cells in the starting cell's connected component.

**Return value**

- The grid after recoloring exactly the component's border cells.

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
- Explanation: The center belongs to the component but is not on its border.
