## General

Each balloon is a closed horizontal interval `[a, b]`. An arrow fired at coordinate `x` bursts that balloon exactly when $a\le x\le b$. One arrow can therefore burst a group of balloons whenever their intervals share at least one common coordinate.

The greedy strategy processes balloons by increasing right endpoint. Whenever an uncovered balloon is encountered, it fires the next arrow at that balloon's right endpoint. Choosing the earliest available endpoint leaves as much room as possible for the same arrow to intersect later balloons.

**Sort by where balloons end**

`sorted(points, key=lambda x: x[1])` produces a new list ordered by each interval's ending coordinate `b`. The original `points` list is not rearranged because the solution uses `sorted`, not `points.sort()`.

The variable `last` stores the coordinate of the most recently chosen arrow. It starts at negative infinity, meaning no real interval can already contain it. `ans` starts at zero because no arrows have yet been fired.

For each sorted interval `[a, b]`, there are two cases:

- If `a <= last`, the current arrow lies at or to the right of the interval's start. Because intervals are processed by nondecreasing end, the chosen `last` is also no greater than the current `b`. Thus $a\le\texttt{last}\le b$, and this balloon is already burst.
- If `a > last`, the current interval begins strictly after the last arrow. That arrow cannot hit it, so the algorithm must use another arrow. It increments `ans` and sets `last = b`, firing at the current balloon's right endpoint.

The strict comparison is essential. Intervals are closed, so if `a == last`, an arrow at that shared endpoint hits the current balloon and no new arrow is needed.

**Why fire at the right endpoint**

Consider the first balloon not yet covered in ending-time order, with interval `[a, b]`. Every valid solution must fire some arrow `x` inside this interval; otherwise this balloon survives. Since $x\le b$, replace that arrow with one at `b`.

This replacement cannot hurt any balloon at or after the current position that the original arrow also hit. Such a later interval `[c, d]` has $d\ge b$ because of the sort order. If it contained `x`, then $c\le x\le b$. Together with $b\le d$, this gives $c\le b\le d$, so it also contains the replacement arrow at `b`.

Therefore there is always an optimal solution whose next arrow is exactly at the earliest ending uncovered balloon's right endpoint. The greedy choice uses no more arrows than an optimal solution at this step. Removing all intervals hit by that arrow leaves the same kind of problem on the remaining intervals, so repeating the argument proves the complete greedy result is optimal.

**A trace of the first example**

For `[[10,16],[2,8],[1,6],[7,12]]`, sorting by end gives `[1,6]`, `[2,8]`, `[7,12]`, `[10,16]`.

1. `[1,6]` is not covered because `last` is negative infinity. Fire at `6`; now `ans = 1` and `last = 6`.
2. `[2,8]` contains `6`, so the existing arrow bursts it.
3. `[7,12]` starts after `6`, so fire at its end `12`; now `ans = 2` and `last = 12`.
4. `[10,16]` contains `12`, so it is already covered.

The answer is two.

For `[[1,2],[2,3],[3,4],[4,5]]`, the algorithm fires at `2` for the first interval. The second interval starts exactly at `2`, so it is covered. The third starts at `3 > 2`, causing an arrow at `4`, which also covers the fourth interval at its left endpoint. Again the result is two.

**Why counting only the latest arrow is enough**

Once intervals are sorted and an arrow is placed at the earliest uncovered end, any later interval that fails to contain this most recent arrow starts to its right. It also cannot be hit by any earlier arrow, because earlier greedy arrows are at coordinates no greater than `last`. Thus there is no need to store all arrow positions or test each balloon against all of them. The single value `last` summarizes the only arrow that could possibly cover the current interval.

## Complexity detail

Let $n$ be the number of balloons. Sorting the intervals by right endpoint takes $O(n\log n)$ time. The subsequent scan visits each interval once and performs constant work, adding $O(n)$ time. Sorting dominates, so total time is $O(n\log n)$.

Python's `sorted` constructs a new list of $n$ interval references and its sorting implementation may use linear temporary storage. The auxiliary space bound is therefore $O(n)$, matching the manifest. The scan itself uses only the two scalar variables `ans` and `last`, or $O(1)$ extra space beyond the sorted copy.

If the input were already sorted by end and that fact were part of the contract, the scan alone would run in $O(n)$ time. It is not guaranteed here, so sorting is necessary.

## Alternatives and edge cases

- **Sort by starting coordinate and maintain an overlap:** Track the intersection end of the current overlapping group and start a new arrow when the intersection becomes empty. This can also be correct, but the end-sorted greedy has a cleaner exchange argument and only one arrow coordinate.
- **Merge overlapping intervals naively:** Pairwise overlap is not enough to show an entire group shares one point. Any merging method must maintain the common intersection, not merely a chain of overlaps.
- **Try every endpoint:** Testing many candidate arrow subsets is exponential and unnecessary; the exchange argument proves earliest right endpoints are sufficient candidates.
- **Touching intervals:** `[1,2]` and `[2,3]` share coordinate `2`, so one arrow bursts both. The exact condition uses `a > last`, not `a >= last`.
- **Disjoint intervals:** Each new interval starts after the previous arrow, so each requires its own arrow.
- **Nested balloons:** Sorting puts the smallest right endpoint first. An arrow there bursts every containing interval whose start is no greater than that endpoint.
- **Duplicate intervals:** The first copy causes an arrow if needed; all identical copies contain the same arrow and add no count.
- **Negative coordinates:** Initializing `last` to `-inf` works below every finite endpoint, and comparisons require no special treatment.
- **Extreme 32-bit endpoints:** The method performs comparisons only, so it has no subtraction overflow risk in fixed-width languages.
- **Nonempty input guarantee:** The loop will fire at least one arrow. Starting from `ans = 0` also makes the logic robust for an empty list, which would return zero outside the stated contract.
