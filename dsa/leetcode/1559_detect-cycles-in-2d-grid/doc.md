# Detect Cycles in 2D Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1559 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/detect-cycles-in-2d-grid/) |

## Problem Description
### Goal

You are given an $R \times C$ grid of lowercase English letters. Two cells are adjacent when they share a horizontal or vertical side. A valid cycle is a path of at least four cells whose cells all contain the same letter, whose first and last cells are adjacent, and which does not reuse any cell except for closing the path at its start.

Determine whether at least one such cycle exists anywhere in the grid. The cycle may belong to any same-letter connected component and does not need to touch the grid boundary.

### Function Contract
**Inputs**

- `grid`: A rectangular matrix with $2 \le R,C \le 500$.
- Every `grid[r][c]` is a lowercase English letter. Movement is allowed only up, down, left, or right.

**Return value**

Return `true` if the grid contains a valid same-letter cycle of length at least four; otherwise return `false`.

### Examples
**Example 1**

- Input: `grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]`
- Output: `true`

**Example 2**

- Input: `grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]`
- Output: `true`

**Example 3**

- Input: `grid = [["a","b","b"],["b","z","b"],["b","b","a"]]`
- Output: `false`
