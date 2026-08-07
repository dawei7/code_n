## Function Contract

**Inputs**

- `n`: The number of grid rows.
- `m`: The number of grid columns.
- `sources`: A non-empty array of distinct source coordinates and their initial positive colors, with each entry formatted as `[row, column, color]`.

Rows are indexed from `0` through `n - 1`, and columns from `0` through `m - 1`. Adjacency is orthogonal; diagonally touching cells do not spread directly to one another. Every time step uses the grid state from the beginning of that step, so competing arrivals are resolved together rather than by iteration order.

**Return value**

Return an $n$-by-$m$ integer matrix containing the final color of every cell after the simultaneous four-directional spreading process stops.
