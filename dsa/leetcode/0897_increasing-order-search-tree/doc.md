# Increasing Order Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 897 |
| Difficulty | Easy |
| Topics | Stack, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/increasing-order-search-tree/) |

## Problem Description
### Goal
Given the `root` of a binary search tree, rearrange its nodes in in-order sequence.

The leftmost node of the original tree must become the new root. Every node in the result must have no left child, and successive in-order nodes must be connected through right-child pointers. Consequently, the result is a single rightward chain whose values appear in increasing order.

Return the root of this rearranged tree.

### Function Contract
Let $n$ be the number of nodes and $h$ be the height of the input tree.

**Inputs**

- `root`: the root node of a binary search tree containing $1 \leq n \leq 100$ nodes.
- Every node value satisfies $0 \leq \texttt{Node.val} \leq 1000$.

**Return value**

Return the leftmost original node as the root of a tree in which every left pointer is `None` and each right pointer leads to the next node in in-order sequence.

### Examples
**Example 1**

- Input: `root = [5,3,6,2,4,null,8,1,null,null,null,7,9]`
- Output: `[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]`

**Example 2**

- Input: `root = [5,1,7]`
- Output: `[1,null,5,null,7]`

**Example 3**

- Input: `root = [2,1]`
- Output: `[1,null,2]`
