## General

**A city alone is not enough to describe progress**

Reaching the same city after using different numbers of discounts creates different future possibilities. A route that costs slightly more but preserves discounts may become better later.

The algorithm therefore treats `(city, k)` as a state, where `k` is the number of discounts already used. There are `n * (discounts + 1)` valid states.

Each undirected highway `[a, b, c]` is stored in both adjacency lists. From state `(i, k)` across a highway of toll `v`, there are two transitions:

- pay the full toll and reach `(j, k)` with added cost `v`;
- use a discount and reach `(j, k + 1)` with added cost `v // 2`.

Integer floor division is exactly the required discounted toll calculation for nonnegative tolls.

**Run Dijkstra on the expanded state graph**

The heap `q` starts with `(0, 0, 0)`: zero cost, city 0, zero discounts used. Heap tuples are ordered first by cost, so `heappop` always selects the currently smallest path cost.

`dist[i][k]` records the best cost at which state `(i, k)` has already been expanded. It begins at infinity.

When a valid state is popped, the source expands it only if `cost` is strictly smaller than the stored value. It then records the cost and pushes both transition choices for every neighboring highway.

The implementation does not perform decrease-key operations. It may push multiple entries for the same state; later, expensive duplicates fail `dist[i][k] > cost` and are ignored. This lazy pattern is standard for heap-based Dijkstra.

**Handle the discount limit through an extra rejected layer**

The source always pushes the discounted transition with `k + 1`, even when `k == discounts`. Such an entry has too many discounts. It is safe because the first pop-time check is `if k > discounts: continue`, before indexing `dist`.

This creates some useless heap entries but never treats an invalid path as an answer. A more selective implementation could push the discounted transition only when `k < discounts`.

**Why returning at the destination is safe**

The code checks `i == n - 1` immediately after rejecting invalid discount counts. The first valid destination entry removed from the min-heap has the smallest cost among every queued route.

All transition costs are nonnegative, including discounted zero tolls. Dijkstra's ordering guarantees no not-yet-generated valid path can later reach the destination more cheaply than this first popped destination cost. Therefore, the early return is correct even before storing that destination state in `dist`.

If the heap empties without a valid destination state, no route exists and the method returns `-1`.

**Why the layered shortest path is correct**

Every legal real route corresponds to a path in the expanded graph: use the full-cost transition on undiscounted highways and the next-layer transition where a discount is spent. The layer never exceeds the allowed count.

Conversely, every valid expanded-graph path specifies a real route and exactly which highways receive discounts. Its accumulated edge weights equal the real paid toll.

Thus the requested answer is the minimum distance from state `(0,0)` to any `(n-1,k)` with valid `k`. Dijkstra finds minimum distances in this nonnegative graph, and the first valid destination popped is the minimum over all layers.

## Complexity detail

Let $E$ be the number of highways and $K$ the discount limit.

There are $n(K+1)$ valid states. Each settled layer-state examines its city's incident highways, for $O(E(K+1))$ valid relaxations in aggregate. Heap operations cost $O(\log(n(K+1)))$, giving

$$
O(E(K+1)\log(n(K+1)))
$$

time, plus graph construction. The unconditional invalid discounted pushes add only a comparable constant-factor number of heap operations.

The graph uses $O(n+E)$ space, the distance table uses $O(n(K+1))$, and the heap can hold many state-edge candidates. A conservative bound is $O((n+E)(K+1))$, matching the manifest.

## Alternatives and edge cases

- **Ordinary Dijkstra by city only:** This discards how many discounts remain and can prune a route that is more valuable later. The discount count must be part of the state.
- **Bellman-Ford:** All costs are nonnegative, so repeated global relaxation is unnecessary. Dijkstra is the natural shortest-path method.
- **Dynamic programming by discount layers:** Repeated shortest-path passes can work but are less direct than one expanded-state Dijkstra.
- **Push discounted edges conditionally:** Checking `k < discounts` before pushing avoids invalid layer `K + 1` entries while preserving the algorithm.
- **No discounts:** Only layer zero is valid. Discounted pushes enter layer one and are skipped; full-cost Dijkstra still works.
- **More discounts than route edges:** Discounts are optional, so the answer may use fewer than the allowance.
- **Odd toll:** `v // 2` correctly drops the fractional half.
- **Zero toll:** Nonnegative zero edges remain compatible with Dijkstra; strict distance improvement prevents endless expansion of equal-cost states.
- **Disconnected destination:** The heap eventually empties and `-1` is returned.
- **Multiple routes to one state:** The heap may contain duplicates, but only a strictly improving pop expands neighbors.
- **Undirected highways:** Both adjacency directions are required because travel is allowed either way.
- **Early destination return:** It occurs only after rejecting `k > discounts`, so an illegally over-discounted path can never be returned.
