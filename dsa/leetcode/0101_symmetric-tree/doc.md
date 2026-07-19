# Symmetric Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 101 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/symmetric-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, decide whether its structure and values are symmetric about a vertical line through the root. The two sides do not need identical child directions; instead, each node on the left must mirror a node of the same value on the right, with left and right children exchanged.

Return `True` only when this mirrored correspondence holds throughout both subtrees. A missing child must be paired with a missing child in the opposite position, so equal traversal values alone are insufficient. An empty tree and a tree containing only its root are symmetric.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

`True` when the tree is symmetric; otherwise `False`.

### Examples
**Example 1**

- Input: `root = [1, 2, 2, 3, 4, 4, 3]`
- Output: `True`

**Example 2**

- Input: `root = [1, 2, 2, null, 3, null, 3]`
- Output: `False`

**Example 3**

- Input: `root = [1]`
- Output: `True`
