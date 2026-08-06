## Function Contract

**Inputs**

- `n`: the number of nodes, labeled from `0` through `n - 1`.
- `edges`: the directed edges, where each row `[a_i, b_i]` points from `a_i` to `b_i`.
- `source`: the node at which every considered path begins.
- `destination`: the node at which every considered path must terminate.

Self-loops and repeated parallel edges may occur. Only nodes and cycles reachable from `source` affect the result; a disconnected invalid component does not create a path from `source`.

Let $V = n$ and let $E = \lvert\texttt{edges}\rvert$.

**Return value**

- `true` exactly when at least one path runs from `source` to `destination`, every reachable terminal is `destination`, and the source-reachable subgraph contains no directed cycle; otherwise, `false`.
