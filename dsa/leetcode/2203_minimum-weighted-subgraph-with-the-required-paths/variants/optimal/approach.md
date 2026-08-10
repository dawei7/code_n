## General

The two source-to-destination routes may share a suffix. If they first come together at some node `v`, the required weight separates into three directed path costs:

- `src1` to `v`;
- `src2` to `v`;
- `v` to `dest`.

The exact solution computes the shortest value for each of these components at every possible meeting node and minimizes their sum.

**Build forward and reversed graphs**

For each directed edge `f -> t` of weight `w`:

- `g[f]` stores `(t, w)` for travel in the original direction;
- `rg[t]` stores `(f, w)` for travel in the reversed graph.

The reversed edge does not change the original problem. It is a computational tool for finding distances toward `dest` with one single-source shortest-path run.

**Run Dijkstra from both sources**

`dijkstra(g, src1)` returns array `d1`, where `d1[v]` is the minimum weight of a directed path from `src1` to `v`.

The analogous run from `src2` creates `d2`.

All edge weights are positive, satisfying Dijkstra's requirement that once the smallest current distance is finalized, no later route through nonnegative edges can improve it unexpectedly.

**Compute every node-to-destination distance**

Running `dijkstra(rg, dest)` follows reversed edges outward from `dest`.

A reversed path from `dest` to `v` corresponds edge-for-edge to an original directed path from `v` to `dest` with the same total weight. Thus `d3[v]` is the needed forward distance from `v` into the destination.

Without reversal, one would need a separate Dijkstra run from every possible meeting node or a different all-pairs method.

**Understand the heap relaxation**

Each Dijkstra run initializes all distances to infinity except its source at zero. The min-heap stores candidate pairs `(distance, node)`.

When a popped distance `d` exceeds the current `dist[u]`, that heap entry is stale and skipped. Otherwise every outgoing edge is relaxed: if reaching `v` through `u` improves its distance, the array is updated and the new pair enters the heap.

Multiple heap entries for one node are harmless because only the current best one is expanded.

**Test every possible meeting node**

`zip(d1, d2, d3)` produces the three relevant distances for node zero, then node one, and so on. `sum(v)` computes

$$
d_1[v]+d_2[v]+d_3[v].
$$

If any component is unreachable, it is infinity and the sum cannot become the finite minimum.

The smallest finite sum is returned. If all candidates remain infinite, no node can be reached from both sources and continue to `dest`, so the method returns `-1`.

**Why an optimal subgraph has a meeting-node interpretation**

Take a minimum-weight feasible subgraph and choose one source-to-destination path for each source within it. Because weights are positive, unnecessary cycles and branches can be removed.

Once the two paths meet, both can use one common continuation to `dest`. If they split and later rejoin, retaining only one of the split continuations cannot hurt reachability and removes positive weight. Therefore a minimum solution can be viewed as two prefixes meeting at some `v` followed by one shared suffix.

The three parts of that minimal structure have weights at least `d1[v]`, `d2[v]`, and `d3[v]`. Hence every feasible optimum is at least the minimum candidate sum.

Conversely, for any node `v` with finite distances, choose corresponding shortest paths for the three components. Their union is a feasible subgraph. If paths overlap before `v`, the union counts shared edges only once and can be even lighter than the arithmetic sum, never heavier. The global minimum structure argument ensures some meeting node attains the true optimum.

Together these directions establish that the minimum summed distances equal the minimum subgraph weight.

## Complexity detail

Let $m$ be the number of edges. One binary-heap Dijkstra run takes $O((n+m)\log n)$ time in the standard bound. Three runs change only the constant factor, so total time remains $O((n+m)\log n)$.

The forward and reversed adjacency lists contain $O(n+m)$ structure, three distance arrays contain $O(n)$ entries, and a heap may hold $O(m)$ candidates. Total auxiliary space is $O(n+m)$.

The manifest bounds match the exact implementation.

## Alternatives and edge cases

- **Run Dijkstra only forward from `dest`:** This gives distances from destination to nodes, the wrong direction in a directed graph; reversing edges is essential.
- **Floyd–Warshall:** All-pairs shortest paths cost $O(n^3)$ and cannot handle $n=10^5$.
- **Bellman–Ford:** It supports negative weights but is unnecessary and much slower because all weights are positive.
- **Meeting at `src1` or `src2`:** The formula allows any node; a zero source-to-self distance handles these cases.
- **Meeting at `dest`:** Then `d3[dest] = 0`, representing two independent paths that share no earlier suffix.
- **Parallel directed edges:** Relaxation naturally chooses the cheaper useful route.
- **Unreachable component:** Infinity excludes that meeting node.
- **No feasible subgraph:** Every triple contains infinity and the return becomes `-1`.
- **Shared edges:** The conceptual union pays once; the optimal meeting-node proof accounts for shared suffix structure.
- **Positive weights:** They justify Dijkstra and removal of unnecessary cycles or split branches.
- **Stale heap entries:** The distance comparison prevents obsolete candidates from being expanded.
- **Input preservation:** Edges are copied into adjacency structures and not modified.
