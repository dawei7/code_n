## General

**Fix the middle index.** For a chosen middle position $j$, the expression separates into a left contribution, `nums[i]`, the fixed subtraction `-nums[j]`, and a right contribution, `nums[k]`. Maximizing the triplet for this $j$ therefore requires the greatest value before $j$ that is strictly smaller than `nums[j]`, together with the greatest value after $j$ that is strictly larger than `nums[j]`.

**Precompute the best right endpoint.** Build `suffix_maximum` from right to left, so `suffix_maximum[j + 1]` is the largest value at a legal index $k > j$. If this maximum is not strictly greater than `nums[j]`, then no right endpoint can make $j$ part of a valid triplet. Otherwise, the maximum is automatically the best possible right contribution because the expression increases with `nums[k]`.

**Query the greatest legal left value.** Values reach $10^9$, so first sort the distinct values and assign them ranks. A Fenwick tree stores the maximum value observed at each rank prefix. Immediately before evaluating $j$, insert `nums[j - 1]`; the tree then represents exactly the indices $i < j$. Querying through `rank(nums[j]) - 1` considers only strictly smaller ranks and returns the greatest legal `nums[i]`. A zero result means that no smaller left value exists.

Whenever both endpoints exist, evaluate `left - nums[j] + right` and keep the global maximum. For each $j$, monotonicity of the expression proves that replacing either endpoint with the greatest legal value cannot make the result worse. The suffix maximum supplies that optimal right endpoint, while the Fenwick prefix maximum supplies the optimal left endpoint among exactly the earlier indices. Since every possible middle index is considered, the largest evaluated value is the maximum over all valid triplets.

## Complexity detail

Let $n$ be the length of `nums`. Sorting the distinct values for coordinate compression takes $O(n \log n)$ time. The suffix scan takes $O(n)$ time, and each of the $n$ middle positions performs one Fenwick update and at most one query in $O(\log n)$ time. The total is therefore $O(n \log n)$ time. The rank map, suffix maxima, and Fenwick tree require $O(n)$ space.

## Alternatives and edge cases

- **Balanced ordered set:** A tree set can locate the predecessor of `nums[j]` directly in $O(\log n)$ time, but Python's standard library has no balanced ordered-set type; the compressed Fenwick tree supplies the same query without an external dependency.
- **Quadratic middle scan:** For every $j$, scanning all earlier values for the best legal left endpoint is straightforward but takes $O(n^2)$ time in the worst case.
- **Cubic triplet enumeration:** Testing every $(i, j, k)$ expresses the definition directly but costs $O(n^3)$ time and is infeasible for $n=10^5$.
- **Strict inequalities:** The Fenwick query stops at the rank before `nums[j]`, and the suffix maximum must be explicitly greater than `nums[j]`; equal values cannot serve as either endpoint.
- **Index order:** Insert only `nums[j - 1]` before evaluating $j$, and read the suffix starting at `j + 1`, so both endpoint indices remain on the correct side of the middle.
- **Greatest rather than smallest left value:** Because `nums[i]` is added, the optimal predecessor is the largest observed value below `nums[j]`, not the smallest value in the prefix.
- **Guaranteed existence:** The contract promises at least one increasing triplet, so at least one middle index has both endpoints; initializing the answer to zero is safe because every valid value is positive.
- **Large values:** Coordinate compression preserves comparisons without allocating storage proportional to the $10^9$ value bound.
