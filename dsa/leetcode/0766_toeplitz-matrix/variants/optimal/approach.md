## General
**Reduce each diagonal to adjacent comparisons**

Every cell outside the first row and first column has an upper-left predecessor on the same diagonal. Compare `matrix[row][column]` with `matrix[row - 1][column - 1]`. Return false at the first mismatch.

**Why local equality covers the whole diagonal**

If every adjacent pair on a diagonal is equal, transitivity makes every value on that diagonal equal to its first value. Conversely, any diagonal containing two different values must have some first position where its value changes, and that cell fails the upper-left comparison. Checking all eligible cells is therefore both necessary and sufficient.

## Complexity detail
For `m` rows and `n` columns, the scan performs one comparison for each of $(m - 1)(n - 1)$ eligible cells, taking $O(mn)$ time. It uses only loop indices, for $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Traverse each diagonal once:** Starting from the first row and first column also visits every cell in $O(mn)$ time, but needs more boundary logic.
- **Hash by `row - column`:** All cells with the same difference share a diagonal; storing their first values takes $O(m + n)$ space.
- **Recheck every diagonal prefix:** Walking back to the diagonal start for every cell is correct but can take $O(mn \min(m,n))$ time.
- **Single row or column:** Every diagonal has length one, so the result is always true.
- **Negative and repeated values:** Equality comparisons require no value restrictions.
- **Late mismatch:** The scan must inspect the entire matrix unless it finds a failure.
- **Rectangular shape:** The same upper-left relation works without requiring a square matrix.
