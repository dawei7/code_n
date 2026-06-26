# Validate Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_104` |
| Frontend ID | 98 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [validate-binary-search-tree](https://leetcode.com/problems/validate-binary-search-tree/) |

## Problem Description & Examples
### Goal
Validate whether a binary tree (level-order array) is a valid BST: left subtree < node < right subtree.

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

bool - True if valid BST

### Examples
**Example 1**

- Input: `root = [5, 1, 4, None, None, 3, 6]`
- Output: `False`

**Example 2**

- Input: `root = [50]`
- Output: `True`

**Example 3**

- Input: `root = [18, 73]`
- Output: `False`

---

## Underlying Base Algorithm(s)
- [Tree preorder traversal](tree_01_preorder-traversal.md)
- [Tree inorder traversal](tree_02_inorder-traversal.md)
- [Level-order traversal](tree_05_level-order-traversal.md)
- [Lowest common ancestor](tree_17_lowest-common-ancestor.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
