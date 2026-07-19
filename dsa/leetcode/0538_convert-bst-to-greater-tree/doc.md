# Convert BST to Greater Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 538 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-bst-to-greater-tree/) |

## Problem Description
### Goal
Given a binary search tree with unique values, transform every node in place. Its new value must equal its original value plus the original values of all nodes whose values are greater.

Return the root of the transformed tree, preserving the existing node structure and child links. All sums are based on original values, so an earlier update must not be counted again as though it were another node. The maximum-valued node remains unchanged, while smaller nodes accumulate an increasingly large suffix of the BST's sorted values.

### Function Contract
**Inputs**

- `root`: the root of a binary search tree

**Return value**

- The root of the tree after every node has been replaced by its greater-or-equal value sum

### Examples
**Example 1**

- Input tree: `[4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]`
- Output tree: `[30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8]`

**Example 2**

- Input tree: `[1, 0, 2]`
- Output tree: `[3, 3, 2]`

**Example 3**

- Input tree: `[0, null, 1]`
- Output tree: `[1, null, 1]`
