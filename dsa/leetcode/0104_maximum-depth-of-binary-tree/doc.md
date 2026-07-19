# Maximum Depth of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 104 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, measure how far the tree extends along its longest downward route. A route begins at the root, follows child pointers, and ends at a leaf, which is a node with no children.

Return the maximum number of nodes encountered on any such root-to-leaf route. Depth counts nodes rather than edges, so a tree containing only its root has depth `1`. An empty tree has no route and therefore has maximum depth `0`; an unbalanced branch may determine the answer even when most of the tree is shallow.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

The tree's maximum depth; an empty tree has depth `0`.

### Examples
**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `3`

**Example 2**

- Input: `root = [1, null, 2]`
- Output: `2`

**Example 3**

- Input: `root = []`
- Output: `0`
