# Balanced Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 110 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/balanced-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, determine whether the tree is height-balanced. The height of a subtree is the length of its longest downward node path, and the balance condition must be evaluated independently at every node.

Return `True` only if each node's left and right subtree heights differ by at most one. A balanced root does not guarantee a balanced tree when a deeper descendant violates the condition, so the entire structure matters. Empty subtrees have height zero, making an empty tree and any single-node tree balanced; return `False` as soon as any level contains an excessive height difference.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

`True` if the entire tree is height-balanced; otherwise `False`.

### Examples
**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `True`

**Example 2**

- Input: `root = [1, 2, 2, 3, 3, null, null, 4, 4]`
- Output: `False`

**Example 3**

- Input: `root = []`
- Output: `True`
