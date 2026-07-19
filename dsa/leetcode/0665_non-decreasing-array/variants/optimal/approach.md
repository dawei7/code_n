## General
**Locate adjacent inversions**

Scan from left to right. An adjacent pair with `nums[i - 1] > nums[i]` must be repaired by changing one of those two values; changing any other position cannot fix their ordering. A second inversion after one repair proves that more than one change is required.

**Choose the repair that preserves the outer neighbor**

At the first inversion, prefer lowering `nums[i - 1]` to `nums[i]`. This is safe when there is no element two places back or `nums[i - 2] <= nums[i]`; it keeps the right side as small as possible without breaking the left side.

Otherwise, lowering the left value would create an inversion with `nums[i - 2]`, so raise `nums[i]` to `nums[i - 1]`. The already validated prefix remains unchanged, and the raised current value becomes the effective predecessor for the next comparison.

**Why one local decision is sufficient**

Every earlier pair was nondecreasing before the first inversion. The chosen repair is exactly the only direction that keeps the repaired pair compatible with that prefix. Continuing the scan verifies compatibility with the remaining suffix. If no later inversion occurs, the modified array is a concrete valid witness; if one occurs, the sole allowed change has already been used and no single edit can fix both disjoint violated pairs.

## Complexity detail
The scan examines each adjacent pair once, taking $O(N)$ time. The repair is made in place and only a violation counter is stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Track an adjusted previous value without mutating the array:** preserves the input and has the same bounds, but requires careful handling of the value two positions back.
- **Try changing every index and rescan:** is easy to validate exhaustively but takes $O(N^2)$ time.
- **Count inversions only:** is insufficient because one inversion such as `[3, 4, 2, 3]` may be impossible to repair without creating another.
- An already nondecreasing array needs no change and returns `True`.
- Arrays of length one or two always satisfy the condition.
- Equal adjacent values are valid because the target order is nondecreasing, not strictly increasing.
- A repair at either endpoint has only one outer neighbor to preserve.
