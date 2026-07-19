# Arithmetic Slices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 413 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/arithmetic-slices/) |

## Problem Description
### Goal
Given an integer array, an arithmetic slice is a contiguous subarray of at least three elements in which every adjacent pair has the same difference. The common difference may be positive, negative, or zero.

Return the total number of arithmetic slices. Different start or end positions count as different subarrays, so a long arithmetic run contains several shorter qualifying slices within it. Noncontiguous subsequences do not count, and arrays with fewer than three elements return `0`. The function returns only the count rather than the ranges or their common differences.

### Function Contract
**Inputs**

- `nums`: the integer array

**Return value**

- Return the number of contiguous arithmetic subarrays with at least three elements.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `3`

**Example 2**

- Input: `nums = [1]`
- Output: `0`

**Example 3**

- Input: `nums = [1,3,5,7,9]`
- Output: `6`
