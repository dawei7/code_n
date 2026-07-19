## General
**Group cells by a stable diagonal key**

Moving from `(row, column)` to `(row + 1, column + 1)` preserves `row - column`, so use that difference as the key for a list of diagonal values. Scan the matrix once and append every value to its key's list.

Sort each list in descending order. Then scan matrix cells again in normal row-major order and replace each cell by popping from the end of its diagonal list. Row-major order encounters cells of a fixed diagonal from top-left to bottom-right, while each pop returns the smallest remaining value. Consequently every diagonal is written back in ascending order and no value crosses to another diagonal.

The grouping partitions all cells by their unique difference key, sorting preserves each group's multiset, and the second traversal assigns that multiset in the required order. These facts establish both value preservation and the ordering condition.

## Complexity detail
There are $mn$ stored values. Sorting a diagonal of length at most $L$ costs $O(k\log k)$ for its length $k$; summed across diagonals, this is bounded by $O(mn\log L)$. The groups collectively store $mn$ values, so auxiliary space is $O(mn)$.

## Alternatives and edge cases
- **Counting sort per diagonal:** Since values lie between 1 and 100, frequency arrays can reduce sorting to $O(mn)$ time, but the comparison-sort grouping is more general.
- **Sort from each boundary start:** Extracting, sorting, and replacing each diagonal directly uses only $O(L)$ temporary space and the same comparison-sort time bound.
- **Selection sort each diagonal:** It avoids a library sort but can take $O(mnL)$ time.
- **One row or one column:** Every diagonal contains one cell, so the matrix is unchanged.
- **Duplicate values:** They remain duplicated and their relative identity is irrelevant.
- **Rectangular matrices:** Top-row and left-column starts together cover every diagonal exactly once.
