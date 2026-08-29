## General

**Maintain all currently available seats in a min-heap.** The required reservation is always the smallest-numbered unreserved seat. A min-heap is designed to expose the smallest stored value while supporting removals and later insertions efficiently.

The single field `self.q` represents exactly the set of available seat numbers. Reserved seats are absent. Because the operation guarantees prevent unreserving an already available seat, no seat number appears twice.

**Initialization is already a valid heap.** The constructor assigns

`self.q = list(range(1, n + 1))`.

This produces `[1, 2, 3, ..., n]`. Python’s heap representation requires every parent value to be no greater than its children. A globally increasing array automatically satisfies that property, so the code does not need to call `heapify`. All seats are present exactly once, matching the initially available state.

The constructor stores no separate `n` because later operations only need the current heap. Bounds are guaranteed by the caller’s valid method calls.

**Reserve the smallest seat.** `heappop(self.q)` removes and returns the heap root. In a min-heap, the root is the smallest available value, so the method returns precisely the seat required by the contract. Removing it also changes the state to reserved: it is no longer in the availability heap.

After removing the root, `heappop` moves another element to the root and sifts it down until the heap property is restored. Future calls therefore continue to see the smallest remaining seat.

The problem guarantees at least one unreserved seat for every `reserve` call, so the code does not need to handle an empty heap or raise a custom error.

**Unreserve by reinserting.** `heappush(self.q, seatNumber)` adds the seat back to the available collection. The heap operation initially places it at the end and sifts it upward while it is smaller than its parent. This ensures it can become the root immediately if it is now the smallest available seat.

The contract guarantees that `seatNumber` is currently reserved. That guarantee is essential because the exact implementation does not maintain a separate membership set. An invalid duplicate unreserve would insert the same seat twice and permit it to be reserved twice, but such a call is outside the allowed sequence.

**Trace the sample.** Initially, the heap contains one through five. The first pop returns one, and the second returns two. Unreserving two pushes it back; because it is smaller than every other available seat, it rises to the root. The next reserve returns two again. Subsequent pops return three, four, and five. Pushing five after it is unreserved makes it available for the next request.

**State invariant.** After construction and after every operation, `self.q` contains each unreserved seat exactly once and no reserved seat. It also satisfies the min-heap ordering property.

Initialization establishes the invariant. A valid `reserve` removes the smallest element, so that one seat changes from available to reserved while all others remain; `heappop` restores heap order. A valid `unreserve` inserts the one reserved seat named by the caller; `heappush` restores heap order and uniqueness follows from the valid-call guarantee. By induction, every reserve returns the smallest member of the true available-seat set.

**Why a heap fits arbitrary unreservations.** If seats were only ever reserved and never returned, a simple counter would be sufficient. Unreservation can make an old, small number available again, so the next answer is not necessarily the next never-used number. The heap merges returned seats into the same minimum selection rule without scanning all seats.

**Exact pre-initialization tradeoff.** This implementation stores all `n` seats immediately. An alternative design can keep a counter for never-reserved seats and a heap only for seats that were unreserved, reducing initial storage and setup. The exact source chooses the simpler invariant that one heap is the complete availability set.

## Complexity detail

Constructing `range` and its list takes `O(n)` time and `O(n)` space. No separate heap-building pass is required because the increasing list already satisfies heap order.

Each `reserve` uses `heappop` and each `unreserve` uses `heappush`. With at most `n` available entries, either operation takes `O(log n)` worst-case time. For `q` total operations, the operation cost is `O(q log n)` after `O(n)` initialization.

The heap stores at most `n` integers, so object space is `O(n)`. No output history or membership table is retained.

## Alternatives and edge cases

- **Counter plus returned-seat heap:** Track the smallest never-reserved number and heap only unreserved seats. This avoids storing all seats initially and often uses less memory.
- **Balanced ordered set:** It also supports minimum removal and reinsertion in logarithmic time, but Python’s standard library has no built-in tree set.
- **Boolean array plus linear scan:** Availability flags are simple, but finding the next smallest seat can degrade to `O(n)` after arbitrary unreservations.
- **Simple increasing counter alone:** It fails when a previously reserved smaller seat is unreserved and must be chosen before new larger seats.
- **One seat:** The heap alternates between one entry and empty under the guaranteed valid reserve and unreserve sequence.
- **Unreserve the smallest number:** Heap push moves it toward the root, making it the next reservation.
- **Unreserve a large number:** It remains in the appropriate heap position until all smaller available seats are used.
- **Reserve when none available:** The source does not guard this because the contract guarantees it never occurs.
- **Duplicate unreserve:** The source does not prevent duplicate heap entries because the contract guarantees only reserved seats are unreserved.
- **Seat bounds:** The constructor and valid calls ensure every stored number remains from one through `n`.
- **Already-heapified initialization:** The increasing list needs no `heapify` call; adding one would be correct but redundant.
- **No stored `n`:** The heap fully captures runtime availability, so the constructor parameter need not remain as a field.
