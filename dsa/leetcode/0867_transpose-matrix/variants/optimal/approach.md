## General
**Allocate the swapped dimensions**

The result needs one row for each input column. For result row `j`, visit every input row `i` in order and append `matrix[i][j]`. This directly implements the defining relation `result[j][i] = matrix[i][j]` and works for square, tall, and wide matrices without special cases.

Each input coordinate `(i, j)` maps to one unique output coordinate `(j, i)`, so no value is omitted or duplicated. Conversely, every valid output coordinate maps back to a valid input coordinate. The constructed dimensions and entries therefore form exactly the transpose.

**Preserve the input**

Construct separate result rows instead of trying to swap cells in place. In-place symmetric swaps are straightforward only for square matrices; a rectangular transpose changes the outer and inner dimensions. A fresh matrix keeps the caller's input unchanged and naturally supports all permitted shapes.

## Complexity detail
The nested construction reads and writes each of the $mn$ entries once, giving $O(mn)$ time. The returned matrix contains $mn$ integers, so its storage is $O(mn)$; excluding required output storage, the loop uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Repeated immutable row copies:** Extending a result row by rebuilding all of its existing entries is correct but can take quadratic time for a tall one-column matrix.
- **In-place diagonal swaps:** This works for square matrices, but rectangular inputs require reshaping and cannot use the same simple operation.
- **Language transpose helper:** A built-in such as `zip` can be concise, but tuple outputs may need conversion to the required mutable nested-list shape.
- **Single cell:** Swapping its row and column indices leaves `[[value]]` unchanged.
- **Single row:** It becomes a column with one value per result row.
- **Single column:** It becomes one result row containing all input values in order.
- **Negative and repeated values:** Transposition changes only coordinates, never the stored integers.
