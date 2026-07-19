# N-ary Tree Postorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 590 |
| Difficulty | Easy |
| Topics | Stack, Tree, Depth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/n-ary-tree-postorder-traversal/) |

## Problem Description
### Goal
Given the root of an n-ary tree, return the postorder traversal of its node values. In postorder, completely traverse each child subtree from left to right before visiting the current node itself.

Return the values in exactly that visitation order. An empty tree produces an empty list, and a node may have any number of children. The level-order serialization used for the input only separates groups of children with null markers; those markers are not nodes and do not appear in the traversal result.

### Function Contract
**Inputs**

- `root`: the app representation of an N-ary node as `[value, children]`, recursively, or `None` for an empty tree

**Return value**

- A list of node values in left-to-right children-first postorder

### Examples
**Example 1**

- Input: `[1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`
- Output: `[5, 6, 3, 2, 4, 1]`

**Example 2**

- Input: `[7, []]`
- Output: `[7]`

**Example 3**

- Input: `None`
- Output: `[]`
