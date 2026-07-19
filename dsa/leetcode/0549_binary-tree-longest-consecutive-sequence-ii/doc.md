# Binary Tree Longest Consecutive Sequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 549 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/) |

## Problem Description
### Goal
Given a binary tree, choose a path of connected nodes without revisiting any node. The path may move from a child up through its parent and down into another child, but adjacent values along the complete path must change by exactly one in one consistent direction: strictly increasing or strictly decreasing.

Return the maximum number of nodes in such a consecutive path. The path may start and end anywhere and need not include the root. A turn through a parent can join one increasing branch with one decreasing branch when their values align, but a sequence that reverses numerical direction partway through its traversal is invalid.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

- The length of the longest increasing or decreasing consecutive path

### Examples
**Example 1**

- Input tree: `[1, 2, 3]`
- Output: `2`

**Example 2**

- Input tree: `[2, 1, 3]`
- Output: `3`

**Example 3**

- Input tree: `[1]`
- Output: `1`
