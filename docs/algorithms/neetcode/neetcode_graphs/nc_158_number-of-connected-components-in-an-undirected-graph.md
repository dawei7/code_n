## Problem Description & Examples
### Goal
You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where `edges[i] = [a, b]` indicates that there is an edge between `a` and `b` in the graph.

Return the number of connected components in the graph.

### Function Contract
**Inputs**

- `n`: int
- `edges`: List[List[int]]

**Return value**

int - number of components

### Examples
**Example 1**

- Input: `n = 5, edges = [[0, 1], [1, 2], [3, 4]]`
- Output: `2`

**Example 2**

- Input: `n = 2, edges = []`
- Output: `2`

**Example 3**

- Input: `n = 2, edges = [[0, 1]]`
- Output: `1`

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
