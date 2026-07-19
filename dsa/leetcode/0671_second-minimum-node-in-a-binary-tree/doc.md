# Second Minimum Node In a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 671 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/) |

## Problem Description
### Goal
You are given a non-empty special binary tree with non-negative node values. Every node has either zero or exactly two children, and each internal node's value equals the smaller value of its two children's values.

Return the second minimum value in the set of all node values in the tree: the smallest value strictly greater than the overall minimum. Repeated occurrences of the minimum do not become a second distinct value. If no greater node value exists, return `-1`.

### Function Contract
**Inputs**

- `root`: the root of a special binary tree satisfying the child-count and minimum-value rules

**Return value**

- The second smallest distinct value in the tree, or `-1` if all nodes have the same value

### Examples
**Example 1**

- Input: `root = [2,2,5,null,null,5,7]`
- Output: `5`

**Example 2**

- Input: `root = [2,2,2]`
- Output: `-1`

**Example 3**

- Input: `root = [1,1,3,1,1,3,4]`
- Output: `3`
