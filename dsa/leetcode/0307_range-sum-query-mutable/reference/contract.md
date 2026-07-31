## Function Contract

**Inputs**

- `arr`: The app adapter's source array.
- `n`: The number of leading values from `arr` used to construct native `NumArray`.
- `queries`: Ordered app operations of the form `["update", index, val]` or `["sum", left, right]`.
- `q`: The number of leading operations from `queries` to execute.

**Return value**

Return the results of the executed `sum` operations in order. Updates change subsequent query results and produce no output.
