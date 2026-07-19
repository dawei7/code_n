# Binary Tree Inorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 94 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Stack, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-inorder-traversal/) |

## Problem Description
### Goal
You are given the root of a binary tree, which may be empty. Traverse its nodes in inorder: recursively process the entire left subtree, then visit the current node, and finally process the entire right subtree.

Return the visited node values in exactly that sequence. Every existing node must contribute once, while absent children contribute nothing. For a binary search tree this order is nondecreasing, but the traversal contract applies to arbitrary binary trees as well.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

The node values in inorder traversal order.

### Examples
**Example 1**

- Input: `root = [1, null, 2, 3]`
- Output: `[1, 3, 2]`

**Example 2**

- Input: `root = []`
- Output: `[]`

**Example 3**

- Input: `root = [1]`
- Output: `[1]`
