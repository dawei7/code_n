## General

The replacement for a cell depends on its entire column, so determine that column's maximum before changing any of its `-1` entries. Begin with a row-by-row copy named `answer`; this follows the required output model and prevents replacements from altering the source matrix used to derive maxima.

Process one column at a time. Scan its $m$ original values to obtain `column_maximum`, then scan the same column in `answer`. Replace a copied value exactly when it equals `-1`. Every non-negative value is retained, including `0`, and the source guarantee ensures the computed maximum is non-negative.

After a column is processed, all of its positions satisfy the requested rule: original non-`-1` values are unchanged, and every original `-1` has become the maximum of that original column. Applying this argument independently to all $n$ columns proves that the returned matrix is complete and correct.

## Complexity detail

Copying the matrix touches $mn$ cells. Each column then receives two $m$-element scans, so the total time is $O(mn)$. The returned copy contains $mn$ values and therefore uses $O(mn)$ space. Apart from the required output matrix, the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Precomputed maximum array:** Store all $n$ column maxima first and then traverse the matrix row by row. This also takes $O(mn)$ time, but it adds $O(n)$ auxiliary storage beyond the output.
- **Recompute for every missing cell:** Scanning a full column separately for each `-1` remains correct but can require $O(m^2n)$ time when many cells need replacement.
- **In-place modification:** Updating `matrix` itself can produce the same values, but making `answer` as a copy preserves the source object and matches the stated construction.
- **No missing values:** The copied matrix is returned unchanged even though each column maximum is still well defined.
- **Zero maximum:** A column containing only `-1` and `0` must replace every `-1` with `0`, not leave it unchanged.
- **Rectangular shape:** Row and column counts may differ; column traversal must use $n$ rather than assuming a square matrix.
