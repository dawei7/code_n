## General

**Sort intervals by starting day**

Meeting days are inclusive and intervals may overlap. Sorting `meetings` lexicographically places them in nondecreasing start order, with end order breaking equal starts.

Variable `last` is the farthest day covered by any processed meeting. Initially zero represents the boundary immediately before work day 1.

For meeting `[st, ed]`:

- if `last < st`, days strictly between `last` and `st` have no processed meeting;
- there are `st - last - 1` such days;
- then `last = max(last, ed)` extends the covered prefix if this meeting reaches farther.

After all meetings, days `last + 1` through `days` are free, contributing `days - last`.

**Why overlap is not double-counted**

If a meeting begins at or before `last`, it overlaps or touches the already covered region and creates no free gap. Updating with maximum retains whichever end reaches farther.

If a contained interval ends before `last`, maximum leaves `last` unchanged. It cannot reduce known coverage.

Inclusive endpoints explain the minus one. If coverage ends on day 3 and next meeting starts day 5, only day 4 is free: $5-3-1=1$.

**Example**

For ten days and sorted meetings `[1,3]`, `[5,7]`, `[9,10]`:

- before first meeting there are zero free days;
- gap between 3 and 5 contributes day 4;
- gap between 7 and 9 contributes day 8;
- no tail remains after day 10.

Answer is 2.

For `[1,3]` and `[2,4]`, the second start is within coverage and extends `last` from 3 to 4. The union is treated as one interval.


After processing the sorted prefix, `last` is the maximum covered endpoint and `ans` is the number of uncovered days strictly before or equal to that processed region.

Because future meetings start no earlier than the current one, when `st > last` no future interval can cover days between `last+1` and `st-1`. Counting them is final and safe.

When `st <= last`, there is no uncovered gap before this meeting. Extending the maximum endpoint maintains the invariant. After the loop, no meeting remains to cover the tail, so adding it completes the total.

**Equivalent covered-days viewpoint**

One could merge meetings and subtract the total union length from `days`. The exact code instead accumulates complement gaps directly. Both are equivalent because the calendar days 1 through `days` are partitioned into covered union intervals and the gaps between them.

Direct gap counting avoids separately storing merged intervals. `last` is enough because sorted start times guarantee that only the current farthest covered endpoint can influence the next gap.

For a merged inclusive interval `[a,b]`, covered length would be $b-a+1$. The source's gap formula is the complementary inclusive formula: between covered endpoint $b$ and next start $c$, uncovered length is $c-b-1$.

**Why sorting by start is sufficient**

Lexicographic list sorting also orders ends for equal starts, but correctness does not depend on that tie order. If several meetings share a start, processing any of them first creates no gap, and repeated `max` eventually retains their largest end.

Without sorted starts, seeing a late meeting first could cause the algorithm to count an earlier region as a permanent gap even though an unprocessed meeting covers it. Sorting is what makes every counted gap irrevocable.

**Large day range**

The calendar can contain a billion days, yet only meeting boundaries matter. Arithmetic jumps across a gap in constant time; it never iterates day by day. This is the central reason the interval method scales with meeting count rather than `days`.

**No off-by-one at the tail**

After final covered day `last`, the free days are `last+1, ..., days`. Their inclusive count is `days - (last+1) + 1 = days-last`, exactly the final addition.

**Input mutation**

`meetings.sort()` changes the order of the caller's list. This does not affect the returned count but is a visible side effect. Sorting a copy would preserve input order at additional memory cost.

## Complexity detail

Let $n$ be the number of meetings.

Sorting costs $O(n\log n)$ time, and the merge-style scan costs $O(n)$. Total time is $O(n\log n)$.

Python's list sort may use $O(n)$ temporary memory in the worst case, matching the manifest's $O(n)$ space. The scan itself uses $O(1)$ scalar state.

The algorithm does not allocate by `days`, which can be $10^9$; it works entirely with interval endpoints.

The output is one integer.

## Alternatives and edge cases

- **Merge into an explicit interval list:** Sum merged covered lengths and subtract from days. It is equivalent but stores $O(n)$ merged intervals unnecessarily.
- **Difference array by day:** Impossible when days is up to $10^9$.
- **Sweep events:** Start/end deltas also work after sorting but require care with inclusive endpoints.
- **Meeting covering every day:** No gaps or tail are added, returning zero.
- **Overlapping meetings:** `max(last, ed)` prevents duplicated coverage.
- **Nested meeting:** It does not change `last`.
- **Back-to-back inclusive meetings:** Intervals ending day 3 and starting day 4 leave no free day because formula gives zero.
- **Gap of one day:** End 3 and start 5 contribute exactly day 4.
- **Meeting starting day one:** Initial `last=0` produces no false leading gap.
- **Meeting ending on final day:** Tail contribution is zero.
- **Single meeting:** Leading and trailing gaps are both handled.
- **Input order:** Sorting makes arbitrary original order irrelevant but mutates the list.
