## General

**Represent a one-move reversal as another directed arc**

For every original edge

`u -> v` with cost `w`,

there are two ways it may be traversed:

- Normally from `u` to `v` for cost `w`.
- By using the switch at `v` to reverse that incoming edge for one move, traveling from `v` to `u` for cost `2w`.

The source writes both possibilities into an adjacency list:

`g[u].append((v, w))`

and

`g[v].append((u, 2 * w))`.

The second arc does not permanently reverse the original edge. It is only a representation of the legal action “activate the switch here and immediately traverse this incoming edge backward.” Future moves still see the same original possibilities.

After this transformation, every legal move has become an ordinary directed weighted arc. The path problem can therefore be solved with a standard shortest-path algorithm rather than choosing reversals separately.

**Why the per-node one-use switch does not require an extra state bit**

At first, adding every reverse arc seems to allow the switch at one node to be used repeatedly. A transformed walk could leave a node along a reverse arc, later return to that node, and leave along another reverse arc.

All original costs are positive, and every doubled reverse cost is positive as well. In a positive-weight graph, a minimum-cost path never needs to visit the same node twice. If a walk repeats node `u`, the portion from its first occurrence of `u` to the next occurrence is a positive-cost cycle. Removing that entire cycle joins the prefix and suffix at the same node, preserves a valid walk, and strictly lowers the cost.

Therefore some optimal transformed path is simple: it visits each node at most once. A simple path can depart from a node only once, so it can traverse at most one reverse arc associated with that node’s switch. The original “at most once per node” restriction is automatically respected by the shortest useful path.

This argument is why the source does not expand the state into combinations of used switches. Tracking one Boolean per node would create an impossible `2^n` state space and is unnecessary under positive weights.

**Why Dijkstra is the appropriate shortest-path algorithm**

The transformed graph has no negative edges. Normal arcs cost at least one, and reverse arcs cost at least two. Dijkstra’s algorithm is designed for exactly this setting.

The array `dist` stores the smallest cost discovered so far from node zero to every node. Initially every entry is infinity except `dist[0] = 0`. The priority queue begins with `(0, 0)` and always removes the pending node occurrence with the smallest tentative distance.

When `(d, u)` is removed, the source examines every transformed outgoing arc `u -> v` of weight `w`. Traveling through it would produce

`nd = d + w`.

If `nd < dist[v]`, this route is strictly better than every previously discovered route to `v`. The method updates `dist[v]` and pushes `(nd, v)` into the heap.

**Discard stale heap entries**

Python’s heap does not directly decrease an existing key. Whenever a shorter route to a node is found, the source pushes a new pair and leaves the older, larger pair in the heap.

Later, an obsolete pair may be removed. The condition

`if d > dist[u]: continue`

recognizes it: a smaller cost has already been recorded for `u`, so relaxing edges from the larger `d` cannot improve anything. Skipping stale entries keeps the algorithm correct and avoids unnecessary neighbor scans.

No explicit `visited` array is required. The distance comparison provides the same protection while allowing multiple tentative improvements before the best entry is finalized.

**Why the first valid destination removal is final**

After stale entries are skipped, if `u == n - 1`, the source returns `d` immediately. The heap guarantees that no pending entry has a smaller distance. Because all future routes extend pending distances by non-negative weights, none can later reach the destination more cheaply.

This early return avoids processing parts of the graph that cannot affect the requested source-to-destination answer. If the heap empties without removing the destination at its current best distance, no transformed path reaches it, so the method returns `-1`.

**Every legal route and transformed path correspond**

Take a route in the original problem. Replace every normal traversal by its normal arc and every switch-assisted reverse traversal by the added doubled-cost arc. The node sequence and total cost are unchanged, so every legal route appears in the transformed graph.

In the other direction, take a minimum transformed path. A normal arc is an original directed edge. A doubled reverse arc from `v` to `u` corresponds to activating `v`’s switch on original edge `u -> v` and immediately traversing it. The simple-path argument ensures no node’s switch is needed twice. Thus the transformed minimum corresponds to a legal original route of the same cost.

Since the transformation preserves the optimum in both directions and Dijkstra finds the transformed graph’s minimum distance, the returned result is the requested minimum cost.

**Trace the first example**

Original edge `0 -> 1` with weight three produces a normal arc of cost three and a reverse option `1 -> 0` of cost six.

Original edge `3 -> 1` with weight one produces normal arc `3 -> 1` of cost one and reverse option `1 -> 3` of cost two. Dijkstra can therefore follow `0 -> 1` for three and then the added `1 -> 3` arc for two, totaling five.

That second arc precisely represents using node one’s switch on its incoming edge from node three. The original edge remains conceptually directed `3 -> 1`; only that single traversal goes backward.

In the second example, the ordinary directed path `0 -> 2 -> 1 -> 3` costs three. Added reverse arcs do not force a reversal; they merely add choices. Dijkstra retains the cheaper all-normal path.

## Complexity detail

Let `V = n` and let `E` be the number of original edges. Graph construction creates exactly `2E` stored arcs and takes `O(V + E)` time including the adjacency-list allocation.

Each successful relaxation pushes one heap entry. There can be `O(E)` successful relaxations and stale removals in the lazy priority-queue implementation. A conservative bound for the exact Python source is `O((V + E) log E)` time because the heap may contain `O(E)` entries.

Under the usual simple-graph model, `E = O(V^2)`, so `log E = O(log V)` and this is conventionally written as `O((V + E) log V)`, matching the manifest. An indexed priority queue with true decrease-key also gives the standard `O((V + E) log V)` bound directly. If arbitrary parallel edges are allowed, `O((V + E) log E)` is the safer exact lazy-heap statement.

The adjacency lists require `O(V + E)` space. The distance array uses `O(V)`, and the heap can contain `O(E)` pending entries, so total auxiliary space is `O(V + E)`.

Doubling the number of arcs changes only a constant factor. The source does not allocate any state for subsets of switches.

## Alternatives and edge cases

- **State-expanded search over used switches:** Remembering which of `V` node switches were used would lead toward `2^V` combinations. Positive weights and simple optimal paths make that state unnecessary.
- **Bellman–Ford:** It handles negative edges but would cost `O(VE)`. All transformed weights are positive, so Dijkstra is substantially more efficient.
- **Breadth-first search:** BFS minimizes edge count, not weighted cost. Original weights vary and reverse arcs cost twice their originals, so a FIFO queue is not valid.
- **Permanently reverse edges:** The operation applies only to one immediate traversal. Mutating the graph would incorrectly affect later moves; adding a separate reverse option models the rule faithfully.
- **Add reverse cost `w` instead of `2w`:** This underprices switch use. Every reverse option must store exactly twice the original edge’s cost.
- **Use a switch at the edge’s source:** Reversing `u -> v` is initiated after arriving at `v`, so the added arc leaves `v` and conceptually uses node `v`’s switch.
- **No reversal needed:** Normal arcs remain present at their original costs, so Dijkstra can choose an entirely original directed path.
- **Destination unreachable:** If neither normal nor legal reverse arcs connect node zero to node `n - 1`, the heap empties and the source returns `-1`.
- **Parallel edges:** They may create several arcs between the same nodes with different weights. Relaxation naturally retains whichever yields the smaller total distance.
- **Self-loops:** A positive self-loop cannot improve a minimum path. It may be stored but never produces a smaller distance.
- **Cycles:** Every transformed cycle has positive cost. Removing it makes a route cheaper, which is also what justifies the per-node switch simplification.
- **Early destination return:** It is safe only after the stale-entry check. Returning from an obsolete larger destination entry before checking `dist` could be incorrect.
- **Integer costs:** The maximum route cost can exceed one edge’s bound, but Python integers do not overflow. Other languages should use a sufficiently wide integer type.
- **Missing imports:** The stored source refers to `List`, `inf`, `heappop`, and `heappush` without importing them. Standalone Python would need the corresponding `typing`, `math`, and `heapq` imports unless supplied by the harness.
