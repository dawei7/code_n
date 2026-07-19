# Binary Tree Maximum Path Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 124 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/) |

## Problem Description
### Goal
Given a nonempty binary tree with possibly negative node values, consider paths made from nodes connected by parent-child edges. A path may start and end at any nodes, may travel up through a common ancestor and down another branch, and each node may appear in the path at most once.

Return the largest sum of values along one such nonempty path. The chosen path does not have to include the root or reach a leaf, and a single node is itself a valid path. Because all surrounding values can be harmful, an entirely negative tree must return its least negative node rather than an empty-path sum of zero.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

The maximum sum among all valid nonempty paths.

### Examples
**Example 1**

- Input: `root = [1, 2, 3]`
- Output: `6`

**Example 2**

- Input: `root = [-10, 9, 20, null, null, 15, 7]`
- Output: `42`

**Example 3**

- Input: `root = [-3]`
- Output: `-3`
