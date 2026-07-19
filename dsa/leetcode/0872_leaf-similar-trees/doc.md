# Leaf-Similar Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 872 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/leaf-similar-trees/) |

## Problem Description
### Goal
Read the leaves of a binary tree from left to right. Their values, in that order, form the tree's leaf value sequence. For example, a tree whose leaves are encountered with values `6`, `7`, `4`, `9`, and `8` has leaf value sequence `[6,7,4,9,8]`; values stored at internal nodes do not appear in the sequence.

Two binary trees are leaf-similar exactly when their leaf value sequences are identical. Given the head nodes `root1` and `root2`, return `true` if and only if the two trees are leaf-similar.

### Function Contract
**Inputs**

- `root1`: the root of the first nonempty binary tree.
- `root2`: the root of the second nonempty binary tree.
- Each tree contains between $1$ and $200$ nodes, and every node value is between $0$ and $200$.
- Let $n_1$ and $n_2$ be the numbers of nodes in the first and second trees, and let $h_1$ and $h_2$ be their respective heights.

**Return value**

Return `true` when the two left-to-right leaf value sequences contain the same values in the same order; otherwise, return `false`.

### Examples
**Example 1**

- Input: `root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]`
- Output: `true`

Both trees have leaf value sequence `[6,7,4,9,8]`.

**Example 2**

- Input: `root1 = [1,2,3], root2 = [1,3,2]`
- Output: `false`

The first sequence is `[2,3]`, while the second is `[3,2]`.

**Example 3**

- Input: `root1 = [1,2,3], root2 = [7,8,3,2]`
- Output: `true`

The tree shapes and internal values differ, but both leaf sequences are `[2,3]`.
