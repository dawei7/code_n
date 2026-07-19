# Pseudo-Palindromic Paths in a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1457 |
| Difficulty | Medium |
| Topics | Bit Manipulation, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/) |

## Problem Description
### Goal

You are given the root of a non-empty binary tree. Every node stores a digit
from $1$ through $9$. Each root-to-leaf path contributes the sequence of node
values encountered from the root down to that leaf; a leaf is a node with no
left or right child.

A path is pseudo-palindromic when its values can be rearranged into a
palindrome. The existing path order does not itself need to read the same in
both directions: only the multiset of values must admit at least one
palindromic permutation.

Return the number of root-to-leaf paths satisfying that condition. Count paths,
not distinct value sequences, so two different leaves contribute separately
even when their paths contain the same values.

### Function Contract
**Inputs**

- `root`: the root of a binary tree containing $n$ nodes, where
  $1 \le n \le 10^5$ and every `Node.val` lies in $[1,9]$.

Let $h$ denote the tree height, measured as the maximum number of nodes on a
root-to-leaf path.

**Return value**

Return the integer number of root-to-leaf paths whose node values can be
permuted to form a palindrome.

### Examples
**Example 1**

- Input: `root = [2,3,1,3,1,null,1]`
- Output: `2`
- Explanation: Paths `[2,3,3]` and `[2,1,1]` can be rearranged as palindromes,
  while `[2,3,1]` cannot.

**Example 2**

- Input: `root = [2,1,1,1,3,null,null,null,null,null,1]`
- Output: `1`

**Example 3**

- Input: `root = [9]`
- Output: `1`
- Explanation: Every one-value sequence is already a palindrome.
