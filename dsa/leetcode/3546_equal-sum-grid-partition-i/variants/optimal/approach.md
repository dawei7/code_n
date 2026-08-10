## General

**A straight cut is determined by complete row or column prefixes**

A horizontal cut between rows `i` and `i+1` places rows zero through `i` in the top section and all later rows in the bottom.

A vertical cut between columns `j` and `j+1` places columns zero through `j` on the left and all later columns on the right.

No other submatrix shapes are permitted. Therefore, it is enough to compare cumulative sums of whole leading rows and whole leading columns with half of the total grid sum.

**Reject an odd total immediately**

Let total grid sum be `s`. Equal integer section sums would each be `s/2`. If `s` is odd, no such integer split exists, so the source returns false immediately.

This is a necessary condition, not a sufficient one; an even total still needs a cut boundary whose prefix sum is exactly half.

**Check horizontal cuts**

`pre` starts at zero. For each row, the source adds `sum(row)`. After processing row `i`:

`pre` equals the sum of every cell in rows zero through `i`.

The complementary bottom section has sum `s-pre`. They are equal exactly when:

`2*pre = s`.

The condition also requires `i != len(grid)-1`. A cut after the final row would leave the second section empty, which the problem forbids.

Although the loop computes the full-grid prefix at the final row, it explicitly refuses to treat that boundary as a cut.

**Check vertical cuts**

The source resets `pre` and traverses:

`zip(*grid)`.

Each yielded tuple `col` contains one complete grid column from top to bottom. After adding its sum at column `j`, `pre` is the sum of columns zero through `j`.

The same equality `2*pre=s` detects equal left and right totals, while `j != columns-1` ensures the right section is non-empty.

Horizontal success returns immediately; if none exists, vertical cuts are checked. The task permits either orientation, so this ordering cannot miss a valid answer.

**Why no two-dimensional prefix table is needed**

Every candidate section spans the full width or full height. For a horizontal cut, only row totals matter; for a vertical cut, only column totals matter.

A full 2D prefix matrix can answer these sums, but it stores information about arbitrary rectangles that the problem never asks for. Two running scalars are logically sufficient.


Every legal horizontal cut has a unique last top-row index `i < m-1`. On iteration `i`, `pre` is exactly its top-section sum. If the cut is equal, the source's equality succeeds.

Conversely, whenever the equality succeeds at a nonfinal row, the top and bottom are both non-empty and have sums `pre` and `s-pre=pre`. Thus the source returns true only for a valid cut.

The vertical proof is identical with column indices. If neither scan succeeds, no allowed boundary creates equal sums, so false is correct.

**A two-by-two example**

For `[[1,4],[2,3]]`, total is ten. After the first row, `pre=5` and the row is not final, so `2*pre=10` proves a horizontal cut with sums five and five.

For a one-row grid, the horizontal loop cannot accept its only row because it is final. The vertical scan still considers every boundary before the last column.

**Exact-source space caveat**

The algorithmic idea needs only constant scalar state beyond the input. However, the exact Python expression `zip(*grid)` creates one iterator per row and yields a tuple containing all `m` entries of each column. At least `O(m)` transient/reference storage is involved.

Therefore the protected Python implementation's practical auxiliary space is `O(m)`, not a strict `O(1)`, even though it avoids a full `O(mn)` matrix. An index-based nested loop accumulating column sums could use `O(n)` column totals, while rescanning each column with scalar state avoids the tuple but retains linear time.

## Complexity detail

Let the grid have `m` rows and `n` columns, with `mn <= 100,000`.

Computing the total visits every cell once. The horizontal scan sums every row again, and the vertical scan visits every cell through column tuples in the worst case. A constant number of full traversals gives `O(mn)` time.

The exact source uses `O(m)` auxiliary iterator/tuple space during `zip(*grid)`. It otherwise stores only scalar sums. This is smaller than a 2D prefix table but does not literally match the manifest's `O(1)` claim for Python execution.

Grid sums can reach `10^10`, so fixed-width implementations should use 64-bit integers. Python is safe automatically.

## Alternatives and edge cases

- **2D prefix sum:** Correct in `O(mn)` time but uses `O(mn)` space for more general rectangle queries than needed.
- **Store row and column sums:** Two arrays give `O(m+n)` space and a straightforward single cell pass.
- **Rotate the grid:** Lets one horizontal routine handle both orientations but allocates another matrix.
- **Check arbitrary submatrices:** The cut must span the whole grid, so arbitrary rectangle enumeration solves a different problem.
- **Odd total:** Immediate false is safe because integer halves cannot be equal.
- **One row:** No horizontal cut is legal, but vertical cuts may be.
- **One column:** No vertical cut is legal, but horizontal cuts may be.
- **Two cells total:** There is exactly one possible boundary along the non-singleton dimension.
- **Cut after the last row or column:** Explicit final-index checks reject the empty complementary section.
- **Positive entries:** Prefix sums strictly increase, but the source does not rely on early termination; equality logic is sufficient.
- **First possible boundary:** It is checked after the first row or column, so both sections are non-empty when another line remains.
- **zip space behavior:** The conceptual running-sum method is constant-state, but exact Python tuple/iterator materialization gives an `O(m)` caveat.
- **Even total without matching boundary:** The scans finish and correctly return false.
