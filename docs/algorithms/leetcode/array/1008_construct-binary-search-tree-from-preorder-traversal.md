# Construct Binary Search Tree from Preorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1008 |
| Difficulty | Medium |
| Topics | Array, Stack, Tree, Binary Search Tree, Monotonic Stack, Binary Tree |
| Official Link | [construct-binary-search-tree-from-preorder-traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/) |

## Problem Description & Examples
### Goal
Given the preorder traversal of a binary search tree with distinct values, rebuild the tree.

### Function Contract
**Inputs**

- `preorder`: List[int]

**Return value**

TreeNode - root of the reconstructed BST

### Examples
**Example 1**

- Input: `preorder = [8, 5, 1, 7, 10, 12]`
- Output: tree with level order `[8, 5, 10, 1, 7, None, 12]`

**Example 2**

- Input: `preorder = [1, 3]`
- Output: tree with root `1` and right child `3`

**Example 3**

- Input: `preorder = [4, 2]`
- Output: tree with root `4` and left child `2`

---

## Underlying Base Algorithm(s)
Recursive preorder parsing with upper bounds.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(h)` recursion depth
