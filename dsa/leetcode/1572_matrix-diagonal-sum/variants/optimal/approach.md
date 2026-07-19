## General
**Derive both diagonal columns from the row**

In row `index`, the primary-diagonal cell is `mat[index][index]`. The secondary-diagonal column mirrors that index across the matrix, so its cell is `mat[index][N - 1 - index]`. Add both values for every row. This visits exactly the two requested diagonal positions and ignores every other matrix cell.

**Correct the unique overlap**

For even $N$, the diagonal column indices are never equal, so all $2N$ visited cells are distinct. For odd $N$, they coincide only when `index = N // 2`; the center was then added twice. Subtract that one center value after the scan.

Every diagonal cell appears in its own row's two selected positions. The parity argument identifies the only possible duplicate, proving that the corrected total counts the union of both diagonals exactly once.

## Complexity detail
The algorithm performs constant work for each of $N$ rows, so it takes $O(N)$ time rather than scanning all $N^2$ matrix cells.

Only the matrix dimension, loop index, and running total are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Two separate diagonal sums:** sum the primary and secondary diagonals independently and subtract the center for odd $N$. This has the same $O(N)$ time and $O(1)$ space.
- **Full matrix scan:** inspect every coordinate and add it when `row == column` or `row + column == N - 1`. It is correct but takes $O(N^2)$ time.
- **Set of coordinates:** insert both diagonal positions into a set before summing. It prevents duplicate counting but uses unnecessary $O(N)$ space.
- **One-by-one matrix:** its only cell belongs to both diagonals and must be returned once.
- **Odd dimension:** exactly one center cell overlaps.
- **Even dimension:** the diagonals cross between cells, so no correction is needed.
- **Off-diagonal values:** they never affect the result, regardless of magnitude.
- **Equal diagonal values:** positions, not value equality, determine whether a cell is counted once or twice.
