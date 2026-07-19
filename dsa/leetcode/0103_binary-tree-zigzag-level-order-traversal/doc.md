# Binary Tree Zigzag Level Order Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 103 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) |

## Problem Description
### Goal
Given the root of a binary tree, return the zigzag level order traversal of its node values. The root level is read from left to right, the next level from right to left, and all following levels continue this alternating pattern.

Return one list for each level, ordered from the root toward the leaves. Reversing a level changes only the order in which its values appear; it does not change parent-child relationships or the order used to discover the following level. Omit missing children entirely, and return an empty list when the tree has no root.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

A list of value lists in alternating zigzag level order.

### Examples
**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `[[3], [20, 9], [15, 7]]`

**Example 2**

- Input: `root = [1]`
- Output: `[[1]]`

**Example 3**

- Input: `root = []`
- Output: `[]`
