# Breadth-First Search (BFS)

| | |
|---|---|
| **ID** | `graph_02` |
| **Category** | graphs |
| **Complexity (required)** | $O(n²)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 8/10 |
| **Wikipedia** | [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) |

## Problem statement

Given a graph `G = (V, E)` and a source vertex `s`, traverse
the graph **level by level**: visit all vertices at distance
`1` from `s` before any at distance `2`, then distance `3`,
and so on. Output: the BFS order, the distance from `s` to
each reachable vertex, and (optionally) the predecessor of
each vertex for path reconstruction.

**Input:** a graph (adjacency list or matrix), a source `s`.
**Output:** BFS order, distance array, predecessor array.

**Example:**

```
    0 - 1 - 3
    |   |   |
    2 - 4   5
    |
    6

Adjacency:
  0: [1, 2]
  1: [0, 3, 4]
  2: [0, 4, 6]
  3: [1, 5]
  4: [1, 2]
  5: [3]
  6: [2]

BFS from 0:
  Order: 0, 1, 2, 3, 4, 6, 5
  Dist:  0:0, 1:1, 2:1, 3:2, 4:2, 5:3, 6:2
```

## When to use it

- The single most important graph algorithm. Asked in some
  form at every interview.
- Foundation for **shortest path on unweighted graphs**,
  **connected components**, **bipartite check**, **level-
  order tree traversal**, and **garbage collection** (mark
  and sweep).

## Approach

BFS uses a **FIFO queue** (the deque). The invariant: when
a vertex leaves the queue, its shortest distance from `s`
is known.

```
mark s as visited
enqueue (s, dist=0)
while queue not empty:
    dequeue (u, du)
    for each neighbor v of u:
        if v not yet visited:
            mark v as visited
            dist[v] = du + 1
            parent[v] = u
            enqueue (v, du + 1)
```

**Performance:** each vertex is enqueued at most once, and
each edge is examined at most twice (once from each endpoint,
in an undirected graph). Total: $O(V + E)$ for an adjacency-
list representation. For an adjacency matrix: $O(V²)$.

**Why it gives shortest path on unweighted graphs:** when we
first visit a vertex `v`, every path to `v` must go through
some neighbor that is itself at distance ≤ dist[v] - 1, and
those neighbors are processed before `v`. So `dist[v]` is
optimal.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_02: Breadth-First Search.

Pure-graph BFS on adjacency lists, returns visit order.
"""


def solve(num_nodes, edges):
    from collections import deque
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = [False] * num_nodes
    order = []
    q = deque([0])
    seen[0] = True
    while q:
        u = q.popleft()
        order.append(u)
        for v in sorted(adj[u]):
            if not seen[v]:
                seen[v] = True
                q.append(v)
    return order
```

</details>

## Walk-through

Graph from the example. BFS from `s = 0`.

`visited = {0}`, `queue = [(0, 0)]`, `order = []`, `parent = {0: None}`.

| Iter | dequeue | neighbors | newly visited | queue after |
|---|---|---|---|---|
| 1 | (0, 0) | 1, 2 | 1 (dist 1), 2 (dist 1) | [(1, 1), (2, 1)] |
| 2 | (1, 1) | 0, 3, 4 | 3 (dist 2), 4 (dist 2) | [(2, 1), (3, 2), (4, 2)] |
| 3 | (2, 1) | 0, 4, 6 | 6 (dist 2); 4 already visited | [(3, 2), (4, 2), (6, 2)] |
| 4 | (3, 2) | 1, 5 | 5 (dist 3) | [(4, 2), (6, 2), (5, 3)] |
| 5 | (4, 2) | 1, 2 | none new | [(6, 2), (5, 3)] |
| 6 | (6, 2) | 2 | none new | [(5, 3)] |
| 7 | (5, 3) | 3 | none new | [] |

BFS order: `[0, 1, 2, 3, 4, 6, 5]`. Distances match. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V + E)$ for adjacency list, $O(V²)$ for matrix | $O(V)$ |
| **Average** | $O(V + E)$ | $O(V)$ |
| **Worst** | $O(V + E)$ | $O(V)$ |

The required complexity is $O(n²)$ for cOde(n)'s n²-matrix
variant.

## Variants & optimizations

- **Bidirectional BFS** — run from both `s` and `t`; stop
  when the frontiers meet. ~2x speedup in practice.
- **Multi-source BFS** — initialize the queue with all
  sources. Useful for "rotting oranges", "walls and gates".
- **0-1 BFS** — when edges have weight 0 or 1, use a deque:
  push 0-weight edges to the front, 1-weight to the back.
  $O(V + E)$ without Dijkstra's $O((V + E)$ log V). See
  `graph_17`.
- **BFS for bipartite check** — alternate-color the levels.
  If a level has both colors and any edge connects same
  colors, not bipartite.
- **BFS for connected components** — repeat BFS from each
  unvisited vertex.

## Real-world applications

- **Social network "degrees of separation"** — BFS from a
  person, count layers until you reach another.
- **Web crawlers** — BFS from seed URLs, follow links
  layer by layer, with politeness delays.
- **Garbage collection** — "mark and sweep" GC walks the
  object graph in BFS order from root references.
- **Peer-to-peer networks** — BitTorrent uses a Kademlia-
  style BFS for neighbor discovery.
- **Shortest-hop routing in unweighted networks** — BFS
  gives minimum-hop paths.
- **Game AI pathfinding** — unweighted grids use BFS;
  weighted use A*.

## Related algorithms in cOde(n)

- **[graph_03 — DFS](graph_03_dfs.md)** — the other
  fundamental graph search. (d=4/10, r=8/10)
- **[graph_04 — Dijkstra](graph_04_dijkstra.md)** — BFS
  generalized to non-negative weighted graphs. (d=5/10, r=8/10)
- **[search_03 — BFS Grid](search_03_bfs-grid.md)** — the
  concrete 2D-grid version. (d=5/10, r=8/10)
- **[graph_17 — 0-1 BFS](graph_17_01-bfs.md)** — for graphs
  with 0/1 edge weights. (d=5/10, r=8/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
