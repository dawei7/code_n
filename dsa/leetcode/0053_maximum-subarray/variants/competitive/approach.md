## General

**Maintain the best subarray ending here**

For each value `x`, `curr` is the maximum sum of a non-empty contiguous subarray whose final element is `x`. Such a subarray either begins at `x` or extends the best subarray ending at the preceding position. The update

`curr = max(curr + x, x)`

compares exactly those two possibilities.

There is no reason to extend a previous ending that is worse than `curr`: all candidate extensions add the same current value, so the largest previous ending remains largest afterward. This compresses all possible starting points into one scalar.

**Why starting over can be optimal**

If the old `curr` is negative, `curr + x` is smaller than `x`, so every subarray carrying that negative prefix is worse than the one starting at the current position. If old `curr` is positive, extending gains that positive amount. If it is zero, the two choices tie.

This local rule does not greedily throw away negative current elements. A negative `x` may be included when the accumulated positive ending remains useful. For example, after sum 4, adding `-1` yields ending sum 3, which can later grow to 6. The algorithm decides whether to discard the entire earlier ending, not whether to reject each negative value in isolation.

**Keep a separate global result**

`curr` must end at the current position and may decrease when a negative value arrives. `result` remembers the maximum `curr` ever observed. Updating `result = max(result, curr)` after every recurrence considers the best subarray for each possible right endpoint.

The final answer may therefore end before the array does. A late negative suffix can lower `curr` without erasing an earlier maximum stored in `result`.

**Negative-infinity initialization**

Both variables begin at `float("-inf")`. On the first element `x`, `curr + x` remains negative infinity, so the maximum chooses `x`. `result` then becomes `x`. This behaves like initializing from the first array value while allowing one uniform loop over all elements.

The initialization also enforces the non-empty requirement. A default of zero would incorrectly return zero for an array containing only negative values. Negative infinity cannot win against any valid integer element, so at least one real element always enters the state.

The input constraint guarantees at least one loop iteration. On an empty out-of-contract list, the method would return negative infinity rather than a meaningful subarray result.

**Trace for an all-negative input**

For `[-8, -3, -6]`, the first iteration makes both states `-8`. At `-3`, extending would give `-11`, so `curr` restarts at `-3` and `result` becomes `-3`. At `-6`, restarting gives `-6`, which does not improve the global result. The correct answer is the one-element subarray `[-3]`.

**Why the recurrence covers all contiguous subarrays**

Assume `curr` after the previous iteration is the best sum among subarrays ending there. Every subarray ending at the current position either starts at the current element or has a prefix ending immediately before it. The best extendable prefix is precisely old `curr`, so the recurrence produces the best current ending.

By induction, this holds at every index. Every non-empty contiguous subarray ends somewhere, and `result` takes the maximum of the best ending sum at every such position. Therefore, it equals the global maximum subarray sum.

**Numeric types in this source**

Although initialization uses floating-point negative infinity, after the first valid integer is processed both `curr` and `result` become integers because `max` selects `x`. Subsequent additions are integer additions. The returned value for every valid non-empty input is therefore the correct integer, not negative infinity or a rounded floating-point approximation.

## Complexity detail

The method iterates directly over `nums` once. Each element causes one addition and constant many comparisons, so time is $O(n)$.

Only `curr`, `result`, and the loop variable are stored. Direct list iteration creates no suffix copy or dynamic-programming table, so auxiliary space is genuinely $O(1)$, matching the manifest. The input is not modified.

## Alternatives and edge cases

- **First-element initialization:** Set both states to `nums[0]` and iterate from index 1 without slicing. It avoids the infinity sentinel and still uses constant space.
- **Equivalent clipped-prefix formula:** `curr = max(curr, 0) + x` expresses the same recurrence after valid initialization.
- **Track subarray boundaries:** Record a tentative start when restarting and save start/end indices when `result` improves. The problem asks only for the sum, so this state is omitted.
- **Divide and conquer:** Combine left, right, and crossing maxima for the requested follow-up. It is more subtle and typically $O(n \log n)$.
- **Prefix sums and minimum prefix:** The maximum subarray ending at a position equals the current prefix sum minus the smallest earlier prefix. This also gives linear time but uses a different invariant.
- **All-negative input:** Negative infinity prevents the empty subarray from being chosen; the largest individual value is returned.
- **One value:** The first uniform iteration replaces both infinities and returns that value.
- **Zero values:** Zero can correctly be the answer when all other choices are negative.
- **Late negative suffix:** It may lower `curr` but cannot lower `result`.
- **Empty input outside the contract:** No valid non-empty subarray exists, and the source would leave the sentinel unchanged.
- **Input preservation:** Iteration reads each integer without sorting, slicing, or assignment.
