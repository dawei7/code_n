# Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_171` |
| Frontend ID | 1489 |
| Difficulty | Hard |
| Topics | Union-Find, Graph Theory, Sorting, Minimum Spanning Tree, Strongly Connected Component |
| Official Link | [find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) |

## Problem Description & Examples
### Goal
Given a weighted undirected connected graph with `n` vertices numbered from `0` to `n - 1`, and an array `edges` where `edges[i] = [ai, bi, weighti]` represents a bidirectional and weighted edge between nodes `ai` and `bi`. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST).

An MST edge is critical if deleting it increases the MST weight. An edge is pseudo-critical if it can appear in at least one MST, but not necessarily all.

Return a list of two lists: `[critical_edges, pseudo_critical_edges]`.

### Function Contract
**Inputs**

- `n`: int
- `edges`: List[List[int]]

**Return value**

List[List[int]] - critical and pseudo-critical edge indices

### Examples
**Example 1**

- Input: `n = 4, edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]`
- Output: `[[], [0, 1, 2, 3]]`

**Example 2**

- Input: `n = 3, edges = [[0, 1, 7], [0, 2, 5]]`
- Output: `[[0, 1], []]`

**Example 3**

- Input: `n = 3, edges = [[0, 1, 10], [0, 2, 5]]`
- Output: `[[0, 1], []]`

---

## Underlying Base Algorithm(s)
- [Dijkstra shortest path](graph_04_dijkstra.md)
- [Kruskal minimum spanning tree](graph_08_kruskal-s-mst.md)
- [Prim minimum spanning tree](graph_10_prim-s-mst.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
