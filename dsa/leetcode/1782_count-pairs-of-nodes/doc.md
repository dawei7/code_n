# Count Pairs Of Nodes

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-pairs-of-nodes/) |
| Frontend ID | 1782 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Graph Theory, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An undirected graph has `n` nodes labeled from `1` through `n`. Its edge list may contain the same unordered pair more than once, so the graph is a multigraph rather than necessarily a simple graph.

For two distinct nodes `a` and `b`, consider every edge connected to at least one of them. An edge joining `a` directly to `b` belongs to this collection only once, even though it contributes to the degree of both endpoints. For each value in `queries`, count the unordered node pairs `(a, b)` with $a < b$ whose number of incident edges is strictly greater than that value.

Return the counts in the same order as the queries.

### Function Contract

**Inputs**

- `n`: the number of nodes, labeled from `1` through `n`.
- `edges`: undirected edges `[u, v]`; repeated endpoint pairs represent distinct parallel edges.
- `queries`: thresholds applied independently to every unordered pair.

Let $E = \lvert\texttt{edges}\rvert$, $Q = \lvert\texttt{queries}\rvert$, and $P$ be the number of distinct unordered endpoint pairs represented in `edges`. If `degree(x)` is the degree of node `x` and `shared(a, b)` is the number of direct edges between `a` and `b`, then the incident-edge count for that node pair is

$$
\operatorname{incident}(a,b)
= \operatorname{degree}(a) + \operatorname{degree}(b)
- \operatorname{shared}(a,b).
$$

**Return value**

- Return an array of length $Q$. Its $i$-th value is the number of pairs satisfying $\operatorname{incident}(a,b) > \texttt{queries[i]}$.

### Examples

**Example 1**

- Input: `n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]`
- Output: `[6,5]`

The two entries `[1,2]` and `[2,1]` are parallel edges between the same nodes. They contribute to both degrees, but each is counted only once when the incident edges of pair `(1, 2)` are evaluated.

**Example 2**

- Input: `n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]`
- Output: `[10,10,9,8,6]`

**Example 3**

- Input: `n = 3, edges = [[1,2]], queries = [1]`
- Output: `[0]`

Every pair has exactly one incident edge, so no pair is strictly above the threshold.
