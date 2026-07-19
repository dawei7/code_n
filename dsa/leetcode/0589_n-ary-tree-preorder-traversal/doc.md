# N-ary Tree Preorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 589 |
| Difficulty | Easy |
| Topics | Stack, Tree, Depth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/n-ary-tree-preorder-traversal/) |

## Problem Description
### Goal
Given the root of an n-ary tree, return the preorder traversal of its node values. In preorder, visit the current node first and then traverse each of its children from left to right using the same rule.

Return the values in exactly that visitation order. An empty tree produces an empty list, and a node may have any number of children. The level-order serialization used to describe inputs does not change the traversal rule: null separators identify child groups but are not tree nodes or output values.

### Function Contract
**Inputs**

- `root`: the app representation of an N-ary node as `[value, children]`, recursively, or `None` for an empty tree

**Return value**

- A list of node values in root-first, left-to-right preorder

### Examples
**Example 1**

- Input: `[1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`
- Output: `[1, 3, 5, 6, 2, 4]`

**Example 2**

- Input: `[7, []]`
- Output: `[7]`

**Example 3**

- Input: `None`
- Output: `[]`
