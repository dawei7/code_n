## General

Every cell offers exactly two next moves: straight down to the same column or down-right to the next column. This makes the problem a collection of overlapping smaller questions: what is the minimum sum from a particular cell to the bottom?

The selected solution answers those questions bottom-up. When it processes a cell, both possible continuation costs in the row below have already been computed.

**The dynamic-programming state**

Let the triangle have $r$ rows. `f[i][j]` is the minimum sum of a valid path that starts at `triangle[i][j]`, includes that cell, and ends somewhere in the bottom row.

The required answer is `f[0][0]` because the triangle has one top cell and every complete path begins there.

The table is allocated as a square `(r + 1) x (r + 1)` grid of zeros, even though only triangular positions are meaningful. The extra row `f[r]` acts as a zero-cost base just below the actual bottom row.

**Why the extra zero row works**

For a bottom-row cell `(r - 1, j)`, the recurrence reads `f[r][j]` and `f[r][j + 1]`. Both are zero. Therefore:

`f[r - 1][j] = triangle[r - 1][j]`.

That is exactly correct: a path starting on the bottom row already ends there and includes only its current value.

Using this artificial base removes a separate bottom-row branch. It is safe because zeros are used only as continuation costs beneath actual leaves, not as optional exits from higher rows.

**The choice at an interior row**

From cell `(i, j)`, the only legal next cells are `(i + 1, j)` and `(i + 1, j + 1)`. Their stored values are the best costs from those children to the bottom.

Any complete path through the current cell must choose one of them. Taking the smaller child cost and adding `triangle[i][j]` therefore gives:

$$
f[i][j]
=
\texttt{triangle}[i][j]
+
\min\bigl(f[i+1][j],f[i+1][j+1]\bigr).
$$

There is no need to remember which child won because the function returns only the minimum sum, not the actual path.

**Why rows are processed upward**

The outer loop visits `i = r - 1, r - 2, ..., 0`. By the time row `i` is processed, row `i + 1` is complete.

Within one row, every cell reads only the row below, so left-to-right column order is safe. Cells in the same row do not depend on one another.

A top-down fill would need best costs from parents instead and would require special handling for left and right boundaries. Bottom-up movement is simpler because every non-bottom triangle cell always has exactly two legal children.

**Why the recurrence gives the global minimum**

For the bottom row, the table stores each cell value, which is the exact minimum path beginning there.

Assume row `i + 1` stores exact minimum continuation sums. Every path from `(i, j)` first chooses one of its two legal children and then follows a path from that child. The best possible continuation through each child is already known, so choosing their minimum and adding the current value is exact.

This establishes the state definition for row `i`. Applying the argument upward reaches `(0, 0)`, proving that `f[0][0]` is the minimum over every legal top-to-bottom path.

**Tracing the Reference example**

For bottom row `[4, 1, 8, 3]`, the zero base produces the same costs `[4, 1, 8, 3]`.

Moving up to `[6, 5, 7]` gives:

- six plus `min(4, 1)`, producing seven;
- five plus `min(1, 8)`, producing six;
- seven plus `min(8, 3)`, producing ten.

The next row `[3, 4]` becomes `[3 + min(7, 6), 4 + min(6, 10)] = [9, 10]`. The top value two becomes `2 + min(9, 10) = 11`.

The choices correspond to values two, three, five, and one.

**Negative values require no special handling**

The recurrence compares complete optimal continuation sums, not individual next values. Negative numbers can make a longer-looking route cheaper, but every path has exactly one cell per row, and the stored child costs already include all future effects.

Greedy selection of the smaller immediate child would be incorrect because a slightly larger child can lead to much more negative descendants. Dynamic programming evaluates the entire remaining route.

**Input and source behavior**

The method never modifies `triangle`; it writes all results into `f`. The positive row-count constraint guarantees `f[0][0]` corresponds to a real top cell.

The annotation uses `List[List[int]]` without importing `List`. A standalone environment must supply it or add `from typing import List`.

## Complexity detail

Let $N$ be the total number of triangle cells and $r$ the number of rows. Since

$$
N=\frac{r(r+1)}{2}=\Theta(r^2),
$$

the nested loops perform exactly one constant-time update per cell. Time is $\Theta(N)=\Theta(r^2)$, matching the manifest's $O(N)$ claim.

The selected source allocates `(r + 1)^2` integer cells in `f`. Its exact auxiliary space is $\Theta(r^2)=\Theta(N)$, not the manifest's $O(r)$.

Only one row below is needed at a time, so a rolling list can reduce workspace to $O(r)$. An in-place bottom-up update of the input can reduce extra space further to $O(1)$, but neither optimization appears in this exact source.

The returned integer uses constant output space. The quadratic table is entirely auxiliary because the contract does not request the intermediate costs.

## Alternatives and edge cases

- **One-dimensional bottom-up DP:** Copy the bottom row and repeatedly replace each prefix cell with the current triangle value plus the minimum of two children. It uses $O(r)$ space.
- **In-place triangle update:** Overwrite each cell with its minimum continuation cost. It uses $O(1)$ extra space but destroys the caller's input.
- **Top-down rolling row:** Store the minimum root-to-current cost for each cell. Boundary cells have one parent and interiors have two.
- **Memoized recursion:** Define the same minimum-from-cell state recursively and cache it. It uses $O(N)$ memo space plus $O(r)$ call stack.
- **Greedy smaller child:** Incorrect because it ignores all values below that child.
- **One-row triangle:** Both child base costs are zero, so the sole value is returned.
- **Negative cells:** Fully supported; do not clamp sums to zero or assume monotonic growth.
- **Triangle shape:** Row `i` must contain `i + 1` values so child indices `j` and `j + 1` exist.
- **No input mutation:** The separate table preserves every original row.
- **Artificial base row:** Zeros are valid only because they sit below bottom cells in the recurrence.
- **Unused square cells:** Much of `f` lies outside the triangle and is never read; this is the source of avoidable quadratic space.
- **Missing typing import:** `List` must exist when annotations are evaluated.
- **Space mismatch:** The manifest's $O(r)$ describes a rolling-row alternative, not this square table.
- **Integer range:** Python integers handle sums automatically; fixed-width implementations should accommodate up to $r$ bounded cell values.
