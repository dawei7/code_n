## General

**Record changes at locations instead of simulating every trip**

Passengers from trip `[x, f, t]` occupy seats beginning at pickup location `f` and stop occupying them at drop-off location `t`. The occupied interval is therefore half-open: it includes `f` and excludes `t`.

The solution represents this interval with two events. It adds `x` to `d[f]` and subtracts `x` from `d[t]`. No entry is needed at every intermediate kilometer. When these changes are accumulated from west to east, the added passengers remain in the running total until the subtraction at their destination removes them.

**Size the location timeline**

`mx = max(e[2] for e in trips)` finds the farthest drop-off location. The input is guaranteed nonempty, so the maximum exists. The difference array has indices zero through `mx`, giving every pickup and drop-off a valid bucket.

Locations farther east than `mx` do not matter because all trips have ended. Locations with no event remain zero, meaning the occupancy continues unchanged across them.

**Combine simultaneous pickups and drop-offs**

Several trips can start or end at the same location. Their changes add in one bucket. A drop-off contributes a negative value and a pickup contributes a positive value; the net bucket applies both before the car continues east.

This matches the half-open trip semantics. Passengers whose destination is location five no longer consume seats after reaching five, so those seats can be used by passengers picked up there. The net difference correctly allows that transfer without depending on an arbitrary ordering of separate events.

**Recover occupancy with a prefix sum**

`accumulate(d)` produces the running sum of difference entries. At location $p$, that sum equals the number of passengers from all trips satisfying $f \le p < t$.

Each trip contributes `+x` to every prefix after its start and then has its contribution canceled by `-x` at its end. Summing these independent contributions proves that the prefix total is exactly the seats occupied on the segment beginning at that location.

The expression `all(s <= capacity for s in accumulate(d))` checks every recovered occupancy. If any prefix sum exceeds capacity, `all` stops immediately and returns false. If every sum is within the limit, it returns true.

Passenger totals cannot become negative for a valid collection of trip intervals when all events are considered from the initial empty car: every subtraction corresponds to passengers previously added by that same trip. The algorithm does not need a separate lower-bound check.

**Why checking only event-coordinate buckets is enough**

The implementation scans every integer coordinate through `mx`, including coordinates without events. Occupancy is constant between event locations, so its maximum can change only where a pickup or drop-off occurs. The dense scan is convenient because the coordinate limit is only one thousand.

If all recovered values are at most `capacity`, the car has enough seats at every portion of its eastward route. If one is larger, all passengers whose intervals cover that location would have to be present simultaneously, so no scheduling choice can repair the overload. This proves the returned Boolean.

## Complexity detail

Let $n$ be the number of trips and $L$ the farthest drop-off coordinate. Finding `mx` costs $O(n)$, recording events costs another $O(n)$, and scanning the difference array costs $O(L)$. The precise generalized time is $O(n+L)$.

The constraints cap $L$ at 1000, a fixed constant independent of $n$. Under that bounded domain, the package simplifies the time complexity to $O(n)$.

The difference array contains $L+1$ integers, so its generalized auxiliary space is $O(L)$. With $L \le 1000$, this is treated as $O(1)$ in the package. The prefix sums are generated lazily by `accumulate`, and `all` does not materialize another array.

## Alternatives and edge cases

- **Sorted event list:** Create pickup and drop-off events, sort by location, and scan the running occupancy. This supports large coordinates in $O(n\log n)$ time; drop-offs must be ordered before pickups at the same point or combined by location.
- **Ordered difference map:** Store only nonzero changes in a dictionary, sort its keys, and accumulate. It uses $O(n)$ space and avoids a dense coordinate range.
- **Min-heap of active trips:** Sort trips by pickup, remove all destinations reached before each pickup, and track occupied seats. This costs $O(n\log n)$ and is more complex than the bounded-coordinate difference array.
- **Simulate each passenger or kilometer per trip:** Updating every point inside every interval can cost $O(nL)$. Endpoint differences encode the same coverage much more efficiently.
- **Pickup and drop-off at the same location across trips:** Negative and positive changes share one bucket, so freed seats are immediately available.
- **Capacity exactly reached:** The check uses `<=`, so occupancy equal to capacity is valid.
- **Capacity exceeded briefly:** Even one prefix sum above capacity makes `all` return false, as required.
- **Overlapping trips:** Their interval contributions add automatically in the prefix total.
- **Nonoverlapping trips:** Earlier passengers are subtracted before later pickups, so only each trip’s own load remains on its segment.
- **Trip ending at `mx`:** Its subtraction fits at the final array index. The value after that location is irrelevant because no trip continues.
- **Pickup at zero:** The addition at `d[0]` appears in the first prefix sum, representing passengers entering at the initial location.
- **Input order:** Trips may be arbitrary because event additions are commutative and the prefix scan supplies geographic order.
- **Nonempty trips:** The maximum drop-off call relies on the guaranteed minimum of one trip.
