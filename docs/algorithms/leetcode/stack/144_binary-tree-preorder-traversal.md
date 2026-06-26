# Binary Tree Preorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_89` |
| Frontend ID | 144 |
| Difficulty | Easy |
| Topics | Stack, Tree, Depth-First Search, Binary Tree |
| Official Link | [binary-tree-preorder-traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) |

## Problem Description & Examples
### Goal
Given a BST (as a level-order array) and two values `p` and `q`, find the lowest common ancestor (LCA). The LCA is the lowest node that has both p and q as descendants (including itself).

### Function Contract
**Inputs**

- `root`: List - BST level-order
- `p`: int
- `q`: int

**Return value**

int - value of the LCA node

### Examples
**Example 1**

- Input: `root = [6, 2, 8, 0, 4, 7, 9], p = 2, q = 8`
- Output: `6`

**Example 2**

- Input: `root = [50, 34, 98, 6, 54, None, None], p = 54, q = 6`
- Output: `50`

**Example 3**

- Input: `root = [33, 18, 98, 9, 73, None, None], p = 33, q = 9`
- Output: `33`

---

## Underlying Base Algorithm(s)
- [Tree preorder traversal](tree_01_preorder-traversal.md)
- [Tree inorder traversal](tree_02_inorder-traversal.md)
- [Level-order traversal](tree_05_level-order-traversal.md)
- [Lowest common ancestor](tree_17_lowest-common-ancestor.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
