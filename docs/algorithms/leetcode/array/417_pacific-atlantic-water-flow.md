# Pacific Atlantic Water Flow

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_151` |
| Frontend ID | 417 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Official Link | [pacific-atlantic-water-flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) |

## Problem Description & Examples
### Goal
There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

Water can flow in 4 directions (up, down, left, right) from a cell to another one with an equal or lower height.

Return a list of grid coordinates `[r, c]` where water can flow to both the Pacific and Atlantic oceans.

### Function Contract
**Inputs**

- `heights`: List[List[int]]

**Return value**

List[List[int]] - cells that flow to both oceans

### Examples
**Example 1**

- Input: `heights = [[1, 2], [2, 1]]`
- Output: `[[0, 0], [0, 1], [1, 0], [1, 1]]`

**Example 2**

- Input: `heights = [[13, 14], [2, 9]]`
- Output: `[[0, 0], [0, 1], [1, 0], [1, 1]]`

**Example 3**

- Input: `heights = [[5, 19], [3, 9]]`
- Output: `[[0, 0], [0, 1], [1, 0], [1, 1]]`

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
