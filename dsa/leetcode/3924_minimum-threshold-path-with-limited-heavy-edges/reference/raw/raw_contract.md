## Function Contract

**Inputs**

- `n`: The number of nodes, labelled from `0` to `n - 1`.
- `edges`: The undirected weighted edges. Each entry `[u, v, w]` joins `u` and `v` with weight `w`.
- `source`: The starting node.
- `target`: The destination node.
- `k`: The greatest number of heavy edges that a valid path may traverse.

Let $m$ be `edges.length`. For a chosen integer threshold $T$, an edge of weight $w$ is light exactly when $w \le T$; otherwise it is heavy.

**Return value**

Return the minimum integer $T$ for which some `source`-to-`target` path contains at most `k` heavy edges. Return `-1` if no such path exists. When `source == target`, the empty path is valid and the minimum threshold is `0`.
