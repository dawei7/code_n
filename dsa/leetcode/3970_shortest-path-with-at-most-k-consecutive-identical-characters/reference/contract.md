## Function Contract

**Inputs**

- `n`: The number of graph nodes, numbered from `0` to `n - 1`.
- `edges`: A list of triples `[u, v, w]`, each representing a directed edge from node `u` to node `v` with positive weight `w`.
- `labels`: A lowercase string of length `n`; `labels[i]` is the character assigned to node `i`.
- `k`: The maximum permitted length of any consecutive run of one character in the route's node-label string.

Let $m = \lvert\texttt{edges}\rvert$. The cost of a route is the sum of the weights of all directed edges it takes. The route consisting only of node `0` has cost zero, so when `n = 1` the answer is `0`.

**Return value**

Return the minimum cost of a valid route from node `0` to node `n - 1`. Return `-1` if no such route exists.
