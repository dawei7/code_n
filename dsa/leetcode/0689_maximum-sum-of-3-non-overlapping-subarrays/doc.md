# Maximum Sum of 3 Non-Overlapping Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 689 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Sliding Window, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) |

## Problem Description
### Goal
Given an integer array `nums` and an integer `k`, choose three non-overlapping contiguous subarrays, each having length exactly `k`, so that the sum of all values in the three intervals is as large as possible.

Return the zero-based starting index of each interval in increasing order. If multiple triples have the same maximum sum, return the lexicographically smallest index list. The intervals may touch at endpoints but may not share an array position, and their internal order remains the array's order.

### Function Contract
**Inputs**

- `nums`: a positive integer array with room for at least three length-`k` windows
- `k`: the common positive subarray length

**Return value**

- Three increasing start indices for the maximum-total non-overlapping windows, with lexicographically smallest tie-breaking

### Examples
**Example 1**

- Input: `nums = [1,2,1,2,6,7,5,1], k = 2`
- Output: `[0,3,5]`

**Example 2**

- Input: `nums = [1,2,1,2,1,2,1,2,1], k = 2`
- Output: `[0,2,4]`

**Example 3**

- Input: `nums = [1,2,3,4,5,6], k = 2`
- Output: `[0,2,4]`
