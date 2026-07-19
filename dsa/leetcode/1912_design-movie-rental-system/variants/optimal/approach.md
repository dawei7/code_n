## General
**Index the two orderings**

Store the immutable price for every `(shop, movie)` key. For each movie, maintain a min-heap of available candidates ordered by `(price, shop)`. Maintain one global min-heap of rented candidates ordered by `(price, shop, movie)`. A set records which keys are currently rented.

`search` extracts at most five valid entries from one movie heap, records their shop IDs, and pushes those valid entries back so searching does not change availability. `report` performs the analogous bounded extraction from the global rented heap and returns `[shop, movie]` pairs. Heap tuple order implements every required tie-break directly.

**Make lazy deletion safe across repeated cycles**

Removing an arbitrary `(shop, movie)` from a heap would be expensive, so state changes leave old heap records in place. Associate each copy with a monotonically increasing version. Every rent or drop increments that version, and every newly pushed heap record includes it.

A heap record is valid only when its version equals the copy's current version and its rented state matches the heap. This rejects stale records from all earlier cycles. In particular, dropping a copy does not make its original pre-rental record valid again, so repeated searches can never return the same shop twice.

**Preserve the state transitions**

Renting increments the version, marks the key rented, and pushes its current record into the global rented heap. Dropping increments again, clears the rented state, and pushes a current record into the per-movie available heap. The problem's validity guarantees mean neither operation needs to recover from an illegal state.

## Complexity detail
Construction inserts $E$ records and costs at most $O(E\log E)$. Each rent or drop performs one heap insertion in $O(\log(E+Q))$ time. A search or report returns at most five valid records and performs $O(\log(E+Q))$ work per returned record, plus stale removals. Every stale record is removed only once, so those removals are amortized across the full operation sequence. The total time is $O(E\log E + Q\log(E+Q))$.

Prices, states, versions, and initial heap records use $O(E)$ space. Each update can add one lazy heap record, so the worst-case space across $Q$ operations is $O(E+Q)$.

## Alternatives and edge cases
- **Ordered sets:** Balanced ordered sets support direct deletion and insertion without stale records, with the same logarithmic operation bounds, but Python's standard library does not provide one.
- **Scan the inventory:** Filtering and sorting every search or report is simple and correct but can take $O(E\log E)$ per query.
- **Fewer than five matches:** Return every valid match without padding.
- **Equal prices in search:** The smaller shop index comes first.
- **Equal prices in reports:** Compare shop first, then movie.
- **Repeated rent/drop cycles:** Version checks must invalidate every older record so a copy appears at most once.
- **Unknown or fully rented movie:** `search` returns an empty list.
