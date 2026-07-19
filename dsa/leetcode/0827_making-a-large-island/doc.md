# Making A Large Island

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 827 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/making-a-large-island/) |

## Problem Description

### Goal

You are given an $n \times n$ binary matrix `grid`. An island is a group of cells containing `1` that are connected 4-directionally: consecutive cells share a horizontal or vertical side, while diagonal contact alone does not connect them. The size of an island is its number of cells.

You may change at most one cell containing `0` into `1`. Choose whether and where to apply that operation so that the resulting grid contains an island as large as possible. Return the size of that largest island. If the grid already contains only `1` cells, the unchanged whole grid is the answer.

### Function Contract

**Inputs**

- `grid`: an $n \times n$ matrix whose entries are `0` or `1`, where $1 \le n \le 500$

**Return value**

- The maximum size of a 4-directionally connected island after changing at most one `0` to `1`

### Examples

**Example 1**

- Input: `grid = [[1, 0], [0, 1]]`
- Output: `3`
- Explanation: Changing either `0` that touches both existing `1` cells joins them through the new land cell.

**Example 2**

- Input: `grid = [[1, 1], [1, 0]]`
- Output: `4`
- Explanation: Changing the only `0` extends the existing island to the entire grid.

**Example 3**

- Input: `grid = [[1, 1], [1, 1]]`
- Output: `4`
- Explanation: There is no `0` to change, and the existing island already occupies all four cells.
