# Construct Binary Tree from String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 536 |
| Difficulty | Medium |
| Topics | String, Stack, Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-string/) |

## Problem Description
### Goal
Given a string representation of a binary tree, each node begins with its signed integer value, followed by zero, one, or two parenthesized child representations. Children occur in preorder: the first parenthesized subtree is left and the second is right.

Construct and return the represented binary tree. Empty parentheses may mark a missing left child when a right child must still be written, while an omitted trailing child is simply absent. Parse multi-digit and negative values, preserve the complete nesting structure, and consume the full string rather than stopping after one node or treating parentheses as ordinary characters.

### Function Contract
**Inputs**

- `s`: the tree encoding, containing signed decimal integers and balanced parentheses

**Return value**

- The root of the represented binary tree, or an empty tree when `s` is empty

### Examples
**Example 1**

- Input: `s = "4(2(3)(1))(6(5))"`
- Output tree: `[4, 2, 6, 3, 1, 5]`

**Example 2**

- Input: `s = "-4(2)(3)"`
- Output tree: `[-4, 2, 3]`

**Example 3**

- Input: `s = "4()(5)"`
- Output tree: `[4, null, 5]`
