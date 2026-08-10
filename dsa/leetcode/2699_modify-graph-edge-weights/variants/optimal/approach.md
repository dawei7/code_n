## General

**Treat unknown edges as progressively enabled**

Known positive edge weights cannot change. An edge marked `-1` must eventually receive a positive value.

The exact solution begins by ignoring every unknown edge and measuring the shortest path using only fixed edges. It then considers unknown edges in input order, enabling each at the minimum legal weight one until the shortest distance crosses down to the target.

The first crossing edge is increased just enough to make the distance exactly equal to `target`.

**How the helper computes distance**

`dijkstra` builds an $n$ by $n$ adjacency matrix initialized to sentinel `inf = 2 * 10**9`. Unknown edges are skipped, while each active edge is written symmetrically because the graph is undirected.

It stores tentative distances from `source`, repeatedly selects the unvisited vertex with smallest distance by a full scan, and relaxes every possible neighbor by scanning its matrix row.

This is the array-and-matrix form of Dijkstra for nonnegative active weights.

**Why the finite infinity sentinel is sufficient**

The target is at most $10^9$, while `inf` is $2\cdot10^9$.

The algorithm only needs to distinguish a path no greater than target from one safely above target or unavailable. It never needs an exact shortest value above the sentinel for its decisions.

The same sentinel is also a legal final unknown-edge weight because the allowed maximum is inclusive.

**First impossibility case: fixed path already too short**

Let `d` be the shortest path when all unknown edges are unavailable.

If `d < target`, that all-fixed path will remain in the graph under every assignment. Unknown-edge weights cannot increase a path that does not use them.

Therefore the final shortest distance can never rise to target, and the method returns an empty list immediately.

**When the fixed path already equals target**

If `d == target`, the known edges already provide the desired shortest path.

Every unknown edge is set to `inf`. Any path using one then costs more than target, while the existing fixed path remains unchanged at target.

The flag `ok` records that no crossing edge needs to be found.

**Enable unknown edges with weight one**

If the fixed-only distance is above target, each encountered unknown edge is first assigned weight one, the smallest legal value.

Earlier unknown edges remain at one. Later unknown edges are still `-1` and remain ignored by the helper.

As more minimum-weight edges are enabled, the shortest distance can only stay the same or decrease. This monotonic sequence eventually either stays above target or crosses to at most target.

**Why the first crossing edge can absorb the exact slack**

Suppose adding the current edge at weight one changes the shortest distance to `d <= target`. Immediately before enabling it, every path that avoided this edge had length greater than target.

Thus every path now at or below target must use the current edge. Increase its weight by:

$$
\Delta=\texttt{target}-d.
$$

The currently shortest path rises from $d$ to target. Any other path using the edge rises by the same $\Delta$ and cannot become less than target because it was at least $d$. Paths avoiding the edge remain above target.

Therefore the new shortest distance is exactly target.

**Finish unused unknown edges safely**

After `ok` becomes true, every later unknown edge is assigned `inf`.

This fulfills the requirement to replace all `-1` weights while preventing those not involved in the construction from introducing a shorter route.

Earlier enabled edges stay at one, and the crossing edge retains its adjusted value.

**When no solution exists after all edges**

If every unknown edge has been enabled at minimum weight one and the shortest distance is still greater than target, no legal assignment can do better.

Every unknown weight must be at least one, so any other assignment can only keep or increase path lengths. The method returns `[]`.

**Input mutation**

The method edits the third entry of each unknown edge directly in `edges`.

On success, that same list contains the returned assignment. On a late failure, some weights may already have changed even though an empty list is returned; callers should not assume failure preserves the original input.

**Manifest mismatch**

The manifest describes a two-pass heap-based strategy with $O((n+m)\log n)$ time. The exact source instead reruns an adjacency-matrix $O(n^2)$ Dijkstra after potentially every unknown edge.

This document follows the checked-in implementation and reports its actual repeated-run cost.


The initial comparison proves the fixed-too-short case impossible and the fixed-equal case safe with large unknown weights.

Otherwise progressive weight-one activation enumerates a monotone path-distance sequence. If it never reaches target, even the globally smallest legal unknown weights are insufficient. At the first crossing, all newly competitive paths use the crossing edge, so adding exactly the slack makes their minimum target while older paths remain above it. Large later weights preserve that equality.

These cases cover every possible result, so a returned assignment is valid and an empty result is justified.

## Complexity detail

Let $u$ be the number of unknown edges and $m$ the total edge count. One helper run builds an $O(n^2)$ matrix, loads $m$ edges, and performs $O(n^2)$ selection and relaxation work, for $O(n^2+m)$ time.

There is one initial run and up to $u$ later runs, so worst-case time is $O((u+1)(n^2+m))$, commonly simplified to $O(un^2)$ for this dense bound. The adjacency matrix and distance/visited arrays use $O(n^2)$ space. This differs materially from the manifest's heap bound.

## Alternatives and edge cases

- **Heap-based adjacency-list reruns:** Reduces each Dijkstra run but can still repeat it for many unknown edges.
- **Two carefully designed Dijkstra passes:** Can assign weights during relaxation and achieve the manifest's near-linearithmic target, but it is not the exact source.
- **Fixed-only distance below target:** Impossible because that immutable path cannot be lengthened.
- **Fixed-only distance equal target:** Set every unknown edge to `2 * 10**9`.
- **All weight-one distance above target:** Impossible because no unknown edge may be smaller than one.
- **First crossing equals target:** Slack is zero, so the crossing edge remains one.
- **Disconnected active subgraph:** The sentinel represents an unavailable route until unknown edges connect it.
- **Multiple shortest paths using the crossing edge:** All rise by the same slack and remain at least target.
- **Later unknown edges:** Must receive legal values and are neutralized with the maximum weight.
- **Known edges:** Never modified.
- **Failure mutation:** A failed late attempt may leave the supplied edge list partially rewritten.
