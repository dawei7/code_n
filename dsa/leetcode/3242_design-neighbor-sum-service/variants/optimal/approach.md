## General

Let $q$ be the number of calls made after construction.

**Use distinct values as direct keys**

Every integer from $0$ through $n^2-1$ occurs exactly once, so a value can index an array without a hash lookup or coordinate search. Allocate two arrays of length $n^2$: one for orthogonal sums and one for diagonal sums.

During construction, visit each cell `(row, column)`. For its value, inspect the four orthogonal direction offsets. Add a neighbor only when its row and column remain inside the matrix. Repeat with the four diagonal offsets and store that second total. Each cell performs at most eight constant-time boundary checks.

After preprocessing, `adjacentSum(value)` and `diagonalSum(value)` return their respective array entries directly. Because each sum was formed from exactly the permitted in-bounds offsets, every returned value contains all and only the requested neighbors.

## Complexity detail

Construction visits $n^2$ cells and performs constant work per cell, so it takes $O(n^2)$ time. Each of the $q$ queries takes $O(1)$ time, making the complete trace $O(n^2+q)$. The two lookup arrays contain $2n^2$ integers and use $O(n^2)$ space.

## Alternatives and edge cases

- **Store coordinates and sum on demand:** A value-to-position table also gives $O(n^2)$ construction, $O(1)$ queries, and $O(n^2)$ space; precomputing removes repeated boundary work.
- **Scan the grid for every query:** This uses little additional state but costs $O(n^2)$ per call and repeats a search whose answer never changes.
- **Precompute by adding each cell to its neighbors:** This is equivalent, but separating orthogonal and diagonal direction lists makes their semantics explicit.
- A corner has two orthogonal neighbors and one diagonal neighbor.
- A non-corner boundary cell has three orthogonal neighbors and two diagonal neighbors.
- An interior cell may have four neighbors of each kind.
- The value `0` is an ordinary matrix entry and may have a positive neighbor sum.
- Neighbor values may sum to more than $n^2-1$ even though each individual entry lies in that range.
- Queries do not mutate the matrix, so repeated calls for the same value return the same result.
