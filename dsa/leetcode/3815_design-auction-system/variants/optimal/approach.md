## General

Each `(itemId, userId)` pair has exactly one current amount, but additions and updates can repeatedly change it. A hash map is the authoritative store for those current bids. It makes replacement, update, and removal expected $O(1)$ operations.

To answer highest-bidder queries efficiently, maintain a separate heap for each item. Python's heap is a min-heap, so store a bid as `(-bidAmount, -userId)`. The smallest tuple then represents the greatest amount; among equal amounts, it represents the greatest user ID, exactly matching both source priorities.

Removing or replacing an arbitrary heap entry directly would require locating it inside the heap. Instead, use lazy invalidation:

- `addBid` and `updateBid` overwrite the authoritative map amount and push the new heap tuple.
- `removeBid` deletes the authoritative map entry but leaves its old heap tuple in place.
- `getHighestBidder` compares the heap top with the map. If that user no longer has the displayed amount for the item, the tuple is stale and is popped. The first matching tuple is returned; an exhausted heap means no bids remain.

The map test makes every returned tuple current. The heap ordering makes that current tuple at least as highly ranked as every tuple beneath it. If a higher-ranked active bid existed, its matching tuple would occur before the returned one and could not have been discarded as stale. The returned user is therefore exactly the required winner. If cleanup empties the heap, every historical tuple is stale, so the map contains no active bid for that item and `-1` is correct.

## Complexity detail

Let $Q$ be the total number of method calls. Each addition or update pushes one entry into a heap of at most $Q$ historical entries, taking $O(\log Q)$ time. Removal takes expected $O(1)$ time in the map. A query can pop several stale entries, each in $O(\log Q)$ time, but every pushed entry is popped at most once over the entire call sequence. Consequently, all $Q$ calls take $O(Q\log Q)$ total time; one cleanup-heavy query can take $O(Q\log Q)$ in the worst case.

The authoritative map and all historical heap entries together use $O(Q)$ space.

The benchmark defines size as the number of bids added to one item and then issues the same number of queries. The lazy heap performs $O(Q\log Q)$ total work. The slower control scans all current bids for that item on every query and therefore takes $O(Q^2)$ time.

## Alternatives and edge cases

- **Scan the current bids per query:** A nested map alone gives simple updates and removals, but `getHighestBidder` becomes linear in the number of bidders for the item and a query-heavy trace becomes quadratic.
- **Ordered set per item:** A balanced tree keyed by `(amount, userId)` supports exact deletion and maximum lookup in $O(\log Q)$ time, but Python's standard library does not provide this structure.
- **Indexed eager heap:** Tracking every heap position can support direct updates and removals, but maintaining indices through swaps is more complex than lazy invalidation.
- **Replacement through `addBid`:** An existing user's previous tuple must become stale; treating the second call as another active bid would violate the one-bid-per-pair contract.
- **Amount tie:** Negating both tuple components makes the greater `userId` win when amounts are equal.
- **Update to a smaller amount:** The old larger tuple may stay near the heap top, so every query must validate the amount against the authoritative map.
- **Removed highest bidder:** Lazy cleanup must continue until the next current tuple is found, not return the removed user.
- **Empty or previously used item:** Return `-1` whether the item never received a bid or all of its bids were removed.
- **Independent items:** Each item owns a separate heap, while the map key includes `itemId`; activity for one item cannot affect another item's winner.
