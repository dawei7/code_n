## General

For every cell containing one, the algorithm records the length of a line ending at that cell in each of four directions:

- vertical;
- horizontal;
- diagonal from top-left;
- anti-diagonal from top-right.

Four padded dynamic-programming matrices `a`, `b`, `c`, and `d` store those lengths.

Rows and columns in the DP tables are shifted by one relative to `mat`. Input `mat[i - 1][j - 1]` corresponds to DP coordinate `(i, j)`.

Padding gives each table `m + 2` rows and `n + 2` columns filled with zero. It lets transitions read border predecessors without separate bounds branches.

**Vertical line.** `a[i][j] = a[i - 1][j] + 1` extends the run ending directly above.

**Horizontal line.** `b[i][j] = b[i][j - 1] + 1` extends the run ending directly to the left.

**Main diagonal.** `c[i][j] = c[i - 1][j - 1] + 1` extends the top-left-to-bottom-right run.

**Anti-diagonal.** `d[i][j] = d[i - 1][j + 1] + 1` extends the top-right-to-bottom-left run.

The extra right padding column is especially useful for `j + 1` at the input's right edge.

Transitions run only when the input cell is one. If it is zero, all four DP entries stay at their initialized zero, correctly breaking every line passing through that cell.

**Why row-major order satisfies dependencies.** The outer loop increases `i`, so all cells in the preceding row are complete before the current row. This covers vertical and both diagonal predecessors.

Within one row, `j` increases, so the horizontal left predecessor is complete. The anti-diagonal predecessor lies in the previous row, so reading `j + 1` does not require right-to-left processing.

After calculating the four lengths, the method updates `ans` with their maximum.

For a horizontal run of four ones, successive `b` values become one, two, three, and four. Other directional values may be shorter, but `ans` records four.

For a diagonal series, each cell reads the prior row and prior column from `c`, increasing the length by one.

**Why each stored value is exact.** A line ending at `(i,j)` in one fixed direction must use the immediately preceding cell in that direction. If the current cell is zero, no line ends there. If it is one, appending it to the predecessor's longest ending line creates a line one longer, and no other path in that same fixed direction can bypass the immediate predecessor.

**Why every valid line is found.** Every horizontal, vertical, diagonal, or anti-diagonal run has a final cell in the scan's coordinate system. The corresponding DP table stores its length at that endpoint. Taking the maximum over all cells and tables therefore includes the global optimum.

The input is not modified. Separate tables keep each direction independent; using one shared number would lose which predecessor orientation it belongs to.

Consider cell `(1, 1)` in input coordinates. Its horizontal count depends on `(1, 0)`, while its vertical count depends on `(0, 1)`. Even when both predecessor lengths happen to equal two, they describe geometrically different lines and cannot be substituted in later transitions. The four arrays preserve that directional identity.

For the first example, the ones at input coordinates `(0, 1)`, `(1, 1)`, and `(2, 3)` do not all form one direction. However, the diagonal cells `(0, 1)`, `(1, 2)`, and `(2, 3)` do form a top-left-to-bottom-right line, so their `c` values grow from one through three. Horizontal and vertical tables simultaneously track their own candidates without interfering.

The anti-diagonal recurrence deserves particular attention: while scanning left to right, its predecessor is to the right, but on the **previous** row. That previous row is already complete, so `d[i - 1][j + 1]` is safe even though the current row's right neighbor has not been processed.

When a zero is encountered, the code performs no explicit reset assignments because every table was initialized to zero and each cell is written at most once. Leaving the entries untouched is exactly equivalent to setting all four directional lengths to zero.

## Complexity detail

Let $r$ and $c$ be matrix dimensions. Every cell is visited once and performs constant work, so time is $O(rc)$.

The exact source allocates four $(r+2)\times(c+2)$ matrices, so its actual auxiliary space is $O(rc)$, not the manifest's $O(c)$ claim. The manifest corresponds to retaining only the previous row plus current-row directional values. This explanation follows the exact implementation while identifying that distinction.

Padding adds only constant rows and columns and does not change the asymptotic bound.

The four-table allocation stores roughly four integers per padded cell. A compressed implementation matters for very wide matrices, even though the source also bounds total cells by 10,000.

## Alternatives and edge cases

- **One-row compressed DP:** Preserve previous-row vertical/diagonal values and current horizontal state to achieve the manifest's $O(c)$ space.
- **Scan separately in four directions:** It can remain linear but repeats matrix traversal and needs careful run resets.
- **Start a walk from every one:** It repeats line work and can become quadratic.
- **All zeroes:** No transition runs and the answer stays zero.
- **Single one:** All four lengths become one.
- **One row:** Only horizontal runs can exceed one.
- **One column:** Only vertical runs can exceed one.
- **Diagonal versus anti-diagonal:** They use different predecessor columns and must be tracked separately.
- **Zero inside a run:** Initialized zero entries reset every direction automatically.
- **Border cells:** Padding supplies safe zero predecessors.
- **Rectangular matrix:** Independent `m` and `n` dimensions are handled directly.
