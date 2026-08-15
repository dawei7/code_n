# Network Recovery Pathways

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3620 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Graph Theory, Topological Sort, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/network-recovery-pathways/) |

## Problem Description

### Goal

A directed acyclic graph contains `n` nodes numbered from $0$ through $n-1`. Each entry `[u, v, cost]` in `edges` is a one-way communication link from `u` to `v` with its recovery cost. The Boolean array `online` identifies currently available nodes; nodes 0 and $n-1$ are always online.

A path from node 0 to node $n-1$ is valid when every intermediate node is online and the sum of its edge costs is at most `k`. Its score is the smallest individual edge cost on that path. Return the largest score among all valid paths, or `-1` when no valid path exists.

### Function Contract

**Inputs**

- `edges`: Directed `[u, v, cost]` edges of a DAG.
- `online`: Availability flags whose length defines the number of graph nodes.
- `k`: The maximum allowed sum of edge costs along the selected path.

The constraints are $2 \le n \le 5\cdot 10^4$, at most $10^5$ edges, $0 \le \texttt{cost} \le 10^9$, and $0 \le k \le 5\cdot 10^{13}$.

**Return value**

Return the maximum possible minimum edge cost on an online path from 0 to $n-1$ whose total cost does not exceed `k`, or `-1` if none exists.

### Examples

#### Example 1

- **Input:** `edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [true,true,true,true], k = 10`
- **Output:** `3`
- **Explanation:** The first route costs 15 and is invalid; route `0 -> 2 -> 3` costs 7 and has score 3.

#### Example 2

- **Input:** `edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [true,true,true,false,true], k = 12`
- **Output:** `6`
- **Explanation:** The path through offline node 3 is unavailable; `0 -> 2 -> 4` costs 12 and has score 6.

#### Example 3

- **Input:** `edges = [], online = [true, true], k = 0`
- **Output:** `-1`
- **Explanation:** No path connects the source to the destination.
