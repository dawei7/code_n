# Find First and Last Position of Element in Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 34 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |

## Problem Description
### Goal
Given an integer array `nums` sorted in non-decreasing order, locate the complete contiguous range occupied by `target`. Duplicate target values, when present, necessarily form one block because the input is sorted.

Return the inclusive indices of the block's first and last elements as `[start, end]`. If the target does not occur, return `[-1, -1]`; an empty array has the same result. The search must take logarithmic time even when the matching block itself is large, so it cannot scan outward through every duplicate.

### Function Contract
**Inputs**

- `nums`: nondecreasing `List[int]`
- `target`: `int`

**Return value**

A two-element `List[int]` containing the inclusive target range or `[-1, -1]`.

### Examples
**Example 1**

- Input: `nums = [5, 7, 7, 8, 8, 10], target = 8`
- Output: `[3, 4]`

**Example 2**

- Input: `nums = [5, 7, 7, 8, 8, 10], target = 6`
- Output: `[-1, -1]`

**Example 3**

- Input: `nums = [], target = 0`
- Output: `[-1, -1]`
