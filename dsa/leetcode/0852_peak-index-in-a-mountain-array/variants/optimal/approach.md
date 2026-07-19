## General
**An adjacent comparison reveals the side of the peak**

Maintain an inclusive search interval `[left, right]` known to contain the peak. Choose `middle = (left + right) // 2` and compare `arr[middle]` with `arr[middle + 1]`. The latter index is safe while `left < right`, because then `middle < right`.

If `arr[middle] < arr[middle + 1]`, the slope is rising. The peak must lie strictly to the right of `middle`, so assign `left = middle + 1`. Otherwise the slope is falling, or `middle` itself is the peak; keep `middle` by assigning `right = middle`.

**The interval cannot discard the unique peak**

On the increasing side every adjacent comparison rises, and on the decreasing side every adjacent comparison falls. Each update therefore removes only indices that cannot be the change point while retaining the peak. The interval shrinks on every iteration. When `left == right`, the invariant leaves that sole index as the unique peak.

## Complexity detail
Each comparison reduces the search interval by roughly half, so the algorithm takes $O(\log n)$ time. It stores only three indices, using $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Linear maximum scan:** The peak is also the array's maximum, so scanning all values is correct but takes $O(n)$ time and misses the required logarithmic bound.
- **Linear slope scan:** Returning the first index whose next value is smaller is also correct for a mountain array, but remains linear.
- **Peak near the left boundary:** The peak may be index `1`; retaining `middle` on a falling comparison prevents skipping it.
- **Peak near the right boundary:** The peak may be index `n - 2`; a rising comparison advances the left boundary toward it.
- **Minimum length:** A three-element mountain is handled by the same comparison and interval invariant.
- **No plateaus:** Strict increase and strict decrease guarantee that equality never needs a branch.
- **No validation step:** The input is guaranteed to be a mountain array, so the algorithm need not detect malformed shapes.
