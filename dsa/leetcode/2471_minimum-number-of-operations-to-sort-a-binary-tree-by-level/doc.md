# Minimum Number of Operations to Sort a Binary Tree by Level

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2471 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/) |

## Problem Description

### Goal

You are given the root of a binary tree whose node values are all unique. A node's level is the number of edges on the path from the root to that node.

In one operation, choose any two nodes at the same level and swap their values. Return the minimum number of operations required so that, at every level, the values read from left to right are in strictly increasing order.

### Function Contract

**Inputs**

- `root`: The root of the binary tree with unique node values.

Let $n$ be the number of nodes and $W$ the maximum number of nodes on any one level. The constraints are $1\le n\le10^5$ and $1\le\texttt{Node.val}\le10^5$.

**Return value**

- The minimum total number of same-level value swaps needed to sort every level in strictly increasing order.

### Examples

#### Example 1

- **Input:** `root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]`
- **Output:** `3`
- **Explanation:** One swap orders level $1$, and two swaps order the values `[7,6,8,5]` at level $2$.

#### Example 2

- **Input:** `root = [1,3,2,7,6,5,4]`
- **Output:** `3`
- **Explanation:** Sorting `[3,2]` costs one swap and sorting `[7,6,5,4]` costs two more.

#### Example 3

- **Input:** `root = [1,2,3,4,5,6]`
- **Output:** `0`
- **Explanation:** Every level is already strictly increasing from left to right.
