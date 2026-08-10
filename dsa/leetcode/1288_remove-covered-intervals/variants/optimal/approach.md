## General

**Sort so a possible covering interval always comes first**

An interval `[a,b)` is covered when an earlier candidate has a start no greater than $a$ and an end no smaller than $b$. Sorting by ascending start establishes the first condition automatically: while scanning, every earlier interval begins at or before the current one.

Intervals with the same start need special handling. The longer interval must appear first, because it covers every shorter interval sharing that start. The key `(x[0], -x[1])` sorts starts upward and ends downward for ties.

Without the negative end tie-breaker, `[1,4)` could be seen before `[1,8)`. The shorter interval might be counted as uncovered even though the later longer interval covers it. Putting `[1,8)` first prevents that mistake.

The source calls `intervals.sort`, so it mutates the caller's list order.

**Track the farthest end reached so far**

Variable `pre` stores the largest right endpoint among intervals already counted as not covered. It begins at negative infinity, ensuring the first sorted interval has `cur > pre` and is counted.

For each interval, the start is ignored in the loop because sorting has already incorporated it. If current end `cur <= pre`, some earlier interval starts no later and ends at least as late. That earlier interval covers the current one, so the count and `pre` remain unchanged.

If `cur > pre`, no earlier interval reaches the current end. Therefore none can cover it, the interval remains, `ans` increases, and `pre` becomes `cur`.

It is sufficient to remember only the maximum end rather than a particular full interval. Any earlier interval responsible for that maximum also has a start no greater than the current start due to sorting. Those two facts are exactly the coverage conditions.

**Why `pre` never decreases**

When an interval is covered, replacing `pre` with its smaller or equal end would forget a stronger covering interval and could make a later covered interval appear new. The code deliberately updates `pre` only on a strict increase. It is therefore a monotone summary of the farthest right boundary reached by any earlier surviving interval. This is the central scan invariant: before processing each interval, `pre` is the maximum end among all earlier intervals. The skip and update branches both preserve it.

**Trace the first example**

Input `[[1,4],[3,6],[2,8]]` sorts to `[[1,4],[2,8],[3,6]]`. The first end four exceeds negative infinity, so it is counted and `pre` becomes four. End eight exceeds four, so that interval is also counted and `pre` becomes eight. End six does not exceed eight, so `[3,6)` is covered by `[2,8)` and skipped. The answer is two.

For same-start intervals such as `[1,8)` and `[1,4)`, descending end order makes eight establish `pre` before four is tested, correctly removing the shorter one.

**Why the greedy scan is correct**

When an interval is skipped, `pre >= cur`. The earlier interval that established `pre` has start at most the current start and end at least the current end, so skipping is justified.

When an interval is counted, its end is larger than every earlier end. Since all possible earlier covering intervals would need an end at least as large, none covers it. A later interval cannot cover it unless it has the same start, but same-start longer intervals were sorted earlier; any genuinely later start is too large to satisfy the coverage definition. Thus every counted interval truly remains.

The scan classifies every interval exactly once, proving that `ans` is the number left after removing covered intervals.

Half-open versus closed right endpoints does not alter these comparisons: coverage still uses $b\le d$, and equal endpoints are sufficient.

## Complexity detail

Let $n$ be the number of intervals. Python sorting takes $O(n\log n)$ comparisons, and the scan takes $O(n)$ time. Total time is $O(n\log n)$.

The loop itself uses $O(1)$ auxiliary space. Python's in-place Timsort may require $O(n)$ temporary memory in the worst case, so the exact implementation's overall auxiliary space is $O(n)$, matching the manifest.

The method returns only an integer and does not build a remaining-interval list.

## Alternatives and edge cases

- **Quadratic pair checks:** Compare every interval with every other interval. It is straightforward but costs $O(n^2)$ time.
- **Sort only by start:** This fails when equal-start intervals appear shortest first; the descending-end tie-break is essential.
- **Track the immediately previous end only:** The maximum end is needed because a much earlier interval may cover the current one even when the immediately previous interval does not.
- **No covered intervals:** Ends strictly increase through the sorted scan, so every interval is counted.
- **All covered by one interval:** The first longest interval sets `pre`, and all remaining ends are no greater.
- **Equal right endpoints:** The later-start interval is covered because `cur == pre` does not pass the strict increase test.
- **Nested intervals:** Descending reachable ends cause all inner intervals to be skipped.
- **Disjoint intervals:** Their ends increase with starts, so they all remain.
- **Unique interval guarantee:** Exact duplicate pairs do not occur, though the same logic would count only one duplicate.
- **Input mutation:** Copy the list before sorting if caller-visible order must remain unchanged.
