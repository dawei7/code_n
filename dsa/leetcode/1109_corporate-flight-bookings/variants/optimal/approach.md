## General
**Represent each inclusive range by two boundary changes:** Allocate a difference array with one extra sentinel position. For a booking `[first, last, seats]`, execute `diff[first - 1] += seats` to begin its contribution at the zero-based position for `first`, then execute `diff[last] -= seats` to end that contribution immediately after flight `last`. The sentinel makes the second update valid even when `last = n`.

**Recover flight totals with a prefix sum:** Scan positions `0` through `n - 1`, updating `current += diff[i]`. The running value contains every booking that has started but not yet ended, exactly the bookings whose inclusive range contains flight `i + 1`. Append that value to the answer.

For any booking, the prefix sum includes its `seats` contribution beginning at `first - 1`. The negative boundary is not encountered until index `last`, so the contribution remains present through output index `last - 1`, corresponding to flight `last`, and disappears afterward. Summing these independent boundary pairs therefore gives precisely the total contribution of all bookings at every flight.

## Complexity detail
Each of the $B$ bookings performs two constant-time boundary updates, and one prefix scan visits the $n$ flights. Time is $O(B+n)$. The difference array and returned answer each have length proportional to $n$, so auxiliary storage is $O(n)$; if the output array itself is reused for differences, extra space beyond the required result can be $O(1)$.

## Alternatives and edge cases
- **Update every covered flight:** Loop from `first - 1` through `last - 1` for each booking. It is straightforward and correct but costs $O(Bn)$ when many bookings cover most flights.
- **Event map plus ordered sweep:** Store boundary changes only at touched labels and process them in order. It can help for sparse labels in a different output contract, but this problem must still produce all $n$ flight totals.
- **Segment tree with lazy propagation:** Supports interleaved range updates and queries, but all updates arrive before one final full output, so the difference array is simpler and asymptotically faster.
- **Single-flight booking:** When `first = last`, the positive and negative boundaries are adjacent and affect exactly one answer position.
- **Full-range booking:** When `[first, last] = [1, n]`, its contribution begins at index zero and ends at the sentinel, so every flight receives it.
- **Overlapping ranges:** Boundary changes add together; the prefix sum naturally carries their combined seat counts through the overlap.
- **Adjacent ranges:** Ending one contribution at the same difference index where another begins preserves both ranges' inclusive endpoints correctly.
