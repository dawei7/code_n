## General

Cities are vertices and directed roads are edges. Every road has the same cost of one, so the shortest-path length is the minimum number of edges from city zero to city `n - 1`. Breadth-first search finds exactly that distance in an unweighted graph.

The graph persists across queries because every query adds a road and no road is removed. The adjacency list `g` begins with the original chain: for each index from zero through `n - 2`, `g[i]` contains `i + 1`. The list has only `n - 1` rows rather than $n$ because destination city `n - 1` has no outgoing road under the forward-edge constraints. The BFS returns as soon as that destination is dequeued, so it never indexes `g[n - 1]`.

For each query `[u,v]`, the code appends `v` to `g[u]`. The road is available not only for the current result but for every later result. It then runs `bfs(0)` against the complete graph built so far and appends the returned distance to `ans`.

**Why BFS layers equal path lengths.** The queue begins with the start city and distance counter `d = 0`. At the beginning of a while-loop iteration, every vertex currently in the queue is at distance `d`. The expression `range(len(q))` freezes the number of vertices in that current layer. Neighbors discovered while processing them are appended behind the layer and are not processed until the next iteration.

When city `n - 1` is removed from the queue, `d` is therefore the number of roads on the path that first discovered it. BFS explores all paths with fewer edges before any path with more edges, so no shorter route can remain undiscovered. Returning `d` at that moment is correct.

The Boolean array `vis` is newly created for every BFS. The start is marked immediately. A neighbor is enqueued only if it has not been visited, and it is marked at enqueue time rather than dequeue time. This ensures each city enters the queue at most once even if several roads lead to it.

After every vertex in the current layer is processed, `d` is incremented. Newly queued vertices then form the next distance layer. The helper uses `while 1` without an empty-queue exit. This is safe under the contract because the original roads `0 -> 1 -> 2 -> ... -> n - 1` are never removed, so the destination is always reachable and BFS always returns.

For `n = 5`, the original shortest route uses four roads. After adding `2 -> 4`, BFS layers are `{0}`, `{1}`, `{2}`, and then a layer containing city four, so the answer is three. Adding `0 -> 2` persists alongside the first shortcut, producing `0 -> 2 -> 4` of length two. Adding `0 -> 4` then makes the answer one.

**Why recomputation is acceptable here.** Adding an edge can lower distances to its destination and to any later vertices reachable from it. Maintaining all consequences incrementally is possible but more involved. In this first version of the problem, both $n$ and the number of queries are at most five hundred. Re-running a straightforward BFS after each addition stays within the intended limits and provides a robust shortest-path computation.

The graph is actually a directed acyclic graph because every legal road goes from a smaller identifier to a larger one. BFS does not need that stronger property; it would remain correct in any unweighted directed graph. The visited array also makes the helper safe against cycles if the road constraints were relaxed, apart from the compact adjacency list needing a row for the last city if it gained outgoing roads.

**Why every reported answer is independent in time but cumulative in roads.** Each query asks for the shortest path after the first $i+1$ additions, so `g` must retain earlier roads. BFS state itself must not persist: `vis` and the queue are recreated because a city visited during the previous shortest-path search still needs to be explored under the newly expanded graph.

## Complexity detail

Let $q$ be the number of queries. After processing query $k$, using one-based counting, the graph contains $n-1+k$ edges. That BFS takes $O(n+n-1+k)=O(n+k)$ time. Summing over all queries gives

$$
\sum_{k=1}^{q}O(n+k)=O(qn+q^2)=O(q(n+q)).
$$

The persistent adjacency list stores $n-1+q$ edges, using $O(n+q)$ space. During one BFS, `vis` and the queue use $O(n)$ temporary space. The returned list uses $O(q)$ space. Whether output is included or excluded, the overall bound remains $O(n+q)$.

The helper may return before examining every edge when the target is found, but the complexity bound uses the worst case. Each city is enqueued once and each outgoing adjacency entry of a dequeued city is examined once.

## Alternatives and edge cases

- **Bottom-up DAG dynamic programming:** Because all edges point to larger identifiers, compute distances to `n - 1` from right to left after every query. It has the same $O(q(n+q))$ total worst-case time and avoids a queue.
- **Top-down memoized recursion:** The DAG permits a shortest-distance recurrence over outgoing neighbors. Reinitializing memoization after each query is necessary, and a long chain risks Python recursion depth.
- **Incremental distance relaxation:** When a new edge improves `dist[v]`, propagate improvements forward through outgoing edges. This may do less work in practice but needs more careful cumulative analysis.
- **Direct BFS after each query:** This is the exact source approach. Its simplicity is well matched to the version-I limit of five hundred nodes and queries.
- **A shortcut directly to the destination:** Once `0 -> n - 1` exists, the answer is one and can never decrease further. The source still runs BFS for later queries, but it returns from the first next layer.
- **A query that does not improve the shortest path:** The road remains in `g`, BFS finds the same distance, and that unchanged value is appended.
- **Persistent roads:** Clearing or rebuilding `g` with only the latest query would be wrong because every answer includes all earlier additions.
- **Fresh visited state:** Reusing `vis` across queries would skip cities and miss paths created by the new road. The helper correctly allocates it per run.
- **No repeated query roads:** The constraint avoids duplicate adjacency entries, although BFS correctness would survive duplicates because `vis` prevents duplicate enqueues.
- **Guaranteed reachability:** The original chain means `while 1` always reaches `n - 1`. Without that guarantee, the helper would need an empty-queue condition and a value representing no path.
- **Forward-only roads:** They make the graph acyclic and ensure `u <= n - 3` under the required gap, so the compact `g` with no destination row is safe.
