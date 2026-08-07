## Description

Given the `root` of a binary tree and an integer `targetSum`, return *the number of paths where the sum of the values along the path equals* `targetSum`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
### Function Contract

**Inputs**

- `root`: The binary tree's `TreeNode` root, or `None` for an empty tree.
- `targetSum`: The integer sum required from a downward path.

Canonical JSON fixtures encode `root` in level order with `null` for missing children. The app runner constructs the
local `TreeNode` objects before calling `solve(root, targetSum)`; LeetCode supplies its own equivalent node class.

**Return value**

Return the number of downward paths whose node values sum to `targetSum`.

### Examples
#### Example 1

![](images/pathsum3-1-tree.jpg)

- **Input:** `root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8`
- **Output:** `3`
- **Explanation:** The paths that sum to 8 are shown.
#### Example 2

- **Input:** `root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22`
- **Output:** `3`
### Constraints

- The number of nodes in the tree is in the range `[0, 1000]`.

- $-10^{9} \le \text{Node.val} \le 10^{9}$

- $-1000 \le targetSum \le 1000$