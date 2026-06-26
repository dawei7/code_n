## Problem Description & Examples
### Goal
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

In this simulation, the graph is represented as adjacency list `adj_list` where `adj_list[i]` is a list of 1-indexed node labels connected to the `(i+1)`-th node.

Return the cloned adjacency list.

### Function Contract
**Inputs**

- `adj_list`: List[List[int]]

**Return value**

List[List[int]] - deep copy of the adjacency list

### Examples
**Example 1**

- Input: `adj_list = [[2], [1]]`
- Output: `[[2], [1]]`

**Example 2**

- Input: `adj_list = [[], []]`
- Output: `[[], []]`

**Example 3**

- Input: `adj_list = [[2], [1]]`
- Output: `[[2], [1]]`

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
