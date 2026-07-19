# Lowest Common Ancestor of a Binary Tree IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1676 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/) |

## Problem Description
### Goal

Given a binary tree and a nonempty collection of distinct nodes from that tree, find their lowest common ancestor. Every supplied node is guaranteed to occur in the tree, and every node value in the tree is unique. A node is considered its own descendant, so a target may itself be the common ancestor sought.

The answer is the deepest node whose subtree contains every supplied target. For a single target, that target is therefore the answer. Values do not impose binary-search ordering; only the parent-child structure determines ancestry. Return the ancestor node itself, not its depth or a path.

### Function Contract
**Inputs**

- `root`: the root of a binary tree containing $N$ nodes with unique values
- `nodes`: a nonempty list of $K$ distinct node references drawn from that same tree

Let $H$ denote the height of the tree.

**Return value**

The lowest common ancestor object shared by every supplied target.

### Examples
**Example 1**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]`
- Output: `2`

**Example 2**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]`
- Output: `1`

**Example 3**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]`
- Output: `5`
