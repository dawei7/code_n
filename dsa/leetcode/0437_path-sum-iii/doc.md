# Path Sum III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 437 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/path-sum-iii/) |

## Problem Description
### Goal
Given a binary tree and an integer `targetSum`, consider every nonempty downward path formed by following parent-to-child links. A path may begin and end at any nodes; it does not need to start at the root or finish at a leaf.

Return the number of distinct paths whose node values sum exactly to the target. Paths with different starting or ending nodes count separately even when their value sequences match. Negative and zero values may make prefix sums repeat, and a path cannot move upward or switch between branches. An empty tree contributes zero paths.

### Function Contract
**Inputs**

- `root`: the app's level-order array representation of the binary tree, using `None` for missing children
- `targetSum`: the required sum of a counted downward path

**Return value**

- Return the number of distinct nonempty downward paths whose values add to `targetSum`.

### Examples
**Example 1**

- Input: `root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], targetSum = 8`
- Output: `3`

**Example 2**

- Input: `root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], targetSum = 22`
- Output: `3`

**Example 3**

- Input: `root = [], targetSum = 0`
- Output: `0`
