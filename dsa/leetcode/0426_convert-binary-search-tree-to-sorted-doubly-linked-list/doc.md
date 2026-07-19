# Convert Binary Search Tree to Sorted Doubly Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 426 |
| Difficulty | Medium |
| Topics | Linked List, Stack, Tree, Depth-First Search, Binary Search Tree, Binary Tree, Doubly-Linked List |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) |

## Problem Description
### Goal
Given the root of a binary search tree, convert its existing nodes into a sorted circular doubly linked list. Binary-search inorder order determines the ascending sequence, and node `left` and `right` pointers become previous and next links respectively.

Return the smallest node as the list head. Following `right` must visit every node once in ascending order before returning to the head; following `left` must traverse the reverse order. Join the largest and smallest nodes in both directions, reuse every original node exactly once, and return `null` for an empty tree.

### Function Contract
**Inputs**

- `root`: the root node of a binary search tree, or `None` for an empty tree

**Return value**

- Return the smallest node; following `right` visits values in ascending order and following `left` visits them in descending order, with both ends joined circularly. Example outputs show one complete forward traversal.

### Examples
**Example 1**

- Input: `root = [4, 2, 5, 1, 3]`
- Output: `[1, 2, 3, 4, 5]`

**Example 2**

- Input: `root = [2, 1, 3]`
- Output: `[1, 2, 3]`

**Example 3**

- Input: `root = []`
- Output: `[]`
