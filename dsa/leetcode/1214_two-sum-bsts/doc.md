# Two Sum BSTs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1214 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, Binary Search, Stack, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/two-sum-bsts/) |

## Problem Description

### Goal

You are given the roots `root1` and `root2` of two binary search trees, together with an integer `target`. A valid choice must take one node from the first tree and one node from the second tree; two nodes from the same tree do not form a candidate.

Return `true` if and only if some cross-tree pair has values whose sum equals `target`. Return `false` when no such pair exists. Node values and the target may be negative, zero, or positive.

### Function Contract

**Inputs**

- `root1`: The root of the first nonempty binary search tree, which contains $n$ nodes.
- `root2`: The root of the second nonempty binary search tree, which contains $m$ nodes.
- `target`: The required sum.

The bounds are $1\le n,m\le5000$. Every node value and `target` lies between $-10^9$ and $10^9$, inclusive.

**Return value**

- `true` when one node from each tree sums to `target`; otherwise `false`.

### Examples

**Example 1**

- Input: `root1 = [2,1,4]`, `root2 = [1,0,3]`, `target = 5`
- Output: `true`

The first tree's `2` and the second tree's `3` form a valid pair.

**Example 2**

- Input: `root1 = [0,-10,10]`, `root2 = [5,1,7,0,2]`, `target = 18`
- Output: `false`

**Example 3**

- Input: `root1 = [8,3,10]`, `root2 = [6,1,9]`, `target = 12`
- Output: `true`
