## General

**A maximum-product version of Dijkstra**

The success probability of a path is the product of its edge probabilities. The stored solution adapts Dijkstra's algorithm: instead of minimizing an additive distance, it maximizes a multiplicative probability.

`dist[v]` stores the best probability discovered so far for reaching node `v` from `start_node`. The starting probability is one because an empty path succeeds with certainty. Every other node begins at zero, meaning no route has been discovered.

For an edge from `a` to `b` with probability `p`, a path reaching `a` with probability `w` reaches `b` with probability `w * p`. If that product exceeds `dist[b]`, the code records the improvement and schedules `b` for processing.

**Building an undirected adjacency list**

The source creates one empty neighbor list per node. For each paired edge and probability, it appends `(b, p)` to `g[a]` and `(a, p)` to `g[b]`. Both directions are required because the graph is undirected.

`zip(edges, succProb)` relies on the guaranteed equal lengths and associates each edge with its matching probability.

**Using a min-heap as a max-heap**

Python's heap returns the smallest key. The queue stores negative probabilities, beginning with `(-1, start_node)`. The most negative value corresponds to the largest positive probability, so it is popped first.

After `w, a = heappop(pq)`, the source executes `w = -w` to recover the positive probability.

An improved node can have older, worse heap entries still waiting. The test `if dist[a] > w: continue` recognizes such a stale entry. A strictly better probability is already known, so expanding the worse route cannot improve any neighbor beyond what expanding the better route can provide.

Equality is not stale. Processing an equal entry is harmless, although under normal strict-improvement pushes duplicate equal entries are limited.

**Relaxing neighbors**

For every `b, p` adjacent to `a`, the assignment expression `t := w * p` computes the probability of extending the current route by that edge.

If `t > dist[b]`, this route is strictly better. The code updates the array and pushes `(-t, b)`. Probabilities equal to the current best need no push because they cannot produce a better product downstream.

The loop processes the heap until empty and returns `dist[end_node]`. If the destination is unreachable, it remains zero, exactly the required result.

**Why the highest-probability ordering is safe**

All edge probabilities lie between zero and one. Extending a path can never increase its probability. Therefore, when the maximum currently known probability is expanded, no route beginning with a lower probability can later surpass it merely by multiplying by values at most one.

More formally, suppose node `a` is popped with its current best `w`. Any alternative unsettled route must have a prefix probability no greater than the largest heap key, which is at most `w`. Multiplying remaining probabilities cannot raise it. This is the maximum-product analogue of Dijkstra's nonnegative-edge argument.

The source does not mark nodes permanently visited, but stale-entry skipping ensures only currently best labels perform useful relaxations.

**Cycles do not help**

A cycle multiplies probability by a value at most one, so inserting it cannot improve a path. An optimal probability can be represented by a simple path, and strict relaxation prevents endless updates from probability-one cycles.

The algorithm stores probabilities rather than predecessor pointers because only the best numeric result is requested. If the actual route were also required, an additional parent array would record which relaxation last improved each node. Omitting it saves state and does not affect the maximum-probability calculation.

## Complexity detail

Let $N$ be the number of nodes and $E$ the number of undirected edges. Building adjacency lists costs $O(N+E)$ time and space.

Each successful relaxation pushes a heap entry. In the standard analysis there are $O(E)$ such pushes and pops, each costing $O(\log E)$. Since a simple graph has $E=O(N^2)$, $\log E=O(\log N)$, yielding $O((N+E)\log N)$ time as stated by the manifest.

The adjacency list uses $O(N+E)$ storage, `dist` uses $O(N)$, and the heap can hold $O(E)$ entries because stale versions remain until popped. Total space is $O(N+E)$.

Floating-point multiplication introduces ordinary rounding, but the accepted tolerance accommodates it. The algorithm compares computed approximations consistently.

## Alternatives and edge cases

- **Negative logarithms:** Transform probability p to cost `-log(p)` and run ordinary shortest-path Dijkstra. Zero-probability edges need special handling.
- **Bellman-Ford relaxation:** Repeatedly scan all edges for $O(NE)$ time. It is simpler conceptually but slower.
- **Queue-based relaxation:** It may work well on some graphs but has $O(NE)$ worst-case time.
- **Unreachable destination:** Its stored probability stays zero.
- **Direct edge versus longer path:** The heap compares products, not hop counts, so a longer route can win.
- **Probability one cycle:** It cannot create a strictly larger label, so strict comparisons prevent infinite pushes.
- **Probability zero edge:** It produces zero and cannot improve an undiscovered zero label.
- **Stale heap entry:** The source skips it when a better array value exists.
- **Undirected edge:** Both adjacency directions must be inserted.
- **Required imports:** `heappop` and `heappush` must be available from `heapq`.
