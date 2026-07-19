# Populating Next Right Pointers in Each Node

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 116 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) |

## Problem Description
### Goal
You are given a perfect binary tree: every internal node has exactly two children, and all leaves occur at the same depth. Each node also has a `next` field that should link horizontally to another node on its own level.

Populate every `next` pointer so that it refers to the immediately adjacent node to the right at the same depth. This may connect nodes belonging to different parents. The rightmost node of every level has no neighbor and must point to `null`. Return the original root after modifying the existing nodes, and leave an empty tree unchanged.

### Function Contract
**Inputs**

- `root`: root of a perfect binary tree, encoded as a level-order `List[int | null]` in app cases

**Return value**

The same root object after all horizontal `next` links are populated. The app validates pointer identity at every level.

### Examples
**Example 1**

- Input: `root = [1, 2, 3, 4, 5, 6, 7]`
- Output links: `[1, #, 2, 3, #, 4, 5, 6, 7, #]`

**Example 2**

- Input: `root = []`
- Output links: `[]`

**Example 3**

- Input: `root = [1]`
- Output links: `[1, #]`
