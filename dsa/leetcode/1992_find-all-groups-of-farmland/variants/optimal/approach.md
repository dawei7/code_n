## General

**Recognize only the top-left corner of a group**

The outer loops inspect every matrix cell in row-major order. A farmland cell is the top-left corner of its rectangular group exactly when it has no farmland immediately above it and no farmland immediately to its left.

The source skips a cell when it is forest, when its left neighbor is farmland, or when its upper neighbor is farmland. The boundary checks `j > 0` and `i > 0` prevent accessing outside the matrix.

Any non-top-left cell in a rectangle is skipped. A cell below the rectangle's first row has farmland above it. A cell in the first row but right of the first column has farmland to its left. Only the actual top-left cell has neither.

This test replaces a visited matrix: the group is reported only at its unique top-left corner even though the input is never modified.

**Find the bottom row**

After discovering top-left coordinate `(i, j)`, the source initializes `x=i` and moves `x` downward while `land[x + 1][j] == 1`.

Because groups are solid rectangles, the first column of the group contains farmland on every row from top to bottom. When the loop stops, `x` is the bottom row coordinate.

The separation guarantee ensures the scan cannot accidentally continue directly into a different group: distinct groups are not four-directionally adjacent.

**Find the rightmost column**

The second while loop begins at `(x, j)`, the bottom-left cell, and moves `y` right while the next cell is farmland. When it stops, `y` is the rightmost column.

Why is scanning only the bottom row enough? The rectangle guarantee says every row of a group spans the same continuous columns. Therefore the right boundary found on the bottom row is also the right boundary for the entire group.

The result `[i, j, x, y]` is exactly top-left row, top-left column, bottom-right row, and bottom-right column.

**Trace the mixed example**

For

`[[1,0,0],[0,1,1],[0,1,1]]`,

cell `(0,0)` is farmland with no upper or left neighbor, so it starts a group. Neither downward nor rightward scan advances, producing `[0,0,0,0]`.

Cell `(1,1)` is another top-left corner. The vertical scan reaches row two. On that bottom row, the horizontal scan reaches column two, producing `[1,1,2,2]`.

Other cells in that rectangle are skipped: `(1,2)` has farmland to its left, and both bottom-row cells have farmland above.

**Why not marking cells still remains linear**

Every cell is checked once by the outer loops. Additional boundary scans occur only for actual groups. Vertical scans travel along distinct group first columns, and horizontal scans travel along distinct group bottom rows. Since groups do not overlap, their scanned boundary cells can be charged to farmland cells of those groups.

Even without that charging detail, the outer $MN$ scan dominates the total lengths of disjoint rectangular boundaries. There is no repeated flood fill from every farmland cell because only top-left cells trigger scans.

**Why the method is correct**

Every reported start is farmland and lacks farmland above and left, so it is the top-left corner of its group. Rectangularity makes the two scans find that group's exact bottom and right boundaries, so every reported rectangle is correct.

Conversely, every group has one top-left cell. The outer scan reaches it, and neither neighbor skip condition applies. Thus the group is reported. Every other cell of that group has farmland above or left and cannot produce a duplicate. Hence every group appears exactly once.

**Input preservation**

Unlike the common greedy variant that writes zero into visited farmland, the exact source only reads `land`. The caller's matrix remains unchanged. This is especially useful when the input must be reused after the method call.

## Complexity detail

Let $M$ be the row count and $N$ the column count. The nested outer loops cost $O(MN)$. Boundary scans across all disjoint groups add at most linear work in the number of farmland boundary cells, so total time remains $O(MN)$.

Only `m`, `n`, `i`, `j`, `x`, and `y` are used beyond the result. Excluding the required answer, auxiliary space is $O(1)$. The result uses $O(G)$ rows for $G$ groups.

## Alternatives and edge cases

- **DFS or BFS:** Finds each connected component and its maximum coordinates in $O(MN)$ time, but uses a visited structure or mutates the grid.
- **Mark the whole rectangle as zero:** Also avoids duplicates, but changes the input and writes every farmland cell.
- **Visited matrix:** Preserves input but spends $O(MN)$ extra space unnecessarily under the rectangle guarantee.
- **Single-cell group:** Both scans stay in place and all four coordinates use that cell.
- **Group touching top edge:** The `i > 0` guard correctly treats the missing upper neighbor as forest.
- **Group touching left edge:** The `j > 0` guard handles it without negative indexing.
- **Group touching bottom or right edge:** Bounds in the while conditions stop safely.
- **All farmland:** Only `(0,0)` qualifies, and the scans find the full matrix rectangle.
- **No farmland:** Every cell is skipped and the result is empty.
- **Several separated rectangles:** Nonadjacency prevents one boundary scan from entering another group.
- **Rectangle guarantee:** Essential; an irregular component could make the bottom-row width unrepresentative of upper rows.
- **Any answer order:** Row-major discovery is valid even though no specific order is required.
- **Input side effects:** The exact solution does not mutate `land`.
