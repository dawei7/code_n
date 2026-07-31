## Function Contract

**Inputs**

- `n`: The number of nodes in the tree.
- `edges`: The `n - 1` undirected edges, each represented by a two-element array `[u_i, v_i]`.
- `x`: The first target node.
- `y`: The second target node.
- `z`: The third target node.

The nodes are labeled from `0` through `n - 1`. The edge list forms one valid tree, and `x`, `y`, and `z` are pairwise distinct.

For any node, compute its three edge-count distances to the targets. After arranging those distances as $a\le b\le c$, the node qualifies exactly when $a^2+b^2=c^2$. A distance may be zero; the definition does not require a positive Pythagorean triplet.

**Return value**

Return the number of nodes whose three target distances satisfy the Pythagorean equation.
