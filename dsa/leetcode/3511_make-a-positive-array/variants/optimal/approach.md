## General

**Turn replacements into an interval-hitting problem**

A bad subarray is any contiguous interval of length at least three whose original sum is non-positive. To make the array positive, every such interval must become positive.

One allowed replacement can set a chosen element to a very large positive integer, up to `10^18`. The total magnitude of all original values in any subarray is at most `10^5 \cdot 10^9 = 10^14`. Therefore, replacing one element of a bad interval by a sufficiently large positive value makes that interval positive. Making values larger cannot turn an originally positive interval into a non-positive one.

This yields an equivalent combinatorial view: choose the minimum number of indices so that every original bad interval contains at least one chosen index. After choosing them, those positions can be replaced by large positive values. An interval containing a chosen position is repaired; an interval containing no chosen position is unchanged, so it must already have had positive sum.

The problem is now a minimum point-cover problem for intervals on a line. Such intervals have a standard greedy solution: process them in increasing order of right endpoint, and whenever the first uncovered interval appears, choose its right endpoint.

The source does not explicitly generate all `O(n^2)` subarrays. It discovers exactly when an uncovered bad interval first ends by maintaining a compact prefix-sum condition.

**Meaning of the scan variables**

The variables have precise roles:

- `l` is the index most recently selected for replacement; it begins at `-1`, just before the array.
- `s` is the sum of the current suffix `nums[l + 1 .. r]` after the value at scan index `r` has been added.
- `pre_mx` is the maximum eligible prefix sum that can be removed from `s` to form a subarray ending at `r` with length at least three.
- `ans` counts selected replacement positions.

Why can the scan ignore intervals beginning at or before `l`? Every future interval that contains `l` is already hit by that replacement. Intervals ending before `l` were handled earlier. Only completely unhit intervals lying to the right of `l` can force another operation.

Define, within the current unhit segment, a relative prefix sum

`P(t) = nums[l + 1] + nums[l + 2] + ... + nums[t]`,

and define `P(l) = 0`. Since `s = P(r)`, a subarray `nums[t + 1 .. r]` has sum

`P(r) - P(t) = s - P(t)`.

It is non-positive exactly when `s <= P(t)`. Its length is `r - t`, so requiring at least three elements means `t <= r - 3`. Consequently, there is an uncovered bad subarray ending at `r` exactly when

`s <= max(P(t))` for eligible `t` from `l` through `r - 3`.

That maximum is what `pre_mx` represents at the moment the condition is tested.

**How the code delays prefixes until they are eligible**

After adding `x = nums[r]`, the source checks:

`r - l > 2 and s <= pre_mx`.

The first part says that at least three positions exist after the last selected index. The second part is the prefix-sum test just derived.

If no bad interval is found and `r - l >= 2`, the source updates `pre_mx` with:

`s - x - nums[r - 1]`.

Because `s` is the sum through `r`, subtracting the final two elements leaves `P(r - 2)`. This prefix is not eligible for a length-three interval ending at the current `r`, but it becomes eligible when the scan advances to `r + 1`:

`(r + 1) - (r - 2) = 3`.

That one-iteration delay is the subtle reason for this exact expression. For the first possible interval, `pre_mx` already contains the empty prefix `P(l) = 0`. Thereafter it accumulates each newly eligible prefix maximum.

For example, when `l = -1` and `r = 2`, the only length-at-least-three interval ending there starts at index zero. The eligible removed prefix is `P(-1) = 0`. The condition simply tests whether the sum of `nums[0..2]` is non-positive. At `r = 3`, `P(0)` has also become eligible, so both `nums[0..3]` and `nums[1..3]` are covered by the maximum-prefix test.

**The greedy action on the first uncovered bad interval**

When the condition succeeds, some bad interval ending at `r` is still unhit. The scan has processed right endpoints in increasing order, so this is the earliest right endpoint at which another replacement is necessary. The algorithm selects `r` itself:

- `ans` increases;
- `l = r` records the chosen index;
- `s = 0` starts the sum for the unhit region after `r`;
- `pre_mx = 0` resets its relative prefix system.

It is unnecessary to modify `nums[r]` numerically. The rest of the algorithm only needs to know which intervals are hit, and `l` records that boundary.

**Why choosing the right endpoint is optimal**

Let `[a, r]` be an uncovered bad interval with the earliest ending position encountered. Any valid solution must choose at least one index `p` inside `[a, r]`; otherwise that interval remains unchanged and non-positive.

Suppose an optimal solution chooses such a `p`. Replace that choice by `r`. This still hits `[a, r]`. It also does not lose coverage of any bad interval considered later that was hit by `p`: a later interval has right endpoint at least `r`, and if it contains `p` then its left endpoint is at most `p \le r`, so it also contains `r`. Thus there is an optimal solution making the greedy choice.

After choosing `r`, the same argument applies independently to intervals lying completely to its right. Repeating the exchange proves that the number of choices made by the source is minimum.

**Why hitting original bad intervals is sufficient**

Choose each greedy position's replacement value sufficiently large and positive. Every originally bad interval contains a chosen position by construction and therefore becomes positive. Every originally positive interval either contains no replacement and stays unchanged, or contains one or more replacements that only raise its sum enough to remain positive. Hence all length-at-least-three subarrays are positive.

Conversely, any set of replacements that makes the final array positive must touch every originally non-positive interval, because an untouched interval retains its original non-positive sum. This establishes both directions of the interval-hitting reduction, rather than merely treating the greedy scan as a heuristic.

## Complexity detail

Let `n = len(nums)`. The source makes one left-to-right pass. Each element causes one addition, a constant number of comparisons, and at most one prefix-maximum update or greedy reset. No index is revisited and no subarray is enumerated explicitly. Time complexity is therefore `O(n)`.

The variables `l`, `ans`, `pre_mx`, `s`, `r`, and `x` occupy constant auxiliary storage. The algorithm does not allocate a prefix-sum array and does not mutate `nums`, so auxiliary space is `O(1)`.

Python integers safely hold the running sums. Under the constraints, ordinary signed 64-bit arithmetic would also be sufficient for original sums because their magnitude is at most `10^14`. The hypothetical replacement values are part of the correctness argument only and are never stored by this implementation.

## Alternatives and edge cases

- **Enumerate every bad subarray:** One could compute all interval sums and then greedily hit the resulting intervals, but there are `O(n^2)` subarrays. The running prefix maximum discovers the earliest-ending uncovered bad interval in linear time without materializing intervals.
- **Dynamic programming over replacement positions:** General set cover is difficult, but intervals on a line have the right-endpoint greedy exchange property. DP adds state without improving the linear result.
- **Replace the most negative element:** A locally very negative value may lie outside the earliest bad interval or cover fewer future bad intervals. Its magnitude does not establish the minimum number of positions.
- **Choose the left endpoint of a bad interval:** This repairs the current interval but offers no exchange guarantee for later-ending intervals. The right endpoint reaches farthest into all intervals that can overlap the current one.
- **Track the minimum prefix instead of the maximum:** A non-positive interval requires `s - P(t) <= 0`, or `P(t) >= s`. Therefore the relevant witness is the maximum eligible prefix, not the minimum.
- **Use all prior prefixes immediately:** Prefix `P(t)` is valid only when `t <= r - 3`. Including `P(r - 2)` or `P(r - 1)` too early would detect forbidden subarrays of length two or one.
- **Exactly zero sum:** The definition requires positive sums, so a zero-sum subarray is bad. The source correctly tests `s <= pre_mx` rather than strict inequality.
- **Length exactly three:** This is the first relevant length and is detected when `r - l > 2`. The delayed prefix update ensures the empty relative prefix is used.
- **Subarrays of length one or two:** They impose no requirement, even if their sums are negative. The length guards prevent them from triggering an operation.
- **Several bad intervals ending together:** One choice at their common right endpoint hits all of them. The maximum-prefix test needs only to establish existence, not count how many witnesses there are.
- **Overlapping bad intervals:** Choosing an early right endpoint may repair many overlaps. Resetting at `l = r` is safe because every interval crossing `l` now contains a replacement.
- **Disjoint bad intervals:** Each disjoint uncovered region necessarily needs its own selected index; the scan resets and discovers it independently.
- **All relevant sums already positive:** The condition never succeeds and `ans` remains zero.
- **Negative and large-magnitude inputs:** Prefix comparisons work without sign assumptions. A fixed-width implementation should use 64-bit sums, not 32-bit integers.
- **Replacement bound:** The proof relies on the allowed `10^18` magnitude exceeding the worst possible original subarray magnitude `10^14`. If replacement values were tightly bounded, merely hitting an interval might not be enough to make its sum positive.
