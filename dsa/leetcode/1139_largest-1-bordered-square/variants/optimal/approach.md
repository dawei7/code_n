## General

**Only the border matters**

A candidate square is valid when every cell on its top, bottom, left, and right sides is `1`. Cells strictly inside the square may contain either `0` or `1`. Checking every border cell separately for every possible top-left corner and side length would repeatedly inspect the same horizontal and vertical runs. The solution preprocesses exactly the information needed to answer each border question in constant time.

Let `m` be the row count and `n` be the column count. Two `m` by `n` tables are built:

- `down[i][j]` is the number of consecutive ones beginning at `grid[i][j]` and continuing downward;
- `right[i][j]` is the number of consecutive ones beginning at `grid[i][j]` and continuing to the right.

If `grid[i][j]` is zero, both values remain zero. If it is one, its downward run is one plus the run beginning immediately below, provided that row exists. Its rightward run is one plus the run beginning immediately to the right, provided that column exists.

**Why preprocessing proceeds from bottom-right to top-left**

Computing `down[i][j]` may read `down[i + 1][j]`, and computing `right[i][j]` may read `right[i][j + 1]`. Those dependent entries must already be known. Iterating rows from `m - 1` down to zero makes the cell below available, and iterating columns from `n - 1` down to zero makes the cell to the right available.

On the last row, there is no cell below, so a one has downward run length one. On the last column, there is no cell to the right, so a one has rightward run length one. The conditional expressions in the exact solution implement these boundaries without allocating a padded extra row or column.

**Test a square through four run lengths**

Consider a square with top-left corner `(i, j)` and side length `k`. Its other relevant corners are:

- top-right at `(i, j + k - 1)`;
- bottom-left at `(i + k - 1, j)`;
- bottom-right at `(i + k - 1, j + k - 1)`.

All four borders are ones exactly when these conditions hold:

- `down[i][j] >= k` for the left border;
- `right[i][j] >= k` for the top border;
- `right[i + k - 1][j] >= k` for the bottom border;
- `down[i][j + k - 1] >= k` for the right border.

Each condition checks a consecutive run that begins at the appropriate corner and spans the entire corresponding side. Values greater than `k` are acceptable because the run may continue beyond the candidate square; only the first `k` cells need to be ones.

These four conditions are sufficient. Every border cell belongs to at least one of those four runs, so if all conditions pass, the complete perimeter consists of ones. They are also necessary. If the square has an all-one border, each of the four indicated runs must extend for at least `k` cells. The test therefore has no false positives or false negatives.

The interior is never checked, which is intentional. For example, a three-by-three square with a zero only in its center remains valid because its four borders are entirely ones.

**Search from the largest possible square downward**

No square can have side length larger than `min(m, n)`. The outer loop begins at that maximum and decreases `k` to one. For a fixed `k`, a top-left row can range from zero through `m - k`, giving `m - k + 1` positions. Similarly, a top-left column ranges through `n - k`, giving `n - k + 1` positions.

As soon as a candidate passes all four border checks, the method returns `k * k`. This early return is correct because every larger side length has already been tested exhaustively. Any later candidate can have only the same or a smaller `k`, so none can have larger area. The problem asks for the number of elements, which is the square's area rather than its side length, hence the multiplication.

If no candidate of any positive size succeeds, the method returns zero. A side-one square is worth noticing: its four sides are all the same single cell. For `k = 1`, each condition asks whether a run beginning at that cell has length at least one, which is true exactly when the cell is `1`. Thus any one anywhere in the grid produces an answer of at least one, and zero is returned exactly when the grid contains no one.

**Why the algorithm is correct as a whole**

The preprocessing recurrence correctly records every downward and rightward run by reverse-order induction. Boundary cells receive one when they contain one; every earlier cell receives one plus the already correct neighboring run precisely when its own value is one.

For each candidate, the four-run equivalence proves that the constant-time test accepts exactly the squares whose borders are all ones. The descending side-length order then proves maximality: the first accepted side length is the greatest possible one. Returning its square area gives exactly the requested number of elements. If no candidate is accepted, even every side-one candidate is zero, so no valid square exists and returning zero is correct.

## Complexity detail

Let `m` and `n` be the grid dimensions, and define `q = min(m, n)`.

Building `down` and `right` visits each of the `mn` cells once and performs constant work, taking `O(mn)` time. The search considers side lengths from `q` down to one. For side length `k`, it checks `(m - k + 1)(n - k + 1)` possible top-left corners, with four constant-time table lookups per candidate.

An upper bound is `q` layers times at most `mn` candidates per layer, which gives `O(mnq)` time. The early return can make common executions much faster when a large valid square is found, but the worst case still examines candidates across all side lengths.

The two preprocessing tables each contain `mn` integers, so the auxiliary space complexity is `O(mn)`. Loop counters and dimensions require only constant additional space. The algorithm does not modify the input grid.

## Alternatives and edge cases

- **Inspect every border cell for every candidate:** This avoids preprocessing but spends `O(k)` time to validate a side-length-`k` square, adding another factor in the worst case. Directional run tables reduce each complete border test to four comparisons.
- **Two-dimensional prefix sums:** A prefix-sum table can count ones in any rectangle. Four thin rectangle queries can verify the borders in constant time, though corners must be handled carefully to avoid misleading double counts. It has similar preprocessing space but is less directly matched to the four side conditions.
- **Store upward and leftward runs instead:** That representation is equally valid if candidates are checked from their bottom-right corners. The chosen downward and rightward runs make a top-left-based test natural.
- **Binary search the side length:** Validity is not monotone in the required direction. A grid may contain a valid larger bordered square while some intermediate size has no placement, so a failed size does not safely eliminate all larger sizes. Descending enumeration is reliable.
- **All-zero grid:** Every run value is zero, no side-one candidate passes, and the method returns `0`.
- **Single one:** Its downward and rightward runs are at least one. The `k = 1` test passes and returns area `1`.
- **One row or one column:** Only side length one is possible because `q = 1`. Any one yields `1`; otherwise the answer is zero.
- **Zeros inside an otherwise valid border:** Interior values are irrelevant and deliberately ignored. The four border-run checks still accept the square.
- **A zero at any corner:** At least two required run checks begin at that corner and have value zero, so the candidate is rejected.
- **Runs longer than the candidate side:** The comparisons use `>= k` rather than equality because a valid border can be part of a longer sequence of ones.
- **Multiple largest squares:** The method returns when it finds the first one in row-major candidate order. Only the maximum area is requested, so the identity or position of the square does not matter.
- **Rectangular grid:** The largest possible side is limited by the smaller dimension. The row and column loop bounds ensure that every tested square stays inside the grid.
