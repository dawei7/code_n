# Binary Subarrays With Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 930 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sliding Window, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-subarrays-with-sum/) |

## Problem Description

### Goal

Given a binary array `nums` and an integer `goal`, count the non-empty subarrays whose elements sum to exactly `goal`.

A subarray is a contiguous part of the original array. Two subarrays with the same sequence of values still count separately when they occupy different index ranges.

Equivalently, count every index pair $(\ell,r)$ with $0 \le \ell \le r < n$ for which the sum of `nums[ell:r + 1]` is `goal`. The selected range must contain at least one element. In particular, when `goal` is zero, every contiguous range consisting only of zeros contributes to the answer.

### Function Contract

**Inputs**

- `nums`: a binary array of length $n$, where $1 \le n \le 3 \cdot 10^4$ and every element is either `0` or `1`.
- `goal`: the required subarray sum, where $0 \le \texttt{goal} \le n$.

**Return value**

Return the number of non-empty contiguous subarrays of `nums` whose sum is exactly `goal`.

### Examples

**Example 1**

- Input: `nums = [1,0,1,0,1], goal = 2`
- Output: `4`

**Example 2**

- Input: `nums = [0,0,0,0,0], goal = 0`
- Output: `15`
