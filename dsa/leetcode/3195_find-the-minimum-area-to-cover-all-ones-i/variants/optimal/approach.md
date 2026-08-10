## General

**An axis-aligned rectangle is fixed by four extremes.** The required rectangle has horizontal and vertical sides, so it can be described by its top row, bottom row, left column, and right column. To contain every cell whose value is one, its top boundary cannot lie below the smallest row containing a one, and its bottom boundary cannot lie above the largest such row. The analogous statement holds for columns.

Define

$$
r_{\min}=\min\{i:\texttt{grid}[i][j]=1\},
\qquad
r_{\max}=\max\{i:\texttt{grid}[i][j]=1\},
$$

and similarly define $c_{\min}$ and $c_{\max}$ over the column coordinates of all ones. The unique tight bounding rectangle spans rows $r_{\min}$ through $r_{\max}$ and columns $c_{\min}$ through $c_{\max}$.

The source names these four quantities `x1`, `x2`, `y1`, and `y2`. It initializes minima to positive infinity and maxima to negative infinity:

`x1 = y1 = inf` and `x2 = y2 = -inf`.

Those sentinels guarantee that the first encountered one replaces all four relevant extremes without needing a special “first one” branch.

**Scan every cell and update only on a one.** The nested `enumerate` loops visit row index `i`, column index `j`, and cell value `x`. Zeros impose no containment requirement and are ignored. For a one, the code updates:

- `x1 = min(x1, i)` for the topmost occupied row;
- `x2 = max(x2, i)` for the bottommost occupied row;
- `y1 = min(y1, j)` for the leftmost occupied column;
- `y2 = max(y2, j)` for the rightmost occupied column.

After processing any prefix of the traversal, these variables are exactly the coordinate extremes among the ones seen so far. The min and max updates preserve that invariant when another one appears. Once every cell has been visited, they are the global extremes.

**Use inclusive dimensions.** If occupied rows range from `x1` through `x2` inclusive, the number of rows is

$$
x_2-x_1+1.
$$

The plus one is essential. For a rectangle covering only row $4$, the height must be $4-4+1=1$, not zero. The width is similarly `y2 - y1 + 1`. Multiplying them gives the number of grid cells in the rectangle:

`(x2 - x1 + 1) * (y2 - y1 + 1)`.

**Why no smaller rectangle can work.** Any valid axis-aligned rectangle must contain a one in row $r_{\min}$ and a one in row $r_{\max}$. Its vertical span must therefore include every row from $r_{\min}$ through $r_{\max}$, so its height is at least $r_{\max}-r_{\min}+1$. Independently, it must contain ones at columns $c_{\min}$ and $c_{\max}$, so its width is at least $c_{\max}-c_{\min}+1$.

The rectangle constructed from those exact four boundaries contains every one: each one's row lies between the row extremes, and each one's column lies between the column extremes. It achieves both necessary lower bounds simultaneously. Any rectangle extending farther in any direction has no smaller area, while moving any boundary inward would exclude at least one extreme one. Hence this bounding rectangle has the minimum possible area.

The extreme row and extreme column do not need to belong to the same one. For example, the topmost one may be near the right edge and the leftmost one near the bottom. An axis-aligned rectangle must satisfy both coordinate ranges at once, which is exactly why four independent extremes determine it.

**Trace a small grid.** For

`[[0,1,0],[1,0,1]]`,

the ones occur at $(0,1)$, $(1,0)$, and $(1,2)$. The row extremes are $0$ and $1$, so height is two. The column extremes are $0$ and $2$, so width is three. The area is $2\cdot3=6$. Although some cells inside that rectangle are zero, the rectangle is allowed to contain zeros; it only needs to contain all ones.

For `[[1,0],[0,0]]`, all four extremes are zero. Both inclusive dimensions are one and the answer is one.

**Why the nonempty-one guarantee matters.** If the grid contained no one, the infinity sentinels would never be replaced, and the arithmetic would not describe a rectangle. The problem explicitly guarantees at least one one, so the return expression always uses finite integer coordinates. The exact source relies on that contract rather than adding a separate empty case.

## Complexity detail

Let $R$ be the number of rows and $C$ the number of columns. The nested loops inspect all $RC$ cells exactly once. Each cell causes constant work, so total time is $O(RC)$. In the worst case, this is necessary: if an algorithm skips an arbitrary cell, that cell could contain the only one that extends one boundary, changing the answer.

Only four boundary variables plus loop variables are stored. Their number does not depend on grid dimensions, so auxiliary space is $O(1)$. The scan reads but never modifies `grid`.

Python's `inf` values are floating-point sentinels, but after at least one one is processed, every boundary becomes an integer index through `min` or `max`. The final result is therefore an integer under the promised input. At most $1000\cdot1000$ cells lie in the rectangle, well within ordinary integer ranges; Python would handle larger products exactly as well.

## Alternatives and edge cases

- **Four directional boundary scans:** Search from the top until finding a one, then from the bottom, left, and right. It can stop early in favorable layouts but still costs $O(RC)$ in the worst case and may revisit cells.
- **Collect all one coordinates:** Taking minima and maxima from a coordinate list is correct, but storing up to $RC$ pairs wastes $O(RC)$ space when four running extremes suffice.
- **Row and column presence arrays:** Mark which rows and columns contain a one, then find first and last marked positions. This uses $O(R+C)$ extra space without improving worst-case scan time.
- **Prefix sums plus binary search:** A 2D prefix structure can answer whether regions contain ones and locate boundaries, but building it already costs $O(RC)$ time and $O(RC)$ space for a one-time query.
- **Exactly one one:** All minima and maxima become that cell's coordinates, producing height one, width one, and area one.
- **All ones:** The extremes are the grid's four outer boundaries, so the answer is the full area $RC$.
- **One occupied row:** `x1 == x2` gives height one; the width still spans from the leftmost to rightmost one.
- **One occupied column:** The symmetric calculation gives width one.
- **Zeros inside the rectangle:** They do not matter. The rectangle need not be filled with ones; it only has to cover all of them.
- **Disconnected one clusters:** Connectivity is irrelevant. The extremes enclose every cluster, including gaps between them.
- **Inclusive endpoints:** Omitting either `+ 1` would produce zero area for a single occupied row or column and undercount every other rectangle.
- **No-one input outside the contract:** The infinity sentinels would remain and the return expression would be invalid. A general-purpose version would handle this separately, but the exact source correctly relies on the stated at-least-one-one guarantee.
- **Rectangles cannot rotate:** “Horizontal and vertical sides” means an axis-aligned bounding box. A tilted geometric rectangle is outside the problem definition.
- **Input preservation:** The method only reads each cell and leaves the grid unchanged.
