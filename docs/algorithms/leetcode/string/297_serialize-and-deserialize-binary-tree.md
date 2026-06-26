# Serialize and Deserialize Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_110` |
| Frontend ID | 297 |
| Difficulty | Hard |
| Topics | String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree |
| Official Link | [serialize-and-deserialize-binary-tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) |

## Problem Description & Examples
### Goal
Serialize a binary tree (level-order array) to a string and deserialize it. The roundtrip should return the same tree.

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

List - roundtrip serialized/deserialized result

### Examples
**Example 1**

- Input: `root = [1, 2, 3, None, None, 4, 5]`
- Output: `[1, 2, 3, None, None, 4, 5]`

**Example 2**

- Input: `root = [54]`
- Output: `[54]`

**Example 3**

- Input: `root = [9, 98]`
- Output: `[9, 98]`

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
