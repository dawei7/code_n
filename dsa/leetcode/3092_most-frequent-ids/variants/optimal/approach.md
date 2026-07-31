## General

**Separate current truth from maximum candidates.** A hash map stores the exact current count for every ID. After applying an update, insert a heap entry containing the negated new count and the ID. Negation turns Python's min-heap into a max-heap by count.

Updating an arbitrary ID can invalidate an older heap entry, but a binary heap cannot delete that entry efficiently by value. Leave it in place. Before reading the maximum, compare the heap's top entry with the current count in the map. If they differ, that entry describes an earlier state and is stale, so remove it. Repeat until the top agrees with the map.

**Lazy deletion preserves the true maximum.** Every current count has an entry inserted when it is created. A stale entry is discarded only when the map proves that its value is no longer current. Once cleanup stops, the top is current. If some other current count were larger, its corresponding heap entry would rank ahead of this top unless an even larger stale entry blocked it; cleanup would remove that blocker. Therefore the remaining top is exactly the largest current frequency.

A zero-count entry is valid and naturally produces `0` when the collection is empty. Retaining zero keys in the map does not affect the maximum.

## Complexity detail

Let $n$ be the number of updates. Each update performs one $O(\log n)$ heap insertion. Although one step may pop several stale entries, every inserted entry can be popped at most once, so all cleanup costs $O(n\log n)$ across the complete run. The total time is $O(n\log n)$, and the count map plus heap use $O(n)$ space.

## Alternatives and edge cases

- **Scan all current counts after every update:** This is simple and correct, but $n$ distinct IDs can make the total work $O(n^2)$.
- **Remove an old heap tuple directly:** Searching a binary heap for an arbitrary entry is linear and destroys the intended update bound.
- **Keep only a running maximum:** Decreasing the unique maximum requires knowing the next-largest current count, which a single scalar cannot provide.
- **Ordered multiset of frequencies:** Removing the old count and inserting the new count gives $O(\log n)$ updates, but Python has no built-in balanced multiset.
- Multiple IDs may tie for the maximum; only the count, not an ID, is returned.
- A negative update may reduce an ID to exactly zero.
- Stale entries can remain below the top without affecting the answer and are removed only if they later reach the top.
- Large positive and negative changes must be applied as whole frequency deltas, not as individual copies.
