# Search in a Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 700 |
| Difficulty | Easy |
| Topics | Tree, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/search-in-a-binary-search-tree/) |

## Problem Description
### Goal
Given the root of a binary search tree and an integer `val`, find the tree node whose value equals `val`.

If the node exists, return that same node as the root of its complete existing subtree, including all of its descendants. If no node has the requested value, return `null`. The binary-search-tree ordering may guide the search, but the returned structure must not be rebuilt, trimmed, or reduced to only the matching value.

### Function Contract
**Inputs**

- `root`: the root of a binary search tree, represented in cases by level-order values
- `val`: the value to locate

**Return value**

- The matching tree node with all of its original descendants, or `null` when no node has value `val`

### Examples
**Example 1**

- Input: `root = [4,2,7,1,3], val = 2`
- Output: `[2,1,3]`

**Example 2**

- Input: `root = [4,2,7,1,3], val = 5`
- Output: `[]`

**Example 3**

- Input: `root = [8,4,12,2,6,10,14], val = 10`
- Output: `[10]`
