# Minimum Depth of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 111 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, find the length of its shortest downward path that reaches a leaf. A leaf is specifically a node with neither a left nor a right child, and path length is measured by the number of nodes visited from the root through that leaf.

Return this minimum node count, or `0` when the tree is empty. A missing child beside a nonempty subtree is not itself a leaf and cannot create a shorter path, so a one-sided tree must be followed until an actual terminal node is reached. A tree containing only its root has minimum depth `1`.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

The minimum root-to-leaf depth, or `0` for an empty tree.

### Examples
**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `2`

**Example 2**

- Input: `root = [2, null, 3, null, 4, null, 5, null, 6]`
- Output: `5`

**Example 3**

- Input: `root = []`
- Output: `0`
