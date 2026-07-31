# Maximum and Minimum Sums of at Most Size K Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3430 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/) |

## Problem Description

### Goal

Given an integer array `nums` and a positive integer `k`, consider every non-empty contiguous subarray containing at most `k` elements. Different start and end indices identify different subarrays, even when their values happen to be equal.

For each eligible subarray, take its minimum element and its maximum element and add both to a running total. Return the final sum across all such subarrays. Values may be negative, so the result is not necessarily positive.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1\le n\le 80000$ and $-10^6\le\texttt{nums[i]}\le10^6$.
- `k`: The maximum permitted subarray length, where $1\le k\le n$.

**Return value**

Return the sum of the minimum and maximum elements over every subarray of length at most `k`.

### Examples

**Example 1**

- Input: `nums = [1,2,3], k = 2`
- Output: `20`

**Example 2**

- Input: `nums = [1,-3,1], k = 2`
- Output: `-6`
