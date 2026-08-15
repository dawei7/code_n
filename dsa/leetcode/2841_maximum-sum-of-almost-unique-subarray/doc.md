# Maximum Sum of Almost Unique Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2841 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/) |

## Problem Description

### Goal

You are given an integer array `nums` and two positive integers `m` and `k`. Consider each subarray whose length is exactly $k$. A subarray is a contiguous, non-empty sequence of elements from the array.

A candidate is almost unique when it contains at least $m$ distinct values; repeated values are allowed as long as that threshold is met. Return the maximum sum among all almost-unique length-$k$ subarrays. If no candidate has enough distinct values, return `0`.

### Function Contract

**Inputs**

- `nums`: A list of positive integers.
- `m`: The minimum number of distinct values required in a candidate.
- `k`: The exact length of every candidate subarray.

The constraints are $1\le\lvert\texttt{nums}\rvert\le2\cdot10^4$, $1\le m\le k\le\lvert\texttt{nums}\rvert$, and $1\le\texttt{nums[i]}\le10^9$.

**Return value**

- The greatest sum of an almost-unique length-$k$ subarray, or `0` if none exists.

### Examples

#### Example 1

- **Input:** `nums = [2, 6, 7, 3, 1, 7], m = 3, k = 4`
- **Output:** `18`
- **Explanation:** All three length-four windows meet the distinct-value threshold. The first and last each sum to `18`, which is maximal.

#### Example 2

- **Input:** `nums = [5, 9, 9, 2, 4, 5, 4], m = 1, k = 3`
- **Output:** `23`
- **Explanation:** Requiring only one distinct value makes every length-three window valid; `[5, 9, 9]` has the greatest sum.

#### Example 3

- **Input:** `nums = [1, 2, 1, 2, 1, 2, 1], m = 3, k = 3`
- **Output:** `0`
- **Explanation:** Every length-three window contains only the values `1` and `2`, so none reaches three distinct values.
