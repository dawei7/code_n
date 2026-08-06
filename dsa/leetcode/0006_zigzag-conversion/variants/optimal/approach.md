## General
**Simulate the path, not the sparse grid**

The drawn zigzag contains many empty cells, but the result depends only on which row receives each character and on the order within that row. Maintain one list buffer for each active row. Scan `s`, append `char` to `rows[row]`, and then move `row` one step down or up according to `direction`.

If `numRows == 1` or `numRows >= len(s)`, no character can complete a turn into a different row ordering, so the active solution returns `s` immediately. Otherwise all `numRows` buffers can receive a character.

**Reverse direction only at the outer rows**

Start with `row = 0` and `direction = 1`. After placing a character in row 0, the next move must be downward. After placing one in row `numRows - 1`, the next move must be upward. Interior rows leave `direction` unchanged.

For four rows, the repeating row sequence is:

```text
0, 1, 2, 3, 2, 1, 0, 1, 2, 3, ...
```

This sequence is the zigzag's vertical coordinate. Horizontal coordinates are unnecessary because appending preserves the left-to-right order within every row.

For `ABCDEFG` with three rows, the visited rows are `0, 1, 2, 1, 0, 1, 2`. The buffers become `AE`, `BDF`, and `CG`; joining them from top to bottom gives `AEBDFCG`.

**Why joining the buffers reproduces row-wise reading**

Before each character is processed, every earlier character is stored exactly once in the row reached by the down-and-up walk, and `row` identifies the correct destination for the current character. Reversing only at the two boundaries reproduces the visual path.

Within a row, characters are encountered in the same order in which they appear from left to right in the drawn arrangement. Each buffer is therefore exactly one visual row with its gaps removed. The nested joins first form each row and then concatenate rows in increasing order, which is precisely the required reading order.

## Complexity detail
Let $n$ be the length of `s`. Each character is appended once and copied once more during the joins, so the time complexity is $O(n)$. The buffers collectively store $n$ characters, and the row collection has at most $min(	exttt{numRows}, n)$ entries, giving $O(n)$ auxiliary space including the constructed output.

## Alternatives and edge cases
- **Rectangular character grid:** mirrors the picture but can allocate $O(n \cdot 	exttt{numRows})$ cells, most of them empty.
- **Direct cycle arithmetic:** is also linear, but middle rows contribute two positions per cycle while the first and last rows contribute one, making boundary mistakes easier.
- **Immutable row strings:** repeated concatenation can copy existing row prefixes and become quadratic; list buffers plus one join avoid that cost.
- **One row:** must return immediately because there is no distinct bottom row at which to reverse.
- **At least as many rows as characters:** every character remains in its own row position, so row-wise reading leaves `s` unchanged.
