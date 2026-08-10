## General

**Replace “exclude the maximum” with one free traversal**

For a fixed path with edge weights $w_1,w_2,\ldots,w_t$, its required cost is

$$
\sum_{j=1}^{t}w_j-\max_j w_j.
$$

Imagine being allowed to traverse exactly one path edge for free. For that fixed path, making edge $j$ free produces $\sum w_i-w_j$. This is smallest when $w_j$ is maximum.

Therefore minimizing over “a path whose maximum edge is excluded” is equivalent to minimizing over “a path plus one chosen free edge.” The algorithm may provisionally make any edge free because an optimal global result will never benefit from making a smaller edge free instead of a larger edge on the same path.

If a path has several equal maximum edges, excluding any one yields the same numeric cost. The statement's “first maximum” rule identifies which occurrence is removed but does not alter the returned sum.

**Create two states for every graph node**

The source runs Dijkstra's algorithm on an implicit layered graph. State `(u,0)` means node `u` has been reached without using the free traversal. State `(u,1)` means it has already been used.

`dist[u][used]` stores the smallest known cost for that exact state. Initially,

`dist[0][0] = 0`

and every other distance is infinity. The priority queue stores triples `(cost,node,used)` and always removes the currently smallest cost.

Keeping the flag in the state is essential. Two routes reaching the same physical node with equal paid cost are not interchangeable if one still owns the free traversal and the other does not.

**Relax the paid transition**

For every original undirected edge $(u,v)$ of weight $w$, either layer may traverse it normally:

$$
(u,\textit{used})\rightarrow(v,\textit{used})
$$

with additional cost $w$.

The source computes `nxt = cur + w` and updates `dist[v][used]` if this is smaller. Adding each input edge in both adjacency-list directions correctly represents the undirected graph.

**Relax the free transition exactly once**

Only a state with `used == 0` may traverse the current edge for no additional cost:

$$
(u,0)\rightarrow(v,1).
$$

The source sets `nxt = cur` and tries to improve `dist[v][1]`. Once this transition changes the flag to one, no later edge can be made free.

Thus every layered route ending in layer one corresponds to an original walk together with exactly one excluded edge. Conversely, choosing an excluded edge on any original path determines one layered route: stay in layer zero before it, cross to layer one on it, and remain there afterward.

**Why ordinary Dijkstra remains valid**

Paid transitions have positive weights, and free transitions have weight zero. Dijkstra requires nonnegative—not strictly positive—transition costs, so the layered graph satisfies its condition.

When a queue entry has `cur > dist[u][used]`, a better entry for the same state was discovered later. The source discards this stale entry instead of processing its outgoing transitions again.

When state `(n-1,1)` is removed from the min-heap, its distance is final. Returning immediately is safe because every unsettled state has at least that much cost. Requiring `used` to be one also ensures an edge was actually excluded. Since $n\ge2$ and the graph is connected, every source-to-target path contains an edge, so a valid layer-one target exists.

**Connect the layered optimum back to a maximum edge**

Take the layered route returned by Dijkstra. It makes some path edge of weight $f$ free and pays total $S-f$, where $S$ is the path's full weight. Let $M$ be the maximum weight on that path. Since $M\ge f$,

$$
S-M\le S-f.
$$

So applying the problem's rule to the same path is no more expensive than the layered result.

In the other direction, any valid problem path can use one of its maximum edges as the layered free transition, producing exactly its defined cost. Hence the best layered result cannot be larger than the best problem result.

The two inequalities force equality. This establishes why allowing an arbitrary free transition does not accidentally solve an easier problem.

**Trace the single-edge shortcut**

In the second example, the direct edge from node zero to node two has weight 50,000. The layer-zero state at node zero crosses that edge for free into `(2,1)` with cost zero. The target layer-one state is then the smallest queue entry and returns zero.

The two-edge route of weights one and one can exclude only one of them and costs one. Dijkstra considers it too, but the zero-cost direct route wins.

**Walks do not create a hidden advantage**

The layered algorithm technically searches walks, not explicitly enumerated simple paths. All transition costs are nonnegative. Removing a cycle cannot increase paid cost, and it does not prevent choosing one free edge on the remaining source-to-target portion; if the removed cycle held the free traversal, a maximum edge on the remaining nonempty route can instead be free.

Therefore an optimum is representable by a simple path, consistent with the path interpretation in the problem.

## Complexity detail

Let $N$ be the node count and $E$ the number of undirected edges. The implicit graph has $2N$ states. Every original direction supplies one paid transition in each layer and one possible layer-changing transition, so its transition count is $O(E)$.

Binary-heap Dijkstra takes $O((N+E)\log N)$ time; using $\log(2N)$ gives the same asymptotic bound. Building and storing the adjacency list costs $O(N+E)$ space, while the two distance columns and queue use $O(N+E)$ additional worst-case space.

The exact source returns as soon as the final layer-one target state is settled, which may save work but does not change the worst-case bound.

## Alternatives and edge cases

- **Try every excluded edge with a separate shortest-path run:** This repeats substantial work and can cost $O(E(N+E)\log N)$.
- **Combine distances around every edge:** Two ordinary shortest-distance arrays can support another derivation, but the layered state directly represents whether the exclusion has been consumed.
- **Make the globally heaviest graph edge free:** The excluded edge must lie on the chosen path; a heavier irrelevant edge cannot help.
- **Use the free traversal twice:** Layer one deliberately has no second zero-cost transition.
- **Return the target in layer zero:** That route has excluded no edge and may overstate the required cost.
- **Parallel maximum weights on one path:** Only one occurrence is free. Equal maxima make the “first” rule cost-neutral.
- **Single-edge source-to-target path:** Its only edge is excluded, so the answer is zero.
- **Zero-weight layered transition:** Dijkstra remains correct because no transition is negative.
- **Undirected representation:** Every listed edge is inserted in both directions even though the input stores `u<v`.
- **Cycles:** Nonnegative costs ensure cycles cannot improve the optimum beyond a simple path.
- **Stale heap entries:** Skipping them prevents redundant relaxation without losing a best route.
- **Large path sums:** Python integers avoid fixed-width overflow.
- **Connected graph:** It guarantees the layer-one target is reachable.
- **First maximum wording:** It affects edge identity only; all tied maximum exclusions subtract the same weight.
