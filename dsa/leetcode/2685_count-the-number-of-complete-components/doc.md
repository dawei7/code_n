# Count the Number of Complete Components

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2685 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [count-the-number-of-complete-components](https://leetcode.com/problems/count-the-number-of-complete-components/) |

## Problem Description

### Goal

An undirected graph has `n` vertices numbered from $0$ through $n-1$. Each pair in `edges` connects two distinct vertices, and no undirected edge is repeated.

A connected component contains exactly the vertices that can reach one another without crossing to a vertex outside the component. Such a component is complete when every pair of distinct vertices in it is joined by an edge. Return how many connected components of the graph are complete. An isolated vertex counts as a complete component because it has no missing pair of vertices.

### Function Contract

**Inputs**

- `n`: The number of vertices, where $1 \le n \le 50$.
- `edges`: The undirected edges. Its length is at most $n(n-1)/2$; every entry contains two different valid vertex indices, and no edge occurs twice.

**Return value**

Return the number of connected components in which every pair of distinct vertices has an edge.

### Examples

#### Example 1

- **Input:** `n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]`
- **Output:** `3`
- **Explanation:** Vertices `0`, `1`, and `2` form a triangle, `3` and `4` form a complete two-vertex component, and vertex `5` is isolated. All three components are complete.

#### Example 2

- **Input:** `n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]`
- **Output:** `1`
- **Explanation:** The triangle on `0`, `1`, and `2` is complete. The other component is missing the edge between `4` and `5`, so it is not complete.

#### Example 3

- **Input:** `n = 1, edges = []`
- **Output:** `1`
- **Explanation:** The single isolated vertex is a complete component.
