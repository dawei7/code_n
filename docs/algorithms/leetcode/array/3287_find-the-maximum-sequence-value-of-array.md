# Find the Maximum Sequence Value of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3287 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Bit Manipulation |
| Official Link | [find-the-maximum-sequence-value-of-array](https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` and an integer `k`, identify two disjoint subsequences of length `k`. The objective is to maximize the bitwise XOR result of the bitwise OR of the first subsequence and the bitwise OR of the second subsequence.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums.length <= 400 and 1 <= nums[i] <= 127.
- `k`: An integer representing the required length of each subsequence.

**Return value**

- An integer representing the maximum possible value of `(OR(subsequence1) ^ OR(subsequence2))`.

### Examples
**Example 1**

- Input: `nums = [1,2,1,3], k = 2`
- Output: `3`

**Example 2**

- Input: `nums = [5,7,8,9], k = 2`
- Output: `14`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming with bitsets (or boolean arrays). Since the maximum value of elements is 127 (which is less than 2^7), the bitwise OR of any subsequence will always be in the range [0, 127]. We precompute all possible OR values for subsequences of length `k` starting from the left and ending at the right. Finally, we iterate through all possible split points to find the maximum XOR of the OR values from the left and right segments.

## Complexity Analysis
- **Time Complexity**: O(n * k * 128), where n is the length of the array. We compute DP states for each index up to k, and each state involves 128 possible OR values.
- **Space Complexity**: O(n * k * 128) to store the DP tables for all possible subsequence lengths up to k.
