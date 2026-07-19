# Number of Connected Components in an Undirected Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 323 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) |

## Problem Description
### Goal
Given `n` vertices labeled `0` through $n - 1$ and undirected edges between selected pairs, group vertices that can reach one another through any sequence of edges. Each maximal mutually reachable group is one connected component.

Return the total number of components. An isolated vertex with no incident edge forms a component by itself, while cycles and multiple routes within a group do not increase the count. Edges have no direction, and components may contain any number of vertices. When there are no edges, the answer is `n`; the task returns only the count, not the groups.

### Function Contract
**Inputs**

- `n`: the number of vertices
- `edges`: pairs `[u, v]` representing undirected edges

**Return value**

The number of maximal groups of vertices connected by paths.

### Examples
**Example 1**

- Input: `n = 5, edges = [[0,1],[1,2],[3,4]]`
- Output: `2`

**Example 2**

- Input: `n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]`
- Output: `1`

**Example 3**

- Input: `n = 4, edges = []`
- Output: `4`
