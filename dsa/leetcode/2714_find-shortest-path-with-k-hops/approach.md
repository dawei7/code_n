## General

**Expand one graph node into hop-count states**

Reaching node $u$ after using $t$ free hops is different from reaching the same node after using another number, because the remaining free-hop budget differs.

The algorithm therefore treats `(u, t)` as a shortest-path state, where $0\le t\le k$ is the exact number of free edges already used.

Matrix `dist[u][t]` stores the minimum paid cost known for that state.

**Build the ordinary undirected adjacency list**

For every edge `[u, v, w]`, the source appends `(v, w)` to `g[u]` and `(u, w)` to `g[v]`.

The same physical edge can be traversed in either direction. All weights are positive, and using a hop changes one chosen traversal's paid cost to zero.

The input graph itself is not modified.

**Start with no free edge used**

At the source, the path cost is zero and no hop has been consumed:

`dist[s][0] = 0`.

The initial heap entry is `(0, s, 0)`. Every later heap entry orders states by current candidate distance first.

**Paid transition**

From popped state `(u, t)` across edge weight $w$, the algorithm may pay normally.

The next state is `(v, t)` with candidate:

$$
\texttt{dis}+w.
$$

If this improves `dist[v][t]`, the table is updated and the state is pushed.

**Free-hop transition**

If `t + 1 <= k`, the same edge may be hopped over at zero cost.

The next state is `(v, t + 1)` with candidate distance `dis`.

This consumes exactly one additional hop and adds no weight. Keeping the hop count in the state prevents using more than $k$ such transitions.

**Why ordinary Dijkstra reasoning applies**

The expanded graph contains only nonnegative transition weights: ordinary edges cost positive $w$, and hop edges cost zero.

Dijkstra's priority queue can therefore explore shortest costs over the expanded states.

The algorithm does not need to decide in advance which original edges receive free treatment. Every path through the expanded graph represents one such choice sequence.

**At most rather than exactly `k`**

The destination may be reached with any hop count from zero through $k$.

The method returns `min(dist[d])`, choosing the cheapest state among all allowed counts.

It does not force wasting all hops when fewer already give the optimal route.

**Trace a path with three edges and two hops**

For edge weights 4, 2, and 6, begin at state `(source, 0)`.

Hop the first edge to reach the next node with cost zero and count one. Pay the middle edge to reach cost two with count one. Hop the last edge to reach the destination with cost two and count two.

The expanded-state route has the same meaning as setting those two selected edge traversals to zero.

**Cycles cannot create unlimited free use**

The original graph may contain cycles. A free transition always increases $t$, so at most $k$ free transitions can occur along any expanded route.

Paid positive cycles cannot improve a shortest path. Zero-cost hop transitions are also bounded by the layered state index.

**Relaxation invariant**

Every finite `dist[u][t]` corresponds to an actual path from `s` to $u$ using exactly $t$ hops and paying that stored candidate cost.

Each paid or free relaxation appends one legal edge choice, preserving realizability. Conversely, every legal original path with hop choices maps step by step to an expanded-state path, so the search space is complete.

Dijkstra relaxation finds the minimum cost for each expanded state.

**Exact stale-entry behavior**

The source does not include the common check `if dis > dist[u][t]: continue`.

An outdated larger heap entry can therefore scan all of $u$'s neighbors again. It cannot corrupt correctness because every write still requires a strict distance improvement, and the best smaller entry is ordered before the stale one.

However, these redundant scans weaken the clean heap-runtime bound claimed in the manifest.


There is a cost-preserving one-to-one correspondence between valid paths with exactly $t$ hopped edges and paths to expanded state `(d, t)`. All expanded transition costs are nonnegative.

The relaxation process therefore computes each state's shortest cost. Taking the minimum destination cost over $t\le k$ yields exactly the shortest path using at most $k$ hops.

Stale entries may repeat work but cannot install a non-improving value.

## Complexity detail

The expanded graph has $n(k+1)$ states and $O(E(k+1))$ transitions. With a stale-entry guard, standard Dijkstra costs $O(E(k+1)\log(n(k+1)))$ time.

The exact source omits that guard. With maximum original degree $\Delta$, a conservative bound including redundant stale scans is $O(E(k+1)(\Delta+\log(n(k+1))))$. The adjacency list, distance table, and heap require up to $O((n+E)(k+1))$ space.

## Alternatives and edge cases

- **Add the stale-entry check:** Preserves behavior and realizes the standard manifest heap bound.
- **Bellman-Ford-style DP by hops:** Can model layers but does not exploit nonnegative weights as efficiently.
- **Explicit expanded graph construction:** Correct but unnecessary because transitions can be generated from `g`.
- **`k = 0`:** Only paid transitions exist, reducing to ordinary shortest path.
- **Use fewer than `k` hops:** Final minimum over all layers permits it.
- **Hop a heavy edge:** Often beneficial, but global path structure decides the optimum.
- **Zero-cost expanded transitions:** Safe for Dijkstra because they are nonnegative.
- **Connected graph:** Guarantees at least one finite destination state.
- **Repeated visits to one original node:** Different hop counts remain distinct states.
- **Stale heap entry:** May add work but cannot worsen a stored distance.
- **Input preservation:** Hopping is represented in state transitions; edge weights are never edited.
