## Function Contract

**Input**

- `matrix`: A nonempty rectangular matrix of nonnegative integers.

Let $n$ be the number of rows, $m$ the number of columns, $A=nm$ the number of cells, and $V=201$ the number of possible cell values. Row and column indices are zero-based when coordinates are discussed. Neighborhood bounds are clipped to the matrix, and the four exact-distance corner positions are excluded only when they are in bounds.

**Return value**

Return the number of nonzero cells for which every considered neighborhood value is at most the cell's own value.
