## Function Contract

**Inputs**

- `grid`: An $n \times n$ matrix whose entries are `0` or `1`.

**Return value**

Return the constructed `Node` representing the complete grid. Leaves store the uniform region value; internal nodes
store four children in top-left, top-right, bottom-left, bottom-right order.
