## General
View the matrix in row-major order as one cyclic array of length $N$. Cell `(r, c)` corresponds to flat index `r * n + c`, and one grid shift is exactly a right rotation of this flat array by one position.

**Collapse all shifts into one rotation**

After `k` shifts, an element moves `k` positions around the same cycle. Reduce `k` with `k %= N`; complete cycles make no change. Flatten the grid once, then form the right rotation by concatenating `flat[-k:]` with `flat[:-k]`. When the reduced shift is zero, retain the flat sequence unchanged.

**Restore the original shape**

Split the rotated sequence into $m$ consecutive slices of length $n$. Row-major flattening and the inverse slicing preserve exactly the transition rules between columns, rows, and the final wrap. Every input element appears once, at flat position `(old_index + k) % N`, so the result is the requested shift.

## Complexity detail
Flattening, rotating, and reshaping each process $N$ values, for $O(N)$ time. The flattened sequence and returned grid contain $O(N)$ values, so auxiliary and output space are $O(N)$.

## Alternatives and edge cases
- **Simulate one shift at a time:** Rebuilding or moving the matrix for every operation costs $O(kN)$ time.
- **Direct destination mapping:** Allocate the result and place each value at `(index + k) % N`; it has the same $O(N)$ bounds without an explicit rotated flat list.
- **Shift by zero:** Return an equal-shaped copy with the same values.
- **Whole cycles:** When `k` is divisible by $N$, the grid is unchanged.
- **Single row or column:** The same flat cyclic rotation handles both shapes without special cases.
- **Negative values:** Values are opaque payloads and do not affect index calculations.
