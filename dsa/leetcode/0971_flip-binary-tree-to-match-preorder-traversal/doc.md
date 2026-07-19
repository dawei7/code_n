# Flip Binary Tree To Match Preorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 971 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [flip-binary-tree-to-match-preorder-traversal](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/) |

## Problem Description

### Goal

You are given a binary tree whose $N$ node values are unique and a length-$N$ sequence `voyage`. The desired sequence is a preorder traversal: visit a node first, then its left subtree, then its right subtree.

You may flip any node by swapping its entire left and right subtrees. Use the fewest node flips needed to make the resulting preorder traversal equal `voyage`, and return the values of the flipped nodes in any order. If no sequence of flips can produce the voyage, return `[-1]`.

### Function Contract

**Inputs**

- `root`: the root of a binary tree containing $N$ uniquely valued nodes.
- `voyage`: a permutation of the $N$ node values describing the required preorder traversal.
- The size satisfies $1 \le N \le 100$, and every value is between $1$ and $N$.
- Serialized trees use level order and `null` for a missing child.

**Return value**

Return the values of a minimum-cardinality set of nodes to flip, in any order, or `[-1]` when the voyage is impossible.

### Examples

**Example 1**

- Input: `root = [1,2], voyage = [2,1]`
- Output: `[-1]`

**Example 2**

- Input: `root = [1,2,3], voyage = [1,3,2]`
- Output: `[1]`

**Example 3**

- Input: `root = [1,2,3], voyage = [1,2,3]`
- Output: `[]`
