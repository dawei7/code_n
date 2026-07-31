# Determine if a Simple Graph Exists

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3656 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Graph Theory, Sorting, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/determine-if-a-simple-graph-exists/) |

## Problem Description
### Goal

The array `degrees` specifies one desired degree for every labeled vertex. Determine whether some undirected simple graph realizes exactly this degree sequence. A simple graph may contain neither a self-loop nor more than one edge between the same pair of vertices.

Return `true` when at least one such graph exists and `false` otherwise. Only existence matters; you do not need to construct the edges.

### Function Contract
**Inputs**

- `degrees`: An array of $n$ integers, where $1\le n\le10^5$ and $0\le\texttt{degrees[i]}\le n-1$.

**Return value**

Return whether `degrees` is graphical: realizable as the vertex degrees of an undirected simple graph.

### Examples
**Example 1**

- Input: `degrees = [3,1,2,2]`
- Output: `true`
- Explanation: Edges `(0,1)`, `(0,2)`, `(0,3)`, and `(2,3)` realize the requested degrees.

**Example 2**

- Input: `degrees = [1,3,3,1]`
- Output: `false`
- Explanation: Both degree-3 vertices must connect to every other vertex, forcing the two degree-1 vertices to have at least degree 2.
