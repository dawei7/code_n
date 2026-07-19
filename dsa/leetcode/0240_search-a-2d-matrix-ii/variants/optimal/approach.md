## General
**Start where one comparison eliminates a row or column**

Begin at the top-right cell. A larger value proves the entire current column is too large, so move left. A smaller value proves the entire current row is too small, so move down.

Before each comparison, every still-possible target cell lies in the submatrix from the current row downward and from column zero through the current column.

Sorted columns justify discarding a column when its top remaining value is too large; sorted rows justify discarding a row when its rightmost remaining value is too small. These moves never discard a possible match, and finding equality returns true. Leaving the matrix means all rows or columns have been safely eliminated.

At the top-right boundary of the remaining submatrix, a value greater than the target rules out its entire column because every lower value is at least as large. A value below the target rules out its entire row because every value to the left is no larger. Equality succeeds immediately; leaving the matrix means these safe eliminations exhausted all candidates.

## Complexity detail
Each step moves left or down, with at most `n` left moves and `m` down moves, for $O(m+n)$ time and constant space.

## Alternatives and edge cases
- **Search every cell:** costs $O(mn)$.
- **Binary-search every row:** costs $O(m \log n)$.
- Empty matrices return false; one row, one column, duplicates, and negative values preserve the same invariant.
