# Subtree of Another Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 572 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, String Matching, Binary Tree, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/subtree-of-another-tree/) |

## Problem Description
### Goal
Given the roots of two binary trees, `root` and `subRoot`, determine whether `subRoot` is a subtree of `root`. A subtree begins at some node of `root` and consists of that node together with all of its descendants; no descendant may be omitted from the selected tree.

Return `True` if some node in `root` begins a tree that is identical to `subRoot`, and `False` otherwise. Identical means that the subtree has the same structure and node values as `subRoot`, including the placement of missing children.

### Function Contract
**Inputs**

- `root`: the root of the main binary tree
- `sub_root`: the root of the candidate subtree

**Return value**

- `True` if some node of `root` begins a tree identical to `subRoot`; otherwise `False`

### Examples
**Example 1**

- Input: `root = [3,4,5,1,2], subRoot = [4,1,2]`
- Output: `True`

**Example 2**

- Input: `root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]`
- Output: `False`

**Example 3**

- Input: `root = [1,2,3], subRoot = [1,2,3]`
- Output: `True`
