# Populating Next Right Pointers in Each Node II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 117 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/) |

## Problem Description
### Goal
You are given an arbitrary binary tree whose nodes include an additional `next` field. The tree may be sparse, its leaves may occur at different depths, and a node may have either child, both children, or neither.

Populate each `next` pointer with the immediately adjacent node to the right on the same level, skipping any absent child positions between them. Neighbors can belong to different parents, and the rightmost existing node at every depth must point to `null`. Modify the supplied nodes in place and return the original root; if the tree is empty, return `null` without creating nodes.

### Function Contract
**Inputs**

- `root`: root of an arbitrary binary tree, encoded as a level-order `List[int | null]` in app cases

**Return value**

The same root object after all horizontal `next` links are populated. The app validates pointer identity at every level.

### Examples
**Example 1**

- Input: `root = [1, 2, 3, 4, 5, null, 7]`
- Output links: `[1, #, 2, 3, #, 4, 5, 7, #]`

**Example 2**

- Input: `root = []`
- Output links: `[]`

**Example 3**

- Input: `root = [1]`
- Output links: `[1, #]`
