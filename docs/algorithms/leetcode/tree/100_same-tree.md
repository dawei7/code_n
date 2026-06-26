# Same Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_95` |
| Frontend ID | 100 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [same-tree](https://leetcode.com/problems/same-tree/) |

## Problem Description & Examples
### Goal
Given `preorder` and `inorder` traversal arrays of a binary tree, construct and return the level-order representation.

### Function Contract
**Inputs**

- `preorder`: List[int]
- `inorder`: List[int]

**Return value**

List - level-order tree

### Examples
**Example 1**

- Input: `preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]`
- Output: `[3, 9, 20, None, None, 15, 7]`

**Example 2**

- Input: `preorder = [1, 3], inorder = [3, 1]`
- Output: `[1, 3]`

**Example 3**

- Input: `preorder = [2, 3], inorder = [3, 2]`
- Output: `[2, 3]`

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
