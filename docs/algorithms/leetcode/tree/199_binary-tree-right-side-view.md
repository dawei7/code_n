# Binary Tree Right Side View

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_101` |
| Frontend ID | 199 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [binary-tree-right-side-view](https://leetcode.com/problems/binary-tree-right-side-view/) |

## Problem Description & Examples
### Goal
Given a binary tree (level-order) where each node contains a digit 0-9, each root-to-leaf path represents a number. Return the total sum of all root-to-leaf numbers.

### Function Contract
**Inputs**

- `root`: List - level-order tree with digit values

**Return value**

int - sum of all root-to-leaf numbers

### Examples
**Example 1**

- Input: `root = [1, 2, 3]`
- Output: `25`

**Example 2**

- Input: `root = [6]`
- Output: `6`

**Example 3**

- Input: `root = [2, 9]`
- Output: `29`

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
