# Delete Node in a BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 450 |
| Difficulty | Medium |
| Topics | Tree, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-node-in-a-bst/) |

## Problem Description
### Goal
Given the root of a binary search tree with unique node values and an integer `key`, remove the node whose value equals the key when it exists. Reconnect its remaining subtrees so every other value stays present and the strict BST ordering remains valid.

Return the possibly changed root. Deleting the root may select a new root, and deletion must correctly handle nodes with zero, one, or two children. When two subtrees exist, replace or reconnect using a valid predecessor or successor arrangement without duplicating a value. If the key is absent, return the tree unchanged; an empty tree remains empty.

### Function Contract
**Inputs**

- `root`: the app's level-order array representation of a BST, using `None` for missing children
- `key`: the value to delete

**Return value**

- The resulting BST in level-order form. If `key` is absent, return the unchanged tree. The native artifact accepts and returns `TreeNode` objects.

### Examples
**Example 1**

- Input: `root = [5, 3, 6, 2, 4, None, 7], key = 3`
- Output: `[5, 4, 6, 2, None, None, 7]`

**Example 2**

- Input: `root = [5, 3, 6, 2, 4, None, 7], key = 0`
- Output: `[5, 3, 6, 2, 4, None, 7]`

**Example 3**

- Input: `root = [], key = 0`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Use ordering to find the only possible target**

At a node, compare `key` with its value. A smaller key can occur only in the left subtree and a larger key only in the right subtree. Recurse along that one search path and reconnect the returned subtree to its parent. If the path reaches an empty child, the key was absent and no link changes.

**Remove nodes with at most one child directly**

If the target has no left child, its right child can replace it; if it has no right child, its left child can replace it. Every value in the replacement subtree already lies within the target's inherited bounds, so the parent can safely point to that child.

**Replace a two-child target with its successor**

When both children exist, find the smallest value in the right subtree by following left links. Copy that inorder successor value into the target, then delete that value from the right subtree. The successor is larger than every value on the left, and no smaller value remains on the right, so both ordering inequalities still hold. Deleting the successor is simpler because it has no left child.

**Adapt tree objects to the app contract**

The app constructs nodes from the level-order input, performs the same BST deletion, and serializes the resulting links back to a trimmed level-order array. This conversion visits the whole output even though the native deletion itself follows only a root-to-leaf path.

#### Complexity detail

For tree height `h`, native search, successor discovery, and rewiring take $O(h)$ time and $O(h)$ recursive stack space. The app's level-order conversion makes the full contract $O(n)$ time and $O(n)$ space; `h` can equal `n` for a skewed tree.

#### Alternatives and edge cases

- **Iterative parent tracking:** rewires the target without recursion and uses $O(1)$ auxiliary space, but the two-child case still needs careful successor-parent handling.
- **Use the inorder predecessor:** replacing with the largest value from the left subtree is symmetric and equally efficient.
- **Rebuild from an inorder list:** preserves the set of values but costs $O(n)$ work regardless of height and may unnecessarily change the tree's shape.
- **Missing key:** reaching `None` returns the original links unchanged.
- **Root deletion:** the returned replacement subtree becomes the new root.
- **Single-node tree:** deleting its value produces an empty tree.
- **Two-child target:** delete the copied successor as well so its value does not appear twice.

</details>
