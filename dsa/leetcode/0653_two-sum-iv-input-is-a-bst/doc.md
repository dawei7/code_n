# Two Sum IV - Input is a BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 653 |
| Difficulty | Easy |
| Topics | Hash Table, Two Pointers, Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) |

## Problem Description
### Goal
Given the root of a valid binary search tree and an integer `k`, determine whether there are two elements in the tree whose values add up exactly to `k`.

Return `True` when such a pair exists and `False` otherwise. The two elements must come from distinct tree nodes; one node cannot be used twice, even when doubling its value would equal `k`. Equal values in separate nodes may form a valid pair if the tree representation permits them.

### Function Contract
**Inputs**

- `root`: the root node of a binary search tree
- `k`: the target integer sum

**Return value**

- `True` if a pair of distinct nodes sums to `k`; otherwise `False`

### Examples
**Example 1**

- Input: `root = [5, 3, 6, 2, 4, null, 7]`, `k = 9`
- Output: `True`

**Example 2**

- Input: `root = [5, 3, 6, 2, 4, null, 7]`, `k = 28`
- Output: `False`

**Example 3**

- Input: `root = [2, 1, 3]`, `k = 4`
- Output: `True`
