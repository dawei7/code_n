# Construct Binary Tree from Inorder and Postorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 106 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Divide and Conquer, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) |

## Problem Description
### Goal
You are given the inorder and postorder traversal sequences of the same binary tree. `inorder` visits a node between its left and right subtrees, whereas `postorder` visits both subtrees before their root. Every value is distinct, and the two arrays contain the same set of nodes.

Reconstruct and return the unique tree consistent with both traversal orders. Subtree boundaries and child directions must agree with both arrays, not merely reproduce their values. Empty traversal arrays describe an empty tree, while any nonempty valid input must produce connected `TreeNode` objects rooted at the original root with all values used exactly once.

### Function Contract
**Inputs**

- `inorder`: node values in left-root-right order
- `postorder`: the same node values in left-right-root order

**Return value**

The reconstructed `TreeNode` root, displayed as a level-order list in app results.

### Examples
**Example 1**

- Input: `inorder = [9, 3, 15, 20, 7], postorder = [9, 15, 7, 20, 3]`
- Output tree: `[3, 9, 20, null, null, 15, 7]`

**Example 2**

- Input: `inorder = [1], postorder = [1]`
- Output tree: `[1]`

**Example 3**

- Input: `inorder = [1, 2], postorder = [1, 2]`
- Output tree: `[2, 1]`
