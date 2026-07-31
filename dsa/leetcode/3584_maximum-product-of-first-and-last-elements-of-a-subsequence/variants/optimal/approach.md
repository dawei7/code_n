## General

For `m >= 2`, suppose index `last` is the subsequence's final position. Its first position may be any index at most `last - m + 1`: after choosing those two endpoints, the interval between them contains enough positions to fill the remaining `m - 2` selections. The interior values never affect the product.

For a fixed last value $x$, the maximum product with any eligible first value must use an extreme. If $x$ is nonnegative, the largest eligible first value is best; if $x$ is negative, the smallest eligible first value is best. Evaluating both the running minimum and maximum handles both signs without a branch.

Scan `last` from `m - 1` through the end of the array. Before evaluating it, incorporate `nums[last - m + 1]` into the running prefix minimum and maximum. Those extrema then cover exactly every possible first index for this last endpoint. Taking the best of the two endpoint products over all iterations examines the optimum for every feasible last index, so the global maximum is found.

When `m = 1`, an eligible subsequence contains one position and therefore has the same first and last element. Products between different indices would be invalid. Handle this case separately by returning the largest square in the array.

## Complexity detail

Let $n$ be the array length. The `m = 1` scan and the general endpoint scan each inspect at most $n$ values, so time is $O(n)$. Only the current extrema, answer, and a few indices are retained, giving $O(1)$ auxiliary space.

The benchmark defines $S=n$, sets `m = S / 2`, and fills the array with ones. Legal tiers 64, 256, and 1024 span 16x. The accepted method processes $\Theta(S)$ endpoint positions. A calibrated slower alternative explicitly tests every feasible first/last pair, requiring $\Theta(S^2)$ time while returning the same product.

## Alternatives and edge cases

- **Enumerate endpoint pairs:** Testing every pair whose gap can hold `m` selected elements is correct, but costs $O(n^2)$ time.
- **Suffix extrema arrays:** Precomputing the minimum and maximum suffix available to each first index also gives $O(n)$ time, but uses $O(n)$ extra space.
- **Sort the values:** Sorting loses the index-order and minimum-gap constraints, so extreme values cannot safely be paired after reordering.
- **Single-element subsequence:** For `m = 1`, square one value; never combine two distinct indices.
- **Full-length subsequence:** When `m = n`, only the complete array is eligible and its original endpoints determine the answer.
- **Negative last value:** Multiplication reverses order, so the smallest eligible first value may produce the largest product.
- **Negative optimum:** Initialize below every legal product rather than at zero, because all feasible products can be negative.
- **Integer width:** Endpoint magnitudes can reach $10^5$, so a product can reach $10^{10}$ and needs a 64-bit integer in fixed-width languages.
