# Continuous Subarray Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 523 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/continuous-subarray-sum/) |

## Problem Description
### Goal
Given a nonempty integer array `nums` and a positive integer `k`, choose a contiguous subarray containing at least two elements. Its sum qualifies when it equals $n \cdot k$ for some integer `n`, including $n = 0$.

Return `True` if any such subarray exists and `False` otherwise. The selected elements must occupy consecutive positions, cannot wrap, and cannot be replaced by an arbitrary subsequence. A zero sum is divisible by `k`, while a one-element match is excluded by the minimum-length rule. The function returns only feasibility, not the interval or multiplier.

### Function Contract
**Inputs**

- `nums`: an array of nonnegative integers
- `k`: a positive integer divisor

**Return value**

- `True` if some length-at-least-two contiguous subarray sums to a multiple of `k`; otherwise `False`

### Examples
**Example 1**

- Input: `nums = [23, 2, 4, 6, 7], k = 6`
- Output: `True`

**Example 2**

- Input: `nums = [23, 2, 6, 4, 7], k = 6`
- Output: `True`

**Example 3**

- Input: `nums = [23, 2, 6, 4, 7], k = 13`
- Output: `False`
