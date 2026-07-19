## General
**Capture the original skyline limits**

Compute the maximum height of every row and every column before changing anything. A building at `(row, col)` cannot exceed either of those two maxima: exceeding the row maximum changes the skyline from one viewing direction, and exceeding the column maximum changes it from the perpendicular direction.

**Raise each cell to its tightest limit**

The greatest legal height at `(row, col)` is therefore `min(row_max[row], column_max[col])`. Add the difference between this bound and the current height for every cell.

This bound is legal because it never exceeds either original skyline limit. Each original row maximum remains present at its original cell, whose bound cannot be below its current height, and the same holds for every column maximum. Thus all skylines stay unchanged. No cell can be raised higher without violating at least one skyline, so independently taking every bound maximizes the total increase.

## Complexity detail
For an `n` by `n` grid, computing maxima and summing increases each scans $n^{2}$ cells, taking $O(n^2)$ time. The row and column maximum arrays use $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Transpose for column maxima:** `zip(*grid)` can expose columns compactly; it has the same asymptotic work but may allocate tuple views.
- **Recompute maxima per cell:** Scanning an entire row and column for every building is correct but takes $O(n^3)$ time.
- **Materialize the raised grid:** Building the final matrix is unnecessary when only the total increase is requested and uses $O(n^2)$ extra space.
- **Single cell:** Its row and column limits equal its height, so the increase is zero.
- **Uniform grid:** Every cell already equals both skyline limits.
- **Zero heights:** They may rise only when both their row and column have taller buildings.
- **Tied maxima:** Multiple buildings may preserve the same skyline; the cellwise bound remains unchanged.
