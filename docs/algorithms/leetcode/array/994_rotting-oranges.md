# Rotting Oranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_150` |
| Frontend ID | 994 |
| Difficulty | Medium |
| Topics | Array, Breadth-First Search, Matrix |
| Official Link | [rotting-oranges](https://leetcode.com/problems/rotting-oranges/) |

## Problem Description & Examples
### Goal
You are given an `m x n` `grid` where each cell can have one of three values:
- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

### Function Contract
**Inputs**

- `grid`: List[List[int]]

**Return value**

int - minimum minutes needed, or -1

### Examples
**Example 1**

- Input: `grid = [[2, 1], [1, 0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[1, 1], [0, 1]]`
- Output: `-1`

**Example 3**

- Input: `grid = [[0, 2], [0, 1]]`
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
