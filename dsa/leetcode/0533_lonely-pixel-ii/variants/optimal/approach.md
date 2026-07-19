## General
**Count columns and whole-row patterns**

Scan each row, add its black pixels to the column counts, and represent the entire row as an immutable pattern. Only patterns containing exactly `target` black cells can satisfy the row condition; count how many times each such pattern occurs.

**Recognize the required block of identical rows**

If a qualifying pattern occurs exactly `target` times, each black position in that pattern appears in all of those rows. A column at that position is valid precisely when its total black count is also `target`; then no additional, different row can contain a black pixel in that column.

**Count pixels by groups rather than individually**

For every pattern occurring `target` times, inspect its black positions. Each position whose column count is `target` contributes all `target` pixels from the identical rows at once.

**Why the grouped count is exact**

Every contributed column has exactly the `target` identical pattern rows as its black rows, so every contributed pixel meets all conditions. Conversely, a valid pixel's row pattern has `target` black cells, its column has `target` black cells, and all black rows in that column are identical; therefore that pattern occurs exactly `target` times and the grouped calculation includes the pixel.

## Complexity detail
Creating patterns, counting columns, and inspecting qualifying patterns process $O(rows \cdot cols)$ characters. Stored row-pattern keys can occupy $O(rows \cdot cols)$ space, while column counts use $O(cols)$.

## Alternatives and edge cases
- **Validate every black pixel directly:** repeatedly counts axes and compares rows, which can become polynomially slower on a dense picture.
- **Group row indices by serialized row:** is equivalent to pattern frequencies but retains unnecessary index lists.
- **Correct row count but wrong column count:** contributes nothing.
- **Correct counts with differing rows:** violates the identical-row condition even if every axis total matches.
- **Pattern occurring more than `target` times:** makes each of its black columns exceed the target count.
- **No qualifying pattern:** returns zero without any special case.
