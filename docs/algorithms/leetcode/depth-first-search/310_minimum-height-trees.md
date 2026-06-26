# Minimum Height Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_162` |
| Frontend ID | 310 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Official Link | [minimum-height-trees](https://leetcode.com/problems/minimum-height-trees/) |

## Problem Description & Examples
### Goal
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of `n` nodes labelled from `0` to `n - 1`, and an array of `n - 1` `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between the two nodes `ai` and `bi` in the tree, choose any node as the root. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

### Function Contract
**Inputs**

- `n`: int
- `edges`: List[List[int]]

**Return value**

List[int] - root labels of MHTs

### Examples
**Example 1**

- Input: `n = 4, edges = [[1, 0], [1, 2], [1, 3]]`
- Output: `[1]`

**Example 2**

- Input: `n = 3, edges = [[0, 1], [1, 2]]`
- Output: `[1]`

**Example 3**

- Input: `n = 3, edges = [[0, 1], [0, 2]]`
- Output: `[0]`

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
