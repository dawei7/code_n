## General

Cells on one upper-left-to-lower-right diagonal share the same value of `row - col`. Such a diagonal begins either in the first column or in the first row. Visiting those two sets of starting cells covers every matrix entry exactly once, provided the first-row pass skips column zero so the main diagonal is not repeated.

For a diagonal starting at `(row, col)`, collect its coordinates while increasing both indices. Sort the corresponding values in non-increasing order when the start lies in the first column; these are exactly the bottom-left diagonals, including the main one. Sort in non-decreasing order when the start lies in the first row to the right of the main diagonal. Write the ordered values back through the collected coordinates in their upper-left-to-lower-right traversal order.

Each value stays on its original diagonal, and sorting directly establishes the required order for that diagonal. Since the starting-cell enumeration is exhaustive and disjoint, every cell receives exactly the value prescribed by its diagonal's rule, which yields the requested matrix.

## Complexity detail

Let $n$ be the side length. The matrix has $n^2$ values. Sorting a diagonal of length $d$ costs $O(d\log d)$, and the sum over all diagonals is bounded by $O(n^2\log n)$. Only one diagonal's coordinates and values are stored at a time, so the auxiliary space is $O(n)$, apart from the returned in-place matrix.

## Alternatives and edge cases

- **Group every diagonal in a dictionary:** The `row - col` key is convenient, but retaining all groups at once uses $O(n^2)$ auxiliary space instead of $O(n)$.
- **Sort every diagonal in one direction:** This violates one half of the contract; first-column starts descend, while first-row starts to the right of the main diagonal ascend.
- **Sort the entire matrix:** Values are not allowed to cross between diagonals, so a global ordering changes the wrong cells.
- **Main diagonal:** Its start is `(0, 0)`, so it belongs to the non-increasing bottom-left group.
- **Single-cell diagonals:** Sorting leaves them unchanged, including the complete matrix when $n=1$.
- **Duplicates and negative values:** Comparison sorting preserves all entries and does not rely on distinctness or sign.
