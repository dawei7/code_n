## General

**Simulate the path a person would draw**

The spiral begins at the top-left cell, moves right, turns down when blocked, then turns left, then up, and repeats. A cell is blocked if it lies outside the matrix or has already been visited. The selected solution models exactly that movement rather than explicitly maintaining shrinking rectangle boundaries.

It performs exactly $mn$ iterations, where $m$ and $n$ are the matrix dimensions. Each iteration appends one current cell and marks it visited. Because the loop count equals the number of cells, the main correctness obligation is to show that the movement never revisits a cell before all cells have been emitted.

**Encode four directions in one compact tuple**

`dirs = (0, 1, 0, -1, 0)` stores overlapping row/column deltas. For direction index `k`, the pair `(dirs[k], dirs[k + 1])` means:

- `k = 0`: `(0, 1)`, move right;
- `k = 1`: `(1, 0)`, move down;
- `k = 2`: `(0, -1)`, move left;
- `k = 3`: `(-1, 0)`, move up.

The repeated zero at the end allows the up pair to use indices 3 and 4 without a special case. Updating `k = (k + 1) % 4` rotates clockwise and wraps from up back to right.

**Mark before choosing the next position**

At the current coordinate `(i, j)`, the algorithm first appends `matrix[i][j]` and sets `vis[i][j] = True`. It then computes tentative next coordinates `(x, y)` using the current direction.

Marking before this check is essential. When the path eventually returns beside an earlier portion of the spiral, `vis[x][y]` detects that entering it would duplicate output and trigger the inward turn. If marking happened afterward, an immediately adjacent earlier cell might incorrectly appear unvisited during the decision.

The boundary conditions reject negative row or column coordinates and coordinates at or beyond `m` or `n`. These checks occur before `vis[x][y]` is evaluated because Python's `or` short-circuits left to right. An out-of-range proposal therefore never indexes the visited grid.

**Turn once when the way ahead is blocked**

If the tentative cell is invalid or visited, `k` advances one direction clockwise. The source then changes `(i, j)` using the possibly updated direction. It does not recompute a second proposal or loop until a free direction is found.

For a rectangular spiral before the final cell, one clockwise turn is sufficient. The visited cells form completed outer path segments, and the remaining cells form an unvisited inner rectangle or line connected at the turn. The direction immediately clockwise points along that next boundary. A second blocked direction can occur after the final cell, but the outer `for` loop ends before the resulting coordinate is read.

For a one-column matrix, the initial right proposal is outside, so the first iteration turns down. For a one-row matrix, movement stays right until the last cell; the coordinate update after that last append is irrelevant.

**A layer-by-layer trace without explicit layers**

For a three-by-three matrix, the direction sequence visits the top row from left to right. The right boundary forces a turn down. The bottom boundary forces a turn left, and the left boundary forces a turn up. When upward motion would enter the already visited top-left cell, the visited test turns right into the center.

Although no boundary variables shrink, the visited ring has the same effect: completed cells become walls around the remaining interior. The walker follows those walls clockwise.

**The movement invariant**

Before each iteration, `(i, j)` is an unvisited valid cell, and `ans` contains every previously visited cell exactly once in spiral order. Appending and marking preserves the one-to-one relationship between output entries and visited cells.

If the forward cell is unvisited and valid, continuing straight follows the current edge of the remaining region. If it is blocked, the clockwise turn enters the next edge. Thus, unless all cells have just been consumed, the new coordinate is another unvisited valid cell. Induction preserves the invariant for all $mn$ iterations.

At termination, `ans` has $mn$ entries and no coordinate was repeated. Since the matrix has exactly $mn$ cells, every cell appears once. The direction decisions establish that their order is the required clockwise spiral.

**The source's actual storage cost**

`vis` contains one Boolean for every matrix cell. Therefore, the selected implementation uses $O(mn)$ auxiliary space. The manifest claims $O(1)$, but that bound describes a boundary-peeling implementation, not this visited-grid source.

The returned `ans` also contains $mn$ required output values. Even when output storage is excluded from auxiliary analysis, `vis` remains a separate proportional allocation, so the exact space cannot be called constant.

## Complexity detail

The `for` loop runs exactly $mn$ times. Every iteration performs constant-time append, mark, boundary checks, at most one turn, and one coordinate update. Time is $O(mn)$.

The visited grid occupies $\Theta(mn)$ space. Direction and coordinate variables use $O(1)$, while the required output list occupies $\Theta(mn)$. Excluding output, exact auxiliary space is still $O(mn)$, contrary to the manifest's $O(1)$ entry.

## Alternatives and edge cases

- **Four shrinking boundaries:** Track top, bottom, left, and right bounds and traverse one perimeter at a time. It achieves the same $O(mn)$ time with genuine $O(1)$ auxiliary space.
- **Destructively mark the matrix:** Replace visited elements with a sentinel. This removes `vis` but mutates input and is unsafe if the sentinel may be a legitimate value.
- **Layer index formulas:** Compute each ring's coordinates directly. It avoids a visited grid but is more vulnerable to duplicate center-row or center-column handling.
- **Single row:** The walker moves right through all cells; only the irrelevant post-final update points outside.
- **Single column:** The first blocked right move turns downward, and all cells are visited once.
- **One cell:** It is appended and marked; any invalid next coordinate is never read because the loop ends.
- **Rectangular rather than square:** Boundary tests use independent `m` and `n`, so either dimension may be larger.
- **Repeated values:** Visitation is coordinate-based, not value-based. Equal integers in different cells are all returned.
- **Input preservation:** The matrix is only read. The separate Boolean grid holds traversal state.
- **Post-final coordinate:** It may be invalid or visited, but no subsequent iteration dereferences it, so it cannot affect the returned answer.
