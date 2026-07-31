## Function Contract

**Inputs**

- `n`: The number of nodes in the tree.
- `edges`: The `n - 1` undirected edges, each represented as `[u, v]`.
- `group`: The group label assigned to each node.

Every two nodes have exactly one path because `edges` forms a valid tree. Each unordered pair is counted once, and a node is never paired with itself.

**Return value**

Return the sum of path lengths over all unordered pairs `(u, v)` with `u != v` and `group[u] == group[v]`.
