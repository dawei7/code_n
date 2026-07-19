# Equal Tree Partition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 663 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/equal-tree-partition/) |

## Problem Description
### Goal
Given the root of a binary tree whose nodes contain integer values, determine whether you can remove exactly one existing parent-child edge so that the original tree separates into two nonempty trees.

Return `True` if the sums of the node values in those two resulting trees can be equal, and `False` otherwise. No node values may be changed or discarded, and the cut must correspond to one edge; merely dividing a collection of values into two equal groups is not sufficient unless one group is an entire detachable subtree.

### Function Contract
**Inputs**

- `root`: the non-null root node of a binary tree whose values may be positive, zero, or negative

**Return value**

- `True` if one parent-child edge can be removed to create equal sums; otherwise `False`

### Examples
**Example 1**

- Input: `root = [5, 10, 10, null, null, 2, 3]`
- Output: `True`

**Example 2**

- Input: `root = [1, 2, 10, null, null, 2, 20]`
- Output: `False`

**Example 3**

- Input: `root = [0, 0]`
- Output: `True`
