## General
**Map time onto a fixed 300-second ring**

Only the most recent 300 timestamp values can contribute to a query. Use two arrays of length 300: one records which absolute timestamp currently owns each slot, and the other records the number of hits at that timestamp. Timestamp `t` maps to slot $t \bmod 300$.

**Reset a slot when a later cycle reuses it**

For `hit(t)`, inspect its slot. If the stored timestamp is not `t`, the slot belongs to a time at least 300 seconds older, so overwrite its timestamp and reset its count to one. If it already belongs to `t`, increment the count. This preserves multiple hits in the same second without mixing different ring cycles.

**Sum only timestamps still inside the window**

For `getHits(t)`, examine all 300 slots and include a count exactly when `t - stored_timestamp < 300`. Chronological input ensures stored timestamps are never in the future. The ring contains the aggregated count for every second that could still be relevant; expired slots either fail this comparison or have already been overwritten. Therefore the sum is precisely the hits in `[t - 299, t]`.

## Complexity detail
A hit performs constant work. A query scans exactly 300 slots, which is $O(1)$ because the five-minute window is fixed rather than input-sized. Both arrays have fixed length 300, so storage is $O(1)$. The app adapter's query-result list is output space.

## Alternatives and edge cases
- **Queue every hit:** supports amortized $O(1)$ eviction but may store many entries when one second receives a burst of hits.
- **Store timestamp-count pairs in a deque:** compresses same-second bursts and uses space proportional to active seconds, but still requires eviction bookkeeping.
- **Keep all history and binary-search:** gives $O(\log n)$ queries and unbounded $O(n)$ storage.
- Hits at timestamp $t - 299$ are included, while hits at $t - 300$ are expired.
- Multiple hits at the same timestamp accumulate in one ring slot.
- A query before any hit returns zero.
- Slot reuse must reset the old count instead of adding across timestamps 300 seconds apart.
