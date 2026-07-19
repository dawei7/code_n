# Number of Ways to Reorder Array to Get Same BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1569 |
| Difficulty | Hard |
| Topics | Array, Math, Divide and Conquer, Dynamic Programming, Tree, Union-Find, Binary Search Tree, Memoization, Combinatorics, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/) |

## Problem Description
### Goal

The array `nums` is a permutation of the integers from `1` through $N$. Insert its values from left to right into an initially empty binary search tree: a smaller value follows left-child links and a larger value follows right-child links until an empty position is found.

Count the reorderings of `nums` that construct exactly the same binary search tree as the original insertion order. Exclude the original ordering itself and return the result modulo $1{,}000{,}000{,}007$.

### Function Contract
**Inputs**

- `nums`: A permutation of every integer from `1` through $N$, where $1 \le N \le 1000$.

**Return value**

Return the number of different reorderings that produce the identical BST shape and key placement, excluding `nums` itself, modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `nums = [2,1,3]`
- Output: `1`

**Example 2**

- Input: `nums = [3,4,5,1,2]`
- Output: `5`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `0`
