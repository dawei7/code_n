# Merge Two Binary Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 617 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-two-binary-trees/) |

## Problem Description
### Goal
Given two binary trees `root1` and `root2`, place their roots and corresponding child positions over one another and merge them into a new binary tree. When both trees contain a node at the same position, the merged node's value is the sum of their values.

When only one tree contains a node at a position, use that non-null node and its structure in the merged tree. Begin the process at the two roots and apply the same rule recursively to left and right children. Return the root of the merged tree; if one input root is null, the other tree supplies the result.

### Function Contract
**Inputs**

- `root1`: the root of the first binary tree, or null
- `root2`: the root of the second binary tree, or null

**Return value**

- The root of a binary tree whose shape is the union of the input shapes
- At a shared position, the result value is the sum of both input values
- At a position occupied by only one tree, the result carries that node's value and descendants

### Examples
**Example 1**

- Input: `root1 = [1,3,2,5]`, `root2 = [2,1,3,null,4,null,7]`
- Output: `[3,4,5,5,4,null,7]`

**Example 2**

- Input: `root1 = [1]`, `root2 = [1,2]`
- Output: `[2,2]`
