## General

**Compress the array into increasing-run lengths.** A maximal strictly increasing run continues while each next value is greater than the current value. It stops before an equal or smaller next value. The answer depends only on the lengths of these runs, not on the actual values, because a selected subarray is strictly increasing precisely when it stays inside one run.

The source computes these lengths online. `cur` is incremented once for each visited element. At position `i`, the run is complete when either `i` is the final index or `x >= nums[i + 1]`. The comparison includes equality because equal adjacent elements violate strict increase.

When a run finishes, `pre` holds the length of the preceding run and `cur` holds the completed current length. After evaluating candidates, the assignment `pre, cur = cur, 0` preserves the completed length for the next boundary and prepares the next iteration to count its first element.

**Derive the candidate inside one run.** Two adjacent subarrays of common length $k$ occupy $2k$ consecutive positions. If all those positions lie in one strictly increasing run of length $L$, splitting any suitable $2k$-element region at its midpoint gives two strictly increasing halves. The largest such $k$ satisfies $2k\le L$, so it is

$$
\left\lfloor\frac{L}{2}\right\rfloor.
$$

This is the source's `cur // 2` candidate. Odd leftover elements do not cause a problem because the two chosen subarrays need not cover the entire run.

**Derive the candidate across a run boundary.** A decrease or equality is allowed between the two subarrays; only comparisons inside each subarray must increase. Therefore the shared boundary between the adjacent blocks may coincide with the break between two consecutive maximal runs.

If the previous run has length $P$ and the current run has length $C$, the left block can take a suffix of at most $P$ elements and the right block can take a prefix of at most $C$ elements. Equal lengths require

$$
k\le\min(P,C).
$$

The largest boundary-crossing candidate is consequently `min(pre, cur)`.

**Why these two candidates are exhaustive.** Consider the contiguous $2k$ positions occupied by any legal answer. A maximal-run break cannot be strictly inside the left half or right half, since that would make the corresponding half non-increasing at that pair. Thus the combined region contains either no run break, placing it inside one run, or exactly one break at the midpoint between halves, placing it across two consecutive runs. These are exactly the two formulas evaluated by the code.

It is impossible for a valid pair to use nonconsecutive runs. Reaching across an intervening run boundary would put a break inside one selected half. This is why remembering only `pre`, rather than all earlier run lengths, is sufficient.

**Update the global maximum at every completed run.** The statement

`ans = max(ans, cur // 2, min(pre, cur))`

retains the best earlier result and adds both structures involving the newly completed run. The initial `pre = 0` makes the cross-boundary candidate harmless for the first run. The final-index condition ensures the last run receives the same processing as all earlier runs.

**Walk through representative run lengths.** If the maximal runs have lengths 4, 6, and 3, the internal candidates are 2, 3, and 1. The consecutive-boundary candidates are `min(4,6)=4` and `min(6,3)=3`. The global answer is four, realized by the last four elements of the first run and the first four elements of the second run. Although the second run alone supports only two length-three halves, pairing it with its neighbor can do better.

If the whole array is one increasing run of length 10, `pre` stays zero when that run is processed and the internal formula returns five. If every adjacent comparison fails, all runs have length one. Internal candidates are zero and cross-boundary candidates are one, so the answer is one, matching two adjacent single-element subarrays.

**Why run-end evaluation loses nothing.** The internal value `cur // 2` is monotone as a run grows, so its greatest value occurs at the run's end. The cross-boundary value requires the current run's final length. Evaluating only at boundaries therefore captures every maximum while performing constant work per element.

**Why the returned maximum is exact.** Every value added to `ans` describes a realizable pair: split a run for `cur // 2`, or take equal suffix/prefix lengths for `min(pre,cur)`. The exhaustive placement argument also shows that no legal pair can exceed both formulas for its containing run or boundary. The maximum of all recorded candidates is therefore neither too large nor too small.

## Complexity detail

Let $n$ be `len(nums)`. The single loop processes each element once. Comparisons and counter updates take constant time, giving $O(n)$ time.

Only `ans`, `pre`, `cur`, and loop variables are retained. Auxiliary space is $O(1)$, and the input array remains unchanged. This is important for the $2\cdot10^5$ upper bound: no run list or per-index table is needed.

## Alternatives and edge cases

- **Materialize every maximal run:** It makes the two formulas easy to apply afterward but spends $O(r)$ extra space for $r$ runs when only the previous length is needed.
- **Increasing-prefix arrays:** Precomputing how far each increasing region extends can solve the problem in linear time with $O(n)$ storage.
- **Binary search the answer:** Feasibility is monotone in $k$, but repeated linear checks cost $O(n\log n)$ and are inferior to the direct maximum formula.
- **Brute-force each $k$ and start:** Rechecking comparisons can become cubic and obscures the run structure.
- **Single maximal run:** The answer is its length divided by two with floor rounding.
- **Boundary can help more than an internal split:** Runs of lengths four and six support $k=4$ across their boundary even though their internal candidates are only two and three.
- **Unequal adjacent runs:** The shorter run is the exact limiting side.
- **All equal values:** Every run length is one, so the answer is one.
- **Strictly decreasing values:** It has the same run-length pattern as an all-equal array.
- **Exactly two elements:** Each singleton is vacuously strictly increasing, so the answer is one.
- **Equality test:** Using `x > nums[i + 1]` would be wrong because it would let equal values remain in a supposedly strict run.
- **Last element:** Treating it as an explicit run ending prevents the final candidate from being omitted.
- **Odd run length:** One unused element is allowed; only the selected subarrays must be adjacent to each other.
- **Large or negative integers:** Only comparisons are performed, so values near either constraint limit behave identically.
- **Input preservation:** The algorithm never sorts or rewrites `nums`, preserving original adjacency.
