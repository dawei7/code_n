# Maximum Number of Moves in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2684 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/) |

## Problem Description

### Goal

You are given an $m \times n$ matrix `grid` of positive integers. A path may start at any cell in the first column.

From `(row, col)`, one move must enter the next column at `(row - 1, col + 1)`, `(row, col + 1)`, or `(row + 1, col + 1)`, provided the destination remains inside the matrix and its value is strictly greater than the current value. Return the maximum number of moves achievable by any valid path.

### Function Contract

**Inputs**

- `grid`: A rectangular matrix with $2 \leq m,n \leq 1000$, $4 \leq mn \leq 10^5$, and values from 1 through $10^6$.

**Return value**

Return the greatest number of valid rightward moves from any first-column starting cell.

### Examples

**Example 1**

- Input: `grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]`
- Output: `3`

**Example 2**

- Input: `grid = [[3,2,4],[2,1,9],[1,1,7]]`
- Output: `0`
