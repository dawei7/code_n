## General
**A negative factor can turn the worst ending product into the best**

For every position, retain both maximum and minimum products among nonempty subarrays ending exactly there. A large negative minimum is not dominated: multiplying it by a later negative value can make it the next large positive maximum.

**Every ending product either restarts or extends one previous extreme**

For current `x`, candidates are `x`, `previous_high * x`, and `previous_low * x`. Taking their maximum and minimum is the direct recurrence. An equivalent optimized form swaps high and low when $x < 0$, then computes `high = max(x, high * x)` and `low = min(x, low * x)`.

Both updates must use the previous extremes; swapping first or saving old values prevents an updated high from contaminating the low calculation.

**Endpoint extrema and global optimum have separate meanings**

After processing index `i`, `high` and `low` are respectively the maximum and minimum products of all nonempty subarrays ending at `i`, while `best` is the maximum product over every ending position through `i`.

**Trace two negatives converting the minimum into the maximum**

For `[-2,3,-4]`, the ending extremes become `(-2,-2)`, then `(3,-6)`. Multiplying by `-4` turns the previous low `-6` into high `24`, which becomes the global answer.

**Both product extremes are necessary after a sign change**

Every subarray ending at the current position either consists only of the current number or extends a subarray ending one position earlier. Among those extensions, only the previous maximum and minimum products can become new extremes: a positive multiplier preserves their order, while a negative multiplier reverses it. Zero is handled by the single-element candidate and restarts both ranges.

The recurrence therefore captures the maximum and minimum product of every possible ending subarray. Updating the global answer from each ending maximum considers every nonempty subarray exactly when its right endpoint is processed.

## Complexity detail
Each number causes constant arithmetic and comparisons once, giving $O(n)$ time. Three running products provide $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate all subarrays:** is straightforward but costs $O(n^2)$ time.
- **Prefix and suffix products:** can also solve the problem linearly, but the two-extreme recurrence states the negative-sign effect directly.
- **Track only the maximum:** fails when a large negative product later meets another negative number.
- A one-element array returns that element, including a negative value. Initialize from the first element rather than one or zero.
- Zero naturally makes both ending extrema zero and permits a fresh subarray to begin at the next position.
