## General
**A negative factor can exchange the best and worst ending products**

After each position, keep `high` and `low`, the maximum and minimum products among nonempty subarrays ending exactly there. The minimum is necessary because multiplying a large negative product by a later negative value can make it the next maximum.

For a new `value`, every ending subarray either starts at that value or extends a subarray ending one position earlier. Thus the only candidates for the new extremes are `value`, `high * value`, and `low * value` using the previous state. When `value < 0`, swap `high` and `low` first because multiplication reverses their order; then update `high = max(value, high * value)` and `low = min(value, low * value)`.

Initialize `high`, `low`, and `best` from the first element so a negative singleton remains eligible. After each recurrence, update `best` from `high`. The ending-state argument covers every subarray when its right endpoint is processed, so the largest ending maximum seen over the scan is the global optimum. A zero is handled by the single-value candidate and naturally resets both ending extremes.

## Complexity detail
Each of the $n$ values causes a constant number of arithmetic operations and comparisons, giving $O(n)$ time. Three scalar products use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate all subarrays:** is direct but takes $O(n^2)$ time.
- **Prefix and suffix products:** can also achieve linear time but expresses zero and sign behavior less directly.
- **Track only the ending maximum:** fails when a negative minimum later becomes positive through another negative factor.
- A one-element array returns that element, including when it is negative.
- Zero can be the global answer and allows a fresh nonempty subarray to begin afterward.
- The recurrence always uses the previous extrema; swapping before multiplication prevents an updated value from contaminating the other state.
