# Reverse Odd Levels of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2415 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/) |

## Problem Description

### Goal

Given the root of a perfect binary tree, reverse the node values at every odd-numbered level. Level 0 contains the root, level 1 contains its two children, and in general a node's level is the number of edges on the path from the root. Reversing a level changes only the left-to-right order of its values.

The tree structure must remain unchanged: do not move nodes or alter parent-child links. A perfect binary tree guarantees that every internal node has two children and every leaf has the same depth, so nodes on opposite sides always have symmetric partners. Return the original root after all odd levels have been updated.

### Function Contract

**Inputs**

- `root`: The root of a perfect binary tree.

Let $n$ be the number of nodes and $h$ the tree height. The contract guarantees $1 \le n \le 2^{14}$, $0 \le \texttt{Node.val} \le 10^5$, and $h = O(\log n)$.

**Return value**

Return the same tree root with the values on levels 1, 3, 5, and so on reversed from left to right.

### Examples

**Example 1**

- Input: `root = [2,3,5,8,13,21,34]`
- Output: `[2,5,3,8,13,21,34]`

**Example 2**

- Input: `root = [7,13,11]`
- Output: `[7,11,13]`

**Example 3**

- Input: `root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]`
- Output: `[0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]`
