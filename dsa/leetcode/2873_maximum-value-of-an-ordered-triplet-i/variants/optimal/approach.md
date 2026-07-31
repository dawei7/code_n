## General

**Compress all earlier index pairs into one difference**

When the scan reaches an index $k$, the multiplier `nums[k]` is fixed and positive. Among all pairs $i < j < k$, only the largest difference `nums[i] - nums[j]` can produce the best triplet ending at $k$.

Maintain `maximum_value`, the largest array value seen before the current index, and `maximum_difference`, the largest value of `nums[i] - nums[j]` over all ordered pairs entirely before the current index. Initialize the difference and answer to zero so that negative triplets never reduce the required result.

For each current `value`, perform the updates in this order:

1. Treat the current index as $k$ and combine `maximum_difference` with `value`.
2. Treat the current index as $j$ and combine it with the earlier `maximum_value` to improve the stored difference.
3. Add the current value to the prefix maximum for future indices.

The ordering preserves $i < j < k$: a difference using the current index as $j$ is not eligible until a later iteration uses some index as $k$.

Before each iteration, `maximum_value` is the maximum of every valid earlier $i$, and `maximum_difference` is the maximum across every valid earlier pair $(i,j)$. The three updates extend those invariants to include the current position. Consequently every ordered triplet is represented when its final index is processed, and the maximum product retained in `answer` is exactly the required value.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. The algorithm scans the array once and performs constant work per value, so it takes $O(n)$ time. It stores three numeric accumulators and uses $O(1)$ auxiliary space.

The benchmark uses $n$ as `size` and places `1000000` at both ends with ones between them at sizes 6, 25, and 100. This preserves one easily verified maximum while requiring every position to be processed. The invariant-based method scales linearly. A correct approach that explicitly scans the left and right sides for every middle index completes all tiers but exhibits quadratic scaling.

## Alternatives and edge cases

- **Three nested loops:** Enumerating every $(i,j,k)$ directly is simple but takes $O(n^3)$ time.
- **Prefix and suffix arrays:** Precomputing the maximum value to the left and right of each middle index gives $O(n)$ time with $O(n)$ auxiliary space.
- **Quadratic middle scan:** Recomputing both side maxima for each $j$ is correct but costs $O(n^2)$ time.
- **Strict index order:** The current value must be tested as $k$ before it is allowed to form a difference as $j$.
- **All increasing values:** Every difference is nonpositive, so the answer remains zero.
- **Equal values:** A zero difference is valid and produces zero, matching the required floor.
- **Large product:** The result can be close to $10^{12}$ even though each input value is at most $10^6$.
