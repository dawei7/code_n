# Maximum Sum BST in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1373 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/) |

## Problem Description

### Goal

Given a binary tree, consider every subtree consisting of a node and all of its descendants. A subtree is a binary search tree when every value in its left subtree is strictly smaller than the root value, every value in its right subtree is strictly greater, and both child subtrees satisfy the same rule.

Find the greatest sum of node values among all subtrees that are binary search trees. If every nonempty BST subtree has a negative sum, return zero, corresponding to selecting no positive-sum subtree.

### Function Contract

**Inputs**

- `root`: the root of a nonempty binary tree containing $N$ nodes.

**Return value**

- The maximum node-value sum of any BST subtree, or `0` when no BST subtree has a positive sum.

### Examples

**Example 1**

- Input: `root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]`
- Output: `20`

**Example 2**

- Input: `root = [4,3,null,1,2]`
- Output: `2`

**Example 3**

- Input: `root = [-4,-2,-5]`
- Output: `0`
