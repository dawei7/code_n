# Count Subarrays With More Ones Than Zeros

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2031 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/) |

## Problem Description

### Goal

Given a binary array `nums`, count its subarrays that contain strictly more
ones than zeros. A subarray must be contiguous; equal numbers of the two values
do not qualify. Each distinct pair of start and end indices is counted
separately, even when another range contains the same value sequence. Elements
inside a chosen range cannot be skipped or reordered.

Return the count modulo $10^9 + 7$ because the total number of qualifying
subarrays can be large.

### Function Contract

Let $N$ be the length of `nums`.

**Inputs**

- `nums`: a list of $N$ values, each either `0` or `1`, where
  $1 \le N \le 10^5$.

**Return value**

- The number of contiguous subarrays having more ones than zeros, reduced
  modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `nums = [0, 1, 1, 0, 1]`
- Output: `9`

**Example 2**

- Input: `nums = [0]`
- Output: `0`

**Example 3**

- Input: `nums = [1]`
- Output: `1`
