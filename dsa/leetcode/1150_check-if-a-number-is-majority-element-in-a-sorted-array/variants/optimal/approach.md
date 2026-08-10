## General

**Exploit the fact that equal values are contiguous**

Because `nums` is sorted in non-decreasing order, every occurrence of `target` appears in one consecutive block. Values smaller than `target` come before that block, and values larger than `target` come after it.

If the block starts at index `left` and ends just before index `right`, then its number of elements is `right - left`. The problem therefore reduces to locating the two boundaries of the target block, which binary search can do without scanning the whole array.

**Find the left boundary**

`bisect_left(nums, target)` returns the first insertion position at which `target` could be placed while keeping the array sorted. Equivalently, it is the first index whose value is greater than or equal to `target`.

If `target` is present, this position is its first occurrence. If it is absent, the position is where it would begin if inserted. It may be zero, somewhere in the middle, or `len(nums)` when every value is smaller.

For example, in `[2, 4, 5, 5, 5, 6]` with target five, `bisect_left` returns two, the index of the first five.

**Find the right boundary**

`bisect_right(nums, target)` returns the first insertion position after all existing values equal to `target`. Equivalently, it is the first index whose value is strictly greater than `target`.

For the same example, it returns five. Indices two, three, and four contain the target, so `right - left = 5 - 2 = 3`.

Using a half-open interval `[left, right)` is convenient: the start is included, the end is excluded, and subtraction gives the count directly. There is no extra `+ 1` and no risk of an off-by-one error around the last occurrence.

**Why absence needs no special test**

If `target` does not appear, there is no interval of equal target values. Both insertion routines return the same boundary: the location between values smaller than the target and values larger than it. Their difference is zero.

For example, with `nums = [1, 3, 7]` and target five, both boundaries are index two. The computed occurrence count is zero, which certainly cannot be a majority. The solution therefore does not need to check `left < len(nums)` or compare `nums[left]` with `target`.

**Apply the strict-majority definition**

A majority must appear more than half the array length, not at least half. With integer arithmetic, the exact condition is

`right - left > len(nums) // 2`.

For odd length `n`, `n // 2` is the greatest integer below half, so a count greater than it is at least `(n + 1) / 2`. For even length, a count equal to `n / 2` is rejected because the comparison is strict.

This matches the second example: target `101` occurs twice in an array of length four. The threshold `len(nums) // 2` is two, and `2 > 2` is false.

**Why the algorithm is correct**

Sorted order guarantees that the target occurrences, if any, occupy exactly the half-open interval beginning at the first value at least `target` and ending at the first value greater than `target`. Those definitions are exactly what `bisect_left` and `bisect_right` return.

Consequently, `right - left` is neither an estimate nor a candidate count; it is the exact frequency of `target`. The final comparison is the definition of a majority element written with integer division. The method returns true if and only if the exact frequency is strictly greater than half the array length.

The approach uses the sorted property fully. It avoids examining elements that binary search can eliminate in halves and remains correct for target blocks at either boundary of the array.

**How the two searches narrow the array**

Each bisection repeatedly inspects a middle position and discards about half the remaining search range. The left search moves toward earlier equal values, while the right search moves past equal values. Though their boundary conditions differ, both converge on insertion positions in the range zero through `n`, including the legal one-past-the-end position.

Using the library functions also makes their well-tested boundary semantics explicit. A hand-written search would need to preserve the same distinction between “first greater than or equal” and “first strictly greater.”

## Complexity detail

Let `n` be `len(nums)`. `bisect_left` takes `O(log n)` time, and `bisect_right` takes `O(log n)` time. Two logarithmic searches are still `O(log n)` because constant factors are omitted. The subtraction and comparison are constant time.

The bisection functions use index variables rather than allocating arrays or slices. The solution stores only `left` and `right`, so its auxiliary space complexity is `O(1)`.

The input array is not copied or modified.

## Alternatives and edge cases

- **Linear frequency count:** Scanning the entire array and counting target values is simple and uses `O(1)` space, but takes `O(n)` time and ignores sorted order.
- **Use a general counter map:** Building frequencies for all values costs `O(n)` time and `O(n)` space even though only one target is queried.
- **One binary search plus a majority offset:** After finding the first occurrence, one can test whether the element `n // 2` positions later is still the target. This uses one search but requires careful bounds handling.
- **Search for `target + 1`:** For bounded integers, a left boundary of `target + 1` can act as the right boundary. `bisect_right` states the intention directly and avoids arithmetic concerns.
- **Target absent:** Both insertion points coincide, producing frequency zero without indexing the array.
- **Target smaller than every value:** Both boundaries are zero.
- **Target larger than every value:** Both boundaries are `n`, the legal insertion position after the array.
- **Target fills the array:** `left` is zero, `right` is `n`, and every nonempty input correctly reports a majority.
- **Exactly half the array:** The strict `>` comparison returns false, as required.
- **Odd array length:** Integer floor division produces the correct threshold for a strict majority.
- **One-element array:** If the sole value is the target, the count is one and the threshold is zero; otherwise the count is zero.
- **Duplicates outside the target block:** They do not affect either target boundary because binary search compares only against `target`.
