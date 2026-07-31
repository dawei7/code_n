## General

The conditions are local: each one concerns a pair of vertically or horizontally adjacent cells. A row-by-row scan can therefore validate every required pair directly.

**Check only neighbors that exist**

At `grid[row][column]`, compare downward when `row + 1 < m`. Those two values must be equal. Compare rightward when `column + 1 < n`; those values must be different. A failed comparison proves immediately that the whole grid is invalid, so return `False`.

Checking downward and rightward is sufficient even though it does not explicitly inspect upward or leftward. Every vertical pair is considered once from its upper cell, and every horizontal pair is considered once from its left cell. If the scan finishes, every applicable adjacency rule has been checked and passed, so the answer is `True`.

## Complexity detail

Let $m$ and $n$ be the numbers of rows and columns. The nested scan visits $mn$ cells and performs only constant work at each one, for $O(m \cdot n)$ time.

The scan uses only its loop indices and dimensions, so its auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Column characterization:** First verify that every column is constant, then compare adjacent values in the first row. This is also $O(m \cdot n)$ time and $O(1)$ auxiliary space, but the direct scan mirrors both rules more closely.
- **Materialize all comparisons:** Building lists or sets of comparison results is correct but consumes unnecessary $O(m \cdot n)$ space.
- A one-cell grid has no neighbors, so both conditions hold vacuously.
- With one row, only the horizontal-difference rule applies; with one column, only the vertical-equality rule applies.
- Equal values in nonadjacent columns are allowed. Only immediate horizontal neighbors must differ.
- A mismatch may occur at the final row or column boundary, so the scan must cover the complete matrix.
