## General
**Represent the next value with two coordinates**

Store the current row and column instead of flattening the input. A helper advances the row coordinate past every exhausted or empty row and resets the column to zero.

After normalization, either the row coordinate is past the vector or `(row, column)` identifies the next unconsumed integer. `hasNext()` only normalizes and checks that state; `next()` reads it and advances the column.

**Normalization skips containers, never values**

The helper advances beyond a row only when the column index has reached that row's length, so every skipped row is empty or fully consumed. Once normalized, the coordinates identify the earliest remaining value in row-major order. `next()` returns that value and advances once, making the same statement true for the following call.

## Complexity detail
Initialization is $O(1)$. Although one normalization may skip several empty rows, each row is skipped once over the iterator's lifetime. Thus `next` and `hasNext` are amortized $O(1)$ and the iterator uses two coordinates, or $O(1)$ auxiliary space. The app's batch adapter necessarily spends $O(L)$ time and returns an $O(L)$ list for the $L$ yielded values.

## Alternatives and edge cases
- **Pre-flatten the vector:** simplifies iteration but requires $O(n)$ initialization time and auxiliary storage.
- **Empty rows:** leading, trailing, and consecutive empty rows are all handled by the same normalization rule.
- **Entirely empty vector:** has no next value after normalization advances past every row.
