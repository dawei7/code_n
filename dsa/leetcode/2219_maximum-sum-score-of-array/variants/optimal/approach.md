## General

**Each index needs one inclusive prefix and one inclusive suffix**

At index `i`, the sum score is the larger of two quantities:

$$
L_i = \sum_{t=0}^{i} \texttt{nums}[t]
$$

and

$$
R_i = \sum_{t=i}^{n-1} \texttt{nums}[t].
$$

Both sums include `nums[i]`. The task then asks for the maximum of `max(L_i, R_i)` over every valid index.

A straightforward method could build arrays containing all prefix sums and suffix sums. That would work in linear time but would store two additional length-`n` arrays. The exact solution observes that indices are processed from left to right, so only the current prefix and suffix totals are needed.

**Initialize the two running sums**

The variable `l` begins at zero because no element has yet joined the inclusive prefix. The variable `r` begins as `sum(nums)` because, before processing index zero, the suffix starting at zero is the entire array.

The answer begins as `-inf` rather than zero. Array values may be negative, and every valid score may also be negative. Initializing to zero would incorrectly return zero even though zero need not be obtainable. Negative infinity is below every finite integer score, so the first processed candidate always replaces it.

The input is nonempty by constraint, guaranteeing the loop executes and `ans` becomes a finite integer before return.

**Maintain exact meanings at the moment of comparison**

At the start of the iteration for value `x = nums[i]`, before `l += x`, `l` equals the sum of elements strictly before index `i`. At that same moment, `r` equals the sum from index `i` through the end.

The first statement in the loop, `l += x`, turns `l` into the inclusive prefix `L_i`. The suffix `r` has not yet been changed, so it is already the inclusive suffix `R_i`. Therefore, exactly when the code executes

`ans = max(ans, l, r)`,

both running values match the two sums named in the problem for the current index.

After comparison, `r -= x` removes the current element. The result is the sum from index `i + 1` through the end, which is precisely the suffix needed at the start of the next iteration.

The order of these three operations is essential. If `r` were reduced before the comparison, it would exclude `nums[i]` and represent the wrong suffix. If `l` were updated after comparison, it would exclude `nums[i]` from the prefix. The exact sequence makes both sides inclusive at the same instant.

**Why one pass visits every possible score**

For index zero, `l` becomes `nums[0]` and `r` is the full-array sum, so the method evaluates the correct prefix and suffix for index zero. After the final subtraction, the loop invariant prepares the next index.

Assume that at the start of iteration `i`, `l` is the sum before `i` and `r` is the sum starting at `i`. Adding `nums[i]` gives `L_i`, and the unchanged `r` equals `R_i`. Subtracting `nums[i]` afterward establishes the same invariant for `i + 1`. By induction, every loop iteration evaluates exactly the required two quantities for its index.

The update includes the previous `ans` and both current sums. After processing index `i`, `ans` is therefore the largest prefix-or-suffix candidate seen at any index from zero through `i`. Once the loop ends, every index has been processed, so `ans` equals the maximum sum score over the whole array.

It is equivalent to first compute `score_i = max(L_i, R_i)` and then maximize those scores. The identity

$$
\max_i \max(L_i, R_i)
= \max(L_0, R_0, L_1, R_1, \ldots)
$$

allows the code to compare `ans`, `l`, and `r` directly rather than create a separate `score_i` variable.

**Trace the running meanings**

For `nums = [4, 3, -2, 5]`, `r` starts at `10` and `l` at zero.

At index zero, `l` becomes `4` while `r` is `10`, so the best seen value becomes `10`. Subtracting `4` leaves suffix total `6` for the next index.

At index one, `l` becomes `7` and `r` is `6`. Neither exceeds `10`. Subtracting `3` leaves `3`.

At index two, `l` becomes `5` and `r` is `3`. After subtracting `-2`, `r` becomes `5`, correctly representing the final suffix beginning at index three. Subtracting a negative number increases the remaining suffix total, which ordinary arithmetic handles without a special branch.

At index three, `l` becomes `10` and `r` is `5`. The final answer remains `10`.

**Negative arrays require genuine candidates**

For `nums = [-3, -5]`, the total and initial suffix are `-8`. At index zero, the prefix is `-3` and suffix is `-8`, so `ans` becomes `-3`. At index one, the prefix is `-8` and suffix is `-5`, leaving the answer at `-3`.

This example shows why neither running sum nor `ans` can be clamped to zero. The score is defined using actual sums, not an option to select an empty prefix or suffix.

**Why prefix or suffix arrays are unnecessary**

The current prefix can be obtained from the previous prefix by adding one value. The current suffix can be obtained from the previous suffix by removing that same value after it has been evaluated. No future iteration needs an older prefix or suffix. Retaining only `l`, `r`, and `ans` captures all information required for the left-to-right sweep.

The method never modifies `nums`. Iterating `for x in nums` reads values in order, and the arithmetic variables alone represent progress.

## Complexity detail

Let `n = len(nums)`. The initial `sum(nums)` scans all `n` elements once. The subsequent loop scans the same `n` elements once more, performing a constant number of arithmetic operations and comparisons per element. Two linear passes remain `O(n)` time.

The solution stores three numeric variables, `l`, `r`, and `ans`, plus the current loop value. Their number does not depend on `n`, so auxiliary space is `O(1)`. No prefix array, suffix array, or result collection is allocated.

Python's `max` accepts the three arguments `ans`, `l`, and `r` directly. Python integers avoid overflow for sums whose magnitudes can reach roughly `10^{10}`. A fixed-width-language implementation should use a wide enough signed type because both large positive and large negative totals are possible.

## Alternatives and edge cases

- **Store prefix and suffix arrays:** Precompute every `L_i` and `R_i`, then scan their pairwise maxima. This is correct and still `O(n)` time, but it uses `O(n)` space that the running-sum sweep avoids.
- **Recompute both sums at every index:** Calling a sum operation on each prefix and suffix leads to `O(n^2)` total time because most elements are repeatedly added.
- **Use only the total and prefix:** Since `R_i = total - L_i + nums[i]` when both sums include index `i`, one could derive the suffix during the loop. This is also constant-space, but maintaining `r` explicitly makes the inclusive timing clear.
- **Initialize the answer to zero:** This fails when all valid prefix and suffix sums are negative. `-inf` or the first actual candidate is required.
- **All values negative:** The optimal score is still negative and often comes from a short prefix or suffix. The algorithm compares genuine inclusive sums without treating an empty selection as available.
- **All values positive:** Prefix sums grow and suffix sums shrink; the full-array sum appears as the suffix at index zero and the prefix at the last index, so it is the answer.
- **Single element:** After adding that element, both `l` and `r` equal it. The method returns the element itself, including when it is negative.
- **Zeros:** Zero values may leave one or both running sums unchanged. They need no special handling.
- **Subtracting a negative value:** The update `r -= x` increases `r` when `x` is negative, correctly removing a negative contribution from the next suffix.
- **Inclusive boundary at index `i`:** The current element belongs to both candidate sums. Updating `l` before and `r` after the comparison is mandatory.
- **Large-magnitude sums:** The result may exceed 32-bit range. Python is safe automatically; fixed-width implementations should use a 64-bit signed integer.
- **Input preservation:** The scan reads `nums` without changing its values or order.
