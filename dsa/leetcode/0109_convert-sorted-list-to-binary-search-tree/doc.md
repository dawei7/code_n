# Convert Sorted List to Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 109 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Divide and Conquer, Tree, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) |

## Problem Description
### Goal
Given the head of a singly linked list whose values are sorted in ascending order, construct a binary search tree containing every list element exactly once. The resulting node values must obey binary-search ordering throughout the entire tree, not only between each parent and its immediate children.

The tree must be height-balanced, meaning the left and right subtree heights differ by at most one at every node. Several balanced shapes may be valid, so the exact root is not prescribed when multiple choices work. Do not lose or duplicate repeated-position list nodes, and return `null` when the input list is empty.

### Function Contract
**Inputs**

- `head`: the head of a sorted linked list, encoded as a `List[int]` in app cases

**Return value**

A height-balanced `TreeNode` root. Multiple valid shapes may exist; app results are checked by values, ordering, and balance.

### Examples
**Example 1**

- Input: `head = [-10, -3, 0, 5, 9]`
- Output: a valid balanced BST such as `[0, -3, 9, -10, null, 5]`

**Example 2**

- Input: `head = []`
- Output: `[]`

**Example 3**

- Input: `head = [1, 3]`
- Output: either `[3, 1]` or `[1, null, 3]`
