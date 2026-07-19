## General
**Represent the next value with two coordinates**

Store the current row and column instead of flattening the input. A helper advances the row coordinate past every exhausted or empty row and resets the column to zero.

After normalization, either the row coordinate is past the vector or `(row, column)` identifies the next unconsumed integer. `hasNext()` only normalizes and checks that state; `next()` reads it and advances the column.

**Normalization skips containers, never values**

The helper advances beyond a row only when the column index has reached that row's length, so every skipped row is empty or fully consumed. Once normalized, the coordinates identify the earliest remaining value in row-major order. `next()` returns that value and advances once, making the same statement true for the following call.

## Complexity detail
Although one normalization may skip several empty rows, each row is skipped once over the iterator's lifetime. Thus operations are amortized $O(1)$ and the iterator uses two indices, or $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Pre-flatten the vector:** simplifies iteration but requires $O(n)$ initialization time and auxiliary storage.
- Leading, trailing, and consecutive empty rows are handled by the same normalization rule; an entirely empty vector has no next value.
