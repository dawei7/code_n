# Convert Sorted Array to Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 108 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) |

## Problem Description
### Goal
Given an integer array whose distinct elements are sorted in ascending order, convert it to a binary search tree containing every array value exactly once. For each node, all values in its left subtree must be smaller and all values in its right subtree must be larger.

The returned tree must also be height-balanced: at every node, the heights of the left and right subtrees may differ by no more than one. More than one tree can satisfy these conditions, so any valid balanced shape is acceptable. Preserve all input values without duplication, and return `null` for an empty array.

### Function Contract
**Inputs**

- `nums`: a strictly increasing list of distinct integers

**Return value**

A height-balanced `TreeNode` root. Multiple valid shapes may exist; app results are checked by their values, BST ordering, and balance.

### Examples
**Example 1**

- Input: `nums = [-10, -3, 0, 5, 9]`
- Output: a valid balanced BST such as `[0, -10, 5, null, -3, null, 9]`

**Example 2**

- Input: `nums = [1, 3]`
- Output: either `[1, null, 3]` or `[3, 1]`

**Example 3**

- Input: `nums = []`
- Output: `[]`
