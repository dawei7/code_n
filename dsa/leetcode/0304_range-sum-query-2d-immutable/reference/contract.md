## Function Contract

**Inputs**

- `matrix`: The immutable rectangular integer matrix used to construct native `NumMatrix`.
- `queries`: The app adapter's ordered `[row1, col1, row2, col2]` inclusive rectangles.

**Return value**

Return one region sum per entry in `queries`, in order. The native interface returns each value from a separate `sumRegion` call.
