# Construct Quad Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_102` |
| Frontend ID | 427 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Tree, Matrix |
| Official Link | [construct-quad-tree](https://leetcode.com/problems/construct-quad-tree/) |

## Problem Description & Examples
### Goal
Given the root of a binary tree (level-order array), flatten it to a "linked list" in-place. The resulting structure uses right pointers only, in preorder traversal order.

Return the flattened list as an array of values.

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

List[int] - preorder values (flattened)

### Examples
**Example 1**

- Input: `root = [1, 2, 5, 3, 4, None, 6]`
- Output: `[1, 2, 3, 4, 5, 6]`

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
