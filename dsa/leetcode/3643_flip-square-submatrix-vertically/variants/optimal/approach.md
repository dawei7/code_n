## General

**Understand what a vertical flip changes**

The selected square starts at row `x` and column `y` and has side length `k`. Its row indices are

`x, x + 1, ..., x + k - 1`,

and its column indices are

`y, y + 1, ..., y + k - 1`.

A vertical flip reverses only the order of these selected rows. It does not reverse the values from left to right. The top row of the square must exchange its selected cells with the bottom row, the second selected row must exchange with the second-to-last row, and so on. Columns outside the selected interval stay untouched, even when they belong to one of those matrix rows. Rows outside the selected square also stay untouched.

This distinction matters in the first example. Rows one and three exchange the values in columns zero through two, but column three remains where it was. The operation is a reflection of the square, not a swap of the matrix’s complete physical row objects.

**Pair each upper row with its reflected lower row**

Suppose `i` is a row in the upper half of the selected square. Its offset from the square’s top is `i - x`. Under vertical reflection, an offset `d` from the top corresponds to the same offset from the bottom. The bottom row is `x + k - 1`, so the reflected row is

`i2 = x + k - 1 - (i - x)`.

For the first selected row, `i = x` and the offset is zero, giving `i2 = x + k - 1`. For the next row, the offset is one, giving `i2 = x + k - 2`. This is precisely the required top-to-bottom pairing.

The source iterates

`range(x, x + k // 2)`.

There are `k // 2` rows in the strict upper half. Processing only this half is important. Once row `i` has exchanged with row `i2`, visiting `i2` later would perform the same exchange again and undo the flip.

For each paired row, the inner loop visits exactly `j = y` through `j = y + k - 1` and performs the simultaneous assignment

`grid[i][j], grid[i2][j] = grid[i2][j], grid[i][j]`.

Python evaluates both right-hand values before assigning either left-hand location, so no temporary variable is needed and neither value is lost.

**Even and odd side lengths**

When `k` is even, every selected row belongs to exactly one pair. For `k = 4`, offsets zero and one pair with offsets three and two.

When `k` is odd, the middle row reflects onto itself. For `k = 5`, offsets zero and one pair with four and three, while offset two is the center. The loop processes `5 // 2 = 2` upper rows and deliberately does nothing to the middle row. That is correct because a vertical reflection leaves the central row in the same position.

When `k = 1`, `k // 2` is zero, so the outer range is empty. A one-cell square is already identical to its vertical reflection, and the original matrix is returned unchanged.

**Why every selected cell reaches its required location**

Take any selected cell at row offset `d` and column offset `c`. A vertical flip should send it to row offset `k - 1 - d` while preserving column offset `c`.

If `d < k // 2`, the outer loop visits its row. The formula for `i2` produces row offset `k - 1 - d`, and the inner loop visits column `y + c`, so the cell is swapped directly into its reflected position.

If `d` is in the lower half, that cell is handled when its matching upper-half row is processed. If `k` is odd and `d = k // 2`, it is in the central row and its reflected row offset is also `d`, so leaving it alone is correct. These cases cover every cell in the square exactly once while touching no cell outside it.

**In-place behavior**

The method changes the supplied `grid` object directly and then returns that same object. It does not construct a second matrix or copy the square. That behavior is useful when the operation is intended as an update, but callers should not expect the original arrangement to remain available after the call.

Only the selected columns are swapped. It would be tempting to write `grid[i], grid[i2] = grid[i2], grid[i]`, but that would exchange entire rows across all `n` columns. Such a shortcut is wrong whenever `y > 0` or `y + k < n` because cells beside the square must remain fixed.

**Trace a smaller square**

Consider a selected `3 x 3` square with top-left coordinate `(1, 0)`. The selected rows are one, two, and three. The outer loop has only `i = 1` because `k // 2 = 1`. Its reflected row is

`i2 = 1 + 3 - 1 - (1 - 1) = 3`.

Columns zero, one, and two are exchanged between rows one and three. Row two is the central row and remains unchanged. Column three is outside the square and is never visited. That produces exactly the transformation shown in the first example.

## Complexity detail

The outer loop processes `floor(k / 2)` row pairs. For each pair, the inner loop swaps `k` selected columns. The exact number of cell-pair swaps is therefore `k * floor(k / 2)`, which is `O(k^2)` time.

This bound depends on the selected square rather than on the entire `m x n` matrix. The algorithm never scans unrelated rows or columns. In the worst case the square may cover a large portion of the matrix, but its work is still precisely proportional to the number of cells that must change sides.

The method uses only loop indices and the reflected-row index `i2`. Python’s simultaneous assignment needs only constant temporary storage for the two cell references and values being exchanged. It allocates no matrix, row, or square-sized structure, so the auxiliary-space complexity is `O(1)`.

The returned matrix itself is not counted as extra space because it is the input object after mutation, not a newly allocated output copy.

## Alternatives and edge cases

- **Two moving row pointers:** Initialize one pointer at `x` and another at `x + k - 1`, swap the selected columns, and move both pointers inward. This is equivalent to the reflected-index formula and has the same `O(k^2)` time and `O(1)` space.
- **Copy and reverse the square:** Extracting the selected cells, reversing their row order, and writing them back is conceptually simple, but it allocates `O(k^2)` extra space that the in-place pairing avoids.
- **Swap complete matrix rows:** Exchanging `grid[i]` and `grid[i2]` is only valid when the selected square spans every matrix column. In the general case it incorrectly changes cells to the left or right of the square.
- **Horizontal versus vertical reversal:** Reversing each selected row changes column order and performs a horizontal flip. This task preserves column offsets and reverses the order of selected rows.
- **Odd `k`:** The unpaired middle row must remain unchanged. Processing only `k // 2` upper rows handles this automatically.
- **`k = 1`:** No swap is required, and both loops correctly leave the grid unchanged.
- **Square at a matrix boundary:** The formula works when `x = 0`, `y = 0`, or the square touches the bottom or right edge. The constraint `k <= min(m - x, n - y)` guarantees every computed index is valid.
- **Cells outside the square:** The row loop stays within `[x, x + k)` and the column loop stays within `[y, y + k)`, so all outside cells are preserved.
- **Repeated values:** Equal cell values do not need special treatment. Swapping equal values may be visually invisible, but the positional transformation remains valid.
- **Input mutation:** The source modifies `grid` in place. A caller needing both versions must make a copy before invoking it; adding a copy inside the method would change the stated auxiliary-space behavior.
- **Missing type import:** The stored source refers to `List` without importing it. The algorithm assumes the judge supplies that typing name; standalone Python would need `from typing import List`.
