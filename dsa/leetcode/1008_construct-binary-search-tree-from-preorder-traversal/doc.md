# Construct Binary Search Tree from Preorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1008 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Tree, Binary Search Tree, Monotonic Stack, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/) |

## Problem Description

### Goal

You are given an integer array `preorder` representing the preorder traversal of a binary search tree. In preorder traversal, a node is visited before its left subtree and then its right subtree.

Construct and return the tree's root. In the required binary search tree, every descendant in `Node.left` has a value strictly less than `Node.val`, and every descendant in `Node.right` has a value strictly greater than `Node.val`. All traversal values are unique, and a tree satisfying the traversal is guaranteed to exist.

### Function Contract

**Inputs**

- `preorder`: an array of $N$ unique integers, where $1\le N\le100$ and $1\le\texttt{preorder[i]}\le1000$.

Let $H$ denote the height of the constructed tree, with a single-node tree having height $1$.

**Return value**

- The root `TreeNode` of the binary search tree whose preorder traversal is `preorder`.

### Examples

**Example 1**

- Input: `preorder = [8, 5, 1, 7, 10, 12]`
- Output: `[8, 5, 10, 1, 7, null, 12]`
- Explanation: The output uses level-order tree serialization; its preorder traversal is the given array.

**Example 2**

- Input: `preorder = [1, 3]`
- Output: `[1, null, 3]`
- Explanation: Since `3` is strictly greater than `1`, it is the root's right child.

**Example 3**

- Input: `preorder = [4, 2]`
- Output: `[4, 2]`
- Explanation: Since `2` is strictly less than `4`, it is the root's left child.
