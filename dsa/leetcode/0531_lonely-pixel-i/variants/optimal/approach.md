## General

**Count black pixels along both axes**

Allocate one counter per row and one per column. Scan every cell once; whenever the cell is `"B"`, increment the
counter for its row and the counter for its column.

**Test both loneliness requirements together**

Scan all coordinates again. A coordinate contributes exactly when it contains `"B"`, its row count is one, and its
column count is one. The generator yields those Boolean conjunctions, and `sum` counts the true values directly.

The first pass records complete black-pixel totals for every row and column. Therefore a black coordinate passes the
second test precisely when no other black coordinate shares either axis with it. Every lonely pixel is counted once,
and a non-lonely or white pixel cannot contribute.

## Complexity detail

Both full scans visit `rows * cols` cells, giving $O(rows \cdot cols)$ time. The two counter arrays use
$O(rows + cols)$ auxiliary space.

## Alternatives and edge cases

- **Rescan a row and column for every black pixel:** is direct but can take
  $O(rows \cdot cols \cdot (rows + cols))$ time on a dense picture.
- **Sets of candidate coordinates:** can track first and repeated black positions, but count arrays express the same
  information more simply.
- **All-white picture:** has no candidate black coordinate and returns zero.
- **Dense black picture:** every black pixel shares both axes and none is lonely.
- **One row or one column:** a black pixel is lonely only when it is the sole black pixel in that entire line.
- **Rectangular picture:** row and column counters must use their distinct dimensions.
