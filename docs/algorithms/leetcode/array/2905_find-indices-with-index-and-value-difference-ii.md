# Find Indices With Index and Value Difference II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2905 |
| Difficulty | Medium |
| Topics | Array, Two Pointers |
| Official Link | [find-indices-with-index-and-value-difference-ii](https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` and two integers `indexDifference` and `valueDifference`, determine if there exists a pair of indices `(i, j)` such that the absolute difference between the indices is at least `indexDifference` and the absolute difference between the values at those indices is at least `valueDifference`. If such a pair exists, return the indices; otherwise, return `[-1, -1]`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `indexDifference`: An integer representing the minimum required distance between indices.
- `valueDifference`: An integer representing the minimum required absolute difference between values.

**Return value**

- A list of two integers `[i, j]` satisfying the conditions, or `[-1, -1]` if no such pair exists.

### Examples
**Example 1**

- Input: `nums = [5, 1, 4, 1], indexDifference = 2, valueDifference = 4`
- Output: `[0, 3]`

**Example 2**

- Input: `nums = [2, 1], indexDifference = 0, valueDifference = 0`
- Output: `[0, 0]`

**Example 3**

- Input: `nums = [1, 2, 3], indexDifference = 2, valueDifference = 4`
- Output: `[-1, -1]`

---

## Underlying Base Algorithm(s)
The problem can be solved using a **Min-Max Tracking** approach. As we iterate through the array with index `j`, we maintain the indices of the minimum and maximum values encountered so far in the range `[0, j - indexDifference]`. By comparing the current value `nums[j]` against the historical minimum and maximum, we can determine in constant time if a valid pair exists.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass through the array.
- **Space Complexity**: `O(1)`, as we only store a few variables to track the indices of the minimum and maximum values.
