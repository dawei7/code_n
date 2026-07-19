# Path With Maximum Minimum Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1102 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/path-with-maximum-minimum-value/) |

## Problem Description

### Goal

Given an $m \times n$ integer matrix `grid`, start at the top-left cell `(0, 0)` and reach the bottom-right cell `(m - 1, n - 1)`. Each move goes to a horizontally or vertically adjacent cell; cells may be revisited, although an optimal path never needs a cycle.

The score of a path is the minimum cell value encountered anywhere on it. Among every valid path between the two corners, return the maximum possible score.

### Function Contract

**Inputs**

- `grid`: an $m \times n$ matrix, where $1 \leq m,n \leq 100$ and $0 \leq \texttt{grid[row][col]} \leq 10^9$.

Let $V = mn$ be the number of cells.

**Return value**

The largest achievable minimum cell value over all four-directional paths from the top-left to the bottom-right cell.

### Examples

**Example 1**

- Input: `grid = [[5, 4, 5], [1, 2, 6], [7, 4, 6]]`
- Output: `4`

**Example 2**

- Input: `grid = [[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]]`
- Output: `2`

**Example 3**

- Input: `grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]`
- Output: `3`
