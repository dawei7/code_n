# Insert into a Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_98` |
| Frontend ID | 701 |
| Difficulty | Medium |
| Topics | Tree, Binary Search Tree, Binary Tree |
| Official Link | [insert-into-a-binary-search-tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) |

## Problem Description & Examples
### Goal
Given the root of a binary tree (level-order array), find the maximum path sum. A path is a sequence of nodes where each pair is connected (no repeated nodes). The path doesn't need to go through the root.

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

int - maximum path sum

### Examples
**Example 1**

- Input: `root = [-10, 9, 20, None, None, 15, 7]`
- Output: `42`

**Example 2**

- Input: `root = [44]`
- Output: `44`

**Example 3**

- Input: `root = [-2, 26]`
- Output: `26`

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
