# Edmonds-Karp (Max Flow)

| | |
|---|---|
| **ID** | `flow_02` |
| **Category** | flow |
| **Complexity (required)** | $O(V * E^2)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 6/10 |
| **Wikipedia** | [Edmonds–Karp algorithm](https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm) |

## Problem statement

Given a directed graph representing a network of pipes with capacities, find the maximum possible flow from a source node S to a sink node T.
You must optimize the Ford-Fulkerson method to ensure it runs in strictly polynomial time, completely independent of the actual capacity values. You achieve this by implementing the **Edmonds-Karp algorithm**.

**Input:** A directed graph with capacities, a source node `s`, and a sink node `t`.
**Output:** An integer representing the maximum total flow.

## When to use it

- This is the standard, safest, and most common algorithm expected in interviews for Max Flow.
- Use it whenever V \le 500. If the graph is significantly larger (e.g., 10^5 vertices), you must upgrade to Dinic's Algorithm.

## Approach

Ford-Fulkerson (`flow_01`) uses DFS to find *any* path from S to T. If capacities are massive, DFS can bounce back and forth pushing tiny increments of flow, taking $O(E x f)$ time, where f is the max flow.

**The Edmonds-Karp Optimization:**
Simply replace the DFS with **Breadth-First Search (BFS)**!
Instead of finding *any* path, BFS mathematically guarantees that we always find the **shortest augmenting path** (in terms of the number of edges).
By always taking the shortest path, we ensure that the distance from S to every node monotonically increases. It can be mathematically proven that because of this, the total number of augmentations (paths found) across the entire algorithm is strictly bounded by $O(V x E)$.

1. **Residual Graph:** Initialize the `capacity` matrix.
2. **BFS Pathfinding:** Run BFS from S. Maintain a `parent` array to reconstruct the path if T is reached.
3. **Bottleneck:** If BFS reaches T, trace the `parent` array backward from T to S to find the minimum capacity edge along the path (`bottleneck`).
4. **Augment:** Trace the `parent` array backward again:
   - Subtract `bottleneck` from the forward edge.
   - Add `bottleneck` to the backward edge.
5. Repeat until BFS can no longer reach T.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for flow_02: Edmonds-Karp.

BFS-based augmenting path. O(V * E^2).
"""


def solve(n, edges):
    from collections import deque
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    flow = 0
    while True:
        parent = [-1] * n
        parent[0] = 0
        q = deque([0])
        visited = [False] * n
        visited[0] = True
        while q and parent[n - 1] == -1:
            u = q.popleft()
            for v in range(n):
                if not visited[v] and cap[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        if parent[n - 1] == -1:
            break
        path_flow = float("inf")
        v = n - 1
        while v != 0:
            u = parent[v]
            if cap[u][v] < path_flow:
                path_flow = cap[u][v]
            v = u
        v = n - 1
        while v != 0:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        flow += path_flow
    return flow
```

</details>

## Walk-through

*(Conceptualizing the Pathological Case)*
Imagine S, T, and intermediate nodes A, B.
`S -> A (1,000,000)`
`S -> B (1,000,000)`
`A -> B (1)`
`A -> T (1,000,000)`
`B -> T (1,000,000)`

- **DFS (Ford-Fulkerson)** might find `S -> A -> B -> T` (3 edges, bottleneck 1), push 1. Then `S -> B -> A -> T` (using backward edge, 3 edges, bottleneck 1). It takes 2,000,000 iterations to finish.
- **BFS (Edmonds-Karp)** finds the *shortest* paths first!
  - It finds `S -> A -> T` (2 edges). Pushes 1,000,000!
  - It finds `S -> B -> T` (2 edges). Pushes 1,000,000!
  - Next BFS finds no paths.
  - Edmonds-Karp finishes the entire graph in exactly 2 iterations! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(E)$ | $O(V^2)$ |
| **Average** | $O(V * E)$ | $O(V^2)$ |
| **Worst** | $O(V * E^2)$ | $O(V^2)$ |

The total number of augmenting paths BFS can find is mathematically bounded by $O(V x E)$.
Each BFS search takes $O(E)$ time.
Total time is exactly $O(V x E)$ x $O(E)$ = $O(V \cdot E^2)$.
Notice this is completely independent of the maximum flow value f!
Space complexity is $O(V^2)$ for the adjacency matrix (or $O(V + E)$ if optimized using lists, though matrices are standard for dense flow graphs).

## Variants & optimizations

- **Dinic's Algorithm:** A massive upgrade. Instead of sending one flow per BFS, Dinic's uses BFS to build a "Level Graph", and then uses DFS to push multiple flows simultaneously along that level graph! Dinic's runs in $O(V^2 E)$ and is the de-facto standard for advanced competitive programming.

## Real-world applications

- **Network Bandwidth:** Calculating the maximum data throughput a telecom network can sustain between two data centers without dropping packets.

## Related algorithms in cOde(n)

- **[flow_01 - Ford Fulkerson](flow_01_ford-fulkerson-max-flow.md)** — The DFS predecessor.
- **[flow_04 - Dinic's Algorithm](flow_04_dinic-s-max-flow.md)** — The heavily optimized successor.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
