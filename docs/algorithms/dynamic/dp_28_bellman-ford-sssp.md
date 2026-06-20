# Bellman-Ford (Dynamic Programming Formulation)

| | |
|---|---|
| **ID** | `dp_28` |
| **Category** | dynamic_programming |
| **Complexity (required)** | $O(V * E)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 6/10 |
| **Wikipedia** | [Bellman-Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) |

## Problem statement

*(This document explores the formal DP state logic of `graph_05`).*

Find the shortest path from a Single Source to all other vertices in a graph that may contain negative weights.

## Approach as a DP Problem

While often taught as "just relaxing edges V-1 times," Bellman-Ford is fundamentally a 2D Dynamic Programming algorithm.

**The DP State:**
Let `dp[k][u]` be the shortest distance from the source to vertex `u` using **at most `k` edges**.

**The Transition:**
To find the shortest path to `u` using `k` edges, we have two choices:
1. **Don't use the k-th edge:** The shortest path used `k-1` or fewer edges. Cost is `dp[k-1][u]`.
2. **Do use a k-th edge:** We arrived at some neighboring node `v` using `k-1` edges, and then took the direct edge `(v, u)` with weight `w`. Cost is `dp[k-1][v] + w`. We try this for *all* incoming edges to `u`.

Therefore:
`dp[k][u] = min(dp[k-1][u], min(dp[k-1][v] + weight(v, u)) for all edges v->u)`

Since a simple path (no cycles) in a graph of V vertices can contain at most V-1 edges, we only need to compute this DP table up to k = V-1.

**Space Optimization:**
Notice that row `dp[k]` ONLY depends on row `dp[k-1]`.
We can drop the `k` dimension and just use a 1D array `dp[u]`, overwriting it in-place!
*(This is functionally identical to the 0/1 Knapsack space optimization).*

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_28: Bellman-Ford (SSSP).

Relax all edges n-1 times.
"""


def solve(n, edges, src):
    INF = 10 ** 9
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist
```

</details>

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V * E)$ | $O(V)$ |
| **Average** | $O(V * E)$ | $O(V)$ |
| **Worst** | $O(V * E)$ | $O(V)$ |

The algorithm explicitly computes V-1 layers (the `k` loop). In each layer, it evaluates all E edges. Total time complexity is strictly $O(V \cdot E)$.
The space optimization reduces the memory footprint from $O(V^2)$ to a single $O(V)$ array.

## Related algorithms in cOde(n)

- **[graph_05 - Bellman-Ford](../graphs/graph_05_bellman-ford.md)** — The graph theory perspective.
- **[dp_27 - Floyd-Warshall](dp_27_floyd-warshall-path.md)** — The 3D DP formulation for All-Pairs shortest paths.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
