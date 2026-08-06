## Function Contract

**Inputs**

- `n`: the number of cities, labeled with the consecutive integers from `1` through `n`.
- `connections`: the available weighted, bidirectional connections. Each entry is `[x_i, y_i, cost_i]`, identifying two distinct endpoint cities and the cost of selecting that connection.

Let $m = \lvert\texttt{connections}\rvert$.

The input can include redundant connections, including more than one entry with the same two endpoints; each entry remains an independently available connection.

**Return value**

- The least possible sum of selected costs that leaves a path between every pair of cities, or `-1` when no such selection exists.
