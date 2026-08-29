## General

**Identify both diagonal coordinates from one row index**

In an $N$-by-$N$ square matrix, the primary diagonal uses coordinates:

`(i, i)`.

The secondary diagonal uses:

`(i, N - i - 1)`.

The source visits each row once with `enumerate(mat)`. Variable `i` is the row index and `row` is that row's list.

It computes `j = n - i - 1`, the secondary-diagonal column for the same row.

Thus one iteration can add every diagonal contribution belonging to row `i` without scanning any off-diagonal cell.

**Always include the primary diagonal**

`row[i]` is the primary-diagonal entry for the current row. It is always added.

As `i` runs from zero through `n-1`, these positions move from the top-left corner to the bottom-right corner. Every primary entry appears exactly once.

No matrix-value condition is involved; membership is determined solely by coordinates.

**Include the secondary entry unless it is the same cell**

`row[j]` is the secondary-diagonal entry. Usually `j != i`, so the source adds it as well.

For an odd-sized matrix, both diagonals meet at the center. At the center row:

$$
i=n-i-1.
$$

That single cell belongs to both diagonal descriptions but must be counted once.

The expression `0 if j == i else row[j]` contributes zero instead of adding the secondary entry again at the intersection.

For an even-sized matrix, no integer row satisfies the equality, so every row contributes two different cells.

**Why the conditional is simpler than subtracting later**

Another common method adds both diagonals for every row and subtracts the center once when `n` is odd.

The exact source prevents duplication locally. Every iteration adds one primary value and either one distinct secondary value or zero when both coordinates coincide.

This makes the invariant “every already-processed diagonal cell has been counted exactly once” hold throughout the loop, not merely after a correction.

**Tracing a three-by-three matrix**

At row zero, `i = 0` and `j = 2`. The source adds top-left one and top-right three.

At row one, both indices equal one. It adds center five once and adds zero for the duplicate secondary coordinate.

At row two, it adds bottom-right nine and bottom-left seven.

The total is one plus three plus five plus nine plus seven, or twenty-five.

**Tracing an even matrix**

For size four, secondary columns are three, two, one, and zero while primary columns are zero, one, two, and three.

No row has equal diagonal columns. Each of four rows contributes two distinct cells, so eight values are summed.

The method requires no parity branch because coordinate equality detects overlap directly.

**The one-cell case**

When `n = 1`, the only iteration has `i = j = 0`.

The source adds `row[0]` and zero, returning the sole matrix value. This handles both diagonals collapsing completely into one cell.

**A loop invariant**

Before processing row `i`, `ans` equals the sum of all distinct primary- and secondary-diagonal cells in earlier rows.

The current iteration adds the row's primary cell. It then adds the secondary cell only if that coordinate is distinct.

No diagonal cell belongs to a different row than its own coordinate row, so later iterations cannot duplicate these cells. The invariant advances.

After every row, the accumulated set is exactly the union of both diagonals, proving correctness.

**Why square shape matters**

The formula `n-i-1` assumes every row has `n` columns and that row and column index ranges have the same length.

The contract guarantees a square matrix. For a rectangular matrix, “both main diagonals” would require a different definition and coordinate range.

**No need to inspect all N squared entries**

Only one or two entries per row can belong to the requested diagonals. Scanning the full matrix would perform unnecessary work.

Direct coordinate formulas reduce the operation to the number of rows.

## Complexity detail

Let $N$ be matrix dimension. The loop runs exactly $N$ times and performs constant indexing and arithmetic per row. Time is $O(N)$, matching the manifest.

`ans`, `n`, loop references, and column `j` use constant auxiliary state. Space is $O(1)$.

The input matrix is read-only, and no diagonal list is constructed.

## Alternatives and edge cases

- **Add both then subtract center:** Sum `mat[i][i]` and `mat[i][n-i-1]` for all rows, then subtract the center for odd `n`. It is equivalent.
- **Scan every cell:** Check whether `i == j` or `i+j == n-1`, but this costs $O(N^2)$.
- **Build diagonal arrays:** It adds unnecessary $O(N)$ storage.
- **Odd dimension:** Exactly one center cell lies on both diagonals.
- **Even dimension:** The diagonals share no cell.
- **One-by-one matrix:** The single value is counted once.
- **Equal values at different cells:** They are separate coordinates and must both be counted.
- **Secondary formula:** The column decreases from `n-1` to zero as the row increases.
- **Positive-value constraint:** It is not required for the indexing logic; the same method would sum negative values correctly.
- **Square guarantee:** It makes primary and secondary diagonal lengths both equal to `N`.
- **No mutation:** Matrix values and row structure remain unchanged.
- **Overlap test:** Comparing coordinates, not values, is the correct way to prevent double counting.
