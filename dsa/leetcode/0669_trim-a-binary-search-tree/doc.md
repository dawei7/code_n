# Trim a Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 669 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/trim-a-binary-search-tree/) |

## Problem Description
### Goal
Given the root of a binary search tree and boundaries `low` and `high`, trim the tree so that every remaining node value lies in the inclusive range `[low, high]`.

Trimming must preserve the relative structure of all retained nodes: a node that was a descendant of another retained node must remain its descendant after out-of-range nodes are removed. Return the root of the uniquely determined trimmed binary search tree. The original root may be removed, so the returned root can differ from the input root or be null.

### Function Contract
**Inputs**

- `root`: the root of a binary search tree with distinct values
- `low`: the inclusive lower value bound
- `high`: the inclusive upper value bound, with `low <= high`

**Return value**

- The root of the tree containing exactly the original nodes whose values are between `low` and `high`, with their valid BST relationships preserved

### Examples
**Example 1**

- Input: `root = [1,0,2], low = 1, high = 2`
- Output: `[1,null,2]`

**Example 2**

- Input: `root = [3,0,4,null,2,null,null,1], low = 1, high = 3`
- Output: `[3,2,null,1]`

**Example 3**

- Input: `root = [2,1,3], low = 2, high = 2`
- Output: `[2]`
