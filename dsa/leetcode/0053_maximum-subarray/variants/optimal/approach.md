## General

**The global problem becomes a local ending-at-this-index question**

Trying every contiguous subarray repeats a great deal of work. A more useful state is: what is the largest sum of a non-empty subarray that must end at the current element? Call that value `f`.

When processing a new value `x`, a subarray ending at `x` has only two meaningful forms. It either starts fresh with `x`, or it extends the best subarray that ended at the previous index. Extending any worse previous ending cannot help because both choices add the same `x`.

The recurrence is therefore

$$
f_i = \max(\texttt{nums}[i], f_{i-1} + \texttt{nums}[i]).
$$

The source writes the equivalent expression `f = max(f, 0) + x`. If the previous ending sum is positive, keep it and add `x`. If it is zero or negative, discarding it is at least as good as carrying it forward, so start a new subarray at `x`.

**Why a negative prefix should be discarded**

Suppose the best subarray ending just before `x` has sum `-5`. Any future subarray that includes that prefix has a total five smaller than the same future suffix without it. Since a new contiguous subarray may start at the current index, retaining a negative ending can never improve a later result.

A positive ending is different: including it increases the total before `x`, so it is always at least as good as starting at `x`. A zero ending ties a fresh start in sum; either representation is fine because only the maximum sum, not the boundaries, is requested.

**`f` and `ans` answer different questions**

`f` is constrained to end at the current position. The maximum subarray overall may have ended earlier, especially if later numbers are very negative. `ans` stores the largest `f` seen at any processed position.

After updating `f` for `x`, the assignment `ans = max(ans, f)` considers every subarray whose right endpoint is the current index. Over the complete scan, every non-empty contiguous subarray has some right endpoint, and the best one ending there is represented by that iteration's `f`. Taking the maximum of these states yields the global answer.

**Initialization preserves the non-empty requirement**

Both `ans` and `f` start as `nums[0]`. This makes the first one-element subarray the initial candidate and guarantees the method never silently chooses an empty subarray with sum zero.

That detail is essential for an all-negative input. For `[-4, -2, -7]`, initialization gives `-4`. At `-2`, `max(-4, 0) + (-2)` becomes `-2`, and `ans` improves to `-2`. At `-7`, the ending sum becomes `-7`, while `ans` remains `-2`. Returning zero would be invalid because the requested subarray must contain at least one element.

The constraint guarantees a non-empty array, so `nums[0]` is safe. A single-element input performs no loop iterations and correctly returns that element.

**A full trace of the main example**

For `[-2,1,-3,4,-1,2,1,-5,4]`, the ending sums are `-2, 1, -2, 4, 3, 5, 6, 1, 5`. The negative ending at the beginning is discarded before 1. The run beginning at 4 then grows through `-1`, `2`, and `1` to reach 6. The later `-5` lowers the ending sum but does not lower `ans`, so the returned maximum remains 6.

This trace shows why the algorithm can include a negative element such as `-1`: a negative value need not end the current subarray if the positive accumulated prefix is still valuable. The decision is based on the total previous ending `f`, not on whether the current `x` is negative.


After processing index `i`, `f` equals the maximum sum of every non-empty subarray ending exactly at `i`. The base case is the one-element subarray at index 0. For the induction step, every ending-at-`i` subarray either consists only of `nums[i]` or extends a subarray ending at `i-1`; choosing the better of those forms proves the recurrence.

At the same point, `ans` equals the maximum sum of any non-empty subarray wholly contained in the processed prefix. Updating it with the new `f` compares the old-prefix optimum with every candidate whose right endpoint is `i`. At the final index, this prefix is the whole array, so `ans` is the required maximum.

**A Python slicing space caveat**

The greedy dynamic-programming state itself uses only two scalars. However, `nums[1:]` creates a new Python list containing every element except the first. The exact selected source therefore allocates $O(n)$ auxiliary memory, even though the manifest says $O(1)$.

Iterating by index or with `itertools.islice` would preserve the same recurrence without copying the suffix. The source remains unchanged; this document reports the concrete slice cost rather than attributing only the conceptual scalar-state bound.

## Complexity detail

The suffix slice copies $n-1$ references in $O(n)$ time, and the loop then examines each copied element once. Every iteration performs constant-time arithmetic and comparisons, so total time is $O(n)$.

`ans` and `f` use constant state, but `nums[1:]` occupies $O(n)$ additional memory. Thus the exact Python implementation uses $O(n)$ auxiliary space, not the manifest's $O(1)$. An index-based traversal would make the manifest space bound accurate.

## Alternatives and edge cases

- **Direct recurrence form:** Write `f = max(x, f + x)`. It is algebraically identical and makes the “start or extend” choice explicit.
- **In-place dynamic programming:** Add a positive previous value into each array position. It uses no extra DP array but mutates the input unnecessarily when two scalars suffice.
- **Divide and conquer:** Combine the best left subarray, best right subarray, and best crossing subarray. It satisfies the follow-up in $O(n \log n)$ time, or can be refined with segment summaries.
- **Brute force:** Extend every starting index while maintaining a running sum. It uses constant space but costs $O(n^2)$ time.
- **All values negative:** First-element initialization ensures the least negative single element wins rather than the forbidden empty sum zero.
- **Single element:** It is both the best ending sum and global result; the loop is empty.
- **Zeros:** A zero may start or extend a tied subarray. Since only the sum is returned, boundary ties do not matter.
- **Large positive run after losses:** Any negative ending prefix is discarded immediately, allowing the later run to start cleanly.
- **Input preservation:** The slice is a copy, and neither it nor the original values are modified.
