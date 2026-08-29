## General

**Search sizes from largest to smallest.** A candidate square is determined by its side length and top-left corner. The outer loop tries `k = min(m, n)` down through two. As soon as any square of a size passes, that size is returned; no smaller size can improve the answer. If none passes, the method returns one because every single cell is trivially a magic square.

**Precompute row and column prefix sums.** `rowsum[i][j]` uses one-based storage and equals the sum of grid row `i - 1` across the first `j` columns. Its recurrence extends leftward prefix `rowsum[i][j - 1]`. Similarly, `colsum[i][j]` equals the sum of grid column `j - 1` across the first `i` rows and extends `colsum[i - 1][j]`.

Both arrays have `(m + 1)` rows and `(n + 1)` columns filled initially with zero. Padding lets a segment beginning at grid index zero subtract a valid zero prefix rather than requiring a boundary branch.

**Define the candidate by inclusive corners.** Helper `check(x1, y1, x2, y2)` receives the zero-based top-left and bottom-right corners. All candidates passed to it are square, with side `x2 - x1 + 1 = y2 - y1 + 1`. It first uses the top row as the common target sum:

`val = rowsum[x1 + 1][y2 + 1] - rowsum[x1 + 1][y1]`.

The right prefix includes column `y2`, and subtracting the prefix before `y1` leaves exactly columns `y1` through `y2`.

**Verify every remaining row.** Rows `x1 + 1` through `x2` are checked against `val` using the same constant-time row-prefix difference. The first row is skipped because it defined `val`. Any mismatch returns false immediately, saving column and diagonal work for an already invalid square.

**Verify every column.** For each column `j` from `y1` through `y2`, the segment sum is

`colsum[x2 + 1][j + 1] - colsum[x1][j + 1]`.

This includes rows `x1` through `x2`. Every column, including the first, must equal `val`. A mismatch again rejects immediately.

**Compute both diagonals directly.** The main diagonal starts at `(x1, y1)` and increments row and column together until `x2`. The anti-diagonal starts at `(x1, y2)`, increments row, and decrements column. Each loop accumulates exactly one cell per square row. Both sums must equal `val`. Row and column prefixes do not directly answer diagonal queries, and only two diagonals exist, so an $O(k)$ direct scan is appropriate.

**Enumerate every placement of one size.** For fixed `k`, top row `i` continues while `i + k - 1 < m`, and top column `j` continues while `j + k - 1 < n`. The calculated `i2` and `j2` are the inclusive bottom and right boundaries. These limits reach every in-bounds `k`-by-`k` submatrix exactly once.

**Why all magic conditions are necessary.** Equal rows alone do not ensure equal columns or diagonals. Equal rows and columns still do not force either diagonal. The helper explicitly checks all `k` rows, all `k` columns, and both diagonals against one common value. Conversely, if every check passes, that is exactly the definition of a magic square; distinct cell values are not required.

**Why the first successful return is globally largest.** The loops examine all placements for a given side before moving to the next smaller side, and sides descend. If `check` succeeds, the candidate really is magic by the line-sum verification. Every unexamined size is smaller, so returning immediately cannot miss a larger answer. Default one handles the only omitted size and is always valid.

**Trace the work saved by prefixes.** Without preprocessing, summing each of `k` rows and `k` columns would inspect $O(k^2)$ cells per candidate. Prefix differences reduce every row and column sum to constant time, leaving $O(k)$ line comparisons and $O(k)$ diagonal traversal. This is the decisive optimization within exhaustive candidate enumeration.

## Complexity detail

Let $S=\min(m,n)$. Prefix construction costs $O(mn)$ time and space. For side length $k$, there are at most $O(mn)$ placements, and checking one placement takes $O(k)$ time in the worst case for rows, columns, and diagonals. Summing over all sizes gives

$$
O\left(mn\sum_{k=1}^{S}k\right)=O(mnS^2).
$$

This matches the manifest. Early rejection and descending early success often reduce actual work but not the worst-case bound.

`rowsum` and `colsum` each contain $(m+1)(n+1)$ integers, so auxiliary space is $O(mn)$. The check helper uses only scalar sums and indices beyond those tables.

Grid values can be up to $10^6$, and a line contains at most 50 values, so line sums fit ordinary 32-bit signed range here. Python integers are safe regardless.

## Alternatives and edge cases

- **Diagonal prefix sums:** Two additional diagonal-prefix tables can make each diagonal sum $O(1)$, but checking all $k$ rows and columns still costs $O(k)$ per candidate, so the overall asymptotic bound remains unchanged.
- **Brute-force all cells per candidate:** Recomputing each line from scratch costs $O(k^2)$ per square and raises the total bound substantially.
- **Check only total row and column sums:** Equal totals across the whole square do not prove each individual row and column is equal. Every line must be tested.
- **Single row or column grid:** No side length above one is enumerated, and the method returns one.
- **One-by-one squares:** They are not passed to `check` because they are always magic; the final return handles them.
- **Repeated values:** Allowed by the definition. The algorithm compares sums only and never imposes uniqueness.
- **Rectangular grid:** Candidate side is bounded by `min(m, n)`, and placement loops independently respect both dimensions.
- **Early mismatch:** The helper returns as soon as a row, column, or diagonal differs. This is safe because one failed required equality disproves the candidate.
- **Prefix off-by-one:** Stored coordinates are shifted by one, while helper corners are zero-based and inclusive. The `+1` endpoints and unshifted subtraction boundaries are essential.
