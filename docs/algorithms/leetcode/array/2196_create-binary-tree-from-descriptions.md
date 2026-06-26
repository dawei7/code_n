# Create Binary Tree From Descriptions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2196 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Tree, Binary Tree |
| Official Link | [create-binary-tree-from-descriptions](https://leetcode.com/problems/create-binary-tree-from-descriptions/) |

## Problem Description & Examples
### Goal
Construct the unique binary tree described by parent-child relationships. Each relationship also says whether the child is the parent's left or right child.

### Function Contract
**Inputs**

- `descriptions`: triples `[parent, child, isLeft]`, where `isLeft` is `1` for a left edge and `0` for a right edge.

**Return value**

The root node of the constructed binary tree.

### Examples
**Example 1**

- Input: `descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]`
- Output: level order `[50, 20, 80, 15, 17, 19]`

**Example 2**

- Input: `descriptions = [[1, 2, 1], [2, 3, 0]]`
- Output: level order `[1, 2, null, null, 3]`

**Example 3**

- Input: `descriptions = [[4, 2, 1], [4, 6, 0]]`
- Output: level order `[4, 2, 6]`

---

## Underlying Base Algorithm(s)
Create or reuse one node object for every encountered value, then assign each child to the indicated side of its parent. Record every value that appears as a child. The root is the sole created node whose value never appears in the child set.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
