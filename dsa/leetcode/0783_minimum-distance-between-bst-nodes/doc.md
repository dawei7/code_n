# Minimum Distance Between BST Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 783 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-distance-between-bst-nodes/) |

## Problem Description

### Goal

Given the root of a binary search tree containing at least two nodes with distinct integer values, consider every pair of different nodes.

Return the minimum absolute difference between their values. Distance here is numerical value difference, not the number of tree edges between nodes. The binary-search-tree ordering determines how values are arranged, but the answer may come from nodes at any depths or branches.

### Function Contract

**Inputs**

- `root`: the root node of a binary search tree with at least two nodes and no duplicate values.

**Return value**

- The minimum absolute difference between any pair of node values.

### Examples

**Example 1**

- Input: `root = [4,2,6,1,3]`
- Output: `1`
- Explanation: Consecutive values such as `1` and `2` differ by one.

**Example 2**

- Input: `root = [1,0,48,null,null,12,49]`
- Output: `1`
- Explanation: The values `0` and `1`, as well as `48` and `49`, attain the minimum.

**Example 3**

- Input: `root = [10,5,15]`
- Output: `5`
- Explanation: Both adjacent values in sorted order differ by five.
