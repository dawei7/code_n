# Invert Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_91` |
| Frontend ID | 226 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [invert-binary-tree](https://leetcode.com/problems/invert-binary-tree/) |

## Problem Description & Examples
### Goal
Given a binary tree (level-order array), imagine looking from the right side. Return the values of the nodes visible from the right (rightmost node at each level).

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

List[int] - rightmost node at each level

### Examples
**Example 1**

- Input: `root = [1, 2, 3, None, 5, None, 4]`
- Output: `[1, 3, 4]`

**Example 2**

- Input: `root = [50]`
- Output: `[50]`

**Example 3**

- Input: `root = [18, 73]`
- Output: `[18, 73]`

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
