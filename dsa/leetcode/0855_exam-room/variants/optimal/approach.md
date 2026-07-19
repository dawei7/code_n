## General
**Represent available choices as gaps between occupied seats**

Use a free interval `(left, right)` for every pair of consecutive occupied boundaries. Virtual boundaries `-1` and `n` represent the room edges. The best seat for an interval is `0` when `left == -1`, `n - 1` when `right == n`, and `(left + right) // 2` otherwise.

Its distance is the full edge gap for a virtual boundary and half the gap for an interior interval. Store intervals in a priority heap ordered first by decreasing distance and then by increasing candidate seat, exactly matching the placement and tie rules.

**Split on arrival and merge on departure**

When `seat()` removes the best valid interval `(left, right)`, let its candidate be `p`. Replace the interval with `(left, p)` and `(p, right)`. Even intervals containing no empty seat remain in endpoint maps, because they identify neighboring occupied seats for a future departure.

For `leave(p)`, the map ending at `p` gives the left neighbor boundary and the map starting at `p` gives the right neighbor boundary. Remove those two intervals and insert their merged interval.

**Discard stale heap entries lazily**

A merge can invalidate an interval that remains buried in the heap. Keep an active interval set; `seat()` pops until it finds a pair still active. Each stale entry was created by an earlier update and is discarded at most once, so lazy removal preserves the amortized bound.

The active intervals always partition the row between consecutive occupied seats and virtual boundaries. Their candidates are exactly the locally best available seats. Selecting the globally highest-priority candidate therefore implements the required maximum distance and lowest-label tie break after every valid trace prefix.

## Complexity detail
Each operation creates or invalidates only a constant number of intervals. Heap pushes and valid pops cost $O(\log q)$; stale entries are popped once over the entire trace, so processing $q$ calls takes $O(q\log q)$ amortized time. The heap, active set, endpoint maps, and output use $O(q)$ space.

## Alternatives and edge cases
- **Sorted occupied list:** Scan every gap for `seat` and insert or remove in sorted order; it is simple and correct but can take $O(q^2)$ total time.
- **Balanced interval tree:** An ordered set augmented with the best gap supports logarithmic operations, but Python's standard library does not provide one directly.
- **Eager heap deletion:** Locating and removing arbitrary heap entries is linear; lazy invalidation avoids that cost.
- **Empty room:** The initial virtual interval chooses seat `0`.
- **One-seat room:** After its only student leaves, merging the two virtual-boundary intervals restores seat `0`.
- **Equal distances:** The heap's candidate-seat key selects the smaller label.
- **Boundary gaps:** Their full length matters because only one occupied endpoint constrains the student.
- **Adjacent occupied seats:** Their interval has no free candidate but must remain in endpoint maps for merging.
- **Leaving a boundary seat:** A virtual endpoint is merged just like an occupied neighbor.
- **Repeated reuse:** Departures and later arrivals may recreate an old interval; active-pair validation distinguishes its current validity.
