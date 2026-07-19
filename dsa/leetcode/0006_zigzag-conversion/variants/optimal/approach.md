## General
**Simulate the path, not the sparse grid**

The drawn zigzag contains many empty cells, but the result depends only on which row receives each character and on the order within that row. Maintain one appendable buffer for each active row. Walk through `s`, append the current character to the current row, and then move the row pointer one step down or up.

At most `min(numRows, len(s))` rows can contain a character. If `numRows` is $1$, or if it is at least the string length, no character can move back upward before the input ends, so `s` itself is already the row-by-row result.

**Reverse direction only at the two outer rows**

Start at row `0` moving downward. After placing a character in the top row, the next move must be downward. After placing one in the bottom row, the next move must be upward. Interior rows do not change the direction.

For four rows, this produces the repeating row sequence:

```text
0, 1, 2, 3, 2, 1, 0, 1, 2, 3, ...
```

This sequence is the zigzag's vertical coordinate. Horizontal coordinates are unnecessary because appending preserves the left-to-right order of characters within every row.

For `ABCDEFG` with three rows, the visited rows are `0, 1, 2, 1, 0, 1, 2`. The row buffers become `AE`, `BDF`, and `CG`; joining them from top to bottom gives `AEBDFCG`.

**Why joining the buffers reproduces the visual reading**

Before each character is processed, every earlier character is stored exactly once in the row reached by the down-and-up walk, and the row pointer identifies the correct position for the current character. Boundary reversals reproduce the visual path, so appending the character preserves that invariant.

Within a row, characters are encountered in the same order in which they would appear from left to right in the drawn arrangement. Therefore each buffer is exactly one visual row with its gaps removed. Concatenating the buffers in increasing row order is identical to reading the completed zigzag row by row.

## Complexity detail
Each of the `n` characters is appended once and copied once more when the row buffers are joined, so the time complexity is $O(n)$. The buffers collectively store exactly `n` characters, and the row collection uses at most `min(numRows, n)` entries, giving $O(n)$ auxiliary space for the constructed output.

## Alternatives and edge cases
- A rectangular character grid mirrors the picture but wastes space on unused cells and requires extra coordinate logic.
- Direct cycle arithmetic uses cycle length `2 * (numRows - 1)` to enumerate characters row by row. It is also linear, but middle rows contribute two indices per cycle while the first and last rows contribute one, making it easier to introduce duplicate or out-of-range indices.
- Repeated insertion into immutable strings can make construction quadratic. Append to mutable buffers and join once.
- `numRows = 1`, an empty or one-character string where permitted by the language wrapper, and `numRows >= len(s)` should return immediately to avoid a direction walk with no distinct bottom row.
