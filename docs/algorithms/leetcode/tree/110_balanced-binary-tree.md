# Balanced Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_94` |
| Frontend ID | 110 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [balanced-binary-tree](https://leetcode.com/problems/balanced-binary-tree/) |

## Problem Description & Examples
### Goal
Given the root of a BST (level-order array) and an integer `k`, return the `k`-th smallest value (1-indexed) in the BST.

### Function Contract
**Inputs**

- `root`: List - BST level-order
- `k`: int

**Return value**

int - the k-th smallest element

### Examples
**Example 1**

- Input: `root = [3, 1, 4, None, 2], k = 1`
- Output: `1`

**Example 2**

- Input: `root = [54, 50, 98], k = 1`
- Output: `50`

**Example 3**

- Input: `root = [73, 18, 98], k = 1`
- Output: `18`

---

## Underlying Base Algorithm(s)
- [Tree preorder traversal](tree_01_preorder-traversal.md)
- [Tree inorder traversal](tree_02_inorder-traversal.md)
- [Level-order traversal](tree_05_level-order-traversal.md)
- [Lowest common ancestor](tree_17_lowest-common-ancestor.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
