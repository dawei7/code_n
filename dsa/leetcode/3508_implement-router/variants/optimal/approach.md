## General

The router needs three different views of the same active packets. A deque preserves global insertion order for FIFO forwarding and capacity eviction. A set of complete `(source, destination, timestamp)` tuples answers active-duplicate checks. Finally, each destination owns a timestamp list for range counting.

Because all `addPacket` calls have non-decreasing timestamps, every destination's timestamp list is also non-decreasing. Removed timestamps do not need to be deleted from the front of these lists. Store `left_index[destination]`, the number of that destination's packets already removed. The active timestamps for a destination are exactly the suffix beginning at this index.

On a nonduplicate insertion, evict the deque front first when the router is full, then append the packet to the deque and set and append its timestamp to the destination history. A duplicate returns `false` before eviction, so a rejected call cannot alter router state.

Both explicit forwarding and automatic eviction use the same removal helper. It pops the global deque front, erases that tuple from the active set, and advances the removed destination's left index. FIFO order implies that removals for any fixed destination occur in the same order as its timestamp history, so this single index always separates removed and active entries.

For `getCount`, binary-search the active suffix. The first position at least `startTime` comes from `bisect_left`, while the first position greater than `endTime` comes from `bisect_right`. Their difference counts precisely the active timestamps in the inclusive interval.

These structures maintain three facts after every method call: the deque contains active packets in FIFO order, the set contains exactly the same packets without order, and each timestamp history's live suffix contains exactly the active packets for that destination. The update rules preserve all three facts, which proves the returned duplicate decisions, forwarded packet, and range counts are correct.

## Complexity detail

Let $q$ be the total number of public method calls. With expected constant-time hash-set operations, `addPacket` and `forwardPacket` take $O(1)$ amortized time. A `getCount` call takes $O(\log q)$ time for two binary searches. Thus an arbitrary sequence of $q$ calls takes $O(q\log q)$ time in the worst case represented by the package bound.

The active deque and set use $O(\texttt{memoryLimit})$ space. Timestamp histories retain every successfully inserted packet, including removed prefixes, so across the complete call sequence the implementation uses $O(q)$ space.

The benchmark spends half of its non-constructor calls inserting packets for one destination and half issuing range counts over the resulting history. It contrasts binary search with a correct router that scans every active packet for each query, whose full workload takes $O(q^2)$ time.

## Alternatives and edge cases

- **Scan the FIFO queue for `getCount`:** This is straightforward and correct, but each query costs $O(\texttt{memoryLimit})$ instead of logarithmic time.
- **Delete timestamps from list fronts:** Physical front deletion shifts the remaining list and can make repeated forwarding quadratic; a live-suffix index avoids that cost.
- **Store only per-destination data:** Range queries become easy, but a separate global order is still required to identify the oldest packet across destinations.
- **Check duplicates after eviction:** This would wrongly discard the oldest packet when the attempted insertion is a duplicate; rejection must occur first.
- **Inclusive interval:** Use the right insertion boundary for `endTime`, so timestamps equal to either endpoint are counted.
- **Equal timestamps:** Different source or destination values make distinct packets, and stable FIFO order still follows insertion order.
- **Duplicate lifetime:** A triple is rejected only while active. After forwarding or eviction removes it, the same triple may be inserted again when the non-decreasing timestamp guarantee permits that call.
- **Empty router:** `forwardPacket` returns `[]`, and every range count is zero.
- **Capacity eviction:** A successful insertion at capacity removes exactly one packet before appending the new one, keeping the size equal to `memoryLimit`.
