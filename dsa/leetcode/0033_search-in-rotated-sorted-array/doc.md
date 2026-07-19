# Search in Rotated Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 33 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/) |

## Problem Description
### Goal
You are given an integer array `nums` sorted in ascending order with distinct values. Before being provided, it may have been rotated at an unknown pivot, moving one leading segment behind the other while preserving the sorted order within both segments.

Find `target` and return its current zero-based index, or return `-1` when it is absent. The array may be unrotated, rotated at any valid boundary, or contain one element. The required logarithmic running time rules out a simple full scan.

### Function Contract
**Inputs**

- `nums`: `List[int]` containing distinct values in rotated increasing order
- `target`: `int`

**Return value**

The target's zero-based index, or `-1` when absent.

### Examples
**Example 1**

- Input: `nums = [4, 5, 6, 7, 0, 1, 2], target = 0`
- Output: `4`

**Example 2**

- Input: `nums = [4, 5, 6, 7, 0, 1, 2], target = 3`
- Output: `-1`

**Example 3**

- Input: `nums = [1], target = 0`
- Output: `-1`
