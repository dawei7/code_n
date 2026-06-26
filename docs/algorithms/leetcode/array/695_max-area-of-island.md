# Max Area of Island

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_147` |
| Frontend ID | 695 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Official Link | [max-area-of-island](https://leetcode.com/problems/max-area-of-island/) |

## Problem Description & Examples
### Goal
You are given an `m x n` binary matrix `grid`. An island is a group of `1`s (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value `1` in the island.

Return the maximum area of an island in `grid`. If there is no island, return `0`.

### Function Contract
**Inputs**

- `grid`: List[List[int]]

**Return value**

int - maximum island area

### Examples
**Example 1**

- Input: `grid = [[1, 1], [0, 0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[1, 1], [0, 1]]`
- Output: `3`

**Example 3**

- Input: `grid = [[0, 0], [1, 0]]`
- Output: `1`

---

## Underlying Base Algorithm(s)
- [Breadth-first search](graph_02_bfs.md)
- [Depth-first search](graph_03_dfs.md)
- [Topological sort](graph_07_topological-sort.md)
- [Union-find](graph_09_union-find.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
