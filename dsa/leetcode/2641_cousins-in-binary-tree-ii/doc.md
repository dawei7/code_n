# Cousins in Binary Tree II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2641 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/cousins-in-binary-tree-ii/) |

## Problem Description

### Goal

You are given the root of a binary tree. Replace every node's value with the sum of the original values of all its cousins. Two nodes are cousins when they occur at the same depth but have different parents; siblings therefore never contribute to one another's replacement value.

The root has depth zero, and a node's depth is the number of edges on the path from the root to that node. Modify the existing tree in place and return its root. A node with no cousins receives zero, which necessarily applies to the root and to every node directly below it.

### Function Contract

**Inputs**

- `root`: The root of a nonempty binary tree containing $n$ nodes, where $1 \le n \le 10^5$ and every original node value is between $1$ and $10^4$, inclusive.

**Return value**

- Return the same root after replacing each node value with the sum of the original values of nodes at the same depth whose parent is different.

### Examples

**Example 1**

- Input: `root = [5, 4, 9, 1, 10, null, 7]`
- Output: `[0, 0, 0, 7, 7, null, 11]`
- Explanation: At depth two, nodes `1` and `10` share a parent and therefore receive the other parent's child value `7`; node `7` receives `1 + 10`.

**Example 2**

- Input: `root = [3, 1, 2]`
- Output: `[0, 0, 0]`
- Explanation: No node has a cousin because the only nodes at depth one are siblings.
