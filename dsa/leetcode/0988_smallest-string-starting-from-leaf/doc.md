# Smallest String Starting From Leaf

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 988 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/smallest-string-starting-from-leaf/) |

## Problem Description

### Goal

You are given the root of a binary tree whose node values range from $0$ through $25$. Interpret value $0$ as `"a"`, value $1$ as `"b"`, and so on through value $25$ as `"z"`.

Every leaf defines a string by starting with that leaf's letter and following its unique path upward to the root, appending each encountered letter. Return the lexicographically smallest of these leaf-to-root strings. Standard prefix ordering applies: when one string is a prefix of another, the shorter string is lexicographically smaller. A leaf is a node with no left or right child.

### Function Contract

**Inputs**

- `root`: the root of a non-empty binary tree with $N$ nodes, where $1\le N\le8500$ and $0\le\texttt{node.val}\le25$.

Let $H$ be the tree height.

**Return value**

- The lexicographically smallest string spelled from any leaf upward to the root.

### Examples

**Example 1**

- Input: `root = [0, 1, 2, 3, 4, 3, 4]`
- Output: `"dba"`

**Example 2**

- Input: `root = [25, 1, 3, 1, 3, 0, 2]`
- Output: `"adz"`

**Example 3**

- Input: `root = [2, 2, 1, null, 1, 0, null, 0]`
- Output: `"abc"`
