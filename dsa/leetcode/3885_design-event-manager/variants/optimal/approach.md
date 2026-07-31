## General

**Separate current truth from historical rankings**

Maintain a hash map from every active `eventId` to its current priority. This map is authoritative: changing a priority overwrites the value, and polling a valid event deletes its ID.

For fast ranking, also keep a heap entry `(-priority, eventId)` for every initial event and every update. Python's min-heap places the most negative priority first, which represents the greatest real priority. For equal priorities, its normal tuple order places the smaller event ID first, exactly matching the required tie-break.

**Invalidate obsolete heap entries lazily**

Updating an arbitrary entry already inside a heap would require locating it. Instead, leave the old tuple in place and push the new tuple. During `pollHighest`, repeatedly pop the heap top and compare it with the authoritative map. A tuple is current only when its ID is still active and its stored priority equals the map's current value. Return and delete the first current event; if cleanup exhausts the heap, return `-1`.

Every returned tuple describes an active event because of the map check. Heap order makes it rank at least as highly as every remaining tuple. If a better active event existed, that event's current tuple would appear earlier and could not be rejected as stale. Thus the returned ID has maximum active priority and the smallest ID among ties. Deleting it makes the poll destructive. If no current tuple remains, every historical entry is stale and the active map is empty, so `-1` is correct.

## Complexity detail

Let $E$ be the initial event count and $Q$ the number of later operations. Construction by heap insertion takes $O(E\log E)$ time. Each update pushes one entry in $O(\log(E+Q))$ time. A poll may discard several stale tuples, but every tuple is popped at most once over the whole trace; therefore all construction and operations take $O((E+Q)\log(E+Q))$ total time. A single cleanup-heavy poll can take $O((E+Q)\log(E+Q))$ in the worst case.

The active map and at most one heap tuple per initial event or update use $O(E+Q)$ space.

The benchmark defines size as the number of initially tied events and follows construction with the same number of polls. The lazy heap performs $O(N\log N)$ total work, while a correct manager that scans all active events on every poll performs $O(N^2)$ work.

## Alternatives and edge cases

- **Scan the active map on every poll:** Updates are simple, but a poll costs linear time and a poll-heavy trace becomes quadratic.
- **Ordered set keyed by priority and ID:** A balanced tree can support exact updates and removal in $O(\log(E+Q))$, but Python's standard library has no built-in ordered set.
- **Eager indexed heap:** Tracking each event's heap position permits in-place changes, but every swap must maintain the index map and is more error-prone than lazy invalidation.
- **Priority decrease:** An obsolete larger-priority tuple may remain at the top and must be rejected against the map.
- **Repeated or unchanged updates:** Duplicate historical tuples are safe; after one current tuple is polled and the map entry is deleted, every duplicate becomes stale.
- **Priority tie:** Store the positive event ID as the heap tuple's second component so the smaller ID wins.
- **Removed event:** A polled event is no longer active, and every remaining tuple for its ID must be ignored.
- **Empty manager:** Once all active events are removed, every later poll returns `-1`, even if stale tuples remain in the heap.
- **Maximum values:** IDs and priorities up to $10^9$ fit directly in Python integers and preserve tuple ordering.
