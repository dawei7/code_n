## General

**The answer depends on shortest travel time to every node**

The signal can follow directed edges, and all edge weights are nonnegative. For each node, the earliest arrival time is the shortest-path distance from source `k`. All nodes have received the signal only when the farthest reachable node receives it, so the final answer is the maximum of these shortest distances.

The exact solution applies Dijkstra’s algorithm using an adjacency matrix and a linear scan to select the next node.

**Build a one-based-to-zero-based adjacency matrix**

The matrix `g` has `n` rows and `n` columns and starts filled with infinity. For each directed edge `(u, v, w)`, the solution writes

`g[u - 1][v - 1] = w`.

Subtracting one converts labels `1..n` to Python indices `0..n-1`. The reverse cell is not written because edges are directed.

Infinity means there is no direct edge. Pair uniqueness guarantees no competing duplicate edge needs to be minimized.

**Initialize tentative distances**

Every distance begins at infinity except the source:

`dist[k - 1] = 0`.

The Boolean array `vis` records nodes whose shortest distance has been finalized.

**Choose the nearest unvisited node**

On every iteration, the inner scan finds an unvisited index `t` with minimum tentative `dist`. It starts with `t = -1` and replaces it upon seeing the first unvisited node or a smaller distance.

Once selected, `vis[t]` becomes true.

Dijkstra’s key fact is that a minimum-distance unvisited node cannot later receive a shorter path through another unvisited node when all edge weights are nonnegative. Any such alternative would first have to reach that other node with distance at least `dist[t]` and then add a nonnegative edge.

**Relax every possible outgoing edge**

The matrix row `g[t]` contains the direct travel time from `t` to every `j`, or infinity when no edge exists. The update

`dist[j] = min(dist[j], dist[t] + g[t][j])`

compares the best known route with a route that first reaches finalized node `t` and then uses its edge to `j`.

Adding infinity leaves an infinite candidate, so absent edges need no explicit branch.

If `t` itself is unreachable, `dist[t]` is infinity and all its relaxations remain infinity. The algorithm still marks one unvisited node each iteration, allowing the fixed `n` iterations to finish safely.

**Why zero-weight edges are valid**

Weights may be zero, but they are never negative. The proof that the selected minimum tentative distance is final still holds. Several nodes can have the same distance; selecting any one of them is safe.

**Compute the network completion time**

After `n` selections, every reachable node has its shortest distance. `ans = max(dist)` is the time when the last node receives the signal.

If any node is unreachable, its entry remains infinity and therefore the maximum is infinity. The method returns `-1` in that case. Otherwise it returns the finite maximum.

**Trace the small example**

With edges `2 -> 1` of weight 1, `2 -> 3` of weight 1, and `3 -> 4` of weight 1, source 2 begins at distance zero.

Selecting node 2 relaxes nodes 1 and 3 to time one. Either may be finalized next. When node 3 is selected, it relaxes node 4 to time two. The final distances are one, zero, one, and two in label order, so the maximum delay is two.

**Why the algorithm is correct**

At every selection, `t` has the smallest tentative distance among unvisited nodes. Nonnegative edges ensure no future route through another unvisited node can improve it, so marking it final is correct. Relaxation considers every route whose final edge leaves `t`, maintaining the best known distance for remaining nodes.

By induction, all finalized distances are shortest-path distances. After all nodes are processed, the maximum finite shortest distance is exactly the earliest time by which every node has received the signal. An infinite distance proves that complete delivery is impossible.

## Complexity detail

Constructing the `n x n` matrix costs `O(n^2)` time for initialization plus `O(e)` edge writes. Dijkstra performs `n` iterations; both selecting `t` and relaxing its full matrix row scan `n` entries. The total time is `O(n^2 + e)`, simplified to `O(n^2)` because matrix initialization already dominates within the simple directed graph.

The matrix uses `O(n^2)` space, while distance and visited arrays use `O(n)`.

The manifest-style `O((n + e) log n)` time and `O(n + e)` space belong to adjacency-list Dijkstra with a binary heap. The exact stored implementation uses neither an adjacency list nor a heap, so its literal bounds are quadratic.

## Alternatives and edge cases

- **Adjacency list plus min-heap:** Store only real edges and repeatedly pop the smallest tentative distance. This gives `O((n + e) log n)` time and `O(n + e)` space and is preferable for sparse large graphs.

- **Bellman-Ford:** Repeatedly relax every edge and handle negative weights. It is unnecessary here because all weights are nonnegative and costs `O(ne)` time.

- **Breadth-first search:** It finds shortest paths only when all edges have equal weight. Varying travel times require weighted shortest-path logic.

- **Unreachable node:** Its distance stays infinity, making the final maximum infinite and the return value `-1`.

- **Single node:** The source distance is zero, so the result is zero even with no useful outgoing path.

- **Zero-weight edges:** Dijkstra remains valid because weights are nonnegative.

- **Directed edges:** Do not add a reverse matrix entry unless that reverse edge is explicitly supplied.

- **Unreachable node selected late:** Its infinite relaxations change nothing; fixed iterations still terminate without a special break.
