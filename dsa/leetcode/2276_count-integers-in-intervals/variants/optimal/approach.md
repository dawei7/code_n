## General

**Store coverage counts over an enormous coordinate domain**

Intervals may use coordinates up to one billion, so an array with one entry per integer is not practical. The solution uses an implicit segment tree: each node represents a contiguous coordinate segment, but child nodes are created only when an operation needs to descend into that segment.

For every node, `v` is the number of covered integers in its inclusive range `[l, r]`. If the whole node range is covered, then

`v = r - l + 1`.

This aggregate lets a query return a segment's coverage count without visiting every coordinate.

**Understand the node fields**

A `Node` stores:

- `l` and `r`, its inclusive coordinate boundaries;
- `mid = (l + r) // 2`, which divides the range;
- `left` and `right` child references, initially absent;
- `v`, the covered-integer count, initially zero;
- `add`, a lazy full-cover marker, initially zero.

`__slots__` fixes these attribute names and avoids a separate instance dictionary for every node, reducing the substantial per-node memory overhead of an implicit tree.

Only additions of coverage occur; no operation clears an interval. Therefore, `add = 1` means the entire segment has been covered and that fact may still need to be pushed to children. Zero means there is no pending full-cover propagation.

**Use an almost-domain-sized root**

The root represents `[1, 10^9 + 1]`, one coordinate beyond the legal input domain. Updates never include that extra coordinate, and `count()` queries only `[1, 10^9]`, so it never contributes to the returned count.

The extra endpoint is an implementation choice rather than a problem value. Because the query does not fully contain the root, counting descends along the boundary needed to exclude `10^9 + 1` instead of simply returning `root.v`.

**Cover a range with** `modify`

`modify(l, r, 1, node)` updates the intersection of interval `[l, r]` with the current node.

If the requested endpoints are reversed, `l > r`, the method returns. Normal public calls satisfy `left \le right`, so this guard mainly makes the helper robust.

If the node's entire segment lies inside the update,

`node.l >= l and node.r <= r`,

the method marks it completely covered. It sets `node.v` to the segment's inclusive length and `node.add` to one, then stops descending. This is the lazy step: potentially millions of coordinates are represented by one node assignment.

If coverage is only partial, the method pushes state downward, recurses left when `l <= node.mid`, and recurses right when `r > node.mid`. These tests select exactly the children whose coordinate ranges can intersect the update. Finally, `pushup` restores the parent's count as the sum of its two children.

**Why repeated and overlapping additions do not double-count**

Coverage is a Boolean property: an integer is either present in at least one interval or it is not. A full-cover assignment sets `v` to the segment length rather than adding the segment length. Adding the same interval twice therefore leaves its nodes at the same covered counts.

For partial overlap, already covered children retain their full counts and newly reached children acquire coverage. `pushup` adds counts of disjoint left and right coordinate ranges, not counts from overlapping update calls. This maintains the size of the union.

**Create and propagate children in** `pushdown`

When a partial operation needs children, `pushdown` creates both if they do not yet exist:

- the left child represents `[node.l, node.mid]`;
- the right child represents `[node.mid + 1, node.r]`.

These inclusive ranges are disjoint and together equal the parent range.

If `node.add` is nonzero, the parent had previously been marked fully covered without descending. Both new or existing children must inherit that fact. Their lazy markers become one and their covered counts become their complete lengths. The parent's marker is then cleared because its information is now represented below.

Without this propagation, a later partial update or query could create zero-valued children under a fully covered parent and incorrectly lose old coverage.

**Restore the parent invariant in** `pushup`

After a partial modification, both children describe disjoint halves of the parent. The assignment

`node.v = node.left.v + node.right.v`

therefore makes `node.v` equal the number of covered integers in the entire parent range. This invariant holds from leaves to root after every update.

Even if the requested interval overlaps previously covered regions, child `v` values already represent union sizes, so their sum remains exact.

**Answer a range query**

`query(l, r, node)` follows the same segment decomposition. If the current node lies entirely inside the requested query range, it returns `node.v` immediately. Otherwise, it pushes down, visits each intersecting child, and adds their results.

The public `count()` queries `[1, 10^9]`, exactly the legal integer domain. Although all updates lie there and the root's extra coordinate is never covered, the query code still descends because the root itself extends one coordinate farther.

An important exact-source behavior is that `query` calls `pushdown`. A read can therefore allocate missing child nodes along the right boundary path and can materialize a lazy full-cover marker in children. It does not change which coordinates are covered, but it can change the internal representation and memory use.

**Trace merging intervals through counts**

After adding `[2, 3]`, the tree's root aggregate represents two covered integers. Adding `[7, 10]` covers four disjoint integers, bringing the union count to six.

Adding `[5, 8]` covers four coordinates, but seven and eight were already covered. Full or partial tree nodes for those overlaps are assigned covered status rather than incremented. Only five and six expand the union, so the count becomes eight.

The tree does not explicitly merge intervals into a list. Its node counts perform the same union accounting hierarchically.

**Why the data structure remains correct**

Initially every existing node has `v = 0`, matching the empty interval set. For a full-cover update, assigning the segment length makes the invariant exact. For a partial update, lazy propagation preserves old coverage, recursive calls correctly update intersecting halves, and `pushup` combines their disjoint union counts.

By induction over operations and tree structure, every node's `v` remains its range's covered count. The public query decomposes the legal domain into disjoint fully included nodes and sums their exact counts, so `count()` returns the number of integers covered by at least one added interval.

## Complexity detail

Let `U = 10^9` be the coordinate range and `Q` the total number of operations. The tree height is `O(\log U)`, about 30.

A contiguous range update is decomposed along at most a constant number of boundary paths per level, so `add` takes `O(\log U)` time with lazy full-cover stops. The public count query excludes only the root's extra endpoint and similarly follows `O(\log U)` levels. Across all calls, time is `O(Q \log U)`.

Nodes are allocated only on visited paths, although `pushdown` creates both siblings at each visited internal node. An operation can create `O(\log U)` nodes, giving `O(Q \log U)` worst-case space. Repeated operations often reuse existing nodes, and a full-cover update can stop high in the tree.

Recursive depth is `O(\log U)`. `__slots__` reduces constants but does not change the asymptotic node count.

## Alternatives and edge cases

- **Ordered disjoint intervals:** Maintain merged intervals in a balanced search tree and a running union length. It can be efficient, but Python lacks a built-in ordered map with the needed predecessor operations.
- **Coordinate array or bitset:** The one-billion-sized domain makes direct storage infeasible.
- **Coordinate compression:** All future endpoints are not supplied in advance to this online class, so static compression is inconvenient.
- **Dynamic interval union list:** A plain sorted list can require linear insertion and merging per add in the worst case.
- **Repeated identical interval:** Full-cover assignment is idempotent and does not increase the count twice.
- **Partially overlapping intervals:** Only previously uncovered coordinates increase ancestor counts.
- **Nested interval:** Adding a range fully inside existing coverage leaves the union count unchanged.
- **Adjacent intervals:** They cover distinct inclusive coordinates, and their lengths add correctly even without explicit interval merging.
- **Single-point interval:** `left == right` descends to or fully covers a segment representing one integer.
- **Full legal domain:** Adding `[1, 10^9]` covers every valid coordinate but not the root's extra `10^9+1`.
- **Count before many adds:** The query still returns the exact current union and may allocate a boundary path due to `pushdown`.
- **Lazy parent followed by partial access:** Propagation fills both children before recursion so existing coverage is preserved.
- **Inclusive endpoints:** Every fully covered node uses `r - l + 1`.
- **Extra root coordinate:** It is excluded explicitly by `query(1, 10^9)` and never appears in a public update.
- **No removal operation:** A one-valued lazy marker is sufficient because coverage never needs to be cleared.
- **Internal mutation during count:** Query allocation changes representation, not the logical set or returned count.
