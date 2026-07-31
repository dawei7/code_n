# Minimum Positive Sum Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3364 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-positive-sum-subarray/) |

## Problem Description

### Goal

Given an integer array `nums` and two inclusive length bounds `l` and `r`, consider every non-empty contiguous subarray whose length is at least `l` and at most `r`. A candidate qualifies only when the sum of all its elements is strictly greater than zero.

Return the smallest qualifying sum. Sums equal to zero and all negative sums must be ignored even if their subarrays have valid lengths. If no allowed subarray has a positive sum, return `-1`.

### Function Contract

**Inputs**

- `nums`: The integer array whose contiguous subarrays are considered.
- `l`: The minimum allowed subarray length.
- `r`: The maximum allowed subarray length.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are $1\le n\le100$, $1\le l\le r\le n$, and $-1000\le\texttt{nums[i]}\le1000$.

**Return value**

- The minimum strictly positive sum of an allowed subarray, or `-1` when none exists.

### Examples

**Example 1**

- Input: `nums = [3, -2, 1, 4]`, `l = 2`, `r = 3`
- Output: `1`
- Explanation: The allowed positive sums are 1, 5, 2, and 3, so the minimum is 1.

**Example 2**

- Input: `nums = [-2, 2, -3, 1]`, `l = 2`, `r = 3`
- Output: `-1`
- Explanation: Every allowed subarray has sum zero or less.

**Example 3**

- Input: `nums = [1, 2, 3, 4]`, `l = 2`, `r = 4`
- Output: `3`
- Explanation: The length-two subarray `[1, 2]` has the smallest positive sum.
