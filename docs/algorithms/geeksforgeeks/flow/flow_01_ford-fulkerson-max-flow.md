# Ford-Fulkerson (Max Flow)

| | |
|---|---|
| **ID** | `flow_01` |
| **Category** | flow |
| **Complexity (required)** | $O(E * f)$ |
| **Difficulty** | 6/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Ford–Fulkerson algorithm](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm) |

## Problem statement

Given a directed graph representing a network of pipes, where each edge has a `capacity`, find the **maximum possible flow** from a `source` node (S) to a `sink` node (T).
You must implement the **Ford-Fulkerson** method using Depth-First Search (DFS) to find augmenting paths.

**Input:** A directed graph with capacities, a source node `s`, and a sink node `t`.
**Output:** An integer representing the maximum total flow.

## When to use it

- The foundation of all network flow problems. Use it to understand the concept of the Residual Graph.
- Do NOT use it in production if edge capacities are massive (e.g. 10^9) or if the capacities are floating-point numbers, as DFS-based Ford-Fulkerson can take extremely long or even loop infinitely on irrational capacities! Use Edmonds-Karp or Dinic's instead.

## Approach

Imagine pouring water into a network of pipes. We want to push as much water as possible.
A naive greedy approach would be: Find a path from S to T. Find the smallest pipe on that path. Push that much water through the whole path. Repeat until no paths exist.
**The Greedy Flaw:** If you greedily push water down a pipe, you might block a later path that actually needed that pipe to achieve a higher *total* flow!

**The Ford-Fulkerson Insight (The Residual Graph):**
Every time we push X units of water forward along an edge `u -> v`, we must artificially add an edge going *backward* `v -> u` with capacity X.
This backward edge acts as an "Undo" button! If a future path discovers it can get a better total flow by routing water *backward* along that pipe (effectively cancelling out our previous greedy mistake and redirecting the water elsewhere), the algorithm allows it!

1. **Residual Graph:** Create a graph storing `capacity`. Initialize `flow = 0`.
2. **Find Path:** Use a simple DFS to find *any* path from S to T where every edge on the path has `capacity > 0`.
3. **Bottleneck:** Find the minimum capacity along this path. Let's call it `bottleneck`.
4. **Augment Flow:** 
   - Add `bottleneck` to the total `flow`.
   - For every edge `u -> v` on the path:
     - Subtract `bottleneck` from `capacity[u][v]`.
     - **Crucial:** Add `bottleneck` to the backward edge `capacity[v][u]`!
5. Repeat steps 2-4 until DFS can no longer find a path from S to T.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for flow_01: Ford-Fulkerson Max Flow.

DFS-based augmenting path. Find path, push bottleneck,
update residual. Repeat.
"""


def solve(n, edges):
    INF = float("inf")
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    max_flow = 0
    while True:
        parent = [-1] * n
        parent[0] = 0
        stack = [0]
        visited = [False] * n
        visited[0] = True
        found = -1
        while stack and found == -1:
            u = stack.pop()
            for v in range(n):
                if not visited[v] and cap[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    if v == n - 1:
                        found = v
                        break
                    stack.append(v)
        if found == -1:
            break
        path_flow = float("inf")
        v = found
        while v != 0:
            u = parent[v]
            if cap[u][v] < path_flow:
                path_flow = cap[u][v]
            v = u
        v = found
        while v != 0:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        max_flow += path_flow
    return max_flow
```

</details>

## Walk-through

Graph:
`S(0) -> A(1)`: cap 10
`S(0) -> B(2)`: cap 10
`A(1) -> B(2)`: cap 1
`A(1) -> T(3)`: cap 10
`B(2) -> T(3)`: cap 10

**Iteration 1:**
- DFS finds path `0 -> 1 -> 2 -> 3` (S -> A -> B -> T).
- Capacities: 10, 1, 10. Bottleneck = 1.
- Push 1 unit.
- Forward edges `(0,1), (1,2), (2,3)` lose 1 capacity.
- Backward edges `(1,0), (2,1), (3,2)` gain 1 capacity.
- Total Flow = 1.

**Iteration 2:**
- DFS finds path `0 -> 1 -> 3` (S -> A -> T).
- Capacities: 9, 10. Bottleneck = 9.
- Push 9 units.
- Total Flow = 1 + 9 = 10.

**Iteration 3:**
- DFS finds path `0 -> 2 -> 3` (S -> B -> T).
- Capacities: 10, 9. Bottleneck = 9.
- Push 9 units.
- Total Flow = 10 + 9 = 19.

No more paths exist. Max flow = 19. ✓ (Notice how DFS made a "mistake" in Iteration 1 by using the middle pipe, but easily routed around it later).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(E)$ | $O(V^2)$ |
| **Average** | Depends | $O(V^2)$ |
| **Worst** | $O(E * f)$ | $O(V^2)$ |

*Where E is the number of edges and f is the maximum flow.*
Why $O(E x f)$? Imagine the graph above, but the middle pipe `A -> B` has capacity 1, and the other pipes have capacity 1,000,000.
If DFS unluckily alternates between path `S->A->B->T` (push 1) and `S->B->A->T` using the backward edge (push 1), it will push exactly 1 unit of flow per iteration! It will require 2,000,000 DFS calls to finish!
Space complexity is $O(V^2)$ to store the dense capacity matrix (or $O(V + E)$ if implemented with an adjacency list of edge objects).

## Variants & optimizations

- **Edmonds-Karp ($O(V E^2)$):** Exactly the same algorithm, but uses BFS instead of DFS. This mathematically prevents the $O(E x f)$ pathological case, ensuring strictly polynomial time regardless of edge capacities!
- **Capacity Scaling:** Only consider edges with capacity \ge \Delta. Start with \Delta as a large power of 2, and halve it each time. This drops the time to $O(E^2 log U)$.

## Real-world applications

- **Traffic Routing:** Calculating the maximum number of cars that can evacuate a city through a network of highways during a hurricane.

## Related algorithms in cOde(n)

- **[flow_02 - Edmonds-Karp](flow_02_edmonds-karp.md)** — The BFS upgrade to this algorithm.
- **[flow_03 - Bipartite Matching](flow_03_bipartite-matching.md)** — A special case of Max Flow where every edge capacity is exactly 1.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
