# Binary Tree Postorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 145 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Stack, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-postorder-traversal/) |

## Problem Description
### Goal
Given the root of a binary tree, traverse every reachable node in postorder. For each subtree, completely visit its left branch, then completely visit its right branch, and record the subtree's root only after both branches are finished.

Return the node values in this precise left-right-root order. Existing nodes must each appear once, while missing children add no placeholders. Repeated values do not merge separate nodes or change their structural ordering. An empty root yields an empty list, and in every nonempty result the final value belongs to the original tree's root.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order list with `null` placeholders in app cases

**Return value**

A list of node values in left-right-root postorder.

### Examples
**Example 1**

- Input: `root = [1,null,2,3]`
- Output: `[3,2,1]`

**Example 2**

- Input: `root = []`
- Output: `[]`

**Example 3**

- Input: `root = [1,2,3,4,5,null,8]`
- Output: `[4,5,2,8,3,1]`
