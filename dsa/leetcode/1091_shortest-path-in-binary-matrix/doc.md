# Shortest Path in Binary Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1091 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/shortest-path-in-binary-matrix/) |

## Problem Description

### Goal

Given an $n\times n$ binary matrix `grid`, find a clear path from the top-left cell `(0, 0)` to the bottom-right cell `(n - 1, n - 1)`. Every visited cell must contain `0`.

Consecutive path cells must be different and 8-directionally connected: they may share either an edge or a corner. The path length is its number of visited cells, including both endpoints. Return the length of the shortest clear path, or `-1` when no clear path exists.

### Function Contract

**Inputs**

- `grid`: an $n\times n$ matrix containing only 0 and 1, where $1 \le n \le 100$.

**Return value**

- The minimum number of cells on a clear path from `(0, 0)` to `(n - 1, n - 1)`, or `-1` if no such path exists.

### Examples

**Example 1**

- Input: `grid = [[0, 1], [1, 0]]`
- Output: `2`

The two open cells touch at a corner, so the diagonal is a valid two-cell path.

**Example 2**

- Input: `grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]`
- Output: `-1`
