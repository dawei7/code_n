## General

The cost limit can be viewed as a threshold. Suppose the final maximum component cost must be at most `T`. Then no retained edge may have weight greater than `T`, because that edge would make its component cost exceed `T`. Edges of weight at most `T` may be retained as needed.

Therefore, threshold `T` is achievable exactly when the graph formed by edges with weight at most `T` can connect the vertices into at most `k` components. The source finds the smallest such threshold by processing edges in increasing weight order with Union-Find.

**Why a forest is sufficient**

Inside one final component, extra cycle edges are never needed for connectivity. Removing a cycle edge does not disconnect the component and cannot increase its cost. Consequently, an optimal result can always be represented as a forest: each component is a tree, and the whole forest has at most `k` trees.

This lets Kruskal's merging process focus only on edges that join different components. Edges closing cycles are irrelevant to both the component count and the minimum possible bottleneck.

**Starting from isolated vertices**

Initially, the Union-Find parent array is `[0,1,...,n-1]` and `cnt = n`. This represents the forest with no edges, where every vertex is its own component. Such an isolated component has cost zero, matching the statement.

The special case `k == n` returns zero immediately. Keeping all vertices isolated already uses at most `n` components and retains no edge, so no negative result can improve on zero.

**Adding edges from lightest to heaviest**

The source sorts `edges` by weight. For each `[u,v,w]`, it finds the current representatives of the endpoints.

If the representatives are equal, `u` and `v` are already connected through edges no heavier than `w`. Adding this edge would create a cycle and would not reduce `cnt`, so the source skips it.

If they differ, the source links one representative to the other and decrements `cnt`. The newly merged forest still uses only processed edges, so its heaviest retained edge is at most `w`.

**Why the first time `cnt <= k` gives the answer**

Because every successful union lowers the integer component count by exactly one, when `k < n` the first crossing is actually `cnt == k`. Let its edge weight be `w`.

The processed edges prove achievability: the selected union edges form a forest with `k` components, and every selected edge has weight at most `w`. Removing all other original edges produces a legal result whose maximum component cost is at most `w`.

To prove no smaller answer exists, consider any threshold `T < w`. Before processing weight `w`, Kruskal has already considered every edge of weight at most `T` (and possibly some heavier values below `w`). The component count is still greater than `k`. Adding every available edge under that smaller threshold cannot connect more than Union-Find already did, because Union-Find merges whenever any edge connects two current components. Therefore, no forest using only edges of weight at most `T` can have at most `k` components.

So `w` is both feasible and minimal.

**Connection to a minimum spanning forest**

Ordinary Kruskal continues until one component remains and constructs a minimum spanning tree. This source stops earlier, when exactly `k` components remain. The selected edges form a minimum-bottleneck `k`-component spanning forest.

The objective is not the sum of selected weights. Nevertheless, increasing-order Kruskal is correct because the answer depends on the first weight threshold at which enough component merges become possible.

**Following the first example**

The weights are 2, 3, 4, and 6. Starting with five components:

- weight 2 joins nodes 1 and 3, leaving four components;
- weight 3 joins node 2 to that component, leaving three;
- weight 4 joins node 0, leaving two.

At `k = 2`, the source returns 4. The weight-6 edge is unnecessary and can be removed, isolating node 4. The nontrivial component's largest retained edge is 4, while the isolated component costs zero.

**Why “at most k” does not require merging farther**

Once there are `k` components, the constraint is satisfied. Continuing toward fewer components can only require edges of equal or greater weight, so it cannot lower the maximum cost. Stopping immediately is optimal.

**Exact implementation details**

`find` applies path compression. The union step simply assigns `p[pu] = pv`; it does not use rank or size. The manifest quotes the inverse-Ackermann Union-Find bound normally associated with path compression plus balanced linking. This exact implementation lacks that second heuristic, though sorting still dominates the overall safe bound.

The call `edges.sort(...)` mutates the input list's order. Edge records are unchanged, but callers do not retain their original sequence.

The final `return 0` is a fallback. Given the promise that the input graph is connected, when `k < n` enough unions must eventually occur to reach `k`, so the loop returns a weight first.

## Complexity detail

Let `m` be the number of edges. Sorting costs `O(m\log m)` time. The scan performs two finds per edge until it returns. With a fully balanced Union-Find, this is `O((n+m)\alpha(n))`; the exact source uses path compression without union by rank or size, so the stronger bound is not directly justified for its individual operations.

A safe overall bound remains `O(m\log m)` for this connected-graph setting, since `m >= n-1` and the sorting term dominates standard logarithmic Union-Find bounds. Initialization costs `O(n)`.

The parent array uses `O(n)` space. Python's in-place sort may use `O(m)` temporary references in the worst case, so a conservative auxiliary-space bound is `O(n+m)`, matching the manifest. No adjacency list is built.

## Alternatives and edge cases

- **Binary search a weight threshold:** Union all edges at most the midpoint and test whether components are at most `k`. It is correct but repeats graph scans; one sorted Kruskal sweep is simpler.
- **Minimum spanning tree then cut:** Build an MST and remove its `k-1` heaviest edges. This yields the same bottleneck value but performs work after the answer is already determined.
- **Union by size or rank:** Adding a balancing array supports the standard `\alpha(n)` amortized guarantee quoted by the manifest.
- **`k = n`:** Keep every vertex isolated and return zero without sorting.
- **`k = 1`:** Kruskal continues until the graph becomes connected; the returned value is the bottleneck edge of a minimum spanning tree.
- **Equal edge weights:** Their internal order does not matter; the first merge reaching `k` returns their shared weight.
- **Cycle edges:** They do not reduce component count and are safely ignored.
- **Isolated final component:** It contains no retained edge and contributes cost zero.
- **Connected-input guarantee:** It makes the fallback zero unreachable for `k < n`.
- **Parallel edges:** Even if present, only an edge that merges components matters; the constraints do not require special handling.
- **Large weights:** Only ordering and the returned threshold matter, so unused numeric gaps incur no work.
- **At most rather than exactly `k`:** Reaching exactly `k` is always sufficient, and further merging cannot improve the bottleneck.
- **Input mutation:** The exact source sorts `edges` in place; pass a copy if original order must be preserved.
