## General
**Turn an average threshold into a sum threshold**

For a candidate average `A`, replace each value `nums[i]` by `nums[i] - A`. A subarray has original average at least `A` exactly when its transformed sum is nonnegative. This converts numerical optimization into a monotone yes/no feasibility test.

**Test every eligible ending position**

Maintain the transformed prefix sum through the current index. For a subarray ending there and having length at least `k`, its start prefix may be any prefix ending at least `k` positions earlier. Subtracting the smallest such prefix maximizes the candidate subarray sum, so feasibility holds once `current_prefix - minimum_eligible_prefix >= 0`.

**Keep prefixes as rolling totals**

Initialize the transformed sum of the first `k` values. As the right endpoint advances, add its transformed value, separately extend the prefix ending `k` positions behind, and maintain the minimum of those eligible prefixes. No prefix array is required.

**Binary-search the monotone answer**

Every feasible average makes all smaller averages feasible, while every infeasible one makes all larger averages infeasible. Search between the minimum and maximum input values, retaining the feasible half for a fixed number of iterations sufficient for `epsilon = 10 ** - 5` precision.

**Why the returned boundary is optimal**

The feasibility test considers every subarray of length at least `k` through its ending prefix and best eligible starting prefix. Binary search preserves an interval containing the transition between feasible and infeasible averages. Repeated halving makes the feasible lower boundary arbitrarily close to the true maximum, within the required tolerance.

## Complexity detail
Let `R = max(nums) - min(nums)` and let `epsilon` be the target precision. Each feasibility check scans `N` values in $O(N)$ time and $O(1)$ space. Binary search performs $O(\log(R / \varepsilon))$ checks, for $O(N \log(R / \varepsilon))$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Prefix-array feasibility:** stores every transformed prefix and uses the same binary search, but requires $O(N)$ extra space.
- **Enumerate all eligible subarrays:** incrementally sums every start/end pair in $O(N^2)$ time.
- **Check only length `k`:** solves the fixed-length variant but misses a longer subarray with a better average.
- When $k = 1$, the answer is the largest element.
- When $k = N$, the whole array is the only candidate.
- All-negative input keeps both search bounds negative and needs no special case.
- A longer window can beat every length-`k` window, so feasibility must allow all eligible starts.
- Fixed iteration count avoids floating-point termination stalls while exceeding the required precision.
