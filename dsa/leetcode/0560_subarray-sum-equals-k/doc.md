# Subarray Sum Equals K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 560 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/) |

## Problem Description
### Goal
Given a nonempty integer array `nums` and integer `k`, consider every nonempty contiguous subarray. A subarray is determined by a start and end index and includes every array element between them.

Return the total number of subarrays whose element sum equals exactly `k`. Different index intervals count separately even when their values are identical, and negative values or zero prevent positive-only sliding-window assumptions. The interval cannot wrap around or skip positions, and the function returns only the count rather than the matching ranges.

### Function Contract
**Inputs**

- `nums`: a non-empty list of integers
- `k`: the target sum

**Return value**

- The number of contiguous subarrays with sum `k`

### Examples
**Example 1**

- Input: `nums = [1, 1, 1], k = 2`
- Output: `2`

**Example 2**

- Input: `nums = [1, 2, 3], k = 3`
- Output: `2`

**Example 3**

- Input: `nums = [1, -1, 0], k = 0`
- Output: `3`
