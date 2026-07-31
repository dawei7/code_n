## General

Arrange the values from largest to smallest. This places every unit of positive contribution as early as possible and postpones the most damaging negative values.

An exchange argument shows why this order is optimal. If two adjacent values are out of descending order, swapping the larger one forward increases the prefix sum ending at the first of those positions and leaves every later prefix sum unchanged. Such a swap cannot turn any positive prefix into a nonpositive one. Repeating these exchanges reaches descending order without decreasing the score, so some optimal arrangement is sorted this way.

Scan that order while maintaining the running sum. Count a prefix only when its sum is strictly greater than zero. Once the sum becomes nonpositive, the current value cannot be positive—otherwise all earlier, no-smaller values would also be positive and their sum could not be nonpositive. Every remaining value is at most the current one, so later sums cannot recover; the scan may stop immediately.

Use a wide running-sum type because up to $10^5$ values of magnitude $10^6$ can produce an absolute sum of $10^{11}$.

## Complexity detail

Let $n$ be the length of `nums`. Sorting dominates the scan, giving $O(n \log n)$ time. Python's sorting implementation can require $O(n)$ auxiliary space; the counter and running sum themselves use $O(1)$ space.

## Alternatives and edge cases

- **Max-heap:** Repeatedly extracting the largest value produces the same order in $O(n \log n)$ time but requires an explicit $O(n)$ heap.
- **Quadratic selection:** Choosing the largest remaining value for every position is correct but takes $O(n^2)$ time.
- **Zero prefix:** The contract requires strict positivity, so a running sum of zero terminates the contributing prefix sequence.
- **Zeros after a positive buffer:** A zero-valued element still contributes when the accumulated sum was already positive.
- **All nonpositive values:** If the largest value is zero or negative, the first running sum is nonpositive and the answer is zero.
- **Large accumulated sums:** A 32-bit signed integer is insufficient for the worst legal total.
