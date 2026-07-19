# Minimum Degree of a Connected Trio in a Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1761 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Graph Theory, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/) |

## Problem Description

### Goal

You are given an undirected graph with nodes numbered from $1$ through $n$. Each pair in `edges` joins two distinct nodes. A connected trio is a set of exactly three nodes in which every pair is directly connected, so the three nodes form a triangle.

The degree of a connected trio is the number of graph edges having exactly one endpoint inside that trio and the other endpoint outside it. Find the minimum degree among all connected trios. If the graph contains no connected trio, return `-1`.

### Function Contract

**Inputs**

- `n`: the number of graph nodes, with $2 \le n \le 400$.
- `edges`: distinct undirected edges `[u, v]` with $1 \le u,v \le n$ and $u \ne v$.

Let $m=\lvert\texttt{edges}\rvert$.

**Return value**

- Return the minimum number of edges leaving any three-node clique.
- Return `-1` when no three nodes are pairwise adjacent.

### Examples

**Example 1**

- Input: `n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]`
- Output: `3`
- Explanation: Nodes `1`, `2`, and `3` form a trio, with one edge from each trio node to an outside node.

**Example 2**

- Input: `n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]`
- Output: `0`
- Explanation: Nodes `1`, `3`, and `4` form a triangle with no edge leaving the trio.

**Example 3**

- Input: `n = 5, edges = [[1,2],[2,3],[3,4],[4,5]]`
- Output: `-1`
- Explanation: The path contains no set of three pairwise adjacent nodes.
