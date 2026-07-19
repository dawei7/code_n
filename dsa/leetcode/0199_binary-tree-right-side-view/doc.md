# Binary Tree Right Side View

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 199 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/) |

## Problem Description
### Goal
Given the root of a binary tree, imagine observing the tree from its right side. At each occupied depth, only the rightmost existing node on that level is visible; this node may belong to a left subtree when no farther-right node exists at that depth.

Return the visible values in top-to-bottom order, beginning with the root's value. Include exactly one value for every nonempty level, omit missing-child placeholders, and determine visibility from structure rather than from node values. An empty tree has no visible levels and returns an empty list, while an unbalanced tree can reveal nodes from different branches as depth increases.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

A top-to-bottom list containing the rightmost node value at each occupied level.

### Examples
**Example 1**

- Input: `[1,2,3,null,5,null,4]`
- Output: `[1,3,4]`

**Example 2**

- Input: `[1,null,3]`
- Output: `[1,3]`

**Example 3**

- Input: `[]`
- Output: `[]`
