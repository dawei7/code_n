# Construct Binary Tree from Inorder and Postorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 106 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Divide and Conquer, Tree, Binary Tree |
| Official Link | [construct-binary-tree-from-inorder-and-postorder-traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) |

## Problem Description & Examples
### Goal
Given inorder and postorder traversals of a binary tree with unique values, reconstruct the original tree.

### Function Contract
**Inputs**

- `inorder`: List[int]
- `postorder`: List[int]

**Return value**

TreeNode - root of the reconstructed binary tree

### Examples
**Example 1**

- Input: `inorder = [9, 3, 15, 20, 7], postorder = [9, 15, 7, 20, 3]`
- Output: tree with level order `[3, 9, 20, None, None, 15, 7]`

**Example 2**

- Input: `inorder = [1], postorder = [1]`
- Output: tree with root `1`

**Example 3**

- Input: `inorder = [2, 1], postorder = [2, 1]`
- Output: tree with root `1` and left child `2`

---

## Underlying Base Algorithm(s)
Recursive tree reconstruction with an inorder index map.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
