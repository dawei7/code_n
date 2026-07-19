# Minimum Absolute Difference in BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 530 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-absolute-difference-in-bst/) |

## Problem Description
### Goal
Given a binary search tree containing at least two nodes, consider every pair of distinct nodes and the absolute difference between their stored values. The BST ordering places node values in sorted order under inorder traversal.

Return the minimum absolute difference among all node pairs. The task compares values rather than node depths or path lengths, and the selected nodes need not have a parent-child relationship. Because the closest values in sorted order determine the minimum, meet the intended traversal complexity without explicitly enumerating every pair.

### Function Contract
**Inputs**

- `root`: the root of a binary search tree containing at least two nodes with distinct values

**Return value**

- The minimum absolute difference between any pair of node values

### Examples
**Example 1**

- Input: `root = [4, 2, 6, 1, 3]`
- Output: `1`

**Example 2**

- Input: `root = [1, 0, 48, null, null, 12, 49]`
- Output: `1`

**Example 3**

- Input: `root = [5, 3, 8]`
- Output: `2`
