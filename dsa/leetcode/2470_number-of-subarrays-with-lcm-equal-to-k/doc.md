# Number of Subarrays With LCM Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2470 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/) |

## Problem Description

### Goal

Given a positive-integer array `nums` and a positive integer `k`, count the subarrays whose elements have least common multiple exactly equal to `k`.

A subarray is a contiguous, non-empty sequence from the original array. The least common multiple of its elements is the smallest positive integer divisible by every element in that subarray. Return the total number of qualifying subarrays.

### Function Contract

**Inputs**

- `nums`: The positive integers from which contiguous subarrays are selected.
- `k`: The required least common multiple.

Let $n=\lvert\texttt{nums}\rvert$ and let $D$ be the number of positive divisors of `k`. The constraints are $1\le n\le1000$ and $1\le\texttt{nums[i]},\texttt{k}\le1000$.

**Return value**

- The number of non-empty contiguous subarrays whose least common multiple is exactly `k`.

### Examples

**Example 1**

- Input: `nums = [3,6,2,7,1], k = 6`
- Output: `4`
- Explanation: The qualifying subarrays are `[3,6]`, `[3,6,2]`, `[6]`, and `[6,2]`.

**Example 2**

- Input: `nums = [3], k = 2`
- Output: `0`
- Explanation: The only subarray has least common multiple $3$, not $2$.
