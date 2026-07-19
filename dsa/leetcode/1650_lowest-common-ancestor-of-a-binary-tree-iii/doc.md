# Lowest Common Ancestor of a Binary Tree III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1650 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Two Pointers, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/) |

## Problem Description
### Goal
Two distinct nodes `p` and `q` belong to the same binary tree. Every node contains a `parent` pointer in addition to its value and child pointers, so either starting node can be followed upward without receiving the root separately.

Return the lowest common ancestor of `p` and `q`: the deepest node that is an ancestor of both. A node counts as its own ancestor, so if one input node lies on the other's path to the root, return that input node.

### Function Contract
**Inputs**

- `p`: one node in a parent-linked binary tree.
- `q`: a different node in the same tree.

The tree contains between 2 and $10^5$ nodes, all node values are unique, and both inputs are guaranteed to exist. Let $h$ be the tree height.

**Return value**

Return the node object that is the lowest common ancestor of `p` and `q`.

### Examples
**Example 1**

- Input: `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1`
- Output: `3`

The two upward paths first share the root node with value 3.

**Example 2**

- Input: `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4`
- Output: `5`

Node 5 is an ancestor of node 4 and is also its own ancestor.

**Example 3**

- Input: `root = [1, 2], p = 1, q = 2`
- Output: `1`
