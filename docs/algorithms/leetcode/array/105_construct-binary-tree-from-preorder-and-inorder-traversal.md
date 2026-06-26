# Construct Binary Tree from Preorder and Inorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_106` |
| Frontend ID | 105 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Divide and Conquer, Tree, Binary Tree |
| Official Link | [construct-binary-tree-from-preorder-and-inorder-traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) |

## Problem Description & Examples
### Goal
Same as nc_95. Given `preorder` and `inorder` traversal arrays, reconstruct and return the inorder of the result.

### Function Contract
**Inputs**

- `preorder`: List[int]
- `inorder`: List[int]

**Return value**

List[int] - inorder of reconstructed tree

### Examples
**Example 1**

- Input: `preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]`
- Output: `[9, 3, 15, 20, 7]`

**Example 2**

- Input: `preorder = [2, 1], inorder = [1, 2]`
- Output: `[1, 2]`

**Example 3**

- Input: `preorder = [1, 2], inorder = [2, 1]`
- Output: `[2, 1]`

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
