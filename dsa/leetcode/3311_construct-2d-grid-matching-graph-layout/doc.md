# Construct 2D Grid Matching Graph Layout

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3311 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Graph Theory, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/) |

## Problem Description

### Goal

An undirected graph has `n` vertices numbered from `0` through `n - 1`. Construct a nonempty rectangular grid whose cells contain every vertex exactly once. Two vertices must occupy horizontally or vertically adjacent cells if and only if their pair appears in `edges`; diagonal contact does not create an adjacency.

The graph is guaranteed to admit at least one such rectangular embedding, but its row and column counts are not supplied. Return any valid layout. Rotations, reflections, and transpositions are all acceptable when they preserve the graph's complete adjacency relation.

### Function Contract

**Inputs**

- `n`: The number of graph vertices, where $2\leq n\leq5\cdot10^4$.
- `edges`: Between 1 and $10^5$ distinct undirected pairs `[u, v]`, with $0\leq u<v<n$.

The input graph is guaranteed to be exactly representable as a rectangular grid graph.

**Return value**

Return any rectangular matrix containing every vertex once such that its horizontal and vertical adjacency pairs are exactly `edges`.

### Examples

**Example 1**

- Input: `n = 4, edges = [[0, 1], [0, 2], [1, 3], [2, 3]]`
- Output: `[[3, 1], [2, 0]]`

Every side of this $2\times2$ arrangement corresponds to one supplied edge.

**Example 2**

- Input: `n = 5, edges = [[0, 1], [1, 3], [2, 3], [2, 4]]`
- Output: `[[4, 2, 3, 1, 0]]`

The graph is a path, so a one-row layout is valid.

**Example 3**

- Input: `n = 9, edges = [[0,1],[0,4],[0,5],[1,7],[2,3],[2,4],[2,5],[3,6],[4,6],[4,7],[6,8],[7,8]]`
- Output: `[[8, 6, 3], [7, 4, 2], [1, 0, 5]]`
