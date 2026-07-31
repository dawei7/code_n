## General

Scanning split indices from right to left makes the entire suffix available as a small running state. Before evaluating split `i`, maintain the sum and minimum of exactly `nums[i + 1:]`. If `total` is the sum of the complete array, then `total - suffix_sum` is precisely `prefixSum(i)`.

Evaluate `prefix_sum - suffix_minimum`, update the maximum, and then insert `nums[i]` into the running suffix before moving to `i - 1`. The insertion adds the value to `suffix_sum` and takes the smaller of it and `suffix_minimum`.

The invariant gives the exact prefix sum and suffix minimum at every valid split. Since every split is evaluated once, the greatest recorded score is the requested maximum. Initializing from the last element also ensures the suffix is never empty.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Computing the total and scanning the split indices take $O(N)$ time. The algorithm stores only a fixed number of integer accumulators, so auxiliary space is $O(1)$. The prefix sum and score can exceed 32-bit range.

## Alternatives and edge cases

- **Suffix-minimum array:** Precompute the minimum beginning at every index and scan prefix sums from left to right. This is also $O(N)$ time but uses $O(N)$ auxiliary space.
- **Direct suffix scans:** Recompute `min(nums[i + 1:])` for every split. This is correct but takes $O(N^2)$ time.
- **Two elements:** There is exactly one valid split.
- **All-negative values:** The maximum score may still be negative, so zero is not a safe initial answer.
- **Inclusive prefix:** `nums[i]` belongs to the prefix; the suffix begins at `i + 1`.
- **Late suffix minimum:** The minimum need not be adjacent to the split, which is why it must be tracked across the full suffix.
