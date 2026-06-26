# Maximum Depth of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_92` |
| Frontend ID | 104 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [maximum-depth-of-binary-tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |

## Problem Description & Examples
### Goal
Given the root of a binary tree (level-order array), count "good" nodes. A node is "good" if the path from the root to that node has no node with a greater value.

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

int - number of good nodes

### Examples
**Example 1**

- Input: `root = [3, 1, 4, 3, None, 1, 5]`
- Output: `4`

**Example 2**

- Input: `root = [7]`
- Output: `1`

**Example 3**

- Input: `root = [3, 10]`
- Output: `2`

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
