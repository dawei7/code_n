# Kth Largest Sum in a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2583 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Breadth-First Search, Sorting, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Kth Largest Sum in a Binary Tree](https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/) |

## Problem Description

### Goal

Given the root of a binary tree and a positive integer `k`, group the nodes by their distance from the root. The level sum for one such group is the sum of every node value at that distance.

Order all level sums from largest to smallest while retaining repeated values as separate entries. Return the `k`th value in that ordering. If the tree contains fewer than `k` levels, return `-1`.

### Function Contract

**Inputs**

- `root`: The root of a binary tree containing `n` nodes.
- `k`: The one-based rank of the requested level sum.

The tree has $2 \leq n \leq 10^5$ nodes, every node value is between $1$ and $10^6$ inclusive, and $1 \leq k \leq n$.

**Return value**

- The `k`th largest level sum, including duplicate sums in the ranking, or `-1` when the tree has fewer than `k` levels.

### Examples

#### Example 1

- **Input:** `root = [5,8,9,2,1,3,7,4,6], k = 2`
- **Output:** `13`
- **Explanation:** The level sums are `5`, `17`, `13`, and `10`; the second largest is `13`.

#### Example 2

- **Input:** `root = [1,2,null,3], k = 1`
- **Output:** `3`
- **Explanation:** The three level sums are `1`, `2`, and `3`.
