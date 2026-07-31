## Function Contract

**Inputs**

- `root`: The `TreeNode` root of a binary search tree whose node values are unique.
- `p`: The target `TreeNode` in that tree.

JSON cases encode `root` in level order and identify `p` by its unique value. The runner resolves `p` to a node in the reconstructed tree before calling `solve(root, p)`.

**Return value**

Return the successor `TreeNode`, or `None` when `p` has no successor. The runner displays and validates the returned node's value.
