## General

**Turning a path problem into a row-by-row decision**

A falling path chooses exactly one cell from every row. After choosing column `j` in one row, the next choice may use column `j - 1`, `j`, or `j + 1`, provided that column exists. The important consequence is that, when we are deciding how cheaply a path can end at one particular cell, we do not need the full history of every possible path. We only need the best path sums that reached the previous row.

That observation gives the dynamic-programming state used by the solution:

- Before processing a row, `f[j]` is the minimum sum of a falling path that ends in column `j` of the previously processed row.
- While processing the current row, `g[j]` becomes the minimum sum of a falling path that ends at the current row's cell in column `j`.

There are `n` columns, so both arrays have length `n`.

**Why an all-zero initial row is correct**

The code begins with `f = [0] * n`. This does not claim that the matrix has a real row of zeros. It is a convenient virtual row placed immediately above the first real row.

For a first-row cell with value `x`, the transition takes the minimum of one, two, or three zeros and adds `x`. Therefore, `g[j]` becomes exactly `x`. This matches the rule that a falling path may start at any cell in the first row: there is no earlier cost and no preferred starting column.

An alternative implementation could copy the first matrix row into `f` and begin the loop at the second row. The virtual-row initialization expresses the same logic with one uniform loop for every row.

**Finding the legal predecessors**

For a cell in column `j`, the legal predecessor columns are `j - 1`, `j`, and `j + 1`, but boundary columns require care. Column `0` has no predecessor at `-1`, and column `n - 1` has no predecessor at `n`.

The code computes:

- `l = max(0, j - 1)`, the first legal predecessor column;
- `r = min(n, j + 2)`, one position after the last legal predecessor column.

Python slices exclude their right endpoint, so `f[l:r]` contains exactly the valid portion of `f` among columns `j - 1` through `j + 1`. The `j + 2` is intentional: to include index `j + 1` in a slice, the exclusive endpoint must be one greater.

The assignment `g[j] = min(f[l:r]) + x` first chooses the cheapest legal path into this cell and then adds the current cell value `x`. It does not matter whether some matrix values are negative. The recurrence compares complete path sums, and adding a negative value is handled naturally.

**Why the solution builds a separate array**

Every state for the current row must depend only on the previous row. If the code overwrote `f` from left to right, a later column could accidentally use a value already updated for the current row. That would mix two rows and could represent an illegal sideways movement.

The fresh array `g` prevents that contamination. During the inner loop, `f` remains the completed previous row and `g` receives only current-row results. After every column has been processed, `f = g` advances the dynamic program by one whole row.

**A small trace**

Suppose one previous-row state is `f = [5, 2, 8]` and the next matrix row is `[4, -3, 6]`.

- For column `0`, the predecessor slice is `f[0:2] = [5, 2]`. The best new sum is `2 + 4 = 6`.
- For column `1`, the predecessor slice is `f[0:3] = [5, 2, 8]`. The best new sum is `2 + (-3) = -1`.
- For column `2`, the predecessor slice is `f[1:3] = [2, 8]`. The best new sum is `2 + 6 = 8`.

The new state is therefore `g = [6, -1, 8]`. Notice that the negative middle value improves paths that reach it, but it does not change which moves are legal.

**Why the final minimum is the answer**

After the last row is processed, `f[j]` is the minimum sum among all falling paths that end at the last-row column `j`. A valid path may finish in any column, so `min(f)` selects the best legal endpoint.

The reasoning can be made precise by induction over the rows. The virtual-row initialization correctly gives every first-row cell a starting cost of zero plus its own value. Assume `f` correctly stores the best sums for one completed row. Every path ending at current column `j` must come from one of the columns in `f[l:r]`, and every state in that slice can legally move to `j`. Taking the minimum therefore considers all and only legal predecessors, while adding `x` accounts for the current cell. Thus `g[j]` is correct for every column. The induction reaches the final row, where taking the minimum gives the globally smallest falling-path sum.

## Complexity detail

Let `n` be both the number of rows and the number of columns in the square matrix.

The outer loop visits all `n` rows, and the inner loop visits all `n` cells in each row. For each cell, the slice contains at most three values, so taking its minimum costs constant time. The total time complexity is therefore `O(n^2)`.

The dynamic program keeps two arrays of length `n`: `f` for the previous row and `g` for the current row. At any moment, their combined size is linear, so the auxiliary space complexity is `O(n)`. The small slices contain at most three elements and do not change that bound.

The input matrix itself already occupies `O(n^2)` space, but that storage belongs to the input and is not additional memory created by this algorithm. The solution also leaves the matrix unchanged.

## Alternatives and edge cases

- **Full two-dimensional dynamic-programming table:** Store the best sum for every cell. The recurrence is easy to visualize, but only the immediately previous row is ever needed, so the extra `O(n^2)` auxiliary space provides no benefit for the returned value.
- **Updating one array in place:** This is possible only with extra care, such as preserving old neighboring values before overwriting them. A straightforward left-to-right overwrite is wrong because it lets the current row influence itself. The separate `g` array makes the row boundary explicit and safer.
- **Top-down recursion with memoization:** A recursive function can ask for the best path beginning at or ending at each cell. Memoization still yields `O(n^2)` time, but it adds recursion overhead and can use `O(n^2)` memo space instead of the rolling `O(n)` state.
- **Greedily choosing the smallest next cell:** A locally smallest neighbor need not lead to the smallest total, because later rows can reward a temporarily larger choice. Dynamic programming preserves the best cost for every possible ending column instead of committing too early.
- **Single-cell matrix:** When `n = 1`, the only slice contains the single virtual zero, and the final minimum is the only matrix value. No special branch is required.
- **First and last columns:** The clamped slice endpoints are essential. They prevent Python's negative indexing from turning a nonexistent left neighbor into the last column and prevent a nonexistent right neighbor from being considered.
- **Negative entries:** Negative values do not break the method and do not require cycle detection. A path always moves down exactly one row, so the dependency graph is acyclic and every path contains exactly `n` cells.
- **Several equally good paths:** The state stores only their shared minimum sum, not the path itself. That is sufficient because the problem asks only for the minimum value. Reconstructing an actual path would require recording predecessor choices.
