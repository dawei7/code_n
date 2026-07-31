## Function Contract

**Inputs**

- `n`: The number of nodes, labeled from `0` to `n - 1`.
- `edges`: The `n - 1` indexed undirected edges of a valid tree; `edges[i]` contains the two endpoints of edge `i`.
- `start`: A binary string giving the initial color of every node.
- `target`: A binary string giving the desired color of every node.

Let $N=n$. Selecting edge `i` toggles exactly the two bits at the endpoints listed in `edges[i]`. Applying edge indices in a different order does not change their combined effect.

**Return value**

Return the increasing list of edge indices in a shortest valid toggle sequence. Return `[]` when `start` already equals `target`, and return `[-1]` when no sequence can reach `target`.
