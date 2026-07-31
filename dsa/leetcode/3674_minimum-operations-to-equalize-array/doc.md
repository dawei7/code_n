# Minimum Operations to Equalize Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3674 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-equalize-array/) |

## Problem Description
### Goal

Given an integer array `nums`, an operation may select any non-empty contiguous subarray `nums[l...r]`. Compute the bitwise AND of every value in that selected range, then replace every selected element with that one result.

Determine the minimum number of such operations needed to make every array element equal. The selected subarray may be the entire array, and an array whose elements are already identical needs no operation.

### Function Contract

**Inputs**

- `nums`: a non-empty list of $n$ positive integers, where $1\le n\le100$ and every value is at most $10^5$.

**Return value**

Return the minimum operation count required to make all entries of `nums` equal.

### Examples

**Example 1**

- Input: `nums = [1, 2]`
- Output: `1`

Selecting the full array replaces both entries by `1 & 2 = 0`.

**Example 2**

- Input: `nums = [5, 5, 5]`
- Output: `0`

No operation is required because the array is already constant.

**Example 3**

- Input: `nums = [7, 3, 7]`
- Output: `1`

The original values differ, but one operation on the full array replaces all of them by their common bitwise AND.
