## General
**The right endpoint identifies the midpoint's rotation segment**

A rotated array of distinct ascending values consists of a higher-valued prefix followed by the lower-valued suffix that begins at the minimum. Maintain a closed interval `[left, right]` containing that boundary and compare `nums[middle]` with `nums[right]`.

If the midpoint value is greater, `middle` lies in the high prefix while `right` lies in the low suffix, so the minimum is strictly to the right and `left = middle + 1` is safe. Otherwise distinctness implies the midpoint is in the low suffix—or the interval is already unrotated—and it may itself be the minimum, so preserve it with `right = middle`.

Both updates keep the minimum inside the interval and strictly reduce its length. When `left == right`, the interval contains exactly one position, which must be the rotation boundary and therefore the minimum value.

## Complexity detail
Each comparison discards at least half of the remaining interval, giving $O(\log n)$ time. The two boundaries and midpoint use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Linear scan or `min`:** is correct but violates the required logarithmic time.
- **Scan for the unique descending edge:** also takes $O(n)$ time in the worst case.
- **Compare only with the first value:** can work with additional boundary handling, while the right-end comparison gives the compact closed-interval invariant directly.
- A one-element or fully rotated array returns its first value.
- A single rotation can place the minimum at the final position.
- Distinctness removes the equality case; problem 154 must shrink through duplicates and can lose logarithmic worst-case time.
