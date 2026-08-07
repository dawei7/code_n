## Function Contract

**Inputs**

- `n`: The number of shops, whose indices are `0` through `n - 1`.
- `prices`: An array of length `n`; `prices[i]` is the local apple price at shop `i`.
- `roads`: The unique undirected roads. Each row `[u, v, cost, tax]` gives its endpoints, empty-travel cost, and loaded-cost multiplier.

Let $m = \texttt{roads.length}$. For an edge $e$, define its empty weight as $c_e$ and its loaded weight as $c_e t_e$. The traveler buys apples at exactly one shop. Choosing the starting shop itself requires no road travel.

**Return value**

Return an integer array `ans` of length `n`. For each start `i`, `ans[i]` is the minimum of the local price and every valid empty journey to a purchase shop followed by a loaded journey back to `i`.
