# Binary Tree Preorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 144 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Stack, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-preorder-traversal/) |

## Problem Description
### Goal
Given the root of a binary tree, traverse every reachable node in preorder. For each subtree, visit its root first, then completely traverse its left subtree, and finally completely traverse its right subtree.

Return the encountered node values in that exact root-left-right order. Missing children contribute no placeholder values, but their absence still determines which existing branch is left or right. Each node must appear exactly once even when values repeat. An empty tree has no visits and therefore produces an empty list, while a single-node tree produces a one-value list.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order list with `null` placeholders in app cases

**Return value**

A list of node values in root-left-right preorder.

### Examples
**Example 1**

- Input: `root = [1,null,2,3]`
- Output: `[1,2,3]`

**Example 2**

- Input: `root = []`
- Output: `[]`

**Example 3**

- Input: `root = [1,2,3,4,5,null,8]`
- Output: `[1,2,4,5,3,8]`
