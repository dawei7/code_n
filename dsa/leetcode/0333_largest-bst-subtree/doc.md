# Largest BST Subtree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 333 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-bst-subtree/) |

## Problem Description
### Goal
Given an arbitrary binary tree, consider the complete rooted subtree at every node. Such a subtree is a binary search tree only when every value in its left branch is strictly smaller than the root and every value in its right branch is strictly larger, with both branches recursively satisfying the same rule.

Return the maximum node count among all rooted subtrees that are valid BSTs. A qualifying region must include all descendants of its chosen root, not an arbitrary pruned selection. Every leaf is a size-one BST, duplicate boundary values violate strict ordering, and an empty tree returns `0`.

### Function Contract
**Inputs**

- `root`: the binary-tree root, represented by a level-order list in app cases

**Return value**

The maximum node count among all subtrees that are valid strict BSTs.

### Examples
**Example 1**

- Input: `root = [10,5,15,1,8,null,7]`
- Output: `3`

**Example 2**

- Input: `root = [2,1,3]`
- Output: `3`

**Example 3**

- Input: `root = [1]`
- Output: `1`
