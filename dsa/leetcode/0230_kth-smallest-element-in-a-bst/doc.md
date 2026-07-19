# Kth Smallest Element in a BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 230 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) |

## Problem Description
### Goal
Given the root of a nonempty binary search tree with distinct values and a valid one-based integer `k`, consider all node values in ascending order. The tree property places every left-subtree value below its node and every right-subtree value above it.

Return the value at rank `k` in that sorted sequence. Thus $k = 1$ selects the minimum node, while `k` equal to the number of nodes selects the maximum. Count tree nodes rather than levels, and return only the selected value—not the node object, a traversal list, or its original structural position.

### Function Contract
**Inputs**

- `root`: the root of a non-empty binary search tree with distinct values
- `k`: a one-based rank between one and the number of tree nodes

**Return value**

The `k`-th smallest value in the tree.

### Examples
**Example 1**

- Input: `root = [3, 1, 4, null, 2], k = 1`
- Output: `1`

**Example 2**

- Input: `root = [5, 3, 6, 2, 4, null, null, 1], k = 3`
- Output: `3`

**Example 3**

- Input: `root = [2, 1, 3], k = 2`
- Output: `2`
