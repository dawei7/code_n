# Minimum Cost to Make at Least One Valid Path in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1368 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/) |

## Problem Description

### Goal

Each cell of an $R\times C$ grid contains a direction sign: `1` points right, `2` left, `3` down, and `4` up. Following a sign may leave the grid, and the original signs do not necessarily provide a path from the top-left cell to the bottom-right cell.

Changing a cell's sign to another direction costs one, and unchanged signs cost zero. Determine the minimum total modification cost needed so that at least one sequence of followed signs reaches the destination. A cell's sign may be modified at most once.

### Function Contract

**Inputs**

- `grid`: an $R\times C$ matrix whose entries are direction codes from `1` through `4`.

**Return value**

- The minimum number of sign changes required to create a valid path from `(0, 0)` to `(R-1, C-1)`.

### Examples

**Example 1**

- Input: `grid = [[1,1,3],[3,2,2],[1,1,4]]`
- Output: `0`

**Example 2**

- Input: `grid = [[1,1,1],[2,2,2],[1,1,1]]`
- Output: `2`

**Example 3**

- Input: `grid = [[4]]`
- Output: `0`
