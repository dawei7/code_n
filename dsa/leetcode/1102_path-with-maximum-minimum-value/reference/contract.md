## Function Contract

**Input**

- `grid`: a nonempty rectangular integer matrix with $m$ rows and $n$ columns.

A valid path starts at `(0, 0)`, ends at `(m - 1, n - 1)`, and moves only between horizontally or vertically adjacent cells. Its score includes both endpoint values and every intermediate cell value.

Let $V = mn$ be the number of cells.

**Return value**

Return the largest possible minimum cell value over every valid corner-to-corner path.
