# Linked List in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1367 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/linked-list-in-binary-tree/) |

## Problem Description

### Goal

Given the head of a nonempty singly linked list and the root of a nonempty binary tree, determine whether the linked-list values appear along some downward path in the tree.

The path may begin at any tree node, but after it begins each next list value must match either the left child or the right child of the preceding matched tree node. The path cannot move upward, skip tree levels, or switch between siblings. Return whether any such complete match exists.

### Function Contract

**Inputs**

- `head`: the first node of a linked list containing $L$ values.
- `root`: the root of a binary tree with $N$ nodes and height $H$.
- Node values lie in a fixed domain of size $U=100$.

**Return value**

- `true` when one downward tree path contains the entire linked-list sequence contiguously; otherwise `false`.

### Examples

**Example 1**

- Input: `head = [4,2,8]`, `root = [1,4,9,null,2,null,4,null,8]`
- Output: `true`

**Example 2**

- Input: `head = [1,4,2,6]`, `root = [1,4,3,null,2,null,null,6]`
- Output: `true`

**Example 3**

- Input: `head = [1,4,2,6,8]`, `root = [1,4,3,null,2,null,null,6]`
- Output: `false`
