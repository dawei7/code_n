# Inorder Successor in BST II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 510 |
| Difficulty | Medium |
| Topics | Tree, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/inorder-successor-in-bst-ii/) |

## Problem Description
### Goal
Given a node `p` in a binary search tree whose nodes contain left, right, and parent pointers, find the node that appears immediately after `p` in an inorder traversal. Inorder visits the left subtree, the node, and then the right subtree, so the successor is the next larger tree position under the BST ordering.

Return the successor node, not merely its value, or `null` when `p` is the final inorder node. The answer is the leftmost node in `p`'s right subtree when that subtree exists; otherwise it may be the first ancestor reached from a left-child branch. Do not require access to the tree root separately.

### Function Contract
**Inputs**

- `node`: a selected BST `Node` with `left`, `right`, and `parent` references

**Return value**

- The inorder-successor `Node`, or `null` if no successor exists

### Examples
**Example 1**

- Input: `tree = [2, 1, 3], node = 1`
- Output: `2`

**Example 2**

- Input: `tree = [5, 3, 6, 2, 4, null, null, 1], node = 6`
- Output: `null`

**Example 3**

- Input: `tree = [5, 3, 6, 2, 4, null, null, 1], node = 4`
- Output: `5`
