## General

**Turn lock order into an assignment problem.** After exactly `j` locks have been broken, the sword factor is `j+1`. If lock `i` has strength `a[i]` and is assigned to zero-based position `j`, its waiting time is

$$
\left\lceil\frac{a_i}{j+1}\right\rceil
=\texttt{(a[i]-1)//(j+1)+1}.
$$

Every lock must occupy one distinct break position, and every position is used once. Minimizing total time is therefore a minimum-cost perfect matching between locks and positions.

**Build a four-layer flow network.** The exact source creates:

- source node `s`;
- one left node per lock;
- one right node per break position;
- sink node `t`.

Source-to-lock edges have capacity one and cost zero. Every lock connects to every position with capacity one and its ceiling waiting cost. Every position connects to the sink with capacity one and cost zero.

Sending `n` units of flow selects exactly one position for each lock and exactly one lock for each position. Total flow cost is the schedule's total time.

**Use residual edges to revise earlier assignments.** `add_edge` adds a forward residual edge with the requested capacity/cost and a reverse edge with zero capacity and negative cost. Once flow uses an assignment, its reverse gains capacity. Later augmenting paths can cancel and rearrange previous choices if that lowers total cost.

This is why independently choosing the cheapest position for each lock would be wrong: positions are shared resources.

**Find minimum reduced-cost augmenting paths.** `slope` repeatedly calls `refine_dual`. It runs Dijkstra over residual edges with positive capacity using reduced costs based on node potentials `dual`. Potentials keep residual edge weights suitable for Dijkstra even though reverse edges have negative original costs.

`prev` stores the chosen incoming edge for each reached vertex. If the sink is unreachable, no further flow can be sent. In this complete bipartite network, a full matching always exists.

After a shortest path is found, the code determines its bottleneck capacity, updates forward and reverse capacities, derives per-unit path cost from the potential, and accumulates flow and total cost.

**Why each augmentation corresponds to an assignment improvement.** A simple source-lock-position-sink path assigns an unused lock to an unused position. Paths that use reverse edges may unassign an earlier pair and reassign a chain of locks/positions. Residual min-cost flow explores exactly the alternating-path changes used in matching algorithms.

**Return only the total cost.** `g.flow(s,t,n)` requests $n$ units and returns `(flow,cost)`. Index one selects the minimum total time. The actual lock order could be reconstructed from saturated assignment edges, but the problem asks only for the cost.

**Trace a matrix entry.** A strength-four lock assigned third, where factor is three, costs $\lceil4/3\rceil=2$. The edge from that lock to position index two carries cost two. Selecting one entry from every row and column creates a full schedule.

**The manifest identifies a different algorithm and wrong space bound.** It calls this the Hungarian algorithm and claims $O(n)$ space. The exact source is a generic successive-shortest-path min-cost-flow implementation. It creates $n^2$ lock-position edges plus their reverse residual edges, so space is necessarily $O(n^2)$.

The dense graph also makes a strict heap-based runtime include logarithmic factors beyond a bare $O(n^3)$ Hungarian bound.

**Why the flow optimum equals the schedule optimum.** Every schedule maps to one unit-capacity perfect matching with equal ceiling costs. Every full integral flow maps back to a unique lock at every position; integer capacities keep augmentations integral. Min-cost flow minimizes over exactly this set, so its returned cost is the minimum time.

## Complexity detail

The network has $O(n)$ vertices and $O(n^2)$ forward edges, doubled in residual storage. It sends $n$ units. Each shortest-path refinement can inspect $O(n^2)$ edges and uses a heap, giving a conservative exact-source bound around $O(n^3\log n)$, though dense-graph and potential analyses may summarize it as cubic.

Space is $O(n^2)$ for adjacency and residual edges, plus $O(n)$ potentials, distances, predecessors, and heap-vertex state. This contradicts the manifest's $O(n)$ space claim.

## Alternatives and edge cases

- **Hungarian algorithm:** It solves the same dense assignment in $O(n^3)$ time and $O(n^2)$ matrix storage; it is not the exact source.
- **Subset DP:** It costs $O(n2^n)$ and is unsuitable for $n=80$.
- **Sort strengths greedily:** Ceiling rounding and one-use positions require a proven assignment optimization, not an assumed order.
- **Single lock:** The sole factor is one, so time equals its strength.
- **Strength divisible by factor:** The ceiling edge cost is exact division.
- **Duplicate strengths:** Locks remain distinct left nodes but have identical cost rows.
- **All capacities one:** They enforce a perfect matching.
- **Reverse residual cost:** It is negative so prior assignments can be canceled consistently.
- **Full matching existence:** Complete lock-position edges guarantee $n$ flow units.
- **Potential updates:** They allow Dijkstra on residual networks with reverse edges.
- **No schedule reconstruction:** Only total cost is returned.
- **Dense memory:** $n^2$ assignment and reverse edges dominate.
- **Manifest mismatch:** The implementation is min-cost flow, not Hungarian, and not linear-space.
- **Required imports:** `NamedTuple`, `Optional`, `Tuple`, `List`, `cast`, `heappush`, and `heappop` must be available.
