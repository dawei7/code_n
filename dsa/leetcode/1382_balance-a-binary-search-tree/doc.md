# Balance a Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1382 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Divide and Conquer, Greedy, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/balance-a-binary-search-tree/) |

## Problem Description

### Goal

Given the root of a binary search tree, construct and return a balanced binary search tree containing exactly the same node values. A binary tree is balanced when, at every node, the heights of its left and right subtrees differ by no more than one.

The input can be highly skewed, and more than one balanced shape may satisfy the requirement. The returned tree must preserve the binary-search-tree ordering while redistributing the values into any valid balanced structure.

### Function Contract

**Inputs**

- `root`: the root node of a binary search tree containing $N$ distinct values, where $1 \le N \le 10^4$.

**Return value**

- The root node of any height-balanced binary search tree containing exactly the input values.

### Examples

**Example 1**

- Input: `root = [1,null,2,null,3,null,4]`
- Output: `[2,1,3,null,null,null,4]`

**Example 2**

- Input: `root = [2,1,3]`
- Output: `[2,1,3]`

**Example 3**

- Input: `root = [1]`
- Output: `[1]`
