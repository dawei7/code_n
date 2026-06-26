## Problem Description & Examples
### Goal
You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [a, b]` indicates that there is an undirected edge between nodes `a` and `b` in the graph.

Return `True` if the edges of the given graph make up a valid tree, and `False` otherwise.

### Function Contract
**Inputs**

- `n`: int
- `edges`: List[List[int]]

**Return value**

bool - True if graph is a valid tree

### Examples
**Example 1**

- Input: `n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]`
- Output: `True`

**Example 2**

- Input: `n = 2, edges = [[1, 0]]`
- Output: `True`

**Example 3**

- Input: `n = 2, edges = [[0, 1]]`
- Output: `True`

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
