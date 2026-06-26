# Redundant Connection

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_159` |
| Frontend ID | 684 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Official Link | [redundant-connection](https://leetcode.com/problems/redundant-connection/) |

## Problem Description & Examples
### Goal
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.

Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input.

### Function Contract
**Inputs**

- `edges`: List[List[int]]

**Return value**

List[int] - redundant edge

### Examples
**Example 1**

- Input: `edges = [[1, 2], [1, 3], [2, 3]]`
- Output: `[2, 3]`

**Example 2**

- Input: `edges = [[1, 2], [2, 3], [1, 2]]`
- Output: `[1, 2]`

**Example 3**

- Input: `edges = [[1, 2], [1, 3], [2, 1]]`
- Output: `[2, 1]`

---

## Underlying Base Algorithm(s)
- [Breadth-first search](graph_02_bfs.md)
- [Depth-first search](graph_03_dfs.md)
- [Topological sort](graph_07_topological-sort.md)
- [Union-find](graph_09_union-find.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
