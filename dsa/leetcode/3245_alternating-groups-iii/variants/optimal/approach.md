## General

A type-one query asks how many circular windows of a given size have different colors across every internal adjacency. Rechecking every possible start after every update would be too slow. The solution represents exactly where alternation fails and maintains the lengths of the alternating stretches between those failures.

Call circular edge `i` the adjacency between tile `i` and tile `(i + 1) % n`. It is a breakpoint, or bad edge, when its two endpoint colors are equal. An alternating group cannot cross a bad edge, because that would place two equal adjacent tiles inside the group. Between two consecutive bad edges, however, every internal adjacency is good, so the tiles form one maximal linear alternating arc.

If one such arc has $L$ tiles, the number of contiguous groups of size $k$ fully contained in it is

$$
\max(0,L-k+1).
$$

There are $L-k+1$ choices for the first tile when $L\ge k$, and none otherwise. Therefore a count query needs only the multiset of current arc lengths, not the individual colors of every candidate group.

**Represent bad edges in circular order.** The Fenwick tree `breakpoints` stores one at every bad edge index and zero elsewhere. Its prefix sums count breakpoints up to an index. The method `find_by_order(r)` performs Fenwick binary lifting to return the index of the $r$-th stored breakpoint. Together, these operations find an inserted or removed edge's predecessor and successor in circular order in $O(\log n)$ time.

The custom `find_by_order` uses a one-based order even though external edge indices are zero-based. It descends powers of two through the Fenwick structure, skipping blocks whose total is smaller than the remaining order. The returned `index` is the corresponding zero-based edge position.

The helper

`arc_length(first, second) = (second - first) % tile_count or tile_count`

computes the number of tiles in the alternating arc after bad edge `first` and through the tile at bad edge `second`. For distinct circular breakpoints, the modular difference is from one through $n-1$. When there is exactly one breakpoint, its successor is itself; the modular difference is zero, and `or tile_count` correctly gives the one maximal arc length $n$.

For example, if bad edges are two and six on an eight-tile circle, one arc starts at tile three and ends at tile six, with length four. The other starts at tile seven, wraps through zero, and ends at tile two, also with length four. The bad edge itself is the adjacency after the arc's final tile, so it is not crossed by a group contained in that arc.

**Store the arc-length distribution.** Two more Fenwick trees are indexed by length. `length_counts[L]` conceptually stores how many arcs have length $L$, while `length_sums[L]` stores their total length, namely $L$ times the count. The helper `change_length(L, delta)` applies the same insertion or deletion to both trees.

When at least one bad edge exists, there is exactly one arc per bad edge, and all arc lengths sum to $n$. Initialization scans all circular edges, inserts the bad indices into `breakpoints`, and inserts every length between consecutive bad edges into the two length trees.

**Answer a group-size query by aggregation.** For requested `size = k`, arcs shorter than $k$ contribute nothing. The code obtains their number and total length with prefix sums through `k - 1`:

`shorter_count = length_counts.prefix_sum(k - 1)`

`shorter_sum = length_sums.prefix_sum(k - 1)`.

It subtracts these from the total number of arcs and total arc length:

`eligible_count = bad_count - shorter_count`

`eligible_sum = tile_count - shorter_sum`.

Each eligible arc contributes $L-(k-1)$. Summing over all eligible arcs gives

$$
\sum L-(k-1)\cdot\text{eligible count},
$$

which is implemented as

`eligible_sum - (size - 1) * eligible_count`.

This answers the query with a constant number of $O(\log n)$ Fenwick prefix operations, regardless of how many arcs exist.

There is one special state: `bad_count == 0`. Then every circular edge alternates, so there is no breakpoint at which to cut the circle into a linear arc. Every one of the $n$ tile positions can begin an alternating group of any legal queried size, which is at most $n-1$. The method returns `tile_count` directly. Treating this as one length-$n$ linear arc would give only $n-k+1$ starts and would incorrectly omit windows that wrap around the arbitrary cut.

**Insert a new breakpoint by splitting one arc.** If no breakpoint currently exists, the new edge becomes the only bad edge. The code inserts it and records one length-$n$ arc. Unlike the zero-breakpoint state, that one bad adjacency supplies a real cut; only windows that avoid it are valid.

Otherwise, `rank_before` counts bad edges with index strictly less than the new edge. Its predecessor is the bad edge with that rank, wrapping to the last edge when the rank is zero. Its successor is the next rank, wrapping to the first edge after the last. Before insertion, predecessor and successor delimit one arc. The helper removes that old length and adds two new lengths, predecessor-to-new-edge and new-edge-to-successor. It then records the breakpoint and increments `bad_count`. The two new lengths add to the removed length, so the invariant that total arc length is $n$ remains true.

**Remove a breakpoint by merging two arcs.** If it is the sole breakpoint, its one length-$n$ linear arc is removed and the system returns to the special fully alternating state. Otherwise, its one-based rank identifies the circular predecessor and successor. The arcs predecessor-to-edge and edge-to-successor are deleted from the length distribution, and their merged predecessor-to-successor length is inserted. The edge's breakpoint marker is removed and `bad_count` decreases.

**Only two edges can change after recoloring one tile.** Updating `colors[index]` affects the adjacency entering that tile, edge `(index - 1) % n`, and the adjacency leaving it, edge `index`. Every other edge compares two unchanged tiles.

Before assigning the new color, the method records whether each affected edge was bad. After assignment, it recomputes each status. A transition from bad to good calls `remove_breakpoint`; a transition from good to bad calls `insert_breakpoint`. Unchanged statuses require no structural work. The two affected edges are processed sequentially, and each helper sees the structure produced by the previous transition, so even an update changing both statuses preserves all invariants.

If the tile already has `new_color`, the source immediately continues. This is correct because no edge status changes, and update queries do not contribute entries to the returned answer. The method does mutate the supplied `colors` list for genuine updates, matching the stateful query contract.

**Why this counts every alternating group exactly once.** With at least one breakpoint, every valid window belongs to exactly one maximal arc because it cannot cross a bad edge. Within its unique arc, its start is one of the $L-k+1$ counted positions. Invalid windows either cross a breakpoint or do not fit in an arc and contribute zero. In the no-breakpoint state, every circular start is valid and counted directly. The breakpoint updates maintain exactly the current equal-color edges, so this reasoning remains true after every recoloring.

## Complexity detail

Let $n$ be the number of tiles and $q$ the number of queries. Scanning colors to find initial bad edges takes $O(n)$. The exact source inserts each initial breakpoint and each initial arc length through Fenwick `add` operations, so initialization takes $O(n\log n)$ in the worst case rather than using a linear Fenwick build.

A type-one query performs a constant number of prefix sums and takes $O(\log n)$ time, except the no-breakpoint shortcut, which is $O(1)$. A type-two query examines two edges and performs at most two breakpoint insertions or removals. Each uses a constant number of prefix sums, order-statistic searches, and tree updates, so it takes $O(\log n)$ time.

Total time is $O((n+q)\log n)$. The colors array itself is supplied and mutated in place. The three Fenwick arrays, each linear in $n$, plus the initial `bad_edges` list use $O(n)$ auxiliary space. The returned answer contains at most $q$ integers.

Fenwick operations are logarithmic because each update or prefix query moves through indices by the lowest set bit. `find_by_order` also examines $O(\log n)$ powers of two.

## Alternatives and edge cases

- **Recount every circular window:** Testing $n$ starts and up to $k$ adjacencies for every type-one query can cost $O(nk)$ per query. Even using a run-length scan still costs $O(n)$ after each update, too much for $5\cdot10^4$ operations.
- **Ordered set plus length multiset:** A balanced search tree can maintain bad-edge predecessors and successors, while another augmented tree stores arc lengths and sums. This matches the conceptual solution, but Python lacks these structures in its standard library. Fenwick trees exploit the bounded integer indices and lengths.
- **Segment tree:** It can provide breakpoint order statistics and length-frequency aggregates with the same $O(\log n)$ operations. It is more code and memory but supports the same invariants.
- **Duplicate every color into a length-$2n$ array:** Duplication simplifies static circular-window scanning, but point updates affect two copies and fast group-size queries still need an augmented run-length structure.
- **No bad edges:** The circle alternates everywhere, and all $n$ starts are valid for every allowed size. This must be handled separately from one linear arc of length $n$.
- **Exactly one bad edge:** There is one genuine cut and one arc of length $n$. A size-$k$ query contributes $n-k+1$, not $n$, because wrapping across the bad edge is forbidden.
- **Arc exactly as long as the query:** It contributes one group. Prefixing only through `size - 1` correctly keeps this arc eligible.
- **Arc shorter than the query:** It is removed through `shorter_count` and `shorter_sum` and contributes zero, preventing a negative term.
- **Wraparound arc:** Modular `arc_length` measures it correctly, and predecessor/successor rank logic wraps between the first and last breakpoint.
- **Update at tile zero:** The affected incoming edge is `n - 1` through modulo arithmetic, so the circular boundary is updated together with edge zero.
- **No-op color update:** The immediate `continue` preserves all trees and correctly emits no answer for a type-two query.
- **Both incident edges change:** One may be inserted while the other is removed, or both may move in the same direction. Recording both old statuses before mutation and then applying transitions preserves the correct before/after comparison.
- **Fenwick length index zero:** Real arcs have lengths from one through $n$, so index zero is unused. Allocating `tile_count + 1` external positions permits an update at length $n$ after the Fenwick class performs its internal one-based shift.
- **Binary colors and odd circles:** A perfectly alternating closed circle is possible only for even $n$, but the zero-breakpoint branch remains logically correct and does not need a parity test.
- **Output order:** Only type-one results are appended, exactly when encountered. Updates change future state but do not insert placeholder values into `answer`.
- **Input mutation:** Genuine type-two queries assign into `colors`. Callers should not expect the original color array to remain unchanged after this stateful simulation.
- **Order-statistic precondition:** `find_by_order` is called only with an order between one and `bad_count`. The wraparound formulas enforce that range; calling it with zero would not represent a valid breakpoint rank.
