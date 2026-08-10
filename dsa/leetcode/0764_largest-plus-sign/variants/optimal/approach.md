## General

**A center’s order is limited by four directional runs**

For cell `(r, c)`, let the consecutive-one counts ending or beginning there be left, right, up, and down. A plus centered there can extend only as far as its shortest arm, so its order is the minimum of those four counts.

The exact solution stores that running minimum directly in `dp[r][c]`.

**Initialize cells as possible ones or definite mines**

Every entry begins as `n`, a safe upper bound on any directional run in an `n x n` grid. Mine coordinates are set to zero.

During directional scans, only zero versus nonzero is used to decide whether a cell is a mine. Reducing a nonmine’s `dp` value never changes its truthiness, so the same matrix can store both occupancy and progressively refined arm limits.

**Scan four directions in paired loops**

For each outer index `i`, the inner loop pairs ascending `j` with descending `k`:

- `dp[i][j]` receives the leftward run ending at row `i`, column `j`.
- `dp[i][k]` receives the rightward run beginning there.
- `dp[j][i]` receives the upward run ending in column `i`.
- `dp[k][i]` receives the downward run beginning there.

Each running counter increases by one on a nonmine and resets to zero on a mine.

**Why taking a minimum after every pass works**

An entry starts above every possible true run length. After the left pass it is limited by left reach. The right update takes the minimum with right reach, then vertical updates add the up and down limitations.

After all four directional contributions, `dp[r][c]` equals exactly the smallest run count, which is the largest valid plus order at that center.

**Why in-place updates do not corrupt mine detection**

The counters test `if dp[cell]`. Mines always remain zero because every minimum with zero stays zero. Nonmines always retain a positive count: each direction sees at least the cell itself, so its run is at least one.

Therefore a previously refined positive value still correctly means “original grid value one.”

**Trace an order-two center**

If a center has at least two consecutive ones including itself in all four directions, its directional counts are each at least two and its minimum is at least two. If a mine interrupts one direction immediately after the center, that direction’s count is only one, limiting the plus to order one regardless of longer other arms.

**Understanding the order convention**

Order counts the center itself. An order-one plus is a single one-valued cell with zero-length arms. An order-two plus needs the center plus one cell in each direction. This is why directional run lengths can be used directly without subtracting one.

**Why the paired loop covers every cell in every direction**

For fixed `i`, ascending `j` visits every column of row `i` from left to right, while descending `k` visits the same row from right to left. At the same time, `dp[j][i]` and `dp[k][i]` visit every row of column `i` from top and bottom.

Repeating this for every `i` covers all rows horizontally and all columns vertically. The pairing is a compact way to perform four complete sweeps, not a partial diagonal traversal.

**No explicit grid is required**

The mine list fully specifies which cells are zero; every other coordinate is one. Initializing `dp` positively and replacing mines with zero reconstructs exactly the occupancy information needed by the scans.

**Why the maximum cell value is the answer**

Every possible plus has one center. For that center, the DP value is its greatest feasible order. Taking the maximum over all cells therefore considers every possible plus and selects the largest.

If every cell is a mine, all values are zero and the answer is zero.


The four scans compute exact consecutive nonmine lengths in their respective directions by the standard reset-or-increment recurrence. Successive minima preserve the smallest of all processed directions.

Once all directions are processed, each cell stores exactly the maximum order supported at that center. The global maximum is therefore exactly the largest axis-aligned plus in the grid.

## Complexity detail

The algorithm initializes `n^2` cells and performs a constant amount of work for each cell in the paired directional scans. Time complexity is `O(n^2)`.

The DP matrix contains `n^2` integers, so auxiliary space is `O(n^2)`. Direction counters and indices use `O(1)` additional state.

## Alternatives and edge cases

- **Four separate matrices:** Store each directional count independently. This is easier to visualize but uses four times the asymptotic storage.

- **Expand from every center:** Trying arm lengths separately can cost `O(n^3)`.

- **Check only horizontal and vertical totals:** Both sides of each axis matter independently; the shortest of four arms determines order.

- **Single nonmine cell:** All four counts are one, giving order one.

- **Mine cell:** Its value remains zero through every pass and cannot be a center.

- **All mines:** The maximum DP value is zero.

- **Values beyond the arms:** They are irrelevant; only consecutive ones through the required arm length matter.
