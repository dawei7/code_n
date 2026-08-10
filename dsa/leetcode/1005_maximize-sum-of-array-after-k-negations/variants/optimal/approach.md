## General

**Measure what one negation does to the sum**

Replacing value `x` by `-x` changes the total sum by

`(-x) - x = -2x`.

For a negative `x`, this change is positive, and a more negative value gives a larger improvement. For a positive `x`, the change is negative, and the smallest absolute value causes the smallest loss. Negating zero changes nothing.

These observations completely determine the greedy order.

**Use the small value range as a counting table**

Values lie between negative one hundred and positive one hundred. `Counter(nums)` stores how many occurrences of each value exist.

Instead of sorting up to ten thousand elements, the code scans the fixed numeric range from `-100` through `-1`. This visits negative values from most negative to least negative, exactly the order of greatest possible sum improvement.

The counter also permits flipping many equal occurrences in one operation on their frequency rather than processing them individually.

**Flip the most negative available values first**

For current negative value `x`:

`m = min(cnt[x], k)`

is how many occurrences can and should be negated before either that value is exhausted or no operations remain.

The updates

`cnt[x] -= m` and `cnt[-x] += m`

move those occurrences to their positive counterpart. Then `k -= m` consumes the operations.

If `k` reaches zero, the loop breaks because every required operation has been assigned.

**Why this greedy order is optimal**

Suppose two remaining negative values satisfy `x < y < 0`, so `x` has larger magnitude. Flipping `x` improves the sum by `-2x`, while flipping `y` improves it by `-2y`. Since `-2x > -2y`, choosing `x` first is never worse.

An exchange argument makes this global: if a proposed optimal plan flips `y` but leaves the more negative `x` unchanged, swap that choice to `x`. The operation count stays the same and the final sum increases or stays equal. Repeating the exchange yields a plan that flips negatives in ascending numeric order, matching the scan.

No positive value should be flipped while an unflipped negative remains, because the former decreases the sum while the latter increases it.

**Only the parity of leftover operations matters**

After all negative values are made nonnegative, there may still be operations to perform because the problem requires exactly `k` negations.

Negating the same index twice restores its original value. Therefore, any even number of leftover operations can be spent in canceling pairs without changing the array or sum. Only an odd remainder forces one net sign change.

The code checks this with `k & 1`.

It does not need to simulate the canceling pairs or reduce `k` explicitly; their net effect is known to be zero.

**Use zero to absorb an odd leftover operation**

If `cnt[0] > 0`, negating zero still produces zero. An odd leftover operation can be used on that zero, and any remaining even operations cancel in pairs.

This is why the odd-remainder correction runs only when `cnt[0] == 0`. When zero exists, leaving the counter unchanged already represents the best possible final multiset.

**Otherwise negate the smallest positive value**

If an odd operation remains, no negative values remain, and no zero exists, some positive value must become negative. The resulting loss for positive `x` is `2x`, so the smallest positive value minimizes the damage.

The loop from one through one hundred finds the first positive count, moves one occurrence from `x` to `-x`, and stops. That single frequency change represents the one unavoidable net negation.

**Trace `[2, -3, -1, 5, -4]` with `k = 2`**

The negative scan encounters `-4` before `-3` and `-1`. It moves one `-4` to four and consumes one operation. It then moves `-3` to three and consumes the second.

The remaining values are equivalent to `[2, 3, -1, 5, 4]`, whose sum is thirteen. Flipping `-1` instead of either larger-magnitude negative would give a smaller improvement.

**Trace leftover operations**

For `[4, 2, 3]` with one operation, there are no negatives or zeros. The odd remainder forces one loss, so the smallest positive value two is changed to negative two. The sum becomes five.

For `[3, -1, 0, 2]` with three operations, first flip `-1` to one. Two operations remain and can cancel on any index, or be applied to zero twice. The maximum final sum is six.

If only one operation remained after negatives but zero existed, applying it to zero would also preserve the sum.

**Compute the sum from final frequencies**

The expression

`sum(x * v for x, v in cnt.items())`

multiplies each numeric value by its final occurrence count. Counter keys whose count fell to zero contribute zero and need not be deleted.

**Why the result is globally maximal**

Every beneficial negative flip is chosen from greatest improvement to smallest. Exchange reasoning proves no other selection of the same number of beneficial flips gives a larger sum.

Once all numbers are nonnegative, even remaining operations have no net effect, while an odd remainder must negate some final value. Zero gives zero loss; otherwise, the smallest positive magnitude gives the least possible loss. These cases exhaust all legal operation counts, so the final frequency multiset has maximum sum.

## Complexity detail

Let `N` be the array length.

Building the counter and computing the final weighted sum take `O(N)` time in the general accounting. The two value-range scans examine at most 100 negative and 100 positive values, fixed constants. Total time is `O(N)`.

Because values come from only 201 possible integers, the counter contains at most 201 keys. Auxiliary space is therefore `O(1)` relative to `N`. The input list is not modified.

## Alternatives and edge cases

- **Sort the array:** Sort ascending, flip negatives while operations remain, then adjust the smallest absolute value for odd parity. It is straightforward but costs `O(N \log N)`.
- **Min-heap:** Repeatedly negate the current minimum and push it back. This costs `O((N + k)\log N)` and may process canceling flips individually.
- **Flip an arbitrary negative first:** It can waste a limited operation on a small improvement while a larger-magnitude negative remains.
- **More operations than elements:** Reusing indices is allowed; after beneficial flips, only leftover parity matters.
- **Zero present:** It absorbs any odd leftover operation with no sum change.
- **All positive values:** Even `k` leaves the maximum sum unchanged through paired flips; odd `k` negates the smallest positive.
- **All negative values with limited `k`:** The method flips the `k` largest magnitudes.
- **`-100` and `100`:** Both endpoints are included by the fixed range scans.
- **Zero-count Counter keys:** They do not affect the weighted sum and keeping them is harmless.
- **Exact operation count:** Canceling pairs justify why unused even operations need no explicit simulation.
- **Input preservation:** Frequency movement produces the result without rewriting `nums`.
