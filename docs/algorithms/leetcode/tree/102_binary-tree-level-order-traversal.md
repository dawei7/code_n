# Binary Tree Level Order Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_100` |
| Frontend ID | 102 |
| Difficulty | Medium |
| Topics | Tree, Breadth-First Search, Binary Tree |
| Official Link | [binary-tree-level-order-traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) |

## Problem Description & Examples
### Goal
Given a binary tree (level-order array), return the zigzag level order traversal - alternate left-to-right and right-to-left per level.

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

List[List[int]] - zigzag traversal

### Examples
**Example 1**

- Input: `root = [3, 9, 20, None, None, 15, 7]`
- Output: `[[3], [20, 9], [15, 7]]`

**Example 2**

- Input: `root = [50]`
- Output: `[[50]]`

**Example 3**

- Input: `root = [18, 73]`
- Output: `[[18], [73]]`

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
