# Maximum Size Subarray Sum Equals k

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 325 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) |

## Problem Description
### Goal
Given an integer array that may contain positive values, negative values, and zeroes, choose a nonempty contiguous subarray whose elements sum exactly to `k`. The interval must use consecutive positions and cannot wrap around or skip elements.

Return the maximum length among all qualifying intervals, or `0` when none exists. Negative numbers mean extending a subarray can either increase or decrease its sum, so ordinary positive-only window assumptions do not apply. Several intervals may share the maximum length; only that length is returned, not the endpoints or subarray values.

### Function Contract
**Inputs**

- `nums`: the integer array
- `k`: the required subarray sum

**Return value**

The greatest length among contiguous subarrays summing to `k`, or zero if none exists.

### Examples
**Example 1**

- Input: `nums = [1,-1,5,-2,3], k = 3`
- Output: `4`

**Example 2**

- Input: `nums = [-2,-1,2,1], k = 1`
- Output: `2`

**Example 3**

- Input: `nums = [1,2,3], k = 7`
- Output: `0`
