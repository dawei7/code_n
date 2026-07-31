# Minimum Number of Visited Cells in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2617 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/) |

## Problem Description

### Goal

You are given a 0-indexed $m\times n$ integer matrix `grid` and begin at its top-left cell `(0, 0)`.

From `(i, j)`, you may move right to `(i, k)` for any $j<k\leq j+\texttt{grid}[i][j]$, or move down to `(k, j)` for any $i<k\leq i+\texttt{grid}[i][j]$. A destination must remain inside the matrix; moves never go left or upward.

Return the minimum number of cells visited by a path that reaches `(m - 1, n - 1)`. The starting and ending cells both count. Return $-1$ when the bottom-right cell cannot be reached.

### Function Contract

**Inputs**

- `grid`: An $m\times n$ matrix where $1\leq m,n\leq 10^5$, $1\leq mn\leq 10^5$, $0\leq \texttt{grid}[i][j]<mn$, and the bottom-right value is $0$.

**Return value**

Return the minimum number of visited cells required to reach the bottom-right corner, or $-1$ if no valid path exists.

### Examples

**Example 1**

- Input: `grid = [[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]]`
- Output: `4`
- Explanation: A shortest valid path includes the start, two intermediate cells, and the destination.

**Example 2**

- Input: `grid = [[3, 4, 2, 1], [4, 2, 1, 1], [2, 1, 1, 0], [3, 4, 1, 0]]`
- Output: `3`
- Explanation: The destination can be reached while visiting three cells.

**Example 3**

- Input: `grid = [[2, 1, 0], [1, 0, 0]]`
- Output: `-1`
- Explanation: Every possible forward path stops before the destination.
