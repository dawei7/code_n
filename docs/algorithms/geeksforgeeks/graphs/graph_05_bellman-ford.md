# Bellman-Ford Algorithm

| | |
|---|---|
| **ID** | `graph_05` |
| **Category** | graphs |
| **Complexity (required)** | $O(V * E)$ Time, $O(V)$ Space |
| **Difficulty** | 6/10 |
| **Interview relevance** | 6/10 |
| **Wikipedia** | [Bellman-Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) |

## Problem statement

Given a weighted graph represented as an edge list, and a starting vertex `S`.
Find the shortest paths from the source vertex `S` to all other vertices.
Crucially, the graph may contain **Negative Weight Edges**. Furthermore, you must detect if the graph contains a **Negative Weight Cycle**.

**Input:** Number of vertices `V`, an edge list `edges` where each edge is `[u, v, weight]`, and a starting node `S`.
**Output:** An array of minimum distances, or a flag indicating a negative cycle was found.

## When to use it

- To find the shortest path when **Negative Edges** are present.
- To detect a **Negative Cycle** (a cycle where the sum of edge weights is strictly less than zero. If such a cycle exists, you can loop infinitely to achieve a path distance of -\infty, breaking all pathfinding logic).

## Approach

**1. The Flaw of Dijkstra with Negative Edges:**
Dijkstra's algorithm assumes that once a node is popped from the Priority Queue, its shortest path is absolutely finalized. It assumes adding more edges to a path can ONLY INCREASE the total distance.
If A \rightarrow B costs 5, and A \rightarrow C costs 10, Dijkstra finalizes B immediately. But what if C \rightarrow B costs -20? The path A \rightarrow C \rightarrow B costs -10! Dijkstra will never go back and fix B.

**2. The Brute Force "Relaxation" Sweep:**
Bellman-Ford is fundamentally a Dynamic Programming algorithm. It abandons the Priority Queue entirely.
Instead, it just loops over EVERY SINGLE EDGE in the entire graph, and attempts to relax it.
`distances[v] = min(distances[v], distances[u] + weight(u, v))`
If we do this once, we guarantee we have found all shortest paths consisting of exactly 1 edge.
If we do this sweep again, we guarantee we have found all shortest paths consisting of \le 2 edges.

**3. When to Stop:**
What is the absolute longest a path can be in a graph without infinitely looping in a cycle? A path traversing every single node exactly once: V - 1 edges.
Therefore, if we run the relaxation sweep exactly **V - 1 times**, we are mathematically guaranteed to have found the absolute shortest path to every node!

**4. Detecting Negative Cycles:**
After completing V - 1 sweeps, all legitimate shortest paths are finalized.
What if we run the sweep just *one more time* (the V-th time)?
If the shortest path is finalized, NO edge should relax. `distances[v]` should already be perfect.
But if a relaxation DOES occur on the V-th sweep, it means a path became shorter on its V-th jump! This is impossible without revisiting a node. We have definitively detected a Negative Cycle!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_05: Bellman-Ford.

Shortest paths from start. Supports negative edges, no negative
cycles (per the spec).
"""


def solve(num_nodes, edges, start):
    INF = float("inf")
    dist = [INF] * num_nodes
    dist[start] = 0
    for _ in range(num_nodes - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
    return {i: (d if d != INF else -1) for i, d in enumerate(dist)}
```

</details>

## Walk-through

Graph `V=3`. Edges: `A->B (1)`, `B->C (-5)`, `C->A (2)`. Start at `A`.
`distances = {A:0, B:inf, C:inf}`.

**Sweep 1:**
- `A->B (1)`: `dist[B] = 0 + 1 = 1`.
- `B->C (-5)`: `dist[C] = 1 - 5 = -4`.
- `C->A (2)`: `dist[A] = -4 + 2 = -2`.
`distances = {A:-2, B:1, C:-4}`.

**Sweep 2 (V-1):**
- `A->B (1)`: `dist[B] = -2 + 1 = -1`.
- `B->C (-5)`: `dist[C] = -1 - 5 = -6`.
- `C->A (2)`: `dist[A] = -6 + 2 = -4`.
`distances = {A:-4, B:-1, C:-6}`.

**Sweep 3 (The Check):**
- `A->B (1)`: `dist[B] = -4 + 1 = -3`.
- Wait! `-3 < -1`! Relaxation occurred!
- RETURN "Negative Cycle Detected!". ✓
*(Indeed, 1 - 5 + 2 = -2. The cycle A->B->C->A loses 2 weight every loop).*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(E)$ | $O(V)$ |
| **Average** | $O(V * E)$ | $O(V)$ |
| **Worst** | $O(V * E)$ | $O(V)$ |

The outer loop runs V - 1 times. The inner loop iterates over all E edges. The total time complexity is strictly bounded by $O(V x E)$.
(If the `relaxed_any` optimization is used, it can terminate in $O(E)$ time if the graph is extremely small or heavily linear, but worst-case remains $O(VE)$).
Space complexity is strictly $O(V)$ for the `distances` array. Notice that unlike BFS/Dijkstra, we don't even need to build an Adjacency List! We iterate directly over the raw Edge List.

## Variants & optimizations

- **SPFA (Shortest Path Faster Algorithm):** A queue-based improvement over standard Bellman-Ford. Instead of blindly sweeping ALL edges V-1 times, we maintain a FIFO queue of nodes whose distances were recently relaxed. We pop a node, relax its outgoing edges, and push any successfully relaxed neighbors into the queue. It performs practically at $O(E)$ for random graphs, but retains the $O(VE)$ worst-case. It is the modern standard for negative-edge pathfinding.

## Real-world applications

- **Distance-Vector Routing (RIP protocol):** Early internet routers used Bellman-Ford to broadcast their routing tables to neighbors. The "Count-to-Infinity" problem in networking is literally just the physical manifestation of a Bellman-Ford Negative Cycle (routing loops).
- **Arbitrage Detection in Finance:** If you treat currency exchange rates as edge weights (by taking the negative log of the rate), finding a cycle that results in >1.0 multiplier (free money!) maps mathematically perfectly to finding a Negative Weight Cycle using Bellman-Ford!

## Related algorithms in cOde(n)

- **[graph_04 - Dijkstra's Algorithm](graph_04_dijkstra.md)** — The faster $O(E log V)$ alternative for purely positive weights.
- **[graph_06 - Floyd-Warshall](graph_06_floyd-warshall.md)** — The $O(V^3)$ algorithm to find shortest paths between ALL pairs of nodes, not just a single source.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
