## General
**Evaluate a group from prefix sums**

Build `prefix[i]`, the sum of the first `i` values. The average of the half-open segment `[start, end)` is then `(prefix[end] - prefix[start]) / (end - start)` in constant time.

**Choose the final cut**

For one group, `dp[end]` is the average of the first `end` values. For each additional group count, compute a new array: to form `groups` groups covering the first `end` values, try every final-group start `split` and combine the previous best `dp[split]` with the average of `[split, end)`.

Every value is positive, so splitting one nonempty group into two strictly positive-average groups cannot reduce the objective. An optimum using at most `k` groups therefore has exactly `k` groups. For a fixed final cut, the recurrence uses the optimal partition of the prefix by induction; trying all legal cuts considers the final boundary of every partition, so the maximum is globally optimal.

**Reuse only the preceding layer**

The transition for one group count reads only the completed previous count. Replace the DP array after each layer instead of storing the whole `k` by `n` table.

## Complexity detail
For each of `k` group layers, up to `n` endpoints try up to `n` preceding cuts, giving $O(k \cdot n^2)$ time. Prefix sums plus two one-dimensional DP layers use $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Top-down memoization:** Cache `(start, groups_remaining)` and try every next cut; it has the same $O(k \cdot n^2)$ time and $O(k \cdot n)$ memo space.
- **Enumerate cut sets:** Testing every choice of $k - 1$ boundaries is correct but combinatorial.
- **Store the full DP table:** It simplifies reconstruction of the chosen cuts but uses $O(k \cdot n)$ space when only the value is requested.
- **One group:** Return the full-array average.
- **One group per value:** When $k = n$, the answer is the sum of all values.
- **Nonempty groups:** The split range must leave at least one value for every group.
- **Floating-point result:** Segment division may be fractional; compare with the accepted numerical tolerance.
