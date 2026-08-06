## Function Contract

**Inputs**

- `root`: The root of a binary search tree, or `None` for an empty tree.
- `key`: The integer value to remove.

**Return value**

- Return the root of the resulting binary search tree. The returned root can differ from `root` when the original root is deleted.

The standalone app defines a minimal local equivalent of LeetCode's injected `TreeNode` model. It accepts and returns level-order tree values, using `None` for a missing child.
