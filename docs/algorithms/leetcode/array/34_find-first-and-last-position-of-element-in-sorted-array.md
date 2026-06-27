# Find First and Last Position of Element in Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 34 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [find-first-and-last-position-of-element-in-sorted-array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |

## Problem Description & Examples
### Goal
Given a sorted array of integers and a target value, identify the starting and ending indices of the target's occurrences. If the target is not present in the array, return `[-1, -1]`. The solution must execute in logarithmic time complexity.

### Function Contract
**Inputs**

- `nums`: A list of integers sorted in non-decreasing order.
- `target`: An integer representing the value to search for.

**Return value**

- A list of two integers `[start, end]` representing the first and last indices of the target.

### Examples
**Example 1**

- Input: `nums = [5,7,7,8,8,10], target = 8`
- Output: `[3,4]`

**Example 2**

- Input: `nums = [5,7,7,8,8,10], target = 6`
- Output: `[-1,-1]`

**Example 3**

- Input: `nums = [], target = 0`
- Output: `[-1,-1]`

---

## Underlying Base Algorithm(s)
Binary Search. Specifically, two modified binary search passes are used: one to find the leftmost insertion point (or occurrence) and one to find the rightmost insertion point (or occurrence).

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`, where `n` is the number of elements in the array, as we perform two binary searches.
- **Space Complexity**: `O(1)`, as we only use a constant amount of extra space for pointers.
