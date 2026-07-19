# Unique Binary Search Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 96 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Tree, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-binary-search-trees/) |

## Problem Description
### Goal
Given `n` distinct ordered keys numbered `1` through `n`, consider all binary search trees that use every key exactly once. Each node must have only smaller keys in its left subtree and only larger keys in its right subtree.

Return the number of structurally unique trees, not the trees themselves. Two trees count separately when any parent-child relationship differs. The actual consecutive key values establish ordering but do not otherwise change the count; for one key, exactly one tree exists.

### Function Contract
**Inputs**

- `n`: the number of distinct consecutive keys

**Return value**

The number of distinct binary search tree structures using keys `1..n`.

### Examples
**Example 1**

- Input: `n = 3`
- Output: `5`

**Example 2**

- Input: `n = 1`
- Output: `1`

**Example 3**

- Input: `n = 4`
- Output: `14`
