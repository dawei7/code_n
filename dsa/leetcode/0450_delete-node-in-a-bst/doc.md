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
