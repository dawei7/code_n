## General

**Replace repeated range sums with a running balance**

An index `i` is a pivot when the sum of elements strictly to its left equals the sum of elements strictly to its right. Computing both sides from scratch for every index would repeat most additions and lead to quadratic time.

The exact solution instead keeps two running sums:

- `left` is the sum of elements strictly before the current index.
- `right` is adjusted to become the sum of elements strictly after the current index.

The total array sum gives an efficient starting point. Initially `left = 0` because no element lies before index `0`, while `right = sum(nums)` still includes every element. During the iteration at value `x = nums[i]`, the code first executes `right -= x`. Only then does `right` represent the strictly-right side required by the pivot definition.

**The order of updates is the algorithm**

For each index, the operations occur in this exact order:

1. Remove the current value from `right`.
2. Compare `left` and `right`.
3. If they differ, add the current value to `left` before advancing.

Moving either update can create an off-by-one-side error. If the comparison happened before subtracting `x`, the right sum would incorrectly include the pivot candidate. If `x` were added to `left` before the comparison, the left sum would also incorrectly include it.

The current element belongs to neither side. The update order makes that fact explicit.

**The loop invariant**

Immediately after `right -= x` and before the equality test:

- `left` equals `nums[0] + ... + nums[i - 1]`.
- `right` equals `nums[i + 1] + ... + nums[n - 1]`.

At the first index, `left` is correctly zero, and removing `nums[0]` from the total leaves exactly the suffix after index zero.

If index `i` is not a pivot, `left += x` prepares the invariant for the next iteration: the next index’s left side includes the current element. At the start of the next iteration, subtracting its current value from `right` similarly removes that candidate from the remaining suffix.

Thus the comparison at every index uses precisely the two sums named in the problem, not approximations or inclusive variants.

**Why returning immediately gives the leftmost pivot**

The loop visits indices in increasing order. Whenever the two side sums are equal, the current index is a valid pivot by the invariant. Returning at that moment is safe because every smaller index has already been checked and rejected. The first equality is therefore the leftmost pivot, exactly as requested.

If the loop finishes without returning, every index failed the equality condition. Returning `-1` then correctly reports that no pivot exists.

**A complete trace**

For `nums = [1, 7, 3, 6, 5, 6]`, the total is `28`.

- At index `0`, subtract `1` so `right = 27` while `left = 0`. They differ; then add `1` to the left.
- At index `1`, subtract `7` so `right = 20` while `left = 1`. They differ; then `left` becomes `8`.
- At index `2`, subtract `3` so `right = 17` while `left = 8`. They differ; then `left` becomes `11`.
- At index `3`, subtract `6` so `right = 11` while `left = 11`. The sums match, so index `3` is returned.

The value `6` at the pivot is in neither side sum. Both sides equal `11`.

**Why negative numbers need no special treatment**

The method relies only on addition, subtraction, and equality. It never assumes that prefix sums increase or that moving right makes one side larger. Negative and zero values therefore work without any change.

For example, later elements may make `right` larger after subtraction if `x` is negative, but it still remains the exact right-side sum. The invariant is algebraic, not monotonic.

**Boundary pivots are handled naturally**

At index `0`, the left side is empty and has sum zero. After subtracting the first value, the method tests whether the remaining suffix also sums to zero.

At the final index, removing its value makes `right = 0` because no elements remain after it. The method tests whether the complete preceding prefix sums to zero.

No separate branch is needed because an empty sum is represented by the initialized or exhausted running total.

**Why the result is correct**

The invariant proves that each equality comparison is exactly the pivot condition for the current index. Therefore the algorithm never returns an invalid index. It examines every index from left to right until it finds a valid one, so an existing pivot cannot be skipped; immediate return also guarantees the smallest valid index. If no equality occurs, no pivot exists. These facts establish both correctness and the leftmost requirement.

## Complexity detail

Let `n` be the number of elements.

Computing `sum(nums)` reads all `n` elements once. The following loop reads them once more, performing constant work per element. Two linear passes still combine to `O(n)` time; constants do not change the asymptotic bound.

The solution stores only `left`, `right`, the loop index, and the current value. Their number does not grow with `n`, so auxiliary space is `O(1)`. The input array is not modified, and the output is one integer.

This is asymptotically optimal in the general case. To conclude that no pivot exists, an algorithm may need to account for every input value because changing an unseen value could change a side sum.

## Alternatives and edge cases

- **Prefix-sum array:** Build cumulative sums, then compute each left and right side in constant time. This also takes `O(n)` time but uses `O(n)` additional storage. The two-running-sum method retains only the information needed at the current index.

- **Recompute both sides for each index:** Summing slices or loops around every candidate is easy to describe but costs `O(n^2)` time and may allocate temporary slices. Most additions are needlessly repeated.

- **Use the equation `2 * left + nums[i] == total`:** This algebraic form is equivalent because `right = total - left - nums[i]`. It can reduce the maintained state to a total and a left sum. The exact solution’s explicit right sum closely mirrors the problem definition.

- **Binary search:** Prefix balances are not monotone when values may be negative, so there is no ordered true/false boundary to search. A linear scan is the reliable method.

- **Pivot at index zero:** `left` is zero, and subtracting the current value leaves the sum strictly to the right. If that is also zero, the method returns zero immediately.

- **Pivot at the final index:** After the last value is removed from `right`, `right` is zero. A zero left sum makes the last index a pivot.

- **Multiple pivots:** The increasing scan and immediate return select the leftmost one.

- **Negative values:** They may cause either running sum to rise or fall, but equality still compares the exact sides. No positivity assumption is used.

- **All zeroes:** At index zero both side sums are zero, so the method returns `0`, the leftmost valid pivot.

- **No pivot:** Every index is checked exactly once, and `-1` is returned only after all comparisons fail.
