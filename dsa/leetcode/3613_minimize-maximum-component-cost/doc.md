# Minimize Maximum Component Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3613 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Binary Search, Union-Find, Graph Theory, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-maximum-component-cost/) |

## Problem Description
### Goal

An undirected connected graph has `n` nodes numbered from $0$ through $n-1`. Each entry `[u, v, w]` in `edges` represents an undirected edge between `u` and `v` with positive weight `w`. You may remove any number of edges, provided the remaining graph contains at most `k` connected components.

The cost of a connected component is the greatest weight among the edges retained inside it. An isolated node has component cost $0$. For a chosen set of removals, the overall cost is the greatest component cost. Return the minimum overall cost attainable while respecting the component limit.

### Function Contract

**Inputs**

- `n`: The number of graph nodes.
- `edges`: The undirected weighted edges as `[u, v, w]` triples.
- `k`: The maximum permitted number of connected components after removals.

The constraints are $1 \le n \le 5\cdot 10^4$, at most $10^5$ edges, $1 \le w \le 10^6$, and $1 \le k \le n$. The input graph is connected.

**Return value**

Return the smallest possible maximum component cost after removing edges while leaving at most `k` connected components.

### Examples

**Example 1**

- Input: `n = 5, edges = [[0, 1, 4], [1, 2, 3], [1, 3, 2], [3, 4, 6]], k = 2`
- Output: `4`
- Explanation: Removing the weight-6 edge isolates node 4; the other component's largest retained weight is 4.

**Example 2**

- Input: `n = 4, edges = [[0, 1, 5], [1, 2, 5], [2, 3, 5]], k = 1`
- Output: `5`
- Explanation: The graph must remain connected, so all three chain edges are required.

**Example 3**

- Input: `n = 3, edges = [[0, 1, 8], [1, 2, 2]], k = 3`
- Output: `0`
- Explanation: Removing every edge leaves three permitted isolated components, each with cost 0.
