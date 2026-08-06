## Function Contract

`solve(root: TreeNode, k: int) -> int`

Let $n$ be the number of nodes in the tree.

**Inputs**

- `root`: the root node of a nonempty binary tree with unique integer values. The app-local `TreeNode` has fields `val`, `left`, and `right`.
- `k`: a value guaranteed to occur in exactly one tree node.

**Return value**

Return the value of a leaf at minimum edge distance from the node whose value is `k`. If several leaves tie at that distance, returning any of their values is valid.
