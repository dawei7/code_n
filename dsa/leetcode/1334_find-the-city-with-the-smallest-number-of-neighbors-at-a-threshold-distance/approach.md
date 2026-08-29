## General

The task is not about the number of direct roads. A city counts as reachable when the **shortest total weight** of some path to it is at most `distanceThreshold`. A path may travel through several intermediate cities, so the solution must compute shortest-path distances before it counts neighbors.

The checked-in implementation runs Dijkstra’s algorithm once from every city. Because `n` is at most one hundred, it uses a dense adjacency matrix and finds the next city with a linear scan instead of using a heap.

**Build a dense view of the undirected graph**

The matrix `g` has `n` rows and `n` columns. Every entry initially equals positive infinity, meaning that no direct road is known. For each edge `[f, t, w]`, the assignments `g[f][t] = g[t][f] = w` store the same weight in both directions because every road is undirected.

The statement guarantees no duplicate edge between a pair of cities, so direct assignment is sufficient. If duplicate edges were allowed, the matrix construction would need to retain the minimum weight rather than whichever edge appeared last.

The diagonal entries of `g` remain infinity. That may initially look strange because the distance from a city to itself is zero, but the per-source distance array handles that fact explicitly with `dist[u] = 0`. Dijkstra does not require a zero-weight self-edge in the adjacency matrix.

**Find all distances from one source**

For a source `u`, `dist[j]` is the best path length discovered so far from `u` to city `j`. Every value begins at infinity except `dist[u]`, which begins at zero. The Boolean array `vis` records which cities have already been finalized.

Each of the `n` rounds performs two operations:

1. Scan every city `j` and choose an unvisited city `k` with the smallest current `dist` value.
2. Mark `k` visited, then scan every possible destination `j` and try the path that reaches `j` through `k`.

The relaxation test `dist[k] + g[k][j] < dist[j]` asks whether the best known route to `k` followed by the direct road from `k` to `j` improves the current route to `j`. When it does, the code stores the smaller total.

All edge weights are positive. Therefore, when `k` is the unvisited city with the smallest tentative distance, no later route through another unvisited city can produce a shorter path to `k`. Any such route would first have to reach a city whose tentative distance is at least `dist[k]` and then add a positive edge. Marking `k` final is safe. Repeating this argument finalizes every finite shortest-path distance.

Disconnected cities are also handled. If every remaining unvisited city has infinite distance, the selection condition still chooses one because `k` starts at `-1` and the first unvisited candidate satisfies `k == -1`. Relaxing from an unreachable city makes no improvements because infinity plus any matrix value remains infinity. After exactly `n` rounds, every city has been marked once, and unreachable distances remain infinite.

**Convert distances into a reachability count**

After Dijkstra finishes, `sum(d <= distanceThreshold for d in dist)` counts distances no greater than the inclusive threshold. Infinite distances fail the test, while a path whose length equals the threshold passes.

This exact expression also counts the source itself because `dist[u]` is zero. The problem describes other reachable cities, so one might expect the source to be excluded. However, every source gains exactly the same extra count of one:

$$
\text{storedCount}(u) = \text{neighborCount}(u) + 1.
$$

Adding the same constant to every candidate does not change which count is smallest and does not change any ties. Thus the returned city is still correct even though the internal counts include self.

**Make the greatest-index tie rule automatic**

The outer loop examines sources in descending order, from `n - 1` down to zero. The current best answer changes only when `t < cnt`, never when the new count merely equals `cnt`. The first city encountered among all cities with the minimum count is therefore the one with the greatest index, and later smaller tied indices cannot replace it.

The initialization `ans, cnt = n, inf` guarantees that the first evaluated city becomes the current answer. After every iteration, `cnt` is the smallest stored count seen so far, and `ans` is the greatest index among the already examined cities having that count. The strict update preserves this property, so after city zero is processed, `ans` satisfies both the minimum-neighbor and maximum-index requirements.

## Complexity detail

Let $n$ be the number of cities and $m$ the number of roads.

Constructing the `n` by `n` matrix costs $O(n^2)$ time to fill and $O(n^2)$ space. Writing the $m$ roads costs another $O(m)$ time, which is at most $O(n^2)$ for this simple undirected graph.

One call to `dijkstra` performs `n` rounds. In every round, selecting `k` scans $n$ cities and relaxing the matrix row scans another $n$ entries. One source therefore costs $O(n^2)$ time. The method runs it for all $n$ sources, giving $O(n^3)$ total time. Counting threshold-reachable cities happens inside each call in $O(n)$ time and does not change the cubic bound.

The adjacency matrix uses $O(n^2)$ space. A single Dijkstra call allocates `dist` and `vis`, each of length $n$, so its temporary space is $O(n)$. Calls are sequential rather than recursive or concurrent, meaning their temporary arrays do not accumulate. The overall auxiliary space is dominated by the matrix at $O(n^2)$.

## Alternatives and edge cases

- **Floyd–Warshall:** Initialize an all-pairs distance matrix and consider each city as an intermediate vertex. It also runs in $O(n^3)$ time and $O(n^2)$ space, and is often the simplest all-pairs formulation for this small dense bound.
- **Heap-based Dijkstra from every city:** An adjacency list and priority queue give roughly $O(n(m + n)\log n)$ time and $O(n + m)$ graph storage. It is generally preferable for sparse large graphs, while the dense scan is simple and predictable for $n \le 100$.
- **Bellman–Ford:** It can handle negative edges, but this problem guarantees positive weights. Repeating Bellman–Ford from every source does unnecessary work and has a worse worst-case bound.
- **Threshold pruning:** A heap implementation may stop expanding paths beyond `distanceThreshold` because only the reachable count matters. The checked-in dense implementation computes all shortest distances, which keeps its reasoning straightforward.
- **Tie handling:** Descending source order must be paired with a strict `<` update. Changing it to `<=` would let smaller indices replace equal-count larger indices and violate the required tie-breaker.
- **Distance exactly at the threshold:** The destination is reachable because the comparison is `<=`, not `<`.
- **Disconnected graph:** Infinite distances are never counted. The array selection still chooses and visits unreachable vertices safely after all reachable vertices are finalized.
- **Self-counting:** The source contributes one to every stored count. This is harmless only because the same constant is added for every candidate; excluding self explicitly would produce the same answer.
- **Single direct road versus a cheaper multi-road path:** Repeated relaxation can replace a direct edge weight with a smaller route through intermediate cities, which is why merely counting matrix entries below the threshold would be incorrect.
- **Positive weights:** Dijkstra’s finalization argument relies on nonnegative weights. The stated strictly positive road weights satisfy that requirement.
- **Duplicate edges outside the contract:** Direct matrix assignment would keep only the last duplicate. If duplicates were allowed, construction should use the minimum weight for each pair.
