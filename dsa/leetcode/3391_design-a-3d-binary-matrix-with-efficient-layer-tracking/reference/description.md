## Description

Maintain a binary cube with dimensions $n\times n\times n$. Every cell begins at zero. A `setCell(x, y, z)` operation changes the selected cell to one, while `unsetCell(x, y, z)` changes it to zero. Applying either operation when the cell already has the requested value leaves the state unchanged.

The cube consists of $n$ two-dimensional layers indexed by the first coordinate $x$. A `largestMatrix()` query must return the layer containing the greatest number of ones. When several layers have the same count—including when every cell is zero—choose the largest layer index.
