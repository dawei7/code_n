## General
**Sweep minimum sizes offline**

Sort rooms by size descending. Attach each query's original index and sort queries by `minSize` descending. Before answering a query, advance through the room list and activate every room whose size reaches the query's threshold. Because later queries have no larger threshold, activated rooms never need to be removed.

The active room IDs are therefore exactly the eligible set for the current query. What remains is an ordered-set search for the nearest ID on either side of `preferred`.

**Implement the ordered set with compressed IDs**

Sort all room IDs once and map each ID to a one-based coordinate. A Fenwick tree stores 1 for an active coordinate and 0 otherwise. Its prefix sums count active IDs up to any coordinate, and binary lifting finds the coordinate containing the $k$th active ID.

Binary search locates the coordinate boundary at `preferred`. The final active ID at or below that boundary is the predecessor candidate; the first active ID at or above it is the successor candidate. At least one exists whenever the active count is nonzero. Compare candidates by the pair `(absolute distance, room ID)`, which directly implements both the main criterion and tie rule.

For each query, the size sweep activates all and only eligible rooms. Any ID smaller than the predecessor is farther left than the predecessor, and any ID larger than the successor is farther right than the successor. Thus no other eligible ID can beat those two boundary candidates. Comparing them selects exactly the requested room, and writing by the saved query index restores input order.

## Complexity detail
Sorting rooms, queries, and IDs costs $O(r\log r+q\log q)$. Each room activation and each query's prefix/rank searches cost $O(\log r)$, so the total is $O((r+q)\log r)$ when expressed against the room-set operations, with query sorting included in the same standard combined bound. The sorted structures, Fenwick tree, indexed queries, and answer use $O(r+q)$ space.

## Alternatives and edge cases
- **Balanced ordered set:** A tree with predecessor and successor operations expresses the sweep directly, but Python's standard library does not provide one.
- **Scan all rooms per query:** It is simple and correct but takes $O(rq)$ time.
- **Insert into a sorted list:** Binary search finds the insertion point, but shifting list elements makes activation $O(r)$ each.
- **No eligible room:** Leave the answer as `-1`.
- **Exact preferred ID:** If eligible, its distance is zero and it must be selected.
- **Equal distance:** Compare IDs after distance so the smaller one wins.
- **Threshold equality:** A room with `size == minSize` is eligible.
- **One-sided candidates:** The preferred ID may lie below every active ID or above every active ID.
- **Repeated queries:** Each is answered independently and returned at its own original position.
