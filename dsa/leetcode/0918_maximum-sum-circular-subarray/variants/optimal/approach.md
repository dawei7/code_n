## General

A maximum circular subarray has one of two forms:

1. It does not wrap, so it is an ordinary contiguous subarray.
2. It wraps from the end to the beginning. Equivalently, it contains the whole array except for one contiguous middle segment.

The solution computes the best ordinary subarray and the best valid complement form in one prefix-sum pass.

Let `s` be the current prefix sum. For prefix sums $P_0=0,P_1,\ldots$, any subarray sum ending at the current position is

$$
P_r-P_\ell
$$

for an earlier prefix $P_\ell$.

**Maximum ordinary subarray.** `pmi` stores the smallest prefix sum seen before the current prefix. Then `s - pmi` is the largest subarray sum ending here. Maximizing it into `ans` over all endpoints gives the ordinary maximum-subarray result.

The update order matters: calculate `s - pmi` before adding current `s` to `pmi`. This guarantees a nonempty subarray because the subtracted prefix occurs strictly before the current one.

**Minimum segment to exclude.** A wrapping subarray uses a suffix plus a prefix. Its sum equals total array sum minus the contiguous middle segment it skips. To maximize the wrapping sum, minimize that excluded segment.

`pmx` stores a largest earlier prefix sum, so `s - pmx` is the smallest subarray sum ending at the current position. `smi` retains the minimum such segment.

However, `pmx` initializes to negative infinity rather than zero. This deliberately excludes subarrays that start at index zero from the minimum-segment candidates. Removing a prefix would leave an ordinary suffix, which is already covered by `ans`. More importantly, for an all-negative array it prevents selecting the entire array as the removed segment and falsely producing an empty circular subarray with sum zero.

After the first element is processed, `pmx` receives its prefix sum. Later minimum segments may start at index one or beyond and may end at the last element. Their complements always contain at least the initial element and are nonempty.

At loop completion, `s` is the total sum. The best complement candidate is

$$
s-\text{smi}.
$$

The answer is the larger of this wrapping candidate and ordinary `ans`.

During the loop, `pmi` and `pmx` summarize prefix sums only; they do not depend on array values being positive. A very negative prefix becomes useful to the ordinary maximum calculation, while a very positive prefix becomes useful for discovering a negative segment to exclude. This symmetry is why one pass can maintain both objectives with four scalar extrema.

**Example `[5,-3,5]`.** The ordinary maximum is 7 from the full array or a suitable prefix/suffix. The minimum removable middle segment is `[-3]` with sum $-3$. Total is 7, so the wrapping sum is $7-(-3)=10$, corresponding to the final 5 followed circularly by the first 5.

**All-negative protection.** For `[-3,-2,-3]`, the best ordinary nonempty subarray is `[-2]`. A standard “total minus global minimum subarray” formula could remove the whole array and yield zero unless guarded. Here the restricted `smi` cannot represent the entire array from index zero, so the complement remains nonempty. Taking the max still returns $-2$.
Every legal circular subarray either crosses the array boundary or it does not. Noncrossing choices are all considered by the minimum-prefix calculation. A crossing choice's omitted elements form one contiguous nonempty middle segment; minimizing that segment maximizes its complement. Conversely, every allowed omitted segment produces a legal wrapping complement using each array position at most once. Taking the maximum of the two classes is therefore exhaustive and correct.

## Complexity detail

Let $n$ be the array length. The loop performs constant work per element.

- **Time complexity:** $O(n)$.
- **Space complexity:** $O(1)$ auxiliary space.

Only running prefix extrema, best sums, and total prefix sum are stored. No duplicated circular array or prefix array is allocated.

## Alternatives and edge cases

- **Kadane maximum plus Kadane minimum:** Compute ordinary maximum, total minus global minimum, and explicitly guard the all-negative case. This is the common equivalent formulation.
- **Duplicate the array:** Searching all length-at-most-$n$ subarrays in a doubled array needs more complex window logic and extra storage if materialized.
- **Try every circular start:** Extending up to $n$ positions from every start costs $O(n^2)$.
- **Return total minus minimum only:** It fails when the optimal subarray is nonwrapping or when removing everything would create an illegal empty result.
- **One element:** `smi` remains infinity, so only ordinary `ans` can win and the element is returned.
- **All positive:** The ordinary full array is optimal; removing a positive segment cannot improve it.
- **All negative:** The largest single value is returned, never zero.
- **Wrapping optimum:** A negative middle segment can be excluded to join a positive suffix and prefix.
- **Zero values:** Nonempty zero-sum subarrays are handled normally.
- **Prefix update order:** Candidate sums must be computed before current prefix extrema update to prevent empty segments.
- **`pmx = -inf`:** This is intentional, not symmetric with `pmi = 0`; it keeps the complement candidate nonempty and avoids redundant prefix removal.
- **No element reuse:** Complementing one contiguous middle segment produces a suffix-plus-prefix path that uses each index at most once.
