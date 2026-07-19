# Maximum Average Subarray II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 644 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-average-subarray-ii/) |

## Problem Description
### Goal
Given an integer array `nums` and an integer `k`, consider every contiguous subarray whose length is greater than or equal to `k`. For each candidate, divide its sum by its own length to obtain its arithmetic average.

Return the maximum average value over all valid subarrays, within the accepted numerical tolerance. The optimal range may contain exactly `k` elements or may be longer, so only checking fixed-length windows is insufficient; however, the elements must always remain contiguous and in their original order.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integers
- `k`: the minimum allowed subarray length, with `1 <= k <= len(nums)`

**Return value**

- The maximum attainable average as a floating-point value within the accepted numerical tolerance

### Examples
**Example 1**

- Input: `nums = [1,12,-5,-6,50,3]`, `k = 4`
- Output: approximately `12.75`

**Example 2**

- Input: `nums = [5]`, `k = 1`
- Output: `5.0`

**Example 3**

- Input: `nums = [4,0,0,4]`, `k = 3`
- Output: `2.0`, using all four values
