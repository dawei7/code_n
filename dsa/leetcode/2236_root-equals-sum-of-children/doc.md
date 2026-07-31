# Root Equals Sum of Children

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2236 |
| Difficulty | Easy |
| Topics | Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/root-equals-sum-of-children/) |

## Problem Description

### Goal

You are given the root of a binary tree containing exactly three nodes. In
addition to the root, the tree has a left child and a right child; neither
child is absent, and there are no deeper descendants. Every node stores an
integer value that may be positive, negative, or zero.

Determine whether the value stored at the root is equal to the sum of the
values stored at its two children. Return `true` when that equality holds and
`false` otherwise. The comparison concerns the three node values only; the
fixed tree structure does not need to be traversed beyond those children.

### Function Contract

**Inputs**

- `root`: The root of a binary tree consisting of exactly the root, its left child, and its right child.

Every node value satisfies $-100\le\texttt{Node.val}\le 100$.

**Return value**

Return whether `root.val == root.left.val + root.right.val`.

### Examples

**Example 1**

- Input: `root = [10, 4, 6]`
- Output: `true`

**Example 2**

- Input: `root = [5, 3, 1]`
- Output: `false`

**Example 3**

- Input: `root = [0, -8, 8]`
- Output: `true`
