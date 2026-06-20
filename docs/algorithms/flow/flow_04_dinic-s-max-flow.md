# Dinic's Algorithm (Max Flow)

| | |
|---|---|
| **ID** | `flow_04` |
| **Category** | flow |
| **Complexity (required)** | $O(V^2 * E)$ |
| **Difficulty** | 8/10 |
| **Interview relevance** | 3/10 |
| **Wikipedia** | [Dinic's algorithm](https://en.wikipedia.org/wiki/Dinic%27s_algorithm) |

## Problem statement

Given a directed graph representing a network of pipes with capacities, find the maximum possible flow from a source node S to a sink node T.
While Edmonds-Karp (`flow_02`) takes $O(V \cdot E^2)$ time and is sufficient for small graphs, you must implement **Dinic's Algorithm** to achieve $O(V^2 \cdot E)$ time. This is strictly required when the graph is dense or V > 500, as it is significantly faster in practice than its theoretical bound suggests.

**Input:** A directed graph with capacities, a source node `s`, and a sink node `t`.
**Output:** An integer representing the maximum total flow.

## When to use it

- Dinic's is the absolute gold standard for Max Flow in competitive programming. If a problem reduces to Max Flow, always use Dinic's.
- It is astonishingly fast on Bipartite Matching graphs, dropping to exactly $O(E \sqrt{V})$ (equivalent to Hopcroft-Karp).

## Approach

Edmonds-Karp uses BFS to find a single shortest path, pushes flow down that one path, and then throws the BFS tree away. This is incredibly wasteful.
**Dinic's Insight:** Why not find ALL shortest paths of the same length at once?

1. **Level Graph (BFS):**
   Run a BFS from S to assign a `level` to every node (its shortest distance from S).
   If T cannot be reached during this BFS, we are completely done! The Max Flow has been found.
   This BFS essentially structures the residual graph into layers (Level 0, Level 1, Level 2). Flow is only allowed to travel strictly from Level L to Level L+1.

2. **Blocking Flow (DFS):**
   Now, run a DFS from S. Because we restrict DFS to only traverse edges where `level[v] == level[u] + 1`, the DFS is physically forced to only take the absolute shortest paths to T!
   When DFS reaches T, it pushes the bottleneck flow, updates capacities (including backward edges), and returns.
   **Crucial Optimization:** We don't stop after one DFS! We keep running DFS on the *same level graph* over and over again until the level graph is completely "blocked" (no more paths to T exist that only go up exactly one level).

3. **The `next_edge` Pointer Optimization:**
   During the repeated DFS calls in Step 2, a node might find that its first 3 neighbors are completely blocked. If we DFS to this node again later, we shouldn't waste time checking those 3 dead neighbors again! We maintain a `ptr` array that remembers the last explored neighbor for every node, skipping dead ends in $O(1)$ time.

4. **Repeat:** Once the current Level Graph is fully blocked, clear the levels and go back to Step 1 to build a new Level Graph.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for flow_04: Dinic's Max Flow.

Compute the max s-t flow in a directed capacitated
"""


def solve(n, edges):
    """Dinic's max flow on an adjacency-matrix residual graph.

    Returns the max flow from 0 to n-1.
    """
    from collections import deque
    INF = float("inf")
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    flow = 0
    while True:
        # BFS builds the level graph.
        level = [-1] * n
        level[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            for v in range(n):
                if level[v] < 0 and cap[u][v] > 0:
                    level[v] = level[u] + 1
                    q.append(v)
        if level[n - 1] < 0:
            break
        # DFS sends blocking flow along level-monotone paths.
        it = [0] * n
        def dfs(u, f):
            if u == n - 1:
                return f
            for i in range(it[u], n):
                v = i
                it[u] = i
                if level[v] == level[u] + 1 and cap[u][v] > 0:
                    pushed = dfs(v, min(f, cap[u][v]))
                    if pushed:
                        cap[u][v] -= pushed
                        cap[v][u] += pushed
                        return pushed
            return 0
        while True:
            pushed = dfs(0, INF)
            if not pushed:
                break
            flow += pushed
    return flow
```

</details>

## Walk-through

*(Conceptual)*
1. **BFS (Level Graph):** Assigns S as Level 0. Finds neighbors A, B as Level 1. Finds T as Level 2.
2. **DFS Loop:**
   - DFS paths MUST be exactly 2 edges long (L0 -> L1 -> L2).
   - DFS finds `S -> A -> T`. Pushes flow.
   - DFS instantly finds `S -> B -> T`. Pushes flow.
   - DFS tries to find another path, but all Level 1 nodes are saturated or blocked. Loop breaks.
3. **BFS 2 (New Level Graph):** Assigns S as L0. Because the direct pipes to T are full, it takes a longer route. A, B are L1, C is L2, T is L3.
4. **DFS Loop:** Only traces L0 -> L1 -> L2 -> L3. Pushes flow.
5. **BFS 3:** Cannot reach T. Max Flow achieved! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V + E)$ | $O(V + E)$ |
| **Average** | Much faster than V^2 E | $O(V + E)$ |
| **Worst** | $O(V^2 * E)$ | $O(V + E)$ |

The total number of Level Graphs built is strictly \le V (since the shortest path distance must increase by at least 1 every phase).
Within a single phase, finding the blocking flow takes $O(V \cdot E)$ due to the dead-end `ptr` array optimization.
Total time is exactly $O(V x V \cdot E)$ = $O(V^2 \cdot E)$.
In practice on random graphs, it runs closer to $O(E \sqrt{V})$, which is why it is vastly preferred over Edmonds-Karp.
Space complexity is $O(V + E)$ using the edge-object adjacency list.

## Variants & optimizations

- **Push-Relabel Algorithm:** An entirely different approach to Max Flow that doesn't use augmenting paths at all, but rather "pushes" excess flow locally between nodes and "relabels" their heights. It runs in $O(V^3)$ or $O(V^2 \sqrt{E})$, often beating Dinic's on extremely dense graphs (see `flow_06`).

## Real-world applications

- **Airline Scheduling:** Assigning flight crews to a massive daily roster of flights where constraints form a deep, highly interconnected bipartite/flow network.

## Related algorithms in cOde(n)

- **[flow_02 - Edmonds-Karp](flow_02_edmonds-karp.md)** — The simpler BFS-based algorithm.
- **[flow_03 - Bipartite Matching](flow_03_bipartite-matching.md)** — Dinic's solves Bipartite Matching graphs in $O(E \sqrt{V})$ time exactly.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
