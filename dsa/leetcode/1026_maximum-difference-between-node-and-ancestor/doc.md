# Maximum Difference Between Node and Ancestor

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1026 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/) |

## Problem Description

### Goal

Given the `root` of a binary tree, consider two different nodes `a` and `b` such that `a` is an ancestor of `b`. Their difference is $\lvert a.\text{val} - b.\text{val} \rvert$.

A node is an ancestor of each of its children and of every node that is an ancestor-descendant continuation through one of those children. Return the maximum difference over all valid ancestor-descendant pairs in the tree.

### Function Contract

**Inputs**

- `root`: the root of a binary tree with $N$ nodes, represented in cases by a level-order array using `null` for absent children.
- The tree satisfies $2 \le N \le 5000$, and every node value is between $0$ and $10^5$, inclusive.
- Let $H$ denote the tree height.

**Return value**

- The largest absolute value difference between two different nodes where one is an ancestor of the other.

### Examples

**Example 1**

- Input: `root = [8,3,10,1,6,null,14,null,null,4,7,13]`
- Output: `7`
- Explanation: Node `8` is an ancestor of node `1`, and their difference is $\lvert 8-1 \rvert=7$, the largest valid value.

**Example 2**

- Input: `root = [1,null,2,null,0,3]`
- Output: `3`
- Explanation: The root `1` is an ancestor of node `3`, giving $\lvert 1-3 \rvert=2$, while node `0` is a descendant of `1` and an ancestor of `3`; the pair `0` and `3` gives the maximum $3$.
