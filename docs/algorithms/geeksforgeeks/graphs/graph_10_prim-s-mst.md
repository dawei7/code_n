# Prim's Algorithm (Minimum Spanning Tree)

| | |
|---|---|
| **ID** | `graph_10` |
| **Category** | graphs |
| **Complexity (required)** | $O(E log V)$ Time, $O(V)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 6/10 |
| **Wikipedia** | [Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm) |

## Problem statement

Given a connected, undirected, and weighted graph. Find a Minimum Spanning Tree (MST) for the graph.
A Minimum Spanning Tree is a subset of the edges that connects all V vertices together, without any cycles, and with the minimum possible total edge weight.

**Input:** Number of vertices `V`, and an adjacency list `adj` where `adj[u] = [(v, weight)]`.
**Output:** An integer representing the minimum total weight of the MST.

## When to use it

- To solve the classic Minimum Spanning Tree problem.
- When the graph is **Dense** (E ~= V^2), Prim's is mathematically superior to Kruskal's because it avoids the $O(E log E)$ global sort!

## Approach

**1. The "Growing Tree" Metaphor:**
Unlike Kruskal's (which blindly grabs the cheapest edges globally and stitches disjoint components together), Prim's algorithm starts from a single root node and slowly grows a single, unified tree outward.

**2. The Priority Queue (Dijkstra's Cousin):**
We maintain a `visited` set to track which nodes are already part of our growing MST.
We maintain a Priority Queue of edges that sit precisely on the *boundary* between our MST and the unvisited nodes.
Initially, we pick node `0`, mark it visited, and push all its outgoing edges into the Priority Queue.

**3. The Greedy Expansion:**
We pop the absolute cheapest edge from the Priority Queue.
If this edge leads to a node `v` that is *already* in our `visited` set, it means adding this edge would create a cycle within our MST! We discard it.
If `v` is unvisited, we have found a valid expansion! We add `v` to the `visited` set, add the edge's weight to our total MST cost, and then push all of `v`'s outgoing edges into the Priority Queue to expand our boundary!

**4. Termination:**
The algorithm terminates when the Priority Queue is empty, or when the `visited` set contains all V vertices.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_10: Prim's MST.

Vertex-growth MST using a min-heap of (weight, from, to) edges.
"""


def solve(num_nodes, edges):
    import heapq
    if num_nodes == 0:
        return []
    adj = [[] for _ in range(num_nodes)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    visited = [False] * num_nodes
    visited[0] = True
    heap = []
    for v, w in adj[0]:
        heapq.heappush(heap, (w, 0, v))
    mst = []
    while heap:
        w, u, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        mst.append((u, v, w))
        for nxt, w2 in adj[v]:
            if not visited[nxt]:
                heapq.heappush(heap, (w2, v, nxt))
    if len(mst) != num_nodes - 1:
        return []
    return sorted(mst)
```

</details>

## Walk-through

Graph `V=4`. `adj = {0: [(1, 10), (2, 6), (3, 5)], ... }`.
`visited = set()`, `pq = [(0, 0)]`.

1. `heappop()` -> `weight=0, u=0`.
   - `0` not visited. `visited.add(0)`. `mst_weight = 0`.
   - Push edges: `(10, 1)`, `(6, 2)`, `(5, 3)`.
   - `pq = [(5, 3), (6, 2), (10, 1)]`.
2. `heappop()` -> `(5, 3)`.
   - `3` not visited. `visited.add(3)`. `mst_weight = 5`.
   - Neighbors of 3: `0 (cost 5)`, `1 (cost 15)`, `2 (cost 4)`.
   - `0` is visited (skip). Push `(15, 1)`, `(4, 2)`.
   - `pq = [(4, 2), (6, 2), (10, 1), (15, 1)]`.
3. `heappop()` -> `(4, 2)`.
   - `2` not visited. `visited.add(2)`. `mst_weight = 5 + 4 = 9`.
   - Neighbors of 2: `0 (cost 6)`, `3 (cost 4)`. Both visited! Push nothing.
   - `pq = [(6, 2), (10, 1), (15, 1)]`.
4. `heappop()` -> `(6, 2)`.
   - `2` IS ALREADY VISITED! Skip!
5. `heappop()` -> `(10, 1)`.
   - `1` not visited. `visited.add(1)`. `mst_weight = 9 + 10 = 19`.
   - `len(visited) == 4`. Terminate!

Result `mst_weight = 19`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(E log V)$ | $O(V + E)$ |
| **Average** | $O(E log V)$ | $O(V + E)$ |
| **Worst** | $O(E log V)$ | $O(V + E)$ |

Every vertex is added to the `visited` set exactly once. Every edge is pushed into the Priority Queue exactly once. Popping from the Priority Queue takes $O(log E)$.
Total time complexity is $O(E log E)$. Since E \le V^2, $O(log E)$ = $O(2 log V)$ = $O(log V)$. Thus, time complexity is conventionally written as $O(E log V)$.
Space complexity is $O(E)$ for the Priority Queue, and $O(V)$ for the `visited` set.
*(Note: A highly advanced Fibonacci Heap can optimize the time to $O(E + V log V)$, making it strictly faster than Kruskal's for dense graphs, but this is never expected in interviews).*

## Variants & optimizations

- **Path Reconstruction:** If you need the actual list of edges in the MST, just modify the PQ to store tuples of `(weight, u, parent_who_pushed_me)`. When you successfully pop and visit `u`, add the edge `(parent, u, weight)` to your `mst_edges` array!

## Real-world applications

- **Maze Generation:** If you assign random weights to a grid graph and run Prim's Algorithm, the resulting MST is a perfectly solvable, cycle-free maze!
- **Traveling Salesperson Approximation:** The absolute shortest path touching all nodes (TSP) is NP-Hard. However, the weight of an MST is a guaranteed lower bound for TSP.

## Related algorithms in cOde(n)

- **[graph_08 - Kruskal's MST](graph_08_kruskal-s-mst.md)** — The Disjoint-Set alternative that sorts edges globally.
- **[graph_04 - Dijkstra's Algorithm](graph_04_dijkstra.md)** — Uses the exact same Priority Queue structure, but Dijkstra's PQ sorts by *total accumulated distance from source*, while Prim's sorts strictly by the *raw weight of the immediate edge*.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
