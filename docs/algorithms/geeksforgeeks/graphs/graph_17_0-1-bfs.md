# 0-1 BFS (Shortest Path)

| | |
|---|---|
| **ID** | `graph_17` |
| **Category** | graphs |
| **Complexity (required)** | $O(V + E)$ Time, $O(V)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 7/10 |
| **GeeksForGeeks Equivalent** | [0-1 BFS (Shortest Path in a Binary Weight Graph)](https://www.geeksforgeeks.org/0-1-bfs-shortest-path-binary-graph/) |

## Problem statement

Given a weighted graph where every edge has a weight of strictly **0 or 1**. Find the shortest path from a starting vertex `S` to all other vertices.

**Input:** Number of vertices `V`, an adjacency list `adj` where `adj[u] = [(v, weight)]` (weight \in {0, 1}), and a starting node `S`.
**Output:** An array of minimum distances from `S`.

## When to use it

- When solving grid-based pathfinding problems where "moving freely" costs 0, but "breaking a wall" or "changing direction" costs 1.
- *Constraint:* Standard Dijkstra works, but takes $O(E log V)$. Because weights are strictly binary, 0-1 BFS solves it in linear $O(V + E)$ time!

## Approach

**1. The Priority Queue Overhead:**
Why does Dijkstra need a $O(log V)$ Priority Queue? Because edge weights can be arbitrary (e.g., 5, 20, 100), meaning candidate distances can jump unpredictably. The PQ is required to forcefully sort them.

**2. The 0-1 Limitation:**
If edge weights are ONLY 0 or 1, and our current node U has a distance of D, its neighbors can ONLY have candidate distances of D (if weight is 0) or D + 1 (if weight is 1).
There are no jumps! The queue of pending nodes will only ever contain nodes with distance D and distance D+1.

**3. The Double-Ended Queue (Deque):**
We can completely replace the expensive Priority Queue with a simple $O(1)$ Double-Ended Queue (`deque`).
When we are at node U (distance D) and evaluate a neighbor V:
- If the edge weight is **0**, the candidate distance to V is still D. This is a "free" move! We want to explore this immediately before exploring any D+1 moves. Therefore, we push V to the **FRONT** of the deque.
- If the edge weight is **1**, the candidate distance to V is D + 1. We should only explore this after all D moves are exhausted. Therefore, we push V to the **BACK** of the deque.

Because we push 0-cost moves to the front, the deque naturally stays perfectly sorted without any $O(log V)$ heap overhead!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_17: 0-1 BFS.

Shortest path on a graph with edge weights in {0, 1}. Use a
deque: pop the left, push 0-weight neighbors to the LEFT and
1-weight neighbors to the RIGHT. This is O(V + E).
"""


def solve(num_nodes, edges, start):
    if num_nodes <= 0:
        return {}
    adj = [[] for _ in range(num_nodes)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    INF = float("inf")
    dist = [INF] * num_nodes
    dist[start] = 0
    from collections import deque
    dq = deque([start])
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    return {i: (-1 if dist[i] == INF else dist[i]) for i in range(num_nodes)}
```

</details>

## Walk-through

`V = 4`. Edges: `0-1 (1)`, `0-2 (0)`, `1-3 (0)`, `2-3 (1)`. Start at `0`.
`dist = [0, inf, inf, inf]`. `queue = [0]`.

1. `popleft()` -> `0` (dist 0).
   - Neighbor `1` (weight 1): Candidate dist = 1. `1 < inf`.
     - `dist[1] = 1`. Weight is 1, push BACK: `queue = [1]`.
   - Neighbor `2` (weight 0): Candidate dist = 0. `0 < inf`.
     - `dist[2] = 0`. Weight is 0, push FRONT: `queue = [2, 1]`.
2. `popleft()` -> `2` (dist 0).
   - Neighbor `3` (weight 1): Candidate dist = 1. `1 < inf`.
     - `dist[3] = 1`. Weight is 1, push BACK: `queue = [1, 3]`.
3. `popleft()` -> `1` (dist 1).
   - Neighbor `3` (weight 0): Candidate dist = 1 + 0 = 1.
     - `1` is NOT strictly less than current `dist[3]` (which is 1).
     - Ignore.
4. `popleft()` -> `3` (dist 1).
   - No neighbors.

Final distances: `[0, 1, 0, 1]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V + E)$ | $O(V)$ |
| **Average** | $O(V + E)$ | $O(V)$ |
| **Worst** | $O(V + E)$ | $O(V)$ |

Every vertex is processed, and its outgoing edges are evaluated. Pushing to the front or back of a deque takes $O(1)$ time. Therefore, the time complexity is strictly $O(V + E)$, matching standard unweighted BFS and vastly outperforming Dijkstra's $O(E log V)$.
Space complexity is $O(V)$ for the deque and the distances array.

## Variants & optimizations

- **Multi-Source 0-1 BFS:** If you have multiple starting points, just push all of them to the deque initially with distance 0!
- **Dial's Algorithm:** A generalization of 0-1 BFS. If edge weights are restricted to small integers bounded by a maximum value W (e.g., weights from 0 to 9), you can use an array of W+1 queues (or buckets) instead of a single deque. This solves the problem in $O(V + E \cdot W)$ time.

## Real-world applications

- **Robot Navigation / Pac-Man:** Finding the optimal path through a grid where "moving forward" costs 0, but "turning 90 degrees" costs 1 unit of time or energy. A state is `(x, y, facing_direction)`.

## Related algorithms in cOde(n)

- **[graph_02 - Breadth-First Search](graph_02_bfs.md)** — The foundation. 0-1 BFS is just BFS with a Double-Ended Queue.
- **[graph_04 - Dijkstra's Algorithm](graph_04_dijkstra.md)** — The slower algorithm you would be forced to use if an edge weight was 2.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
