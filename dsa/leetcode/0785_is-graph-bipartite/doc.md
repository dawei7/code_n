# Is Graph Bipartite?

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 785 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/is-graph-bipartite/) |

## Problem Description

### Goal

Given an undirected graph as an adjacency list, determine whether it is bipartite. A bipartite graph's vertices can be divided into two disjoint groups so that every edge connects a vertex in one group to a vertex in the other.

Return `True` if such a division exists and `False` otherwise. Every vertex must belong to one group, disconnected components may choose their group orientations independently, and no edge may have both endpoints in the same group.

### Function Contract

**Inputs**

- `graph`: an adjacency list where `graph[node]` contains every vertex joined to `node`; vertices are numbered from `0` through `len(graph) - 1`.

**Return value**

- `True` if the graph is bipartite; otherwise `False`.

### Examples

**Example 1**

- Input: `graph = [[1,2,3],[0,2],[0,1,3],[0,2]]`
- Output: `False`
- Explanation: Vertices `0`, `1`, and `2` form an odd cycle.

**Example 2**

- Input: `graph = [[1,3],[0,2],[1,3],[0,2]]`
- Output: `True`
- Explanation: The four-cycle can be split into groups `{0,2}` and `{1,3}`.

**Example 3**

- Input: `graph = [[],[]]`
- Output: `True`
- Explanation: Isolated vertices impose no cross-group conflicts.
