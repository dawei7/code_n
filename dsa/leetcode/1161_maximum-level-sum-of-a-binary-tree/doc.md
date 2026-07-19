# Maximum Level Sum of a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1161 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) |

## Problem Description

### Goal

You are given the root of a nonempty binary tree. The root is at level $1$, its children are at level $2$, and each subsequent child level increases the level number by one.

For every level, sum the values of all nodes on that level. Return the smallest level number $x$ whose sum is maximal among all tree levels. Node values may be negative, so the winning sum is not necessarily positive and the comparison must include every level.

### Function Contract

**Inputs**

- `root`: The root of a binary tree containing $n$ nodes, where $1 \le n \le 10^4$ and every node value lies between $-10^5$ and $10^5$.
- Let $w$ be the maximum number of nodes present on any one level of the tree.

**Return value**

- The smallest 1-indexed level whose node-value sum equals the maximum level sum.

### Examples

**Example 1**

- Input: `root = [1,7,0,7,-8,null,null]`
- Output: `2`

The first three level sums are $1$, $7$, and $-1$.

**Example 2**

- Input: `root = [989,null,10250,98693,-89388,null,null,null,-32127]`
- Output: `2`

**Example 3**

- Input: `root = [1]`
- Output: `1`
