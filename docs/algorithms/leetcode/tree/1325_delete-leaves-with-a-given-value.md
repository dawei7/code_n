# Delete Leaves With a Given Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_108` |
| Frontend ID | 1325 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [delete-leaves-with-a-given-value](https://leetcode.com/problems/delete-leaves-with-a-given-value/) |

## Problem Description & Examples
### Goal
Remove all leaves with value == target from a binary tree (level-order). Repeat until no target leaves remain.

### Function Contract
**Inputs**

- `root`: List
- `target`: int

**Return value**

List - tree after deletion

### Examples
**Example 1**

- Input: `root = [1, 2, 3, 2, None, 2, 4], target = 2`
- Output: `[1, None, 3, None, 4]`

**Example 2**

- Input: `root = [4], target = 4`
- Output: `[]`

**Example 3**

- Input: `root = [1, 3], target = 2`
- Output: `[1, 3]`

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
