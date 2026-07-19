# Binary Search Tree to Greater Sum Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1038 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/) |

## Problem Description

### Goal

Given the `root` of a binary search tree, convert it to a Greater Tree. Replace every original key with that key plus the sum of all original keys that are greater than it, then return the root.

The input obeys the BST rules: every key in a node's left subtree is strictly less than the node's key, every key in its right subtree is strictly greater, and both subtrees obey the same property. All keys are unique.

### Function Contract

**Inputs**

- `root`: the root of a BST with $N$ nodes, represented in cases by a level-order array using `null` for missing children; let $H$ be the tree height.
- $1 \le N \le 100$, and every unique node value lies between $0$ and $100$.

**Return value**

- The root of the same tree after updating node values in place to their greater-sum values.

### Examples

**Example 1**

- Input: `root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]`
- Output: `[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]`

**Example 2**

- Input: `root = [0,null,1]`
- Output: `[1,null,1]`
