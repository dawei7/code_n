# Count Sub Islands

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1905 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Count Sub Islands](https://leetcode.com/problems/count-sub-islands/) |

## Problem Description

### Goal

You receive two binary matrices `grid1` and `grid2` with identical dimensions. A value of `1` denotes land and `0` denotes water. Within either grid, an island is a maximal group of land cells connected through shared horizontal or vertical edges; diagonal contact does not connect cells.

An island from `grid2` is a sub-island only when every one of its land cells occupies a land position in `grid1`. Count how many complete `grid2` islands satisfy this containment condition. Cells beyond the matrix boundary are water.

### Function Contract

**Inputs**

- `grid1` and `grid2`: binary matrices with $m$ rows and $n$ columns.
- The dimensions satisfy $1 \le m,n \le 500$ and are equal for both grids.

**Return value**

Return the number of four-directionally connected islands in `grid2` whose every cell is also land in `grid1`.

### Examples

**Example 1**

- Input: `grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]`
- Output: `3`

**Example 2**

- Input: `grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]`
- Output: `2`

**Example 3**

- Input: `grid1 = [[1]], grid2 = [[1]]`
- Output: `1`
