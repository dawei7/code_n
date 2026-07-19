# Validate Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 98 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/validate-binary-search-tree/) |

## Problem Description
### Goal
You are given the root of a binary tree. Determine whether the complete tree satisfies the strict binary search tree ordering: every value anywhere in a node's left subtree is smaller than that node, and every value anywhere in its right subtree is larger.

Return a boolean result. The rule applies through all ancestors, not only between a node and its immediate children. Duplicate values are therefore invalid. An empty tree is valid, and integer boundary values must be compared without inventing unsafe fixed sentinels.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

`True` if the complete tree is a valid binary search tree; otherwise `False`.

### Examples
**Example 1**

- Input: `root = [2, 1, 3]`
- Output: `True`

**Example 2**

- Input: `root = [5, 1, 4, null, null, 3, 6]`
- Output: `False`

**Example 3**

- Input: `root = [2, 2, 2]`
- Output: `False`
