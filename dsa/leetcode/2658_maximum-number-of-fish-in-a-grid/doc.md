# Maximum Number of Fish in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2658 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/) |

## Problem Description

### Goal

You are given a 0-indexed $m \times n$ matrix `grid`. A cell containing `0` is land. A positive cell is water and contains exactly `grid[r][c]` fish. A fisher may choose any water cell as a starting point, catch all fish in the current cell, and move any number of times between orthogonally adjacent water cells.

Return the largest total number of fish obtainable by choosing the starting cell optimally and visiting every reachable water cell. Movement never passes through land and diagonal cells are not adjacent. If the matrix contains no water cell, return `0`.

### Function Contract

**Inputs**

- `grid`: An $m \times n$ integer matrix, where $1 \le m,n \le 10$ and $0 \le \texttt{grid[r][c]} \le 10$.

**Return value**

- Return the maximum sum of fish in one four-directionally connected component of positive cells, or `0` if none exists.

### Examples

**Example 1**

- Input: `grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]`
- Output: `7`
- Explanation: The connected cells containing `3` and `4` form the richest reachable water component.

**Example 2**

- Input: `grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]`
- Output: `1`
- Explanation: The two water cells are isolated from each other, and either contains one fish.
