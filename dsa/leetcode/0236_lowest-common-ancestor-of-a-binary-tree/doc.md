# Lowest Common Ancestor of a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 236 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) |

## Problem Description
### Goal
Given an ordinary binary tree with unique values and two target nodes known to occur in it, find their lowest common ancestor. A node counts as its own ancestor, so one target is the answer when the other lies within that target's subtree.

Return the value of the deepest node whose subtree contains both targets. Unlike a binary search tree, node values provide no ordering shortcut; ancestry is determined solely by child relationships. If the targets lie in different branches, their first shared branching ancestor is the answer. Return only that node's value under the app contract rather than a path or depth.

### Function Contract
**Inputs**

- `root`: the root of a binary tree with unique values
- `p`: the value of the first target node
- `q`: the value of the second target node

**Return value**

The value of the targets' lowest common ancestor.

### Examples
**Example 1**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1`
- Output: `3`

**Example 2**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4`
- Output: `5`

**Example 3**

- Input: `root = [1,2], p = 1, q = 2`
- Output: `1`
