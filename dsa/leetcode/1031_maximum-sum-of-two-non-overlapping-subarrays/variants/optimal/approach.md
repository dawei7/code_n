## General
**Make every window sum constant-time:** Build a prefix array with `prefix[i]` equal to the sum before index `i`. A length-`length` window starting at `left` then has sum `prefix[left + length] - prefix[left]`.

**Solve one left-to-right ordering:** Suppose the `left_len` window must precede the `right_len` window. Scan each possible `right_start`. Maintain `best_left`, the greatest sum of a `left_len` window ending no later than `right_start`. Combining it with the current right window considers the best valid pair for that boundary without overlap.

**Evaluate both possible orders:** Run the scan once with `first_len` on the left and once with `second_len` on the left. The maximum of those results covers every legal pair because two non-overlapping subarrays must have one entirely before the other.

For a fixed ordering and right boundary, `best_left` contains every feasible left window seen so far and retains the greatest one. Thus the scan chooses the optimal pair for each right window. Taking all right windows and both orders proves the final maximum is global.

## Complexity detail
Building prefix sums costs $O(N)$ time and space. Each ordered scan advances across the array once, with $O(1)$ work per position, so both scans together remain $O(N)$ time. The prefix array uses $O(N)$ auxiliary space.

## Alternatives and edge cases
- **Rolling window sums:** Maintain the current left and right sums directly to achieve $O(N)$ time and $O(1)$ auxiliary space, at the cost of more index bookkeeping.
- **Enumerate every window pair:** Prefix sums make each pair evaluation constant-time, but there are $O(N^2)$ pairs.
- **Only one fixed order:** This misses answers where the `second_len` window must occur first.
- **Exact total length:** When the lengths sum to $N$, both subarrays together cover the entire array and the answer is its total sum.
- **Zero values:** The method does not rely on strictly positive contributions.
- **Overlap trap:** Individually largest windows may overlap; the maintained boundary prevents combining them.
