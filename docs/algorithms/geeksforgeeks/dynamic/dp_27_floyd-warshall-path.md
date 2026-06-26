# Floyd-Warshall (Dynamic Programming Formulation)

| | |
|---|---|
| **ID** | `dp_27` |
| **Category** | dynamic_programming |
| **Complexity (required)** | $O(V^3)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 7/10 |
| **Wikipedia** | [Floyd-Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm) |

## Problem statement

*(This document explores the formal DP state logic of `graph_06`).*

Find the shortest paths between **All Pairs** of vertices in a weighted graph. Negative weights are allowed, but negative-weight cycles are not.

## Approach as a DP Problem

Floyd-Warshall is not just a graph algorithm; it is a textbook 3D Dynamic Programming algorithm.

**The DP State:**
Let `dp[k][i][j]` be the shortest distance from node `i` to node `j` using ONLY vertices from the set `{0, 1, 2, ... k}` as intermediate stops.

**The Transition:**
If we want to compute the shortest path using nodes up to `k` (`dp[k][i][j]`), we have two choices:
1. **Don't use node `k`:** The shortest path relies entirely on the previous set of nodes. Cost is `dp[k-1][i][j]`.
2. **Do use node `k`:** We walk from `i` to `k` (using nodes up to `k-1`), and then walk from `k` to `j` (using nodes up to `k-1`). Cost is `dp[k-1][i][k] + dp[k-1][k][j]`.

Therefore:
`dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j])`

**Space Optimization:**
Notice that `dp[k]` ONLY ever relies on the values from `dp[k-1]`.
Furthermore, `dp[k-1][i][k]` and `dp[k-1][k][j]` do not change when computing the `k`-th layer because paths ending or starting at `k` can't use `k` as an *intermediate* step anyway!
Therefore, we can completely drop the `k` dimension from our DP table and simply update a 2D matrix in place!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_27: Floyd-Warshall Path Reconstruction.

Standard Floyd-Warshall with a next[][] matrix to
reconstruct the path. Return [] if dest is unreachable.
"""


def solve(n, edges, src, dest):
    if src == dest:
        return [src]
    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    nxt = [[-1] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
            nxt[u][v] = v
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k] if nxt[i][k] != -1 else k
    if dist[src][dest] == INF:
        return []
    path = [src]
    cur = src
    while cur != dest:
        cur = nxt[cur][dest]
        if cur == -1:
            return []
        path.append(cur)
    return path
```

</details>

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V^3)$ | $O(V^2)$ |
| **Average** | $O(V^3)$ | $O(V^2)$ |
| **Worst** | $O(V^3)$ | $O(V^2)$ |

The 3 tightly nested loops `k`, `i`, and `j` clearly define the $O(V^3)$ time complexity.
The in-place DP optimization reduces the space complexity from $O(V^3)$ to $O(V^2)$.

## Related algorithms in cOde(n)

- **[graph_06 - Floyd-Warshall](../graphs/graph_06_floyd-warshall.md)** — The graph theory perspective.
- **[dp_28 - Bellman-Ford](dp_28_bellman-ford-sssp.md)** — The 2D DP formulation for Single-Source shortest paths.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
