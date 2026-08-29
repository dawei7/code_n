## General

**Every valid pair has one of two orders**

The two chosen subarrays cannot overlap. Therefore, either the `firstLen` subarray is entirely before the `secondLen` subarray, or the `secondLen` subarray is entirely before the `firstLen` subarray.

The optimal solution performs one linear sweep for each order. Within a sweep, it fixes the start of the right-hand subarray and remembers the best compatible left-hand subarray seen so far.

This avoids testing every pair of windows. There can be `O(N)` possible positions for each length, and comparing all pairs would be quadratic. A running maximum compresses all earlier compatible choices into one value.

**Prefix sums make every window sum constant time**

The line `s = list(accumulate(nums, initial=0))` builds an array of length `n + 1` where `s[i]` is the sum of `nums[0:i]`. The initial zero is essential because it makes windows starting at index zero use the same formula as every other window.

The sum of the half-open subarray `nums[l:r]` is

`s[r] - s[l]`.

Everything before `l` appears in both prefix sums and cancels. The method can therefore evaluate any fixed-length window in constant time without summing its elements again.

**First sweep: `firstLen` before `secondLen`**

The variable `i` is the split point and the start of the current right-hand `secondLen` window. It begins at `firstLen`, the earliest index that leaves enough room for a full `firstLen` window on the left.

At each iteration, the window

`nums[i - firstLen:i]`

is the newest length-`firstLen` window ending at or before the split. Its sum is `s[i] - s[i - firstLen]`. The variable `t` retains the maximum sum of every such left window considered so far.

The current right window is

`nums[i:i + secondLen]`

with sum `s[i + secondLen] - s[i]`. It starts exactly at the split, while every window represented by `t` ends at or before the split. They cannot overlap. A gap is allowed when the best left window ended before `i`.

The candidate total is the best compatible left sum `t` plus the current right sum. `ans` keeps the maximum candidate.

The loop condition `i + secondLen - 1 < n` is equivalent to `i + secondLen <= n`. It ensures that the current right window's last index remains inside the array.

**Why updating `t` before `ans` is correct**

At split `i`, a left window ending exactly at `i` is compatible with a right window starting at `i`. Adjacent subarrays do not overlap. Therefore, the newest left window must be included in `t` before the current pair is evaluated.

If the update occurred afterward, the algorithm would incorrectly exclude touching windows and could miss the optimum.

**Second sweep: reverse the lengths**

The first sweep cannot represent a solution in which the `secondLen` window comes first. The exact code resets `t = 0` and starts `i = secondLen`.

Now `t` tracks the best length-`secondLen` window ending at or before `i`, and the current right window has length `firstLen`. The formulas are the same with the roles exchanged:

- Left candidate: `s[i] - s[i - secondLen]`.
- Right candidate: `s[i + firstLen] - s[i]`.

Taking the maximum across both sweeps covers every possible non-overlapping arrangement.

The algorithm does not simply swap variable names conceptually; it reruns the scan because a different length on the left produces a different set of best prefix windows.

**Trace the first example**

Use `nums = [0,6,5,2,2,5,1,9,4]`, `firstLen = 1`, and `secondLen = 2`.

In the first sweep, one-element windows are on the left and two-element windows are on the right. As `i` advances, `t` becomes the largest single value before the current pair. This order can find choices such as an early one-element window followed by a later pair.

The optimal example has the opposite order: pair `[6,5]` comes before single value `[9]`. The second sweep tracks the best length-two window in the prefix. By the time the right one-element window reaches nine, `t` is eleven from `[6,5]`. Their total is twenty, and `ans` records it.

The elements between those windows do not matter. Subarrays must be contiguous individually, but the two selected subarrays may have an unused gap between them.

**Why `t` is a sufficient summary**

For a fixed right window beginning at `i`, only two facts about a left window matter:

- It must end no later than `i`.
- Its sum should be as large as possible.

Its exact starting index has no effect on compatibility once its end is known to be within the prefix. Therefore, all eligible left windows can be replaced by their maximum sum `t`. As `i` increases, one new left window becomes eligible, so `t` can be updated incrementally.

**Why the algorithm finds the optimum**

Take any valid pair. If the length-`firstLen` window is first, let `i` be the start of its length-`secondLen` window. During the first sweep at that `i`, `t` includes every length-`firstLen` window ending no later than `i`, including the chosen one. The candidate considered by the algorithm is therefore at least as large as this pair.

If the length-`secondLen` window is first, the same argument applies to the second sweep. Thus every valid pair is matched or improved by some candidate.

Conversely, every candidate constructed by either sweep combines a left window ending at or before `i` with a right window starting at `i`. It is a valid non-overlapping pair with the required lengths. The maximum candidate is therefore neither below nor above the true optimum; it equals it.

**Why zero initialization is safe**

Both `t` and `ans` begin at zero. The source guarantees `nums[i] >= 0`, so every window sum is nonnegative. Before `ans` uses `t` in either loop, `t` is updated with a real left window. No empty window is selected.

If negative array values were allowed, a general implementation should initialize running maxima to negative infinity rather than zero. Under this contract, zero is safe and simpler.

## Complexity detail

Let `N = len(nums)`. Building prefix sums takes `O(N)` time. Each of the two sweeps advances `i` monotonically and performs constant work per position, so together they take `O(N)` time. Total time is `O(N)`, matching the manifest.

The prefix-sum list contains `N + 1` integers and uses `O(N)` space. All other variables are scalars, and the generator used by `accumulate` is immediately materialized only into that one list. Total auxiliary space is `O(N)`.

A sliding-window variant can reduce auxiliary space by maintaining current sums directly, but the prefix array makes both directional formulas concise and reliable.

## Alternatives and edge cases

- **Try every pair of window starts:** Prefix sums make each sum constant time, but there are still `O(N^2)` pairs to test. The running best compatible left window removes that quadratic pairing.
- **Precompute best-left and best-right arrays:** Store maximum fixed-length window sums for every prefix and suffix, then combine at split points. This is also `O(N)` time and `O(N)` space but requires more arrays.
- **Sliding windows without prefix sums:** Maintain the current right-window sum and the best eligible left-window sum as the split advances. It can achieve `O(1)` auxiliary space but has more update bookkeeping.
- **Run only one order:** This misses cases such as the first example, where the `secondLen` window appears before the `firstLen` window. Both sweeps are necessary unless the lengths and logic are handled symmetrically in another way.
- **Equal lengths:** The two sweeps become equivalent, but running both remains correct and only changes a constant factor.
- **Adjacent windows:** An end index equal to the other window's start is non-overlapping under half-open indexing and is intentionally allowed.
- **Unused gap:** The running maximum may come from a window ending well before `i`. Gaps are permitted, so retaining that earlier maximum is correct.
- **Lengths fill the entire array:** There is only one split for each order. The loops evaluate the two possible placements, which may have the same total.
- **All zeroes:** Every candidate sum is zero, and the initial answer remains the correct value zero.
- **Nonnegative-value dependency:** Zero initialization relies on the source constraint. With negative values, use a negative-infinity sentinel.
- **Prefix index zero:** `initial=0` makes `s[firstLen] - s[0]` correctly evaluate a window beginning at the array's first element.
- **Loop boundary:** The condition permits a right window ending exactly at `n` in half-open form and rejects any window that would extend beyond the array.
- **Subarray versus subsequence:** Each chosen block is contiguous because every sum uses one uninterrupted prefix interval. Only the gap between the two blocks may be skipped.
