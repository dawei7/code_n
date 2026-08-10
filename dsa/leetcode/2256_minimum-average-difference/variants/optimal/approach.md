## General

**Maintain both side sums while moving the split**

At index `i`, the left part contains positions zero through `i` and the right part contains `i + 1` through `n - 1`. Recomputing both sums from scratch at every index would repeat work.

The solution begins with `pre = 0` and `suf = sum(nums)`. Before processing an element, `pre` holds the sum strictly to its left and `suf` includes it and all later elements.

For current value `x`, the code executes:

- `pre += x`, making `pre` the sum through index `i`;
- `suf -= x`, making `suf` the sum strictly after index `i`.

These are exactly the two sums required for that split.

**Compute rounded-down averages**

The left part contains `i + 1` elements, so its average is

`a = pre // (i + 1)`.

The right part contains `n - i - 1` elements. If that count is positive, its average is

`suf // (n - i - 1)`.

At the final index, the right part is empty and its average is defined as zero. The conditional assignment to `b` avoids division by zero and implements that rule directly.

All input values and sums are nonnegative, so Python floor division `//` is exactly the stated rounding down.

**Evaluate the average difference**

`t := abs(a - b)` calculates the absolute difference and stores it in `t` through the assignment expression. The method compares `t` with the smallest value `mi` seen so far.

If `t < mi`, both `ans` and `mi` are updated. A strict comparison is essential for tie-breaking: when a later index has the same minimum difference, it does not replace the earlier `ans`. Since indices are scanned from zero upward, the retained index is the smallest minimum.

**Why the running sums are exact**

Initially, `pre + suf` equals the total array sum. Moving `x` from `suf` to `pre` preserves this equality and moves exactly the current element across the conceptual split.

After the updates at index `i`:

$$
\texttt{pre} = \sum_{j=0}^{i} \texttt{nums}[j]
$$

and

$$
\texttt{suf} = \sum_{j=i+1}^{n-1} \texttt{nums}[j].
$$

Thus, both integer divisions use the correct numerators and denominators for every index.

**Why the chosen index is globally correct**

The loop evaluates every valid split index exactly once. For each one, the previous argument proves `t` equals its defined average difference.

`mi` begins at infinity, so index zero always establishes the first real candidate. After each iteration, `mi` is the smallest difference in the processed prefix of indices, and `ans` is its earliest index. The update rule preserves this invariant.

After index `n - 1`, all choices have been processed, so `ans` is the smallest index attaining the global minimum.

**Trace the final-index rule**

For the last index, `pre` is the total sum and `suf` is zero. Left average is total divided by `n`, while right average is explicitly zero. This matches the problem's empty-average convention.

For a one-element array, the only iteration uses that same rule. The method returns index zero.

**Why no prefix array is needed**

Only the current prefix sum is used before moving to the next index. The total suffix can be maintained by subtraction. Storing all prefix or suffix sums would consume linear space without making the per-index computation faster.

The input list is read only.

**The order of the two sum updates matters**

The loop is evaluating a split that includes `nums[i]` on the left. Therefore, the current value must be added to `pre` and removed from `suf` before either average is calculated. Computing the averages first would instead describe the boundary before index `i`: the left side would omit the current element and the right side would still contain it. At `i = 0`, that mistaken order would even try to average an empty left part. Thinking of each iteration as physically moving one value across the split makes the required order easier to remember.

There is also no risk that updating `pre` changes the value needed for `suf`. Both updates use the same current value `x`, and subtraction transforms the old suffix sum into the exact remaining-right sum. This is why one total sum and one running prefix are sufficient.

## Complexity detail

`sum(nums)` scans `n` elements once. The main loop scans them once more and performs constant arithmetic per index. Total time is `O(n)`.

The method stores a fixed collection of numeric variables: `pre`, `suf`, `n`, `ans`, `mi`, and current values. Auxiliary space is `O(1)`.

The total sum can reach `10^{10}`. Python integers represent it safely; a fixed-width implementation should use a sufficiently wide type.

## Alternatives and edge cases

- **Recompute both sums per index:** It is direct but takes `O(n^2)` time.
- **Prefix and suffix arrays:** They give constant-time split sums after preprocessing but use `O(n)` extra space.
- **Floating-point averages:** They are unnecessary and can disagree with required integer rounding. Floor division must happen before subtraction.
- **Round the final difference:** That changes the operation order; each average is rounded down separately.
- **Single element:** The right average is zero and index zero is returned.
- **Final index:** Explicit empty-side handling avoids division by zero.
- **Difference tie:** Strict improvement preserves the earlier index.
- **Zero values:** Running sums and averages handle them naturally.
- **Minimum difference zero:** It is unbeatable, though the scan continues and retains its first occurrence.
- **Large total sum:** Wide integer arithmetic is required in fixed-width languages.
- **Nonnegative guarantee:** It makes `//` match ordinary truncating integer division for these sums.
- **Input preservation:** No array element is changed.
