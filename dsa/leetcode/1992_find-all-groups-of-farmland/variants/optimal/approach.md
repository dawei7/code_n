## General
**Recognize only top-left farmland cells**

Scan the matrix in row-major order. A farmland cell begins a group exactly when
there is no farmland immediately above it and no farmland immediately to its
left. Any other cell in a filled rectangle has at least one of those two
neighbors unless it is the rectangle's unique top-left corner.

The boundary checks also handle groups touching the top or left edge: a
missing neighbor is treated as non-farmland.

**Extend along the rectangle boundaries**

From a detected top-left corner, move downward in its column while farmland
continues to find `bottomRow`. Independently move rightward in its row to find
`rightColumn`. The filled-rectangle guarantee means these two extents describe
the entire group; no interior search or visited matrix is necessary.

**Why every group appears exactly once**

Every rectangular group has one top-left cell, and that cell passes both
neighbor tests. All its other cells fail at least one test, so the group cannot
be emitted twice. Forest cells are ignored, and non-adjacency prevents one
group's boundary from extending into another. Consequently the recorded
corners are complete, disjoint, and exact.

## Complexity detail
The row-major scan visits all $MN$ cells. Boundary extensions across all
detected rectangles add at most their total heights and widths, which is
$O(MN)$ over disjoint groups. Total time is therefore $O(MN)$. Aside from the
required output list and a fixed number of indices, the algorithm uses
$O(1)$ auxiliary space.

## Alternatives and edge cases
- **DFS or BFS with a visited matrix:** Traverse every farmland component and
  track its coordinate extremes. This is also $O(MN)$ time but uses
  $O(MN)$ additional space in the worst case.
- **Mark farmland in place:** Flood-fill or clear each found rectangle to avoid
  revisiting it. This can use constant auxiliary space but mutates the input.
- **Rescan a component from every farmland cell:** Deduplicating the resulting
  rectangles is correct, but a large group is traversed repeatedly and can
  require quadratic work in the number of cells.
- A single farmland cell is a valid one-by-one rectangle with identical corner
  coordinates.
- Groups may be one row tall or one column wide.
- Diagonally touching rectangles remain separate because adjacency is
  four-directional.
- An all-forest matrix returns an empty list; an all-farmland matrix returns one
  rectangle spanning the complete grid.
- Output order does not affect correctness.
