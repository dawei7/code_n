# Inorder Successor in BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 285 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/inorder-successor-in-bst/) |

## Problem Description
### Goal
Given a binary search tree with unique values and an existing target node `p`, find the node that appears immediately after `p` in an inorder traversal. Because inorder visits BST values in ascending order, this successor is the smallest stored value strictly greater than `p.val`.

Return the successor node under the native contract, or `null` when `p` is the tree's maximum and no successor exists. The app adapter receives and returns node values while preserving the same meaning. A successor may be the leftmost node of `p`'s right subtree or a higher ancestor; it is not necessarily an immediate child.

### Function Contract
**Inputs**

- `root`: the root of a BST with unique values
- `p`: the target node's value in the offline adapter; the native interface receives the target `TreeNode`

**Return value**

The successor value locally, or `null` when none exists. The native method returns the successor `TreeNode` or `None`.

### Examples
**Example 1**

- Input: `root = [2,1,3], p = 1`
- Output: `2`

**Example 2**

- Input: `root = [5,3,6,2,4,null,null,1], p = 6`
- Output: `null`

**Example 3**

- Input: `root = [5,3,6,2,4], p = 4`
- Output: `5`
