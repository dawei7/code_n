## General
**Map each output position directly to its source**

In a row of length $n$, output column $c$ receives the input value from column $n-1-c$ after the horizontal flip. Because that value is binary, XOR with `1` inverts it. Build each output row with the executable transformation `value ^ 1` while iterating through `reversed(row)`.

**Combine the two required operations without an intermediate image**

Reversal changes only positions, and inversion changes only values, so applying the inversion as each reversed value is emitted has exactly the same result as materializing a fully flipped matrix and scanning it again. Process every input row independently and append its transformed row to the result.

Each output cell uses the unique input cell at the mirrored column and stores its complement. Thus every row is horizontally reversed, every bit is inverted once, and row order is preserved. Since this establishes the required value at every matrix coordinate, the returned image is correct.

## Complexity detail
The square image contains $n^2$ cells. Each cell is read once and one output cell is written for it, so the time is $O(n^2)$. The returned matrix contains $n^2$ entries and therefore uses $O(n^2)$ space; apart from that output, the construction needs only loop state.

## Alternatives and edge cases
- **Two explicit passes:** Reverse every row first and then scan the matrix to invert it. This is also $O(n^2)$ but performs an avoidable second traversal.
- **In-place two pointers:** Swap mirrored cells while inverting both, handling the center cell separately for odd $n$. It uses $O(1)$ auxiliary space when mutation is acceptable.
- **Repeated mirrored-source search:** Scanning a row from the beginning to locate the source of every output column is correct but takes $O(n^3)$ time across the matrix instead of using direct indexing.
- **One-cell image:** Reversal has no positional effect, but inversion still changes the bit.
- **Odd row length:** The center cell maps to itself and must still be inverted exactly once.
- **Symmetric row:** Even when reversal leaves the pattern visually unchanged, every bit is complemented.
- **Operation order:** For this bitwise transformation, direct mirrored complementation is equivalent to the required flip-then-invert sequence.
