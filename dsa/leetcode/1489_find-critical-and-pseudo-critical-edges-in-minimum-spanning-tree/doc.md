# Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1489 |
| Difficulty | Hard |
| Topics | Union-Find, Graph Theory, Sorting, Minimum Spanning Tree, Strongly Connected Component |
| Official Link | [LeetCode](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) |

## Problem Description
### Goal

A connected, weighted, undirected graph has `n` vertices numbered from `0` through `n - 1`. Each `edges[i] = [a, b, weight]` describes one bidirectional edge, and index `i` is that edge's identity in the requested output. A minimum spanning tree (MST) connects every vertex without a cycle and has the minimum possible total weight.

Classify the original edge indices. An edge is **critical** when removing it makes the best possible spanning-tree weight larger, so it belongs to every MST. An edge is **pseudo-critical** when it can belong to at least one MST but does not belong to all MSTs. Return `[critical, pseudo_critical]`; indices within either list may be in any order.

### Function Contract
**Inputs**

Let $V=n$ and let $E$ be the number of edges.

- `n`: the vertex count, with $2 \le V \le 100$.
- `edges`: an array with
  $1 \le E \le \min\left(200, V(V-1)/2\right)$.
- Every edge is `[a, b, weight]` with
  $0 \le a < b < V$ and $1 \le \texttt{weight} \le 1000$.
- Every unordered endpoint pair is distinct.
- The graph is connected.

**Return value**

Return two lists:

1. indices of edges that occur in every MST;
2. indices of edges that occur in at least one, but not every, MST.

An edge that occurs in no MST belongs to neither list. Index order inside each category is unrestricted, but the two category positions are fixed.

### Examples
**Example 1**

- Input: `n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]`
- Output: `[[0,1],[2,3,4,5]]`
- Explanation: Edges zero and one are forced in every optimum. Each of edges two through five can be selected in some optimum, while the heavier final edge cannot.

**Example 2**

- Input: `n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]`
- Output: `[[],[0,1,2,3]]`
- Explanation: Removing any one edge from the equal-weight cycle gives an MST, so every edge is optional but eligible.
