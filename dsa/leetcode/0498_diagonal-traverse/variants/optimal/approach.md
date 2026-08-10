## General

Cells belong to the same top-right-to-bottom-left diagonal when their row and column indices have the same sum. Moving one row down and one column left changes `i + j` by `+1 - 1 = 0`, so the sum remains constant. The solution names that constant `k` and processes diagonals in order from `k = 0` through `k = m + n - 2`.

There are `m + n - 1` diagonals in an `m` by `n` matrix. The smallest index sum is zero at `(0, 0)`. The largest is `(m - 1) + (n - 1) = m + n - 2`. Python's `range(m + n - 1)` includes exactly those values.

**Find the topmost valid cell for one diagonal.** The traversal inside every diagonal moves down-left with `i += 1` and `j -= 1`. It therefore needs to begin at the diagonal's topmost or rightmost endpoint.

When `k < n`, column `k` exists in the first row, so the starting cell is `(0, k)`. The code sets `i = 0` and `j = k`.

When `k >= n`, column `k` would be outside the matrix. The diagonal instead begins in the last column `n - 1`. Solving `i + (n - 1) = k` gives `i = k - n + 1`. These are exactly the two conditional assignments in the source.

From that start, the loop continues while `i < m` and `j >= 0`. The start is already guaranteed to have nonnegative `i` and `j < n`, so those two changing boundaries are sufficient. Every iteration appends `mat[i][j]` to the temporary list `t`, moves down one row, and moves left one column.

For a three-by-three matrix, the diagonal `k = 2` starts at `(0, 2)` and collects positions `(0, 2), (1, 1), (2, 0)`. Their values in the example are `[3, 5, 7]`.

**Reverse every even-numbered diagonal.** The down-left collection direction matches the required output direction only for alternating diagonals. The first diagonal, `k = 0`, must conceptually travel up-right, although it contains just one element. More generally, even `k` diagonals must be output in the reverse of their down-left collection order. The code applies `t = t[::-1]` when `k % 2 == 0`.

Odd diagonals already need the down-left order and are extended unchanged. In the three-by-three example:

- `k = 0` collects `[1]` and reversal leaves `[1]`;
- `k = 1` collects `[2, 4]` and keeps that order;
- `k = 2` collects `[3, 5, 7]` and reverses to `[7, 5, 3]`;
- `k = 3` collects `[6, 8]` unchanged;
- `k = 4` contributes `[9]`.

Concatenating them gives `[1, 2, 4, 7, 5, 3, 6, 8, 9]`.

**Why every cell appears exactly once.** Every valid cell `(i, j)` has one unique sum `k = i + j`, so it belongs to exactly one outer-loop iteration. The start formulas and down-left walk enumerate every valid cell with that sum. No cell can belong to two diagonals because it cannot have two different index sums. Therefore extending `ans` after each diagonal returns all `m * n` values with neither omissions nor duplicates.

Reversing changes only the order inside a diagonal. It does not affect which cells belong to that diagonal or the order in which diagonals themselves are appended. The even/odd alternation consequently produces the required zigzag traversal.

The matrix is guaranteed nonempty, so `len(mat[0])` is safe and no empty-input branch is needed. Rectangular shapes are handled by the start formulas; a matrix with one row or one column reduces to diagonals of length one.

## Complexity detail

Every matrix value is appended to one temporary diagonal and then extended into `ans` exactly once. Reversing even diagonals processes those values one additional time, but the total across all diagonals remains $O(mn)$. Therefore time is $O(mn)$.

The required result list stores $mn$ values. The temporary `t` holds at most `min(m, n)` values, the maximum diagonal length. In this Python source, reversing with `t[::-1]` can create another temporary list of the same size. Auxiliary space excluding output is $O(\min(m,n))$; including the required output, total space is $O(mn)$ as recorded by the manifest.

## Alternatives and edge cases

- **Direct zigzag simulation:** Track one cell at a time, move up-right or down-left, and handle boundary bounces. It can use $O(1)$ auxiliary space but has more corner-specific state transitions.
- **Group by `i + j` in a dictionary:** Append every cell to its diagonal bucket, then reverse alternating buckets. It is easy to derive but stores the full matrix again.
- **One row:** Every diagonal has one value, so the output stays in left-to-right order despite alternating reversal calls.
- **One column:** Each diagonal also has one value, producing top-to-bottom order.
- **Wide matrix:** Early diagonals start along the first row; only after `k >= n` do starts move down the last column.
- **Tall matrix:** The same formulas remain valid, and the down-left loop stops at the bottom before the column becomes negative where appropriate.
- **Parity convention:** Diagonals are zero-indexed. Even `k` is reversed; describing them as human-numbered first, third, fifth diagonals refers to the same set.
- **Nonempty guarantee:** The implementation immediately reads `mat[0]` and relies on the stated positive dimensions.
