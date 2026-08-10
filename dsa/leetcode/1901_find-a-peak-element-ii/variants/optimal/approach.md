## General

**Binary-search rows and inspect one row maximum.** Bounds `l` and `r` identify a range of rows guaranteed to contain a peak. At each step, `mid` is the lower middle row. The source finds a column `j` containing that row's maximum. Because `mat[mid][j]` is maximal within its row and horizontally adjacent cells are unequal, it is strictly greater than its left and right neighbors whenever they exist.

That leaves only vertical direction to decide. The algorithm compares the selected maximum with the cell directly below it, `mat[mid + 1][j]`. The loop condition `l < r` guarantees `mid < r`, so the next row exists.

**Move toward a strictly larger downward neighbor.** If `mat[mid][j] <= mat[mid + 1][j]`, adjacent cells cannot be equal by contract, so the below cell is strictly larger. The current row maximum is not a peak, and an ascending path begins downward. A peak is guaranteed in the lower part, so `l = mid + 1` discards the current and upper rows.

If `mat[mid][j] > mat[mid + 1][j]`, the selected value already dominates its horizontal neighbors and its lower neighbor. If its upper neighbor is smaller, it is itself a peak. If the upper neighbor is larger, an ascent leads into the upper part. In either case a peak exists at or above `mid`, so `r = mid` safely retains that half.

**Why following ascent guarantees a peak.** Matrix values are finite, and adjacent values are unequal. Starting from a cell and repeatedly moving to a larger adjacent neighbor must terminate because values strictly increase and no cell can repeat. The terminal cell has no larger neighbor and is therefore a peak. The row-maximum comparison determines which side contains such an ascent path without examining every cell in both halves.

**Return the maximum of the surviving row.** When `l == r`, the retained interval has one row. The method again finds that row's maximum and returns `[l, column]`. The binary-search invariant guarantees this row maximum dominates the relevant vertical neighbors; row maximality gives horizontal dominance. The virtual outer perimeter of negative ones handles a first or last row without special comparisons, and all matrix values are positive.

**Why an arbitrary maximum index is acceptable.** `max(mat[mid])` obtains the row's maximum value, and `.index(...)` returns its first occurrence. Multiple equal maxima in one row cannot be horizontally adjacent because adjacent cells differ, but may occur farther apart. The standard direction argument applies to the selected occurrence. The task accepts any peak, so choosing the first maximum is sufficient.

**Trace the second example.** In matrix `[[10,20,15],[21,30,14],[7,16,32]]`, the first middle row is row one and its maximum is 30 at column one. The cell below is 16, so the search keeps rows zero through one. It next considers row zero, whose maximum 20 has 30 below it, so it moves down to row one. The surviving row maximum is 30, returned at `[1, 1]`.

**Why the method meets the requested shape.** It does not binary-search a numeric value or require the matrix to be globally sorted. It uses local gradient information from each selected row maximum. Each comparison eliminates roughly half the rows while preserving existence of some peak.

**Inputs remain unchanged.** Row maxima and indices are read only. No sentinel border is physically added, and the matrix is not reordered.

## Complexity detail

Using the statement's notation, let $m$ be the number of rows and $n$ the number of columns. Binary search performs $O(\log m)$ iterations. In each iteration, `max(row)` scans $n$ entries and `row.index(maximum)` scans up to $n$ again. The final row repeats that work. Total executed time is $O(n\log m)$.

This is one of the two complexity forms allowed by the problem, but it differs from the manifest's written $O(m\log n)$ orientation. Searching columns and scanning rows would give that transposed bound; the exact source searches rows.

Only bounds, midpoint, column index, and temporary maximum values are used. `max` and `index` do not allocate proportional collections, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Binary-search columns instead:** Find a column maximum and compare its right neighbor. This gives $O(m\log n)$ time and may be preferable when there are far fewer rows than columns.
- **Scan every cell:** Checking all neighbors costs $O(mn)$ and ignores the required logarithmic dimension.
- **Hill climbing from an arbitrary cell:** Strict ascent eventually finds a peak, but a poorly chosen path can visit many cells and lacks the requested worst-case bound.
- **Single row:** The loop does not move vertically; returning the row maximum gives a 1D peak against the negative outer border.
- **Single column:** Each row scan is constant time, and binary search finds a vertical peak in $O(\log m)$.
- **Peak on a boundary:** Missing neighbors are conceptual `-1`, smaller than every positive matrix value, so no explicit sentinel storage is needed.
- **Multiple peaks:** The retained-half decisions may lead to any one of them. The contract accepts every valid peak coordinate.
- **Nonadjacent equal row maxima:** `index` picks the first. Adjacent inequality and the vertical direction proof still support the chosen occurrence.
- **Adjacent-equality guarantee:** It turns the source's `else` case into a strict downward increase even though the condition is written with `>` versus its negation. Without that guarantee, plateau handling would require care.
