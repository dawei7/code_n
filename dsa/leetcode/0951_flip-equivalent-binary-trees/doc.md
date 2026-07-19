# Flip Equivalent Binary Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 951 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/flip-equivalent-binary-trees/) |

## Problem Description

### Goal

A flip operation on a binary tree chooses any node and swaps its entire left and right child subtrees. Any number of nodes, including none, may be flipped.

Two binary trees are flip equivalent exactly when some sequence of these operations can make their node values and structure identical. Flipping changes only the ordering of child subtrees; it never changes a node value, creates a node, or removes one. Given `root1` and `root2`, determine whether they are flip equivalent and return the corresponding boolean result.

### Function Contract

Let $n$ be the total number of nodes across both trees, and let $h$ be the greater tree height.

**Inputs**

- `root1`: the root of a binary tree, or `None`.
- `root2`: the root of a binary tree, or `None`.
- Each tree has from $0$ through $100$ nodes, with unique values within that tree from $0$ through $99$.

**Return value**

Return `true` if flips can make the trees identical; otherwise return `false`.

### Examples

**Example 1**

- Input: `root1 = [1, 2, 3, 4, 5, 6, null, null, null, 7, 8]`, `root2 = [1, 3, 2, null, 6, 4, 5, null, null, null, null, 8, 7]`
- Output: `true`

Flips at nodes with values `1`, `3`, and `5` make the trees identical.

**Example 2**

- Input: `root1 = []`, `root2 = []`
- Output: `true`

**Example 3**

- Input: `root1 = []`, `root2 = [1]`
- Output: `false`
