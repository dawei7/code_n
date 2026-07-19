## General
**Delay each refueling decision until it is necessary**

Treat `startFuel` as the farthest position currently reachable. Scan stations in position order and place the fuel from every reachable station into a max-heap. The heap represents stops the car could have made while passing those positions; choosing one later is a bookkeeping device that produces the same final fuel as choosing it at the station.

If the current reach is still below `target`, one additional stop is necessary. Remove the largest available fuel amount from the heap, extend the reach by that amount, and count the stop. Newly reachable stations then become eligible. If the heap is empty while the target remains out of reach, no past station can supply more fuel and the trip is impossible.

**The largest reachable fuel is the safe greedy choice**

At any point where another stop is required, every station in the heap has already been reachable under the current choices. All candidate stops cost exactly one toward the objective. Selecting the largest fuel amount gives at least as much reach as selecting any other candidate for that same stop count, so it cannot exclude a station or destination that an alternative choice would reach.

By applying this exchange at every required stop, the greedy process maintains the greatest achievable reach for its number of stops. The first stop count that reaches `target` is therefore minimum.

## Complexity detail
Each of the $n$ stations is inserted into the heap once and removed at most once. Heap operations cost $O(\log n)$, so total time is $O(n\log n)$. The heap can contain $O(n)$ fuel values, giving $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Dynamic programming by stop count:** Tracking the farthest distance reachable with each number of stops is correct but takes $O(n^2)$ time and $O(n)$ space.
- **Always stop at every reachable station:** It guarantees at least as much fuel but can use far more stops than necessary.
- **Choose the nearest station first:** Position alone does not capture usefulness; a farther reachable station may offer much more fuel.
- **Initial fuel reaches `target`:** Return `0` without using any station.
- **First station unreachable:** No later station can be reached either, so return `-1`.
- **Arrive with zero fuel:** Equality between reach and a station or `target` is sufficient.
- **Unused passed stations:** Their fuel remains eligible in the heap until selected or the journey ends.
- **Large distances and fuel values:** Reach totals may exceed 32-bit range, so fixed-width implementations should use a sufficiently wide integer type.
