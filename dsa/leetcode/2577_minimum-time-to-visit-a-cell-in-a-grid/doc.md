# Minimum Time to Visit a Cell In a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2577 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Minimum Time to Visit a Cell In a Grid](https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/) |

## Problem Description

### Goal

You are given an $m \times n$ matrix `grid` of non-negative integers. The value `grid[row][col]` is the minimum time at which cell `(row, col)` may be visited: entering that cell at time $t$ is legal only when $t \geq \texttt{grid[row][col]}$.

You begin in the top-left cell `(0, 0)` at time $0$. At every second you must move to an adjacent cell in one of the four cardinal directions; remaining stationary is not allowed. Consequently, passing time may require moving back and forth between already available cells.

Return the minimum time at which the bottom-right cell `(m - 1, n - 1)` can be visited. Return `-1` when no legal first move exists and the destination is therefore unreachable.

### Function Contract

**Inputs**

- `grid`: An $m \times n$ matrix of non-negative integers, where `grid[row][col]` is the earliest permitted visit time for that cell.

The dimensions satisfy $2 \leq m,n \leq 1000$ and $4 \leq mn \leq 10^5$. Every cell value lies between $0$ and $10^5$, inclusive, and `grid[0][0] = 0`.

**Return value**

- The minimum legal arrival time at `(m - 1, n - 1)`, or `-1` if the destination cannot be reached.

### Examples

**Example 1**

- Input: `grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]`
- Output: `7`
- Explanation: A legal route reaches `(0, 1)` at time $1$, uses accessible cells to keep moving while later cells unlock, and first reaches `(2, 3)` at time $7$.

**Example 2**

- Input: `grid = [[0,2,4],[3,2,1],[1,0,4]]`
- Output: `-1`
- Explanation: At time $1$, neither neighbor of `(0, 0)` is available. Because a move is mandatory, no route can begin.
