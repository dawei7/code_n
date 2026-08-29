## General

**Orient every legal pair from left to right.** The condition is $|i-j| \ge x$. For any pair of distinct ordered positions, name the larger index `i`. Then the smaller index must be at most `i - x`. This lets the algorithm sweep the right endpoint once while maintaining exactly the values from positions that are far enough to its left.

The loop begins at `i = x`. Before comparing `nums[i]`, it inserts `nums[i - x]` into a `SortedList`. On the next iteration it inserts the next newly eligible value, and so on. Therefore, after insertion at right endpoint `i`, the ordered collection contains values from indices zero through `i - x` and no later indices.

Every value in the collection forms a legal pair with `nums[i]`. Conversely, every pair whose right endpoint is `i` has its left value in that collection. This is the eligibility invariant that converts an index-distance condition into an ordered-value query.

**Why only predecessor and successor matter.** Once eligible values are sorted, consider the insertion position of current value `nums[i]`. Values to the left of that position are no greater than the current value, and the closest one in value is the rightmost such predecessor. Values at or to the right are no smaller, and the closest one is the leftmost such successor.

Any earlier predecessor is less than or equal to the immediate predecessor and therefore has an absolute difference at least as large. Any later successor is greater than or equal to the immediate successor and is no better. Thus, the global closest eligible value must be one of these two neighbors in sorted order.

The code calls `bisect_left(sl, nums[i])`. The returned position `j` is the first place whose stored value is at least the current value.

If `j < len(sl)`, `sl[j]` is the successor. Its nonnegative difference is `sl[j] - nums[i]`. If `j` is positive, `sl[j - 1]` is the predecessor, with difference `nums[i] - sl[j - 1]`. The minimum of those candidates updates `ans`.

**Duplicates are retained.** `SortedList` is a multiset-like sequence rather than a set. If the same number occurs at multiple eligible indices, all copies can be stored. This matters because two equal values at legal positions give answer zero. `bisect_left` points to the first equal copy, and the successor difference becomes zero.

**Why the sweep considers every valid pair.** Take any legal pair with indices $p<q$. Since $q-p \ge x$, value `nums[p]` has been inserted by the time the loop reaches `q`. The query at `q` may not compare against that exact value if another eligible value is even closer, but then the compared value yields an equal or smaller difference. Consequently, the best pair for every right endpoint is found, and minimizing those values gives the global optimum.

**The special case `x = 0`.** The loop starts at zero and inserts `nums[i - x] = nums[i]` before querying. Thus the current element is allowed to pair with itself and immediately produces difference zero. This agrees with the literal index condition $|i-j| \ge 0$ as interpreted by the accepted solution. If a separate specification required distinct indices even when `x = 0`, this behavior would need adjustment; the exact code and official constraint handling treat zero as an immediate zero answer.

**No early exit is used.** Once `ans` reaches zero, no smaller absolute difference is possible. The source could return immediately but continues the sweep. This does not affect correctness or the asymptotic bound.

**The exact data structure differs from the manifest.** The manifest describes compressed values and Fenwick-tree order statistics. The source instead relies on `SortedList` for ordered insertion and indexed access. Both support the same predecessor/successor strategy, but their implementation details and precise Python costs are different.

The call is also the module-level `bisect_left` applied to `SortedList`, not the collection's own `sl.bisect_left` method. Python's generic binary search repeatedly accesses sequence positions. A `SortedList` indexed lookup can itself require logarithmic block-location work, so a conservative literal bound for this search is $O(\log^2 n)$. Using the data structure's native bisect method would provide the intended $O(\log n)$ search.

## Complexity detail

Under the usual ordered-multiset abstraction, inserting one value, finding the lower bound, and reading the neighboring entries take $O(\log n)$ time. The loop executes $n-x$ times, so the intended complexity is $O(n \log n)$, matching the manifest's high-level bound.

For the literal Python composition, `SortedList.add` is documented as approximately $O(\log n)$, while generic `bisect_left(sl, value)` performs $O(\log n)$ indexed probes. Since a general indexed probe into the block-based sorted list can take $O(\log n)$ worst-case time, the conservative worst-case bound is $O(n \log^2 n)$. Replacing that call with `sl.bisect_left(value)` recovers the direct $O(n \log n)$ implementation without changing the algorithm.

The sorted collection grows to at most $n-x$ elements and retains duplicates, so it uses $O(n)$ auxiliary space. All other variables are constant-size. The input is read but not sorted or mutated.

The initial value `inf` is always replaced: because $x<n$, the first loop iteration inserts at least one value before querying. Therefore, a finite integer is returned for every valid input.

## Alternatives and edge cases

- **Fenwick tree with coordinate compression:** Compress all values, maintain counts of eligible ranks, and use prefix counts plus order-statistic search to find predecessor and successor ranks. This gives $O(n \log n)$ time and $O(n)$ space and matches the manifest description.
- **Use `sl.bisect_left` directly:** This preserves the exact ordered-list idea while avoiding generic sequence bisection's possible extra logarithmic indexing factor.
- **Balanced binary-search multiset:** A tree supporting lower bound, predecessor, successor, and duplicate counts gives the same intended $O(n \log n)$ bound.
- **Brute-force every legal pair:** This is $O(n^2)$ and cannot handle $10^5$ values.
- **Duplicate eligible values:** They remain separate entries, and an equal current value correctly yields difference zero.
- **`x = 0`:** The current value is inserted before its query, so the method returns zero.
- **`x = n - 1`:** Only the pair between the first and last positions is eligible, and the loop executes once.
- **Current value below every eligible value:** `j = 0`, so only the successor exists.
- **Current value above every eligible value:** `j = len(sl)`, so only the predecessor exists.
- **Negative values outside the stated constraints:** Ordering and absolute-difference logic would still work; positivity is not required by the algorithm.
- **Input preservation:** Values are copied into the ordered collection, while `nums` stays in its original order.
