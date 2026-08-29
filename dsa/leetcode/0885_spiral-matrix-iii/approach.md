## General

The walk follows an infinite clockwise square spiral, even when parts of that spiral lie outside the finite grid. The solution simulates the infinite-grid path and records a coordinate only when it falls inside the requested rectangle.

The starting cell is always valid and is placed in `ans` immediately. If the grid has only one cell, the answer is already complete and can be returned before any movement.

**How spiral leg lengths grow.** A clockwise spiral beginning east uses direction sequence east, south, west, north. The leg lengths are

$$
1,1,2,2,3,3,4,4,\ldots
$$

Each length occurs twice before increasing. The exact solution groups four legs at a time with current odd value `k`:

- east for `k` steps;
- south for `k` steps;
- west for `k + 1` steps;
- north for `k + 1` steps.

It then adds two to `k`. The first group therefore gives lengths 1, 1, 2, 2. The next gives 3, 3, 4, 4, exactly continuing the required pattern.

The directions are represented explicitly as triples `[dr, dc, dk]`. For each of `dk` unit steps, row and column are updated by the direction increments. East adds $(0,1)$, south adds $(1,0)$ because row indices increase downward, west adds $(0,-1)$, and north adds $(-1,0)$.

**Walking outside is different from stopping.** Every simulated step updates `rStart` and `cStart`, whether or not the new coordinate is within bounds. The bounds test controls only whether the coordinate is appended:

```text
0 <= rStart < rows and 0 <= cStart < cols
```

This is essential. If the path were clamped at a boundary or skipped its outside coordinate updates, it would no longer follow the prescribed spiral and might never reenter at the correct place.

**Why valid cells appear in visitation order.** Simulation follows the movement sequence one unit at a time. Whenever the current coordinate is a grid cell, it is appended immediately. Outside positions are omitted but do not reorder the later movement. Thus `ans` is exactly the subsequence of infinite-spiral positions that lie in the grid, in the order visited.

**Why no valid cell is recorded twice.** The expanding square spiral does not revisit an infinite-grid coordinate. Each four-leg group traces new portions of the boundary around the previously traced region. Since the full path has no duplicate coordinates, filtering it to in-bounds coordinates also has no duplicates.

**Why every grid cell is eventually reached.** After each pair of leg-length increases, the spiral encloses a larger axis-aligned rectangle around the start. For any fixed grid cell, the differences between its row and the starting row and between its column and the starting column are finite. Once the spiral radius grows beyond those differences, its walk reaches that coordinate. Because the grid contains finitely many cells, eventually all of them are recorded.

The solution checks `len(ans) == rows * cols` immediately after appending a valid coordinate. At that moment every grid cell has appeared exactly once, so returning is correct and prevents an infinite loop.

For a one-row grid starting at its leftmost cell, the spiral first walks east through the row. The answer becomes complete before the subsequent southward leg, so it returns the expected straight sequence.

For an interior start, the early spiral may repeatedly leave and reenter the rectangle. Those outside steps are necessary connective portions of the same spiral, not wasted logical detours that may be removed.

## Complexity detail

Let $R=\texttt{rows}$, $C=\texttt{cols}$, and let $M$ be a length on the order of $\max(R,C)$ sufficient for the expanding spiral to cover the rectangle from an in-grid start. The spiral performs $O(M^2)$ unit steps before all cells are reached because the total perimeter work through radius $M$ is quadratic.

- **Time complexity:** $O(M^2)$.
- **Space complexity:** $O(RC)$ for the required coordinate output.

The movement state and four direction triples use constant additional space. When the start is near a boundary, some of the $O(M^2)$ simulated positions lie outside the grid, but the same bound covers them.

## Alternatives and edge cases

- **Layer-by-layer boundary formulas:** One can generate square-ring edges directly, but clipping them to a displaced rectangle is more complex than unit simulation.
- **Stop at the grid boundary:** This changes the path. The statement requires continuing outside and possibly returning later.
- **Record every infinite-grid coordinate:** Outside positions must not appear in the answer and would waste storage.
- **Visited set:** The mathematical spiral never revisits a coordinate, so a set is unnecessary. The output length itself determines completion.
- **Single cell:** The initial coordinate is returned immediately.
- **Single row or column:** Most later spiral legs lie outside, but the valid cells are still recorded in correct order.
- **Start at a corner:** The spiral begins by spending more time outside on some legs; unconditional coordinate updates preserve correct reentry.
- **Start near the center:** Early rings contain many valid cells, but the same leg pattern applies.
- **Rows increase southward:** Direction $(1,0)$ is south in matrix coordinates, while $(-1,0)$ is north.
- **Completion check placement:** It must occur after appending a valid cell. Outside positions do not advance the number of visited grid cells.
- **Exact output size:** Every one of the $RC$ cells appears once, so the returned list has exactly $RC$ coordinate pairs.
- **Unbounded outer loop:** Although written as `while True`, the expanding spiral's coverage proof guarantees return for every valid finite grid.
