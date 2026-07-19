# Path In Zigzag Labelled Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1104 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/) |

## Problem Description

### Goal

Consider an infinite binary tree in which every node has two children. Nodes are labelled one row at a time. Odd-numbered rows—the first, third, fifth, and so on—are labelled from left to right, while even-numbered rows are labelled from right to left.

Given one node's `label`, return the sequence of labels on the unique path from the root to that node, including both endpoints.

### Function Contract

**Inputs**

- `label`: the target label $L$, where $1 \leq L \leq 10^6$.

The zero-based depth of the target is $d = \lfloor \log_2 L \rfloor$.

**Return value**

A list of $d+1$ labels ordered from the root to the node labelled $L$.

### Examples

**Example 1**

- Input: `label = 14`
- Output: `[1, 3, 4, 14]`

**Example 2**

- Input: `label = 26`
- Output: `[1, 2, 6, 10, 26]`
