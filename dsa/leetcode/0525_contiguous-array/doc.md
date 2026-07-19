# Contiguous Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 525 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/contiguous-array/) |

## Problem Description
### Goal
Given a binary array `nums`, choose a contiguous subarray and count its `0` and `1` values. A qualifying interval contains exactly the same number of zeroes as ones, so its length is necessarily even.

Return the maximum length of a qualifying contiguous subarray. The interval cannot skip positions or combine separated pieces, and equal total counts elsewhere in the array do not help a selected interval. If no nonempty balanced interval exists, return `0`; the function returns only the length, not the endpoints or balanced values.

### Function Contract
**Inputs**

- `nums`: a binary integer array

**Return value**

- The greatest length of a contiguous interval with equal zero and one counts, or `0` when none exists

### Examples
**Example 1**

- Input: `nums = [0, 1]`
- Output: `2`

**Example 2**

- Input: `nums = [0, 1, 0]`
- Output: `2`

**Example 3**

- Input: `nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]`
- Output: `6`
