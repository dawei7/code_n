# Boundary of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 545 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/boundary-of-binary-tree/) |

## Problem Description
### Goal
Given a binary tree, its anti-clockwise boundary is assembled from structural regions. Begin with the root, then take the non-leaf left boundary from top to bottom, followed by every leaf from left to right, and finally the non-leaf right boundary from bottom to top.

Return the boundary node values in that order without listing any node twice. When a preferred left or right child is missing, the corresponding boundary continues through the available child. A leaf belongs to the leaf section rather than a side-boundary section, and an empty tree returns an empty list while a one-node tree returns the root once.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

- A list of boundary node values in anti-clockwise order

### Examples
**Example 1**

- Input tree: `[1, null, 2, 3, 4]`
- Output: `[1, 3, 4, 2]`

**Example 2**

- Input tree: `[1, 2, 3, 4, 5, 6, null, null, null, 7, 8, 9, 10]`
- Output: `[1, 2, 4, 7, 8, 9, 10, 6, 3]`

**Example 3**

- Input tree: `[1]`
- Output: `[1]`
