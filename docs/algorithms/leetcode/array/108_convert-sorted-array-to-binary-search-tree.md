# Convert Sorted Array to Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 108 |
| Difficulty | Easy |
| Topics | Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree |
| Official Link | [convert-sorted-array-to-binary-search-tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) |

## Problem Description & Examples
### Goal
Given a strictly increasing integer array, build a height-balanced binary search tree containing exactly those values.

### Function Contract
**Inputs**

- `nums`: a sorted array of unique integers.

**Return value**

The root node of a height-balanced binary search tree. Multiple valid trees may exist.

### Examples
**Example 1**

- Input: `nums = [-10,-3,0,5,9]`
- Output: a valid tree such as `[0,-10,5,null,-3,null,9]`

**Example 2**

- Input: `nums = [1,3]`
- Output: `[1,null,3]` or `[3,1]`

**Example 3**

- Input: `nums = []`
- Output: `[]`

---

## Underlying Base Algorithm(s)
Divide and conquer, balanced binary search tree construction.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(log n)` recursion stack for a balanced tree, excluding output nodes.
