## General

**Large absolute value can come from either sign**

For a subarray sum $S$, its absolute value is large when $S$ is very positive or very negative. Tracking only the ordinary maximum subarray sum would miss a negative subarray with greater magnitude.

The exact solution runs two mirror-image forms of Kadane's algorithm simultaneously:

- `f` is the maximum sum of a non-empty subarray ending at the current element.
- `g` is the minimum, meaning most negative, sum of a non-empty subarray ending at the current element.

The answer compares `f` with `abs(g)` at every ending position. This covers both directions in which a sum can be far from zero.

**Update the maximum ending sum**

Before reading current value `x`, old `f` is the best maximum sum ending at the preceding index. A subarray ending at `x` either extends that prior subarray or starts fresh at `x`.

Extending is useful only when old `f` is positive. A zero prefix changes nothing, and a negative prefix would lower the new sum. The recurrence:

`f = max(f, 0) + x`

therefore chooses the better of continuing and restarting. Even if the result is negative, it still correctly describes a non-empty subarray ending at the current position. On the next iteration, `max(f, 0)` will discard it if it cannot help.

**Update the minimum ending sum**

The minimum state uses the symmetric reasoning. To make a sum as negative as possible, a negative preceding suffix is helpful, while a positive one should be discarded. Thus:

`g = min(g, 0) + x`.

If old `g` is negative, the current value extends it. If it is positive, zero starts a new subarray at `x`. A positive new `g` is allowed as the minimum ending sum when every candidate ending there is positive; the next iteration can discard it through `min(g, 0)`.

These assignments are independent even though they use the same current value. Each right-hand side reads its own previous state, so updating `f` before `g` does not contaminate `g`.

**Include the empty subarray**

The problem explicitly permits an empty subarray, whose sum and absolute sum are zero. The source initializes `ans = 0`. As a result, the returned value can never be negative, and zero remains available even before any non-empty candidate is examined.

With a non-empty input, the absolute value of any element is nonnegative, so allowing emptiness does not create a larger answer unless all possible non-empty sums also have magnitude zero. For an all-zero array, zero is correctly returned.

The states `f` and `g` themselves model non-empty subarrays after each element. It is only the global answer initialization that explicitly represents the optional empty choice.

**Why taking abs only for g is enough**

`f` is the greatest ending sum. When it is positive, its magnitude candidate is `f`. When `f` is negative, every subarray ending there has a negative sum, and the most negative one is `g`, so `abs(g)` dominates.

Similarly, if `g` happens to be positive, `abs(g)` is no larger than the maximum positive ending value `f`. Therefore:

`ans = max(ans, f, abs(g))`

captures the greatest magnitude without needing `abs(f)` or raw `g` as separate candidates.

**Trace the second example**

For `[2,-5,1,-4,3,-2]`, `f` initially captures positive subarrays such as `[2]`. The minimum state evolves more importantly:

- After two, `g` is two, because the only ending subarray is positive.
- At minus five, the previous positive minimum is discarded, so `g` becomes minus five.
- At one, extending remains beneficial for minimization, producing minus four.
- At minus four, it becomes minus eight.

The absolute value eight corresponds to subarray `[-5,1,-4]`. Later values do not create a greater positive or negative magnitude, so the final answer remains eight.

**Connection to prefix-sum extremes**

Any subarray sum is the difference between two prefix sums. The maximum absolute difference among prefix sums equals the global maximum prefix minus the global minimum prefix. Bidirectional Kadane reaches the same result from an ending-subarray perspective: `f` finds the greatest positive difference ending now, while `g` finds the most negative difference ending now.

The exact source does not allocate or explicitly track prefix extrema, but this equivalence helps explain why one linear pass is sufficient.

**Why the algorithm is correct**

By induction, `f` is the maximum sum among all non-empty subarrays ending at the current index: every such subarray either consists of `x` alone or extends a previous ending subarray, and only the maximum positive previous sum can improve it. The same argument with reversed comparisons proves that `g` is the minimum ending sum.

Every non-empty subarray has some ending index. At that index, the largest positive sum is represented by `f` and the most negative sum by `g`. Comparing `f` and `abs(g)` over every index, together with the empty value zero, therefore finds the maximum absolute sum over all allowed subarrays.

## Complexity detail

Let $n$ be the number of elements. The loop visits each element once and performs a constant number of additions, comparisons, and one absolute-value operation. Time complexity is $O(n)$.

Only `f`, `g`, `ans`, and the current `x` are stored. Their number is independent of $n$, so auxiliary space is $O(1)$, matching the manifest. The input array is not modified, and no prefix or DP array is created.

The largest possible magnitude may be proportional to $n$ times the element bound. Python integers handle it automatically; fixed-width implementations should use a wide enough signed integer type.

## Alternatives and edge cases

- **Prefix extrema:** Track running prefix sum plus the smallest and largest prefix values, then return their difference. It is equally $O(n)$ time and $O(1)$ space.
- **Two separate Kadane passes:** Find the maximum subarray sum normally and the minimum in another pass. It is correct but needlessly reads the array twice.
- **Negate the array:** Run ordinary Kadane on `nums` and on negated values. This captures both signs but may allocate another array unless negation is streamed.
- **Enumerate all subarrays:** Incremental sums reduce the brute force to $O(n^2)$, still too slow for $n=100000$.
- **All positive values:** `f` grows across the full array, while the negative state repeatedly restarts.
- **All negative values:** `g` accumulates the full negative run when that gives the greatest magnitude.
- **All zeros:** Both states and `ans` remain zero, matching the empty and non-empty choices.
- **Single element:** The result is that element's absolute value.
- **Alternating signs:** Each state independently decides whether its previous suffix helps its own objective.
- **Empty subarray:** `ans = 0` represents it without making `f` or `g` empty after processing an element.
- **Non-empty state semantics:** A negative `f` and a positive `g` are valid temporary states, not errors.
- **No absolute value on f:** Positive `f` is already its own magnitude; when negative, `abs(g)` is at least as large.
- **Sequential assignments:** `g` depends only on old `g`, so updating `f` first is safe.
- **Input preservation:** All state is scalar, and `nums` remains unchanged.
