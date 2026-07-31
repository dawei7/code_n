## Function Contract

**Inputs**

- `n`: The number of tree nodes.
- `edges`: The `n - 1` undirected edges, each written as `[a, b]`.

The first and last nodes of a path are its endpoints. A node qualifies if it is an endpoint of any maximum-length simple path, not merely one selected diameter.

**Return value**

Return an `n`-character binary string whose index `i` is `'1'` exactly when node `i` is an endpoint of at least one diameter path.
