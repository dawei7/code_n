# Binary Tree Level Order Traversal II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 107 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) |

## Problem Description
### Goal
Given the root of a binary tree, return the bottom-up level order traversal of its node values. Unlike ordinary top-down level order, the deepest level must appear first and the root's level must appear last.

Return a list of level lists arranged from bottom to top. Values within every individual level still follow the tree's left-to-right order; only the order of the levels is reversed. Nodes at different depths must never be combined, missing children add no placeholders, and an empty input tree produces an empty result rather than a list containing an empty level.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

A list of left-to-right level lists ordered from bottom to top.

### Examples
**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `[[15, 7], [9, 20], [3]]`

**Example 2**

- Input: `root = [1]`
- Output: `[[1]]`

**Example 3**

- Input: `root = []`
- Output: `[]`
