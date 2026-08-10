## General

**The restriction is defined by distances to node `n`**

A path is restricted when every step moves from a node with a larger shortest distance to node `n` to a node with a smaller shortest distance to node `n`. The first task is therefore not to count paths. It is to know the exact value of `distanceToLastNode(x)` for every node `x`.

The graph is undirected and all edge weights are positive. Shortest distances to node `n` can be found by running Dijkstra's algorithm with node `n` as the source. In an undirected graph, the shortest distance from `x` to `n` is the same as the shortest distance from `n` to `x`, so this reversed viewpoint computes exactly the quantities in the definition.

The solution builds an adjacency list `g`. Every input edge `[u, v, w]` is inserted once as `(v, w)` in `g[u]` and once as `(u, w)` in `g[v]`. It then creates a distance array initialized to infinity, sets `dist[n] = 0`, and starts a min-heap with `(0, n)`.

Whenever node `u` is removed from the heap, each neighbor `v` is tested. If traveling from `v` through `u` gives a shorter route to the destination, meaning `dist[u] + w < dist[v]`, the solution records that new distance and pushes a new heap entry for `v`. Positive weights and the min-heap ordering ensure that the smallest possible distances propagate outward from node `n`.

**Turn the undirected graph into an implicit directed acyclic graph**

After the distance phase, consider an undirected edge between `i` and `j`. The counting phase may traverse it from `i` to `j` only when `dist[i] > dist[j]`. Conceptually, this orients every usable edge from a greater distance to a smaller distance.

That orientation cannot contain a directed cycle. Following a directed edge strictly decreases `dist`, so returning to a previously visited node would require its distance to be both strictly smaller and equal to its earlier value. This contradiction means the usable edges form a directed acyclic graph, even though the original graph can have many cycles.

This is the central simplification. Counting unrestricted simple paths in a general graph can be extremely expensive, but counting paths in a DAG is a dynamic-programming problem.

**Memoized depth-first counting**

Define `dfs(i)` as the number of restricted paths that begin at node `i` and finish at node `n`.

If `i == n`, there is one completed path: the path has already reached its destination. Thus `dfs(n)` returns 1.

For every other node, the function examines its neighbors. It follows only neighbors `j` satisfying `dist[i] > dist[j]`, because exactly those steps preserve the restricted-path condition. Every restricted path from `i` must choose one such first neighbor, and after making that choice it can use any restricted path counted by `dfs(j)`. Therefore,

$$
\operatorname{dfs}(i)
=
\sum_{\substack{j\text{ adjacent to }i\\\texttt{dist}[i]>\texttt{dist}[j]}}
\operatorname{dfs}(j).
$$

The `@cache` decorator stores each completed result, so if several incoming paths reach the same node, its suffix count is computed once and reused. Each addition is reduced modulo $10^9+7$, as required.

Although `dfs` is declared before `g`, `dist`, and `mod` are assigned, Python closures look up those names when the function is called. The only call, `dfs(1)`, occurs after the graph and distances are complete, so the references are ready.

**Following the first example**

For the five-node example, shortest distances to node 5 are `dist[5] = 0`, `dist[3] = 1`, `dist[2] = 2`, `dist[1] = 4`, and `dist[4] = 6`. From node 1, edges to nodes 2 and 3 decrease the distance, while the edge to node 4 increases it and is forbidden.

The decreasing choices produce `1 -> 2 -> 5`, `1 -> 2 -> 3 -> 5`, and `1 -> 3 -> 5`. At every arrow the distance strictly falls, and the memoized recurrence counts those three possibilities.

**Why the final count is correct**

Dijkstra's relaxations establish the shortest distance from every node to `n`. The DFS then accepts an edge exactly when it satisfies the problem's strict-distance rule.

For the base case, there is exactly one suffix after reaching `n`. For any other node `i`, partition all valid paths by their first next node `j`. Different first neighbors form disjoint groups, and every allowed group contains exactly the valid suffixes counted by `dfs(j)`. Summing those cached suffix counts therefore counts every restricted path from `i` once and no invalid path. Applying the argument to node 1 proves that `dfs(1)` is the requested answer.

## Complexity detail

Let $E$ be the number of undirected edges. Building the adjacency list takes $O(n+E)$ space and $O(E)$ time. The memoized DFS computes at most one result per node and examines every adjacency-list entry at most once during those first computations, so its counting work is $O(n+E)$. The distance array, cache, and recursion stack use $O(n)$ additional space.

A conventional heap-based Dijkstra implementation that discards stale heap entries runs in $O((n+E)\log n)$ time, which is the bound recorded in the Optimal manifest. The protected code, however, removes the heap key into `_` and never checks whether it differs from the current `dist[u]`. A node can therefore have several queued distances, and every stale removal scans that node's adjacency list again. Correctness is unchanged because relaxations use the best current `dist[u]`, but the strict implementation-level worst case includes those repeated scans.

If $r_v$ is the number of heap entries removed for node $v$, the exact scan cost is $O(\sum_v r_v\deg(v))$. A node can receive multiple improving candidates before its final distance is removed, giving the safe bound $O(\sum_v \deg(v)^2)$, which is $O(E^2)$ in the worst case. Heap operations add $O(E\log E)$. Thus the exact code has a conservative worst-case time bound of $O(E^2+E\log E+n)$, rather than the manifest's standard Dijkstra bound. Adding the usual stale-entry guard would restore $O((n+E)\log n)$.

The heap can retain $O(E)$ candidate entries, so total auxiliary space remains $O(n+E)$, matching the manifest's space bound.

## Alternatives and edge cases

- **Dijkstra with a stale-entry guard:** Keep the popped distance and skip the adjacency scan when it is not equal to `dist[u]`. This preserves the same results and attains the manifest's $O((n+E)\log n)$ time bound.
- **Iterative DAG dynamic programming:** Sort nodes by increasing distance and accumulate path counts without recursion. It avoids recursion-depth risk while using the same distance orientation.
- **Enumerate complete paths:** Backtracking through all decreasing choices repeats common suffixes and can take exponential time; memoization is essential.
- **Run Dijkstra from node 1:** That computes distances to the wrong endpoint. The restriction compares shortest distances to node `n`, so the distance source must be `n`.
- **Breadth-first search:** BFS is insufficient because edge weights vary; the fewest-edge route need not have minimum total weight.
- **Equal distances:** An edge whose endpoints have equal `dist` values is forbidden because the inequality is strict, not non-increasing.
- **Positive weights:** They support Dijkstra and ensure shortest-distance reasoning is well behaved. Negative weights would invalidate this method.
- **Original graph cycles:** They cause no counting cycle because every accepted DFS step strictly decreases distance.
- **Multiple incoming restricted paths:** Cached suffix counts are intentionally reused; the distinct prefixes still make the complete paths distinct.
- **Modulo arithmetic:** Reducing after every addition prevents the count from growing needlessly while preserving the final residue.
- **Single node:** When `n = 1`, `dfs(1)` immediately returns one for the already-complete path.
- **Connected graph guarantee:** Every `dist` becomes finite. No special unreachable-node behavior is needed.
- **Deep decreasing chain:** The recursive DFS can reach depth $O(n)$; in Python, a sufficiently long chain may exceed the runtime's recursion limit. An iterative distance-ordered DP avoids that implementation hazard.
- **Input preservation:** The method builds its own adjacency representation and never mutates `edges`.
