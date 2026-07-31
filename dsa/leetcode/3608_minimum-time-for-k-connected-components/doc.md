# Minimum Time for K Connected Components

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3608 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Binary Search, Union-Find, Graph Theory, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-for-k-connected-components/) |

## Problem Description
### Goal

An undirected graph contains `n` nodes numbered from $0$ through $n-1$. Each entry `[u, v, time]` in `edges` describes an edge between `u` and `v` that is removed at its recorded time.

For a chosen nonnegative time $t$, remove every edge whose recorded time is at most $t$. Determine the minimum $t$ for which the remaining graph has at least `k` connected components. The graph may already be disconnected before any removals; in that case, the answer can be `0`.

All edges sharing a removal time disappear together. Isolated nodes count as connected components.

### Function Contract

**Inputs**

- `n`: The number of graph nodes.
- `edges`: The undirected edges as `[u, v, time]` triples.
- `k`: The required minimum number of connected components.

The constraints are $1 \le n \le 10^5$, at most $10^5$ distinct edges, $1 \le \texttt{time} \le 10^9$, and $1 \le k \le n$.

**Return value**

Return the smallest nonnegative time after whose removals the graph has at least `k` connected components.

### Examples

**Example 1**

- Input: `n = 2, edges = [[0, 1, 3]], k = 2`
- Output: `3`
- Explanation: The two nodes separate when their only edge is removed at time 3.

**Example 2**

- Input: `n = 3, edges = [[0, 1, 2], [1, 2, 4]], k = 3`
- Output: `4`
- Explanation: Removing only the first edge creates two components; removing both creates three.

**Example 3**

- Input: `n = 3, edges = [[0, 2, 5]], k = 2`
- Output: `0`
- Explanation: Node 1 is already isolated, so the original graph has two components.
