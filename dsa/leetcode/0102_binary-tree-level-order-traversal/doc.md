# Binary Tree Level Order Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 102 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/) |

## Problem Description
### Goal
Given the root of a binary tree, return the level order traversal of its node values. The root forms the first level, its existing children form the second, and this grouping continues until every reachable node has been included.

Return a list containing one list per level, ordered from the root downward. Within each level, values must retain their natural left-to-right tree order, including across different parents. Missing children contribute no placeholder values, and an empty tree produces an empty outer list rather than a level containing `null`.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

A list of value lists, one left-to-right list for each tree depth.

### Examples
**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `[[3], [9, 20], [15, 7]]`

**Example 2**

- Input: `root = [1]`
- Output: `[[1]]`

**Example 3**

- Input: `root = []`
- Output: `[]`
