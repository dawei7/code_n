# Find Shortest Path with K Hops

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2714 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-shortest-path-with-k-hops/) |

## Problem Description

### Goal

A connected, undirected, weighted graph has $n$ nodes numbered from $0$ through $n-1$. Each entry `[u, v, w]` in `edges` represents one edge between $u$ and $v$ whose positive weight is $w$. The graph contains neither self-loops nor repeated edges.

Given distinct source and destination nodes `s` and `d`, a path may use a special hop operation on at most $k$ of its traversed edges. Hopping over an edge makes that traversal contribute zero instead of its stored weight. Return the minimum possible total weight of a path from `s` to `d`; fewer than $k$ hops may be used.

### Function Contract

**Inputs**

- `n`: The number of graph nodes, where $2 \le n \le 500$.
- `edges`: The $E$ undirected weighted edges, where $n-1 \le E \le \min(10^4,n(n-1)/2)$ and every weight lies in $[1,10^6]$.
- `s`: The source node.
- `d`: The destination node, distinct from `s`.
- `k`: The maximum number of zero-cost edge traversals, where $0 \le k \le n-1$.

All endpoint indices lie in $[0,n-1]$, and the graph is connected.

**Return value**

Return the minimum path weight from `s` to `d` after making at most $k$ traversed edges free.

### Examples

#### Example 1

- **Input:** `n = 4, edges = [[0,1,4],[0,2,2],[2,3,6]], s = 1, d = 3, k = 2`
- **Output:** `2`
- **Explanation:** On the only simple route $1 \to 0 \to 2 \to 3$, hopping over the edges of weights $4$ and $6$ leaves cost $2$.

#### Example 2

- **Input:** `n = 7, edges = [[3,1,9],[3,2,4],[4,0,9],[0,5,6],[3,6,2],[6,0,4],[1,2,4]], s = 4, d = 1, k = 2`
- **Output:** `6`
- **Explanation:** Along $4 \to 0 \to 6 \to 3 \to 1$, making the two weight-$9$ edges free leaves $4+2=6$.

#### Example 3

- **Input:** `n = 5, edges = [[0,4,2],[0,1,3],[0,2,1],[2,1,4],[1,3,4],[3,4,7]], s = 2, d = 3, k = 1`
- **Output:** `3`
- **Explanation:** The route $2 \to 0 \to 4 \to 3$ costs $1+2+7$ normally; hopping over its last edge reduces the total to $3$.
