# Subarray Product Less Than K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 713 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Sliding Window, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/subarray-product-less-than-k/) |

## Problem Description
### Goal
Given an array `nums` of positive integers and an integer `k`, consider every nonempty contiguous subarray and multiply all values inside it.

Return the number of subarrays whose product is strictly less than `k`. Subarrays are counted by their index ranges, so equal value sequences at different positions contribute separately. A product equal to `k` does not qualify, and noncontiguous subsequences are not considered.

### Function Contract
**Inputs**

- `nums`: a nonempty list of positive integers
- `k`: the exclusive product limit

**Return value**

- The number of contiguous subarrays with product below `k`

### Examples
**Example 1**

- Input: `nums = [10,5,2,6], k = 100`
- Output: `8`

**Example 2**

- Input: `nums = [1,2,3], k = 0`
- Output: `0`

**Example 3**

- Input: `nums = [1,1,1], k = 2`
- Output: `6`
