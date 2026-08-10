## General

**Sort so the median has a fixed index.** The source sorts `nums` in nondecreasing order and defines `m = n >> 1`, which is integer division by two. For odd $n$, this is the unique middle index. For even $n$, it is the second of the two central indices, matching the contract's instruction to use the larger median.

After sorting, making the median equal to `k` is an order-statistics requirement. It is not enough merely to change the current middle value: values on the relevant side may also have to cross `k` so that `k` remains at index `m` after all modifications.

**Always pay for the middle element.** `ans` starts as `abs(nums[m] - k)`. Increasing or decreasing an integer by one costs one operation, so this is the exact unavoidable cost to move the current median value to `k`.

The direction of that move determines which other elements can violate the desired order.

**When the current median is above `k`.** If `nums[m] > k`, setting only the middle element to `k` may leave earlier values also above `k`. Then fewer than $m+1$ values would be at most `k`, and the sorted upper median could remain greater than `k`.

The source scans left from `m - 1`. Every value greater than `k` must be lowered to at most `k`. Lowering it exactly to `k` costs `nums[i] - k` and is cheapest; lowering farther would add useless operations.

As soon as the scan finds `nums[i] <= k`, it breaks. Sorting guarantees that all still earlier values are also at most `k`, so none requires modification.

After this work, positions zero through `m` can all be arranged at or below `k`, with the middle changed to exactly `k`. Values to the right may remain larger without preventing `k` from occupying the median index.

**When the current median is below `k`.** The symmetric issue lies on the right. Values after `m` that are still below `k` would leave too many small values and prevent `k` from becoming the upper median. The source scans right and raises each such value exactly to `k`, paying `k - nums[i]`.

It stops at the first `nums[i] >= k`. All later values are at least as large because the array is sorted, so the remaining suffix is already safe.

If `nums[m] == k`, the source enters this `else` branch, but the very next right value, when present, is at least `k` and causes an immediate break. Thus no unnecessary cost is added.

**Why the opposite side never needs changes.** When lowering an excessive median, elements to its right are allowed to stay above `k`; a median only requires enough elements on the lower side. When raising a deficient median, elements to its left are allowed to stay below `k`. Modifying those already compatible values could not improve feasibility and would only increase cost.

**A trace for `[2,5,6,8,5]` and `k=4`.** Sorting gives `[2,5,5,6,8]` and `m=2`. The middle five costs one to lower. Scanning left finds another five, which also costs one to lower. The next value is two, already at most four, so the scan stops. Total cost is two.

For the same array and `k=7`, the middle five costs two to raise. The next value six is below seven and costs one more. The following eight is already large enough, producing total three.

**Why sorting the original order is safe.** Operations may target any elements, and the final condition depends only on the multiset's median. Original positions have no semantic role. Sorting exposes which values lie on each side of the target order statistic without changing the optimization problem.

**A lower-bound and construction proof.** In the high-median case, the current middle and every scanned-left value above `k` must lose at least its excess; otherwise more than $n-m-1$ values remain strictly above `k` and the median cannot be `k`. The source pays exactly those lower bounds and constructs a feasible multiset by setting each to `k`. The low-median case is symmetric. Therefore, the calculated cost is both necessary and attainable.

## Complexity detail

Python sorting takes $O(n\log n)$ time. The subsequent directional scan visits at most $n$ values once, so sorting dominates and total time is $O(n\log n)$.

`nums.sort()` mutates the input list. CPython's Timsort can use $O(n)$ temporary memory in the worst case, consistent with the local manifest's $O(n)$ space bound. The explicit scalar state after sorting is $O(1)$.

The answer can be large because differences may approach $10^9$ across many elements. Python integers handle the sum; fixed-width implementations should use 64-bit arithmetic.

## Alternatives and edge cases

- **Selection instead of full sorting:** Find the upper median with a linear-time selection algorithm, then partition and sum required deviations. It can reduce expected time but is more complex.
- **Sort and scan all values:** Sum every relevant excess using index conditions without early breaks. It remains $O(n)$ after sorting but does extra constant work.
- **Odd length:** `n // 2` is the unique middle.
- **Even length:** `n // 2` selects the larger of the two central sorted values as required.
- **Median already `k`:** The cost is zero and sorted neighbors cannot force extra changes.
- **All values above `k`:** The middle and enough left-side values are lowered; farther right values may remain.
- **All values below `k`:** The middle and necessary right-side values are raised.
- **Duplicate values:** Each occurrence is a separate array element and contributes its own unavoidable distance when it lies on the required side.
- **Values equal to `k`:** They need no operations and trigger the sorted early-stop condition.
- **Strict scan conditions:** Only `> k` on the left or `< k` on the right costs operations.
- **Input mutation:** Sorting changes `nums` in place, an observable implementation detail.
- **No need to rebuild final order:** The cost calculations describe feasible changes; the method returns only their minimum number.
- **One-element array:** The answer is simply the absolute difference from `k`.
- **Large total:** Use a wide integer outside Python.
- **Why not change an opposite-side value:** It cannot repair the rank condition more cheaply than moving a violating value directly to `k`.
