# Shortest Cycle in a Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2608 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-cycle-in-a-graph/) |

## Problem Description

### Goal

A bidirectional graph has $n$ vertices labeled from $0$ through $n-1$. Each pair `edges[i] = [u_i, v_i]` represents one undirected edge between two different vertices.

There is at most one edge between any pair of vertices, and no vertex has an edge to itself. The graph may be disconnected.

Return the number of edges in the shortest cycle. A cycle starts and ends at the same vertex and does not reuse an edge. If the graph contains no cycle, return $-1$.

### Function Contract

**Inputs**

- `n`: The number of vertices, where $2 \leq n \leq 1000$.
- `edges`: A nonempty list of at most $1000$ distinct undirected edges `[u, v]`, with $0 \leq u,v<n$ and $u\ne v$.

Let $m=\lvert\texttt{edges}\rvert$.

**Return value**

- The length of the shortest graph cycle, or $-1$ when the graph is acyclic.

### Examples

#### Example 1

- **Input:** `n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]`
- **Output:** `3`

The first connected component contains the triangle $0\to1\to2\to0$, which is shorter than the four-edge cycle in the other component.

#### Example 2

- **Input:** `n = 4, edges = [[0,1],[0,2]]`
- **Output:** `-1`

The graph is acyclic.
