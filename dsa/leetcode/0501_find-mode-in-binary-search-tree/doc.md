# Find Mode in Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 501 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-mode-in-binary-search-tree/) |

## Problem Description
### Goal
Given a nonempty binary search tree that may contain duplicate values, count how often every stored value occurs. The tree permits equal keys on either side under its ordering definition, so repeated values remain separate nodes even though they contribute to the same frequency.

Return all modes: every value whose occurrence count equals the maximum frequency in the tree. If several values tie, return them in any order and list each mode once. The result contains values rather than nodes or counts. Meet the follow-up without extra auxiliary space beyond the implicit recursion stack when using the BST's inorder ordering.

### Function Contract
**Inputs**

- `root`: the root node of a nonempty binary search tree

**Return value**

- All tree values whose occurrence count equals the maximum frequency

### Examples
**Example 1**

- Input: `root = [1, null, 2, 2]`
- Output: `[2]`

**Example 2**

- Input: `root = [0]`
- Output: `[0]`

**Example 3**

- Input: `root = [1, null, 2]`
- Output: `[1, 2]`
