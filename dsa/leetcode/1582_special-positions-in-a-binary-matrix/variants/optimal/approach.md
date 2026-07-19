## General
**Count ones along both axes**

Create one counter per row and one per column. Scan every cell once; whenever a cell contains $1$, increment its row counter and column counter.

These counts summarize both uniqueness conditions without repeatedly revisiting entire rows and columns.

**Validate only cells whose two counts are one**

Scan the matrix again. Position `(row, column)` is special exactly when its value is `1`, `row_ones[row] == 1`, and `column_ones[column] == 1`.

If all three conditions hold, the cell is the only $1$ on both axes and must be counted. If any condition fails, either the position is zero or another $1$ shares its row or column, so it cannot be special. This equivalence proves the count is exact.

## Complexity detail
Both full scans visit $RC$ cells, giving $O(RC)$ time.

The row and column counter arrays use $O(R+C)$ auxiliary space.

## Alternatives and edge cases
- **Recount each candidate's row and column:** for every $1$, sum its entire row and column. This is correct but can take $O(RC(R+C))$ time.
- **Store coordinates of ones:** collect every $1$ and frequency-count its row and column. This may reduce work for sparse matrices but uses space proportional to the number of ones.
- **Mutate the matrix with marker counts:** encode row and column totals in reserved cells. This can reduce auxiliary arrays but complicates corner handling.
- **All zeros:** no candidate position exists, so return zero.
- **Single cell containing one:** its row and column counts are both one.
- **Several ones in one row:** none of those cells is special, even if their columns are otherwise empty.
- **Several ones in one column:** the symmetric column conflict disqualifies them.
- **Rectangular matrix:** row and column dimensions need not be equal.
- **Identity matrix:** every diagonal $1$ is special.
