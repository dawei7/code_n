# Longest Univalue Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 687 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-univalue-path/) |

## Problem Description
### Goal
Given the root of a binary tree, find the longest path in which every node has the same value. A path follows parent-child edges and may start and end at any nodes; it may pass through their common ancestor and does not need to include the tree's root.

Return the path's length measured as the number of edges between its endpoints, not the number of nodes. The two sides of a path may extend through different children of one node only when all connected values remain equal. An empty tree has length `0`.

### Function Contract
**Inputs**

- `root`: the root of a binary tree, or `null`

**Return value**

- The maximum edge count of a same-valued path

### Examples
**Example 1**

- Input: `root = [5,4,5,1,1,null,5]`
- Output: `2`

**Example 2**

- Input: `root = [1,4,5,4,4,null,5]`
- Output: `2`

**Example 3**

- Input: `root = [1]`
- Output: `0`
