# Maximum Length of Repeated Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 718 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Dynamic Programming, Sliding Window, Rolling Hash, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) |

## Problem Description
### Goal
Given two integer arrays `nums1` and `nums2`, find a subarray that appears in both arrays. A subarray is a contiguous sequence, so its values must occur in the same order at consecutive positions in each input.

Return the maximum length of any repeated subarray. The matching occurrences may begin at different indices in the two arrays, and equal values outside the selected ranges do not matter. If the arrays share no value, return `0`; noncontiguous common subsequences do not qualify.

### Function Contract
**Inputs**

- `nums1`: the first nonempty integer array
- `nums2`: the second nonempty integer array

**Return value**

- The length of their longest common contiguous subarray, or `0` when they share no value

### Examples
**Example 1**

- Input: `nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]`
- Output: `3`

**Example 2**

- Input: `nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]`
- Output: `5`

**Example 3**

- Input: `nums1 = [1,2,3], nums2 = [4,5,6]`
- Output: `0`
