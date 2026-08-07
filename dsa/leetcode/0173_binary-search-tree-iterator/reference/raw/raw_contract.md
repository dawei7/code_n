## Function Contract

**Inputs**

- `root`: The BST's `TreeNode` root, or `null`.
- `operations`: A sequence beginning with `BSTIterator`, followed by `next` and `hasNext` calls.

JSON cases encode `root` as a level-order array. The runner reconstructs the tree before passing it to `BSTIterator`.

**Return value**

Return one result per operation: `null` for construction, the next integer for `next`, and a boolean for `hasNext`.
