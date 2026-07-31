## Function Contract

**Inputs**

- `n`: The number of vertices, labelled from `0` through `n - 1`.
- `edges`: The ordered edge proposals, each written as `[u, v, w]` for endpoints `u < v` and binary weight `w`.

Let $N=n$ and $M=\lvert\texttt{edges}\rvert$. The graph is undirected, begins empty, and changes only when the current proposal preserves even total weight in every cycle.

**Return value**

Return the number of accepted edges after all $M$ proposals have been processed in order.
