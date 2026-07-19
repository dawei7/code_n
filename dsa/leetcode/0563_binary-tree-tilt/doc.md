# Binary Tree Tilt

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 563 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-tilt/) |

## Problem Description
### Goal
Given the root of a binary tree, define the tilt of a node as the absolute difference between the sum of all values in its left subtree and the sum of all values in its right subtree. An empty subtree has sum `0`, so a leaf has tilt `0`.

Return the sum of the tilts of every node in the tree. Each subtree sum includes all descendants on that side, not only the node's immediate children, and every node's individual tilt contributes once to the final total.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

- The sum of every node's tilt

### Examples
**Example 1**

- Input tree: `[1, 2, 3]`
- Output: `1`

**Example 2**

- Input tree: `[4, 2, 9, 3, 5, null, 7]`
- Output: `15`

**Example 3**

- Input tree: `[21, 7, 14, 1, 1, 2, 2, 3, 3]`
- Output: `9`
