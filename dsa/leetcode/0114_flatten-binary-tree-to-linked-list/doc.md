# Flatten Binary Tree to Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 114 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Stack, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) |

## Problem Description
### Goal
Given the root of a binary tree, transform that same tree into a linear structure using its existing nodes. The final order must match a preorder traversal of the original structure: visit a node, then its left subtree, then its right subtree.

Perform the transformation in place. Each node's `right` pointer must lead to the next node in preorder, every `left` pointer must be set to `null`, and the final node's `right` pointer must also be `null`. Do not allocate a replacement list or return copied values; callers observe the rewired tree through the original root, with an empty tree remaining unchanged.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

`None`; mutate the `TreeNode` structure in place. The app displays the resulting right-skewed tree.

### Examples
**Example 1**

- Input: `root = [1, 2, 5, 3, 4, null, 6]`
- Output tree: `[1, null, 2, null, 3, null, 4, null, 5, null, 6]`

**Example 2**

- Input: `root = []`
- Output tree: `[]`

**Example 3**

- Input: `root = [0]`
- Output tree: `[0]`
