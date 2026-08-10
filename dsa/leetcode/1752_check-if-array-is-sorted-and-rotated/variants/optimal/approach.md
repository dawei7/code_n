## General

**Look at the array as a circle**

Rotating an array changes where the linear representation begins, but it does not change the cyclic order of its elements. If a non-decreasing array is placed around a circle, almost every adjacent pair satisfies “previous value is less than or equal to next value.” There can be only one place where a larger value is followed by a smaller value: the wrap from the sorted array's end back to its beginning.

The exact solution counts these strict decreases around the entire cycle and returns true when there is at most one.

Its whole condition is:

`sum(nums[i - 1] > x for i, x in enumerate(nums)) <= 1`.

Although compact, this line contains the complete circular check.

**Understand the generator's adjacent pairs**

`enumerate(nums)` produces each current index `i` and value `x = nums[i]`. The expression `nums[i - 1]` accesses the preceding value.

For ordinary indices `i > 0`, this compares `nums[i - 1]` with `nums[i]`. At `i = 0`, Python index minus one refers to the last element, so the comparison is `nums[n - 1] > nums[0]`. That special first iteration supplies the circular pair connecting the end back to the beginning.

Each comparison returns a Boolean. In Python arithmetic, `True` contributes one and `False` contributes zero. Applying `sum` therefore counts how many cyclic adjacent pairs are strict decreases.

No array slice, rotated copy, or explicit counter variable is needed.

**Why the comparison is strict**

The original array is sorted in non-decreasing order, not strictly increasing order. Equal adjacent values are valid. Consequently, a break occurs only when the preceding value is greater than the current value.

Using `>=` would incorrectly count equal neighbors as breaks and reject arrays containing duplicates. The strict `>` exactly captures a violation of non-decreasing order.

**Why a valid rotation has at most one decrease**

Begin with a non-decreasing array `A`. All its ordinary adjacent pairs satisfy `A[r] <= A[r + 1]`. After rotating, those same neighbor relationships remain present around the cycle. Only the chosen linear cut changes.

Around the circle, the single potential decrease is between a largest end value and a smallest beginning value. If all values are equal, even that pair is not a strict decrease, so the count is zero. Otherwise the count is one.

For `[3,4,5,1,2]`, the cyclic comparisons are two-to-three, three-to-four, four-to-five, five-to-one, and one-to-two. Only five-to-one decreases, so the sum is one and the function returns true.

For an already sorted nonconstant array such as `[1,2,3]`, ordinary pairs increase, but the circular comparison from three back to one is one decrease. This still passes, corresponding to a rotation by zero.

**Why at most one decrease is also sufficient**

Suppose the cyclic count is zero. Then every circular neighbor is non-decreasing. This is possible only when all values are equal, and the given order is already sorted.

Suppose the count is exactly one, at the transition from index `r` to the next cyclic index. Start reading the circle immediately after that decrease. From there, every adjacent pair until `r` is non-decreasing because no second decrease exists. The resulting linear sequence is sorted in non-decreasing order.

The input `nums` is precisely a rotation of that sequence: it contains the same circular order but starts at index zero instead of immediately after `r`. Therefore one or zero cyclic decreases is not merely necessary; it guarantees that some sorted original array can rotate to `nums`.

If there are two or more decreases, choosing any one cut can hide at most one of them at the linear boundary. Another decrease remains inside the purported original order, so no rotation can make it sorted.

**Trace an invalid example**

For `[2,1,3,4]`, the transition two-to-one is a decrease. The circular transition four-to-two is another decrease. The Boolean generator therefore contributes two true values.

Cutting after two would leave four-to-two inside the sorted reading; cutting after four would leave two-to-one inside it. No other cut helps, so the result false is correct.

**Why the one-line result is correct**

The generator examines every cyclic adjacency exactly once, including the wrap through negative indexing. Its sum is the exact number of violations of cyclic non-decreasing order.

A rotated non-decreasing array has at most one such violation, and any cyclic sequence with at most one violation becomes non-decreasing when cut after that violation. Hence comparing the count with one returns true exactly for the required arrays.

## Complexity detail

Let $n$ be the array length. `enumerate` visits every element once. Each iteration performs one indexed lookup, comparison, and Boolean addition, all constant-time operations. Total time is $O(n)$.

The generator is lazy and does not create a list of $n$ Booleans. Apart from iteration state and the running sum, only a constant amount of memory is used. Auxiliary space is therefore $O(1)$, matching the manifest.

The input is not sorted, copied, rotated, or modified. Python's negative-index lookup is constant time.

## Alternatives and edge cases

- **Try every rotation:** Construct or inspect all $n$ rotations and test each for sorting, which can take $O(n^2)$ time.
- **Compare with a sorted copy:** Sorting costs $O(n\log n)$ and checking rotations can still be quadratic without a string-matching technique.
- **Find a minimum value and scan:** Duplicated minimum values make choosing the correct starting occurrence less direct than counting decreases.
- **Explicit loop counter:** It is equivalent and can return early after a second decrease; the generator version always completes the sum.
- **One element:** Its predecessor through index minus one is itself, so the count is zero.
- **All equal values:** Strict comparison reports no decreases, correctly accepting duplicates.
- **Already sorted array:** The only possible decrease is the circular last-to-first pair, so zero rotation is accepted.
- **Rotation at a duplicate boundary:** Equal values do not create an extra decrease.
- **Two decreases:** No single rotation boundary can eliminate both, so the array is rejected.
- **Strict versus non-decreasing:** The `>` operator is essential; `>=` would be wrong for duplicates.
- **Circular pair:** Omitting `nums[-1] > nums[0]` would accept some invalid arrays with an internal decrease plus a bad wrap.
- **Boolean summation:** Python treats true as one and false as zero, so `sum` is a count.
- **Input preservation:** The method derives a property of the current order without changing `nums`.
- **Value bounds:** The algorithm uses comparisons only, so numeric magnitude does not affect it.
