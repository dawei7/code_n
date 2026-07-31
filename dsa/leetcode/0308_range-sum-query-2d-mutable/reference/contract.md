## Function Contract

**Inputs**

- `matrix`: The initial rectangular integer matrix.
- `operations`: The app adapter's ordered operations, either `["update", row, col, val]` or `["sum", row1, col1, row2, col2]`.

**Return value**

Return the results of all `sum` operations in order. An update changes subsequent sums and contributes no item to the returned list.
