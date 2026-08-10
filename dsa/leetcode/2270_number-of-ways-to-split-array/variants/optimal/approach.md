## General

**A split needs one prefix sum and the total**

For a split after index `i`, the left part is `nums[0:i + 1]` and the right part is `nums[i + 1:n]`. If the total array sum is `s` and the current left sum is `t`, then the right sum is `s - t`.

This identity removes the need to sum both parts for every candidate. The solution computes `s = sum(nums)` once, then grows `t` as the split moves from left to right.

**Exclude the last element from split positions**

The loop is `for x in nums[:-1]`. The slice contains every array value except the final one. After processing an element `x`, the conceptual split lies immediately after that element.

Stopping before the last element is essential because the problem requires at least one value on the right. If the loop included the last element, it would test an illegal split whose right side is empty.

The source guarantees at least two elements, so `nums[:-1]` always contains at least the first element and every legal split position is represented.

**Move the current value into the left sum**

Before the first iteration, `t = 0` means no elements have entered the left side. When the loop reads `x = nums[i]`, it performs `t += x`. After this update,

$$
\texttt{t} = \sum_{j=0}^{i}\texttt{nums}[j].
$$

Since `s` is the sum of the whole array,

$$
\texttt{s} - \texttt{t}
=
\sum_{j=i+1}^{n-1}\texttt{nums}[j].
$$

The comparison `t >= s - t` therefore tests exactly the validity condition for the split after index `i`.

**Use a Boolean as a zero-or-one contribution**

In Python, a comparison returns `True` or `False`, and these behave as integers one and zero in addition. The statement

`ans += t >= s - t`

adds one when the split is valid and zero otherwise. It is a compact version of an explicit conditional increment; it does not add either sum to `ans`.

Every loop iteration corresponds to one different legal split, so adding these indicators yields the number of valid splits.

**Trace the running sums**

For `nums = [10, 4, -8, 7]`, the total is `s = 13`.

- After moving 10 left, `t = 10` and the right sum is `3`. Since `10 \ge 3`, `ans` becomes one.
- After moving 4 left, `t = 14` and the right sum is `-1`. The split is valid, so `ans` becomes two.
- After moving minus eight left, `t = 6` and the right sum is `7`. This split is invalid, so `ans` stays two.

The loop ends there because seven must remain on the right of the final legal split. The method returns two.

**Negative values require no special case**

The input may contain negative numbers. A prefix sum can decrease as the boundary moves, and a negative right sum can make the inequality easier to satisfy. The method never assumes that sums are monotone.

It simply maintains the exact arithmetic identity between total, prefix, and suffix at every position. Because the validity comparison itself is evaluated directly, negative values are handled correctly.

This is also why a two-pointer technique based on increasing sums would be inappropriate: with negative elements, moving a boundary does not guarantee either side's sum moves in one predictable direction.

**Why every valid split is counted exactly once**

The legal split indices are zero through `n - 2`. The slice iteration processes the values at exactly those indices in order. After processing index `i`, `t` is the exact left sum for that split and `s - t` is the exact right sum.

If the inequality holds, the Boolean contributes one; otherwise, it contributes zero. No index is repeated or skipped. Therefore, the final sum of indicators is precisely the count of valid splits.

**Why no prefix array is necessary**

A prefix-sum array would store the left sum for every index. This problem consumes each prefix once, in increasing order, so only the current value is needed. Adding one element to `t` advances from the previous prefix to the next.

The total `s` supplies every suffix by subtraction. This rolling-state idea provides constant-size arithmetic state even though, as discussed in the complexity section, the exact Python loop expression separately creates a list slice.

**The exact source creates a slice**

Although the algorithmic idea needs only constant-size variables, `nums[:-1]` constructs a new list containing `n - 1` references in Python. The loop then iterates over that copy.

Using `for i in range(len(nums) - 1)` with `x = nums[i]`, or iterating an appropriate lazy view, would preserve the same invariant without copying the list. The current explanation and space bound must account for what the submitted source actually does rather than silently replacing its loop.

## Complexity detail

Let `n` be the array length. `sum(nums)` takes `O(n)` time. Creating `nums[:-1]` copies `n - 1` list entries in `O(n)` time, and the loop scans those entries in another `O(n)` pass. Sequential linear passes combine to `O(n)` total time.

The numeric variables `s`, `t`, `ans`, and `x` occupy `O(1)` space. However, the exact slice `nums[:-1]` occupies `O(n)` temporary auxiliary space. Therefore, the executable source's peak auxiliary-space complexity is `O(n)`, despite the manifest's `O(1)` summary of the rolling-sum idea. Replacing the slice with index-based iteration would make that summary exact.

The total can have magnitude up to `10^{10}`. Python integers handle it automatically; a fixed-width implementation should use a 64-bit signed integer for both total and prefix sums.

## Alternatives and edge cases

- **Index-based rolling scan:** Loop through indices zero to `n - 2` without slicing. It keeps the same `O(n)` time and achieves genuine `O(1)` auxiliary space.
- **Prefix-sum array:** It computes every split correctly in `O(n)` time but intentionally stores `O(n)` cumulative sums that the rolling method does not logically need.
- **Recompute both sides for each split:** Summing ranges independently takes `O(n^2)` time.
- **Compare** `2t \ge s`: This algebraically equivalent condition can shorten the expression, but doubling may overflow a narrow fixed-width type; Python is safe either way.
- **Two pointers:** Negative values destroy the monotonicity such a method would normally rely on.
- **Exactly two elements:** There is one legal split after index zero, and the loop evaluates it once.
- **All positive values:** Prefix sums increase, but the general comparison remains unchanged.
- **All negative values:** A more negative right side may make a split valid; exact sums handle this without assumptions.
- **Zero values:** Moving zero leaves `t` unchanged, but the new boundary is still a distinct split and is tested separately.
- **Equality of sums:** The comparison uses `>=`, so equal left and right sums count as valid.
- **Final index:** It is deliberately excluded so the right part never becomes empty.
- **Boolean arithmetic:** `True` contributes one and `False` contributes zero in Python.
- **Large magnitude total:** Wide signed arithmetic is required outside Python because sums may be positive or negative.
- **Temporary slice:** The exact source copies all but one list entry; this is the reason its actual space is linear.
- **Input values:** The original elements are never changed, even though a shallow slice is created.
