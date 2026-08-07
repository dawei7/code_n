## Function Contract

**Inputs**

- `n`: The number of nodes in the rooted tree.
- `edges`: The `n - 1` undirected edges of the valid tree.
- `nums`: The positive value assigned to each node, in node-index order.

The undirected edges are interpreted after rooting the tree at node `0`. For node `i` and one of its ancestors `a`, the pair contributes exactly when `nums[i] * nums[a]` is a perfect square.

**Return value**

Return the total number of qualifying ordered descendant-ancestor pairs. Node `0` contributes no $t_i$ term because it has no ancestor.
