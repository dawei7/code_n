# Range Sum of BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 938 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/range-sum-of-bst/) |

## Problem Description

### Goal

Given the `root` of a binary search tree and integers `low` and `high`, compute the sum of every node value in the inclusive interval from `low` through `high`.

The tree contains at least one node, all node values are unique, and its binary-search-tree ordering may be used: every value in a left subtree is smaller than its ancestor and every value in a right subtree is larger. Values equal to either boundary must be included.

### Function Contract

Let $N$ be the number of nodes, $h$ the tree height, $v$ the number of node values in the requested range, and $a$ and $b$ the values of `low` and `high`, respectively.

**Inputs**

- `root`: the root node of a binary search tree with $N$ nodes. Cases serialize the tree in level order.
- `low`, `high`: inclusive integer bounds satisfying $1 \le a \le b \le 10^5$.
- The tree has $1 \le N \le 2 \cdot 10^4$ unique values, each in $[1,10^5]$.

**Return value**

Return the sum of all node values $x$ such that $a \le x \le b$.

### Examples

**Example 1**

- Input: `root = [10,5,15,3,7,null,18], low = 7, high = 15`
- Output: `32`

**Example 2**

- Input: `root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10`
- Output: `23`
