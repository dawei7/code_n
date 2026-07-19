# Diameter of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 543 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, a path may connect any two nodes by following parent-child edges without visiting an edge or node twice. The path may lie within one subtree and does not have to pass through the root.

Return the tree's diameter, defined as the greatest number of edges on any such path. A one-node tree has diameter zero because its longest path contains no edge, while an empty tree also yields zero under the app contract. Return only the edge count, not the endpoint nodes or the number of nodes on the path.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

- An integer equal to the maximum number of edges on any path between two nodes

### Examples
**Example 1**

- Input tree: `[1, 2, 3, 4, 5]`
- Output: `3`

**Example 2**

- Input tree: `[1, 2]`
- Output: `1`

**Example 3**

- Input tree: `[1]`
- Output: `0`
