# Path With Minimum Effort

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1631 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/path-with-minimum-effort/) |

## Problem Description
### Goal
A hiker starts at the top-left cell of a rectangular `heights` grid and must reach the bottom-right cell. Each cell records its elevation. From a cell, the hiker may move up, down, left, or right while remaining inside the grid.

The effort of a route is not the sum of its climbs. It is the greatest absolute height difference across any single pair of consecutive cells on that route. Return the minimum possible effort among all routes from the start to the destination.

### Function Contract
**Inputs**

- `heights`: an $R\times C$ integer matrix, where $1 \le R,C \le 100$ and $1 \le \texttt{heights[r][c]} \le 10^6$.
- Let $V=RC$ be the number of cells.

**Return value**

Return the minimum achievable maximum edge difference on a four-directional path from `(0,0)` to `(R - 1,C - 1)`.

### Examples
**Example 1**

- Input: `heights = [[1,2,2],[3,8,2],[5,3,5]]`
- Output: `2`

A route through heights `[1,3,5,3,5]` never changes by more than 2.

**Example 2**

- Input: `heights = [[1,2,3],[3,8,4],[5,3,5]]`
- Output: `1`

Following `[1,2,3,4,5]` keeps every step difference at 1.

**Example 3**

- Input: `heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]`
- Output: `0`

There is a start-to-finish route consisting entirely of height-1 cells.
