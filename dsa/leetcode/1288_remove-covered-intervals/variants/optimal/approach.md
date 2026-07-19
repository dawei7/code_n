## General
**Choose an order that exposes every possible cover.** Sort intervals by ascending left endpoint and, when left endpoints tie, by descending right endpoint. Thus any interval capable of covering the current one appears earlier. The descending tie-break is essential: the widest interval with a shared start must be processed before the narrower ones it covers.

Sweep through this order while storing the farthest right endpoint seen. If the current right endpoint is at most that maximum, an earlier interval starts no later and ends no earlier, so the current interval is covered. Otherwise it cannot be covered by any earlier interval, and no later interval starts early enough to cover it; count it as remaining and update the maximum. These two cases prove that the sweep counts exactly the uncovered intervals.

## Complexity detail
Sorting $n$ intervals takes $O(n \log n)$ time, and the subsequent sweep is $O(n)$. Building a sorted copy uses $O(n)$ auxiliary space and leaves the caller's input order unchanged. The sweep itself stores only a counter and one endpoint.

## Alternatives and edge cases
- **Compare every pair:** Testing each interval against every other interval is direct but takes $O(n^2)$ time.
- **Ascending end tie-break:** With equal starts, processing the shorter interval first can count it before discovering the longer interval that covers it.
- **Overlap without coverage:** Crossing intervals such as `[0,10)` and `[5,12)` both remain.
- **Equal right endpoints:** Of intervals ending together, only one with the earliest start can remain.
- **Half-open boundaries:** Coverage uses the given endpoints directly; equality at a boundary still permits coverage.
