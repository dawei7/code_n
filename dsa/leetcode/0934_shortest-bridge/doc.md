# Shortest Bridge

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 934 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [shortest-bridge](https://leetcode.com/problems/shortest-bridge/) |

## Problem Description

### Goal

An $n \times n$ binary `grid` uses `1` for land and `0` for water. An island is a maximal group of land cells connected vertically or horizontally; diagonal contact alone does not connect cells. The input contains exactly two islands.

You may change water cells from `0` to `1`. Return the smallest number of water cells that must be flipped so the two original islands become one four-directionally connected island. The bridge may pass through any water cells but must connect the existing land groups.

### Function Contract

**Inputs**

- `grid`: an $n \times n$ binary matrix, where $2 \le n \le 100$ and exactly two four-directionally connected islands are present.

**Return value**

Return the minimum number of water cells that must be changed to land to connect the two islands.

### Examples

**Example 1**

- Input: `grid = [[0,1],[1,0]]`
- Output: `1`

**Example 2**

- Input: `grid = [[0,1,0],[0,0,0],[0,0,1]]`
- Output: `2`

**Example 3**

- Input: `grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]`
- Output: `1`
