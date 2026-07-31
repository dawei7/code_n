## Function Contract

**Inputs**

- `root`: The `TreeNode` root of a binary tree with unique values.
- `p`: The first target `TreeNode` in that tree.
- `q`: The second target `TreeNode` in that tree.

JSON cases encode `root` in level order and identify `p` and `q` by their unique values. The runner resolves both targets to nodes in the reconstructed tree before calling `solve(root, p, q)`.

**Return value**

Return the lowest common ancestor `TreeNode`. The runner displays and validates its value.
