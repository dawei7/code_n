# Binary Tree Longest Consecutive Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 298 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/) |

## Problem Description
### Goal
Given a binary tree, find a downward path in which each next node is a direct child of the previous node and has value exactly one greater. The path may begin at any node and then follow either left or right child choices, but it cannot move upward or skip levels.

Return the maximum number of nodes in any valid path. A single node is a length-one consecutive path, repeated or decreasing values break the current sequence, and a later descendant may start a new one. Return `0` for an empty tree. The function reports only the length, not the node values or path itself.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

The number of nodes in the longest valid downward consecutive path, or zero for an empty tree.

### Examples
**Example 1**

- Input: `root = [1,null,3,2,4,null,null,null,5]`
- Output: `3`

**Example 2**

- Input: `root = [2,null,3,2,null,1]`
- Output: `2`

**Example 3**

- Input: `root = []`
- Output: `0`
