# Maximum Average Subarray I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 643 |
| Difficulty | Easy |
| Topics | Array, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/) |

## Problem Description
### Goal
Given an integer array `nums` with `n` elements and an integer `k`, consider every contiguous subarray whose length is equal to `k`. Compute each candidate's arithmetic average from the sum of exactly those `k` consecutive values.

Return the maximum average value among all candidates. The selected elements must form one contiguous range rather than an arbitrary subsequence, and the length cannot be shorter or longer than `k`. A floating-point answer with calculation error less than $10^{-5}$ is accepted.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integers
- `k`: the fixed subarray length, with `1 <= k <= len(nums)`

**Return value**

- The maximum average as a floating-point number

### Examples
**Example 1**

- Input: `nums = [1,12,-5,-6,50,3]`, `k = 4`
- Output: `12.75`

**Example 2**

- Input: `nums = [5]`, `k = 1`
- Output: `5.0`

**Example 3**

- Input: `nums = [-5,-2,-3,-4]`, `k = 2`
- Output: `-2.5`
