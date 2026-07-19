# Closest Leaf in a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 742 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/closest-leaf-in-a-binary-tree/) |

## Problem Description
### Goal
Given a binary tree whose node values are unique and a target value `k` that occurs in the tree, find a leaf having the shortest path from the target node. A leaf has no children, and distance is the number of tree edges along a path that may travel through parents as well as children.

Return the value of a closest leaf. The target itself qualifies when it is a leaf. If several leaves have the same minimum edge distance, returning any one of their values is acceptable.

### Function Contract
**Inputs**

- `root`: the root of a nonempty binary tree whose node values are unique
- `k`: a value guaranteed to occur in the tree

**Return value**

- The value of a closest leaf to node `k`; either value is valid when several leaves tie

### Examples
**Example 1**

- Input: `root = [1,3,2], k = 1`
- Output: `3` (the other child `2` is equally valid)

**Example 2**

- Input: `root = [1], k = 1`
- Output: `1`

**Example 3**

- Input: `root = [1,2,3,4,null,null,null,5,null,6], k = 2`
- Output: `3`
