## General

Expanding every subdivided edge into thousands of explicit nodes could make the graph unnecessarily large. The central idea is to compute shortest distances only among original nodes, then count how far the remaining move budget reaches into each subdivided edge from its two endpoints.

An original edge `[u, v, cnt]` becomes a chain with `cnt` inserted nodes and `cnt + 1` unit edges. Therefore traveling all the way from original node `u` to original node `v` costs `cnt + 1` moves. The adjacency list stores exactly that compressed weight in both directions.

**Shortest distances to original nodes.** The intended algorithm is Dijkstra's algorithm from node 0 because all compressed edge weights are positive. `dist[u]` is the smallest known number of moves needed to reach original node `u`. It begins at zero for node 0 and infinity elsewhere.

For a processed pair $(d,u)$ and neighbor edge of weight `cnt + 1`, the candidate distance is `t = d + weight`. If `t < dist[v]`, the solution records the improvement and schedules $(t,v)$ for later processing. Once correct shortest distances are known, an original node is reachable exactly when `dist[u] <= maxMoves`.

The allocation `dist = [0] + [inf] * n` creates $n+1$ entries although valid node labels use only $0$ through $n-1$. The final extra infinity is harmless: it is never addressed by graph edges, and the sum over `dist` includes it as false.

**Count internal nodes without expanding them.** Consider one original edge with `cnt` internal nodes. If original endpoint `u` is reachable in `dist[u]` moves, the remaining budget after reaching it is `maxMoves - dist[u]`. From `u`, each additional move enters one more internal node along the chain. The number reachable from that side is therefore

```text
a = min(cnt, max(0, maxMoves - dist[u]))
```

The maximum with zero handles an unreachable or over-budget endpoint. The minimum with `cnt` prevents counting past all internal nodes into the opposite endpoint.

The same calculation from `v` produces `b`. The two reachable prefixes of the edge may be disjoint or may overlap. Their union contains

$$
\min(\text{cnt},a+b)
$$

internal nodes. If $a+b$ is smaller than `cnt`, the two reached portions do not cover the whole chain and their lengths add. If $a+b$ reaches or exceeds `cnt`, all internal nodes are reachable, but there are still only `cnt` distinct nodes, so the cap prevents double-counting the overlap.

Each original node is counted once by the distance test, and each internal node belongs to exactly one original edge and is counted in that edge's union formula. The final total therefore has no cross-edge duplication.

**Why shortest distances are sufficient.** Reaching an endpoint by any longer route leaves no more moves for entering its incident edges. The shortest route maximizes the remaining budget, so no other path can expose more internal nodes from that endpoint. Counting from both endpoints covers internal nodes that are reachable without requiring the opposite original endpoint itself to be reachable.

For example, an edge with ten internal nodes may be entered six steps from `u` even if the complete eleven-step crossing to `v` is impossible. Those six internal nodes still count. This is why merely counting endpoints or fully traversable compressed edges would undercount.

**Important implementation caveat.** The exact file initializes `q = [(0, 0)]` and removes entries with `heappop(q)`, but it schedules improved entries using `q.append((t, v))` rather than `heappush(q, (t, v))`. Appending does not preserve Python's heap invariant.

Because the code does not permanently mark nodes visited and reschedules every strict improvement, it behaves like a label-correcting worklist: improved distances can propagate again later, and positive weights ensure the relaxation process eventually stabilizes on shortest distances. However, `heappop` on a list that is not maintained as a heap does not guarantee smallest-distance-first processing. Consequently, the exact code does not justify the manifest's Dijkstra time bound. Replacing `append` with `heappush` would implement the intended priority queue and establish $O((n+m)\log n)$ time.

## Complexity detail

Let $n$ be the number of original nodes and $m$ the number of original edges.

- **Intended Dijkstra time complexity:** $O((n+m)\log n)$ when every improved entry is inserted with `heappush`.
- **Counting pass:** $O(n+m)$ after distances are available.
- **Space complexity:** $O(n+m)$ for the adjacency list, distance array, and scheduled entries.

For the exact `append`/`heappop` mixture, the heap ordering guarantee is absent. Repeated relaxations still target correct distances, but the advertised Dijkstra complexity cannot be claimed from this implementation; an adversarial graph can cause extra processing.

## Alternatives and edge cases

- **Explicitly build the subdivided graph:** This is conceptually simple but may add up to $10^4$ nodes per edge and consume excessive time and memory.
- **Correct priority-queue Dijkstra:** Use `heappush(q, (t, v))` and optionally skip stale pops with `if d != dist[u]: continue`. This realizes the intended complexity.
- **Plain breadth-first search on compressed edges:** Edge weights are `cnt + 1` rather than all one, so BFS among original nodes does not compute shortest move counts.
- **Bellman-Ford-style relaxation:** It can compute distances with positive weights but is much slower than properly implemented Dijkstra.
- **No edges:** Node 0 is the only reachable node, regardless of move budget.
- **`maxMoves = 0`:** Only original node 0 is reachable; no unit can be spent entering an internal node.
- **`cnt = 0`:** The edge has no internal nodes. Its compressed weight is one, and its counting contribution is zero.
- **Disconnected graph:** Unreachable endpoints retain infinity, contribute no remaining budget, and are not counted as original nodes.
- **Reach from only one endpoint:** The formula counts that one reachable prefix even if the opposite endpoint is unreachable.
- **Prefixes overlap:** `min(cnt, a + b)` caps the union at the number of distinct internal nodes.
- **Reach endpoint with exactly the budget:** The original endpoint counts, but it leaves zero moves for entering adjacent subdivided edges.
- **Extra distance-array entry:** The $n+1$-st infinity is harmless but unnecessary; a length-$n$ array would be cleaner.
- **Stale scheduled distances:** A correct Dijkstra implementation should skip them for efficiency. The relaxation condition prevents a stale record from overwriting a better distance.
- **No multiple original edges:** Each internal chain belongs to one edge, which makes independent per-edge counting valid.
