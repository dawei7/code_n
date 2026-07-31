## General

The paint order gives values, while completion depends on coordinates. First scan `mat` once and store the row and column of every value. The guaranteed permutation makes this a one-to-one lookup: each `arr[i]` identifies exactly one previously unpainted cell.

Maintain how many cells have been painted in each row and each column. For every value in `arr`, find its coordinates in constant time, increment the corresponding two counters, and compare the row count with the number of columns and the column count with the number of rows. Return immediately when either equality holds.

After processing index `i`, each row counter equals exactly the number of that row's values among `arr[0:i + 1]`, and the analogous statement holds for columns. Consequently, the equality test is true precisely when the current operation has completed a row or column. Processing indices in order and returning at the first true test guarantees the smallest required index.

## Complexity detail

Let $N=mn$ be the number of matrix cells. Building the position map costs $O(N)$ time, and processing at most $N$ paint operations also costs $O(N)$ time, for $O(mn)$ overall. The coordinate map and counters use $O(mn)$ space.

The benchmark uses `size` as $N$ and keeps every row and column one cell short until late in the order. A correct alternative that scans the whole matrix to locate every successive value completes all legal tiers but takes $O(N^2)$ time.

## Alternatives and edge cases

- **Matrix scan per paint:** Search `mat` for `arr[i]` on every operation. This is correct but may take $O((mn)^2)$ time.
- **Paint-time matrix:** Map every value to its index in `arr`, then compute the maximum paint time for each row and column and take the minimum. This is another $O(mn)$ solution.
- A one-row matrix completes some one-cell column on the first paint, and a one-column matrix completes some one-cell row then as well.
- A single operation may complete both its row and column; the returned index is unchanged.
- Values need not appear in numeric order in either `arr` or `mat`.
- The permutation guarantees prevent duplicate paints, so counters never need a visited check.
