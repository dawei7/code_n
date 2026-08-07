## Function Contract

**Inputs**

- `adj_list`: The app's adjacency-list representation, where row `i` lists the one-based neighbors of node $i + 1$; `[]` represents an empty graph.

**Return value**

Return independent adjacency data for a deep copy. The native LeetCode interface returns the cloned `Node` corresponding to the supplied node.
