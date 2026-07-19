# Construct Binary Tree from Preorder and Inorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 105 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Divide and Conquer, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) |

## Problem Description
### Goal
You are given two traversal sequences produced from the same binary tree. `preorder` visits each root before its left and right subtrees, while `inorder` visits the left subtree before the root and then the right subtree. Every node value is distinct, and both arrays contain exactly the same values.

Reconstruct and return the binary tree that yields both sequences. The traversal rules and distinct values determine one unique arrangement, including which nodes belong to each subtree. Preserve the integer values exactly, return `null` when both traversals are empty, and do not return either traversal array as a substitute for the linked tree structure.

### Function Contract
**Inputs**

- `preorder`: node values in root-left-right order
- `inorder`: the same node values in left-root-right order

**Return value**

The reconstructed `TreeNode` root, displayed as a level-order list in app results.

### Examples
**Example 1**

- Input: `preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]`
- Output tree: `[3, 9, 20, null, null, 15, 7]`

**Example 2**

- Input: `preorder = [1], inorder = [1]`
- Output tree: `[1]`

**Example 3**

- Input: `preorder = [2, 1], inorder = [1, 2]`
- Output tree: `[2, 1]`
