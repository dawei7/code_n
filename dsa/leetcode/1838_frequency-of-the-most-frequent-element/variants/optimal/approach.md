## General

**Sort so the cheapest elements to raise are adjacent.** Operations can only increment values. If a chosen target is `T`, only values at most `T` can be changed into it. Among such values, the cheapest ones to raise are the largest values below `T`. After sorting `nums`, those candidates form a contiguous block ending at an occurrence of `T`.

For a sorted window of length `m` ending at index `i - 1`, the target is `nums[i - 1]`. The cost to raise every window value to that target is

`nums[i - 1] * m - sum of the window`.

The first term is the sum after all `m` values become the target. Subtracting their current sum gives the exact number of unit increments required.

**Prefix sums make each window cost constant-time.** After sorting in place, the code creates

`s = list(accumulate(nums, initial=0))`.

This produces a list of length `n + 1` where `s[t]` is the sum of the first `t` sorted values. Therefore, the length-`m` window ending just before `i` has sum `s[i] - s[i - m]`. The check becomes

`nums[i - 1] * m - (s[i] - s[i - m]) <= k`.

No elements are actually incremented. The formula computes how many operations would be needed.

**Check whether a frequency `m` is achievable anywhere.** The nested function `check(m)` scans `i` from `m` through `n`. Each `i` represents one sorted window `[i - m, i - 1]` and uses its last value as the target. If any window costs at most `k`, then frequency `m` is feasible and the function returns `True` immediately. If every possible window is too expensive, it returns `False`.

It is sufficient to test contiguous windows. Suppose some `m` values can be raised to target `T`, which is an existing sorted value. Replacing any selected smaller value with a larger unselected value that is still at most `T` can only reduce the cost. Repeating this exchange yields the `m` closest eligible values, which are consecutive and end at the target. Thus the scan includes an option at least as cheap as every arbitrary selection.

**Why an optimal target can be an existing value.** Raising selected elements beyond the largest selected original value spends extra operations without increasing how many elements are equal. Lowering a target is not allowed for values above it. Therefore, a best group can target its maximum original value, which appears in `nums` and is exactly the right endpoint of its sorted window.

**Feasibility is monotone in `m`.** If a window of `m` values can be made equal within budget, then a group of `m - 1` can also be made equal: remove the smallest value from that valid sorted window. The remaining values use no more operations. Hence all lengths up to the optimum are feasible, and all lengths above it are infeasible. This true-then-false pattern supports binary search.

**Binary-search the largest feasible length.** Bounds `l = 1` and `r = n` are valid because any one existing value already has frequency at least one with zero operations. While `l < r`, the code uses the upper midpoint

`mid = (l + r + 1) >> 1`.

The added one biases the midpoint upward, preventing an infinite loop when only two candidates remain. If `check(mid)` succeeds, the optimum is at least `mid` and `l` moves up. Otherwise, `mid` and every larger length are impossible, so `r = mid - 1`. When the bounds meet, `l` is the largest feasible frequency.

**Trace `[1, 2, 4]` with five operations.** Sorting changes nothing, and prefix sums are `[0, 1, 3, 7]`. For length three, the only target is four. The final sum would be twelve and the current sum is seven, so the cost is five. `check(3)` succeeds, binary search reaches three, and the method returns three.

For `[3, 6, 9]` with two operations, every length-two consecutive window costs three. `check(2)` fails, so only length one remains feasible.

**Why the returned bound is correct.** The window formula exactly characterizes the operations needed for every relevant target and group size. `check(m)` is therefore true exactly when some frequency of at least `m` can be created. Monotonicity makes binary search return the greatest true `m`, which is the requested maximum frequency.

**The exact code mutates the input.** `nums.sort()` rearranges the caller’s list. The method does not replace its values with incremented targets, but their original order is lost. This does not affect the judge’s result, though a non-mutating caller would need to sort a copy.

## Complexity detail

Sorting takes `O(n log n)` time. Prefix-sum construction takes `O(n)`. Binary search performs `O(log n)` feasibility checks, and each check may scan `O(n)` windows. The check phase is therefore `O(n log n)`, making total time `O(n log n)`.

The prefix list `s` has `n + 1` integers, so explicit auxiliary space is `O(n)`. Python’s sort may also use `O(n)` temporary memory. The binary search and each check use only scalar variables beyond those structures.

## Alternatives and edge cases

- **Sliding window:** Sorting and maintaining one moving window sum finds the answer in `O(n)` after sorting, avoiding the extra logarithmic number of scans while retaining total `O(n log n)` time.
- **Try every target and subset:** Enumerating combinations is unnecessary; sorted adjacency and the cost formula characterize the cheapest group for each target.
- **Binary search without prefix sums:** Summing every tested window separately would add another factor of `n` in the worst case.
- **Single element:** Length one is feasible with zero operations, so the returned answer is one.
- **All values equal:** A length-`n` window costs zero and the method returns `n`.
- **Zero effective budget:** Although the local constraints make `k` positive, the method would return the largest existing duplicate frequency when no increments can be spent.
- **Budget exactly equals window cost:** The `<= k` comparison accepts it, as “at most” permits using the whole budget.
- **Large gaps:** They increase the target-times-length difference and cause oversized windows to fail.
- **Duplicate targets:** Consecutive duplicates reduce the cost and are naturally included in sorted windows.
- **Only increments:** Values greater than a target cannot be lowered, which is why candidate windows end at their target rather than straddling it.
- **Input mutation:** Sorting changes order but not values. Use a sorted copy if callers need the original order.
- **Integer width:** Python safely handles `nums[i - 1] * m` and prefix sums; fixed-width languages should use 64-bit arithmetic.
