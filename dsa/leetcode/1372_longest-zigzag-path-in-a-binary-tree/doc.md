# Longest ZigZag Path in a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1372 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/) |

## Problem Description

### Goal

A ZigZag path in a binary tree may begin at any node. Choose an initial move to either the left or right child; after moving left, the next move must go right, and after moving right, the next move must go left. Continue downward while alternating directions.

The path length is its number of traversed edges, which is one less than its number of nodes. Return the maximum ZigZag length available anywhere in the tree. A path containing only one node has length zero.

### Function Contract

**Inputs**

- `root`: the root of a nonempty binary tree containing $N$ nodes and having height $H$.

**Return value**

- The greatest number of edges in any downward path whose directions strictly alternate left and right.

### Examples

**Example 1**

- Input: an alternating five-node chain.
- Output: `4`

**Example 2**

- Input: a three-node chain using two left edges.
- Output: `1`

**Example 3**

- Input: a one-node tree.
- Output: `0`
