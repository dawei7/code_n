## Function Contract

**Inputs**

- `root`: The binary tree's `TreeNode` root, or `None` for an empty tree.
- `targetSum`: The integer sum required from a downward path.

Canonical JSON fixtures encode `root` in level order with `null` for missing children. The app runner constructs the
local `TreeNode` objects before calling `solve(root, targetSum)`; LeetCode supplies its own equivalent node class.

**Return value**

Return the number of downward paths whose node values sum to `targetSum`.
