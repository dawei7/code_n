# Minimum S-T Cut

| | |
|---|---|
| **ID** | `flow_05` |
| **Category** | flow |
| **Complexity (required)** | $O(Max Flow Time)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 6/10 |
| **Wikipedia** | [Max-flow min-cut theorem](https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem) |

## Problem statement

Given a directed graph representing a network of pipes with capacities, a `source` node S and a `sink` node T.
Find the **Minimum S-T Cut**: A specific set of edges that, if completely severed (removed from the graph), would completely disconnect S from T.
Among all possible sets of edges that disconnect S from T, you must find the one where the sum of the capacities of the severed edges is the absolute mathematical minimum.

**Input:** A directed graph with capacities, a source node `s`, and a sink node `t`.
**Output:** A list of the specific edges `(u, v)` that form the Minimum Cut.

## When to use it

- To identify the absolute most vulnerable structural bottlenecks in a network.
- By the **Max-Flow Min-Cut Theorem**, the total capacity of the Minimum Cut is exactly mathematically equal to the Maximum Flow! This profound duality means you can solve Min-Cut using your existing Max-Flow code.

## Approach

1. **Run Max Flow:** First, run any Max Flow algorithm (Ford-Fulkerson, Edmonds-Karp, or Dinic's) on the graph until the network is fully saturated.
2. **The Residual State:** When Max Flow finishes, the algorithm terminates because it can no longer find a path from S to T in the *Residual Graph*. This means the flow is completely blocked by a wall of fully saturated pipes.
3. **Find the Reachable Nodes:** Run a simple BFS or DFS starting from S, strictly following only edges that still have `residual capacity > 0`.
   - The set of all nodes you can reach is called Set A (the nodes still connected to the source).
   - The set of all nodes you cannot reach is called Set B (the nodes cut off from the source).
4. **Identify the Cut Edges:** The Minimum Cut is composed of all the original forward edges that start in Set A and end in Set B.
   - Why? Because these are the exact pipes that were fully saturated (0 residual capacity left), which is why our final BFS couldn't cross them into Set B!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for flow_05: Minimum s-t Cut.

Find the minimum s-t cut in a directed flow network.
"""


def solve(n, edges):
    """Min s-t cut via max-flow then residual reachability.

    Returns a sorted list of (u, v) tuples for the cut.
    """
    from collections import deque
    INF = float("inf")
    # Build a fresh capacity matrix.
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    # Ford-Fulkerson with BFS (Edmonds-Karp) on the residual.
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
        path_flow = INF
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
    # Now DFS from s in the residual to find reachable set.
    reachable = [False] * n
    reachable[0] = True
    stack = [0]
    while stack:
        u = stack.pop()
        for v in range(n):
            if not reachable[v] and cap[u][v] > 0:
                reachable[v] = True
                stack.append(v)
    # Cut edges: original edges from reachable to non-reachable.
    cut = []
    for u, v, c in edges:
        if reachable[u] and not reachable[v]:
            cut.append((u, v))
    cut.sort()
    return cut
```

</details>

## Walk-through

*(Conceptual)*
Original: `S -> A (cap 10)`, `A -> T (cap 5)`, `S -> B (cap 5)`, `B -> T (cap 10)`.

1. **Max Flow:** Total flow is 5 + 5 = 10.
   - The edge `A -> T` is fully saturated (residual cap 0).
   - The edge `S -> B` is fully saturated (residual cap 0).
2. **Final BFS from S:**
   - Can we go to `A`? Yes, `S -> A` originally had 10, we used 5, so 5 remains. `A` is Reachable.
   - Can we go `A -> T`? No, residual is 0.
   - Can we go `S -> B`? No, residual is 0.
   - Reachable (Set A): `{S, A}`.
   - Unreachable (Set B): `{B, T}`.
3. **Find Cut Edges:**
   - Look at original edges going from `{S, A}` to `{B, T}`.
   - Edge `A -> T` is in the cut! (Capacity 5).
   - Edge `S -> B` is in the cut! (Capacity 5).
   - Total Cut Capacity = 10. (Exactly equal to Max Flow!) ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(Max Flow Time)$ | $O(V^2)$ |
| **Average** | $O(Max Flow Time)$ | $O(V^2)$ |
| **Worst** | $O(V * E^2)$ | $O(V^2)$ |

The time complexity is entirely dominated by the initial Max Flow algorithm used to saturate the graph. (E.g., $O(V \cdot E^2)$ if using Edmonds-Karp). The subsequent BFS and edge-scan to find the cut takes a trivial $O(V + E)$ and $O(V^2)$ time.
Space complexity is $O(V^2)$ for the matrices.

## Variants & optimizations

- **Global Minimum Cut (Stoer-Wagner):** What if you just want to find the absolute weakest point in an undirected graph, regardless of S and T? You could run Min S-T Cut for every possible pair of vertices ($O(V^2)$ times), but the Stoer-Wagner algorithm finds the Global Min Cut purely algebraically in $O(V \cdot E + V^2 log V)$ time without using network flow at all!

## Real-world applications

- **Military & Infrastructure:** Identifying the absolute minimum number of bridges or power lines to destroy in order to perfectly sever enemy supply lines from a capital city to a forward base.
- **Image Segmentation:** In computer vision, "Graph Cuts" are used to separate foreground objects from the background by treating pixels as nodes and edge weights as color similarities.

## Related algorithms in cOde(n)

- **[flow_02 - Edmonds-Karp](flow_02_edmonds-karp.md)** — The engine used to saturate the residual graph.
- **[flow_01 - Ford Fulkerson](flow_01_ford-fulkerson-max-flow.md)** — The foundational theorem solver.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
