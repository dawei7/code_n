# Invert Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 226 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/invert-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, invert its structure to form a mirror image. At every existing node, the original left subtree must become the right subtree and the original right subtree must become the left subtree, with the same transformation applied recursively throughout both branches.

Return the root of the inverted tree, reusing the original node values and preserving every node exactly once. Missing children swap positions just like present subtrees. An empty tree returns `null`, and a single-node tree remains structurally unchanged. The operation changes child links rather than merely reversing values within each level.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

The root of the inverted binary tree.

### Examples
**Example 1**

- Input: `[4,2,7,1,3,6,9]`
- Output: `[4,7,2,9,6,3,1]`

**Example 2**

- Input: `[2,1,3]`
- Output: `[2,3,1]`

**Example 3**

- Input: `[]`
- Output: `[]`
