## Function Contract

**Input**

- `binaryMatrix`: a read-only `BinaryMatrix` representing an $m \times n$ row-sorted binary matrix.

The available methods are:

- `binaryMatrix.get(row, col)`: return the value at the valid zero-based position `(row, col)`;
- `binaryMatrix.dimensions()`: return `[m, n]`.

The solution may call `get` at most 1,000 times and may not inspect the hidden matrix directly.

**Return value**

Return the smallest column index containing a `1` in any row. Return `-1` if every cell is `0`.
