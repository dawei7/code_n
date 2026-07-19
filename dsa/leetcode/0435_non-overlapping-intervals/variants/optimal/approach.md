## General
**Turn removals into a maximum compatible selection**

If `k` intervals can be retained without overlap, exactly $n - k$ are removed. Therefore maximize the number kept. Sort intervals by increasing end time and scan them in that order.

**Accept the earliest finishing compatible interval**

Keep `previous_end`, the end of the last selected interval. Select the current interval when its start is at least `previous_end`, then update the boundary to its end. Endpoint equality is allowed because touching intervals do not overlap.

**Why the earliest finish leaves the most choices**

Consider the first interval in any optimal compatible selection. The greedy first interval ends no later because it is the earliest-ending candidate overall. Replacing the optimal selection's first interval with the greedy one cannot invalidate any later interval: every later start that followed the old end also follows the no-later greedy end. Applying the same exchange after each selected interval proves the greedy scan keeps as many intervals as any solution.

**Recover the removal count**

Every rejected interval overlaps the current greedy boundary and cannot be inserted into that selected sequence. Once the scan counts the maximum number kept, subtract it from the original interval count.

## Complexity detail
Sorting `n` intervals dominates the linear scan, giving $O(n \log n)$ time. Python's sorting implementation may use $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Sort by start time:** on an overlap, retain the interval with the smaller end; this is an equivalent $O(n \log n)$ greedy method.
- **Dynamic programming:** compute the longest compatible subsequence after sorting in $O(n^2)$ time and $O(n)$ space.
- **Sort by shortest duration:** can discard a globally useful early-finishing interval and is not generally correct.
- **Touching endpoints:** `[a, b]` and `[b, c]` are compatible.
- **Duplicate intervals:** at most one copy can remain.
- **One interval:** no removal is necessary.
