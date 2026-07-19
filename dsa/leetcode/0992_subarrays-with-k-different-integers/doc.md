# Subarrays with K Different Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 992 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/subarrays-with-k-different-integers/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `k`, count the good subarrays of `nums`. An array is good when it contains exactly `k` different integers; for instance, `[1, 2, 3, 1, 2]` contains the three different integers $1$, $2$, and $3$.

A subarray is a contiguous part of the original array, so equal value sequences occurring at different start or end positions count separately. Return the total number of contiguous subarrays whose number of different integers is exactly `k`.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $1\le N\le2\cdot10^4$ and $1\le\texttt{nums[i]}\le N$.
- `k`: the required number of different integers, where $1\le\texttt{k}\le N$.

**Return value**

- The number of contiguous subarrays containing exactly `k` different integers.

### Examples

**Example 1**

- Input: `nums = [1, 2, 1, 2, 3], k = 2`
- Output: `7`
- Explanation: Four length-two-or-more ranges ending before the final $3$, two shorter alternating ranges, and `[2, 3]` give seven qualifying subarrays.

**Example 2**

- Input: `nums = [1, 2, 1, 3, 4], k = 3`
- Output: `3`
- Explanation: The qualifying ranges are `[1, 2, 1, 3]`, `[2, 1, 3]`, and `[1, 3, 4]`.

**Example 3**

- Input: `nums = [1, 1, 1], k = 1`
- Output: `6`
- Explanation: Every nonempty subarray contains exactly one different integer.
