# Path with Maximum Gold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1219 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/path-with-maximum-gold/) |

## Problem Description

### Goal

You are given a gold mine represented by a grid. Each cell contains a nonnegative integer: a positive value is the amount of gold in that cell, while `0` represents an empty cell. Whenever you enter a gold cell, you collect all of its gold.

From a cell, you may walk one step left, right, up, or down. A path may never enter a `0` cell and may not visit the same cell more than once. You may choose any gold cell as the starting point and may stop at any gold cell.

Return the maximum amount of gold that can be collected along one valid path.

### Function Contract

**Inputs**

- `grid`: An $m\times n$ matrix, where $1\le m,n\le15$ and $0\le\texttt{grid[r][c]}\le100$.

Let $g$ be the number of cells containing gold. The input guarantees $g\le25$.

**Return value**

- The greatest total gold obtainable from one path that obeys all movement and visitation rules.

### Examples

**Example 1**

- Input: `grid = [[0,6,0],[5,8,7],[0,9,0]]`
- Output: `24`

The path `9 -> 8 -> 7` collects `24` gold.

**Example 2**

- Input: `grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]`
- Output: `28`

The path `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7` collects `28` gold.

**Example 3**

- Input: `grid = [[10]]`
- Output: `10`
