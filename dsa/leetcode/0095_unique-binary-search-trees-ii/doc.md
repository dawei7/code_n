# Unique Binary Search Trees II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 95 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Backtracking, Tree, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-binary-search-trees-ii/) |

## Problem Description
### Goal
Given `n`, construct binary search trees using every integer key from `1` through `n` exactly once. Each tree must satisfy the strict ordering rule: all keys in a node's left subtree are smaller, and all keys in its right subtree are larger.

Return one root for every structurally unique valid tree, in any order. Trees that differ in at least one parent-child relationship are different structures even though their inorder value sequence is identical. No valid structure may be omitted or duplicated.

### Function Contract
**Inputs**

- `n`: the number of consecutive keys, with keys `1..n`

**Return value**

A list of `TreeNode` roots representing every distinct valid tree, in any order. App results are displayed as level-order lists.

### Examples
**Example 1**

- Input: `n = 3`
- Output: five distinct binary search trees

**Example 2**

- Input: `n = 1`
- Output: `[[1]]`

**Example 3**

- Input: `n = 2`
- Output: two trees, rooted at `1` and `2` respectively
