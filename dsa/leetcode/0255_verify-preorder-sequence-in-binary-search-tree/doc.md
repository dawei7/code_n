# Verify Preorder Sequence in Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 255 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Tree, Binary Search Tree, Recursion, Monotonic Stack, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/) |

## Problem Description
### Goal
Given an array of distinct integers, decide whether it could be the preorder traversal of some binary search tree. Preorder visits a root before all nodes in its left subtree and then all nodes in its right subtree, while binary-search ordering places smaller values left and larger values right.

Return `True` when one valid tree structure can produce the entire sequence and `False` otherwise. Every array value must be used exactly once in the proposed tree; a later value cannot return to a completed left-side range after traversal has entered a right subtree. Meet the required linear-time and constant-extra-space target for verification.

### Function Contract
**Inputs**

- `preorder`: distinct node values in proposed root-left-right order

**Return value**

`True` exactly when some binary search tree has that preorder traversal.

### Examples
**Example 1**

- Input: `preorder = [5,2,1,3,6]`
- Output: `true`

**Example 2**

- Input: `preorder = [5,2,6,1,3]`
- Output: `false`

**Example 3**

- Input: `preorder = [1,2,3]`
- Output: `true`
