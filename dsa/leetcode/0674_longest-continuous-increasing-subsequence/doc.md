# Longest Continuous Increasing Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 674 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) |

## Problem Description
### Goal
Given an unsorted integer array `nums`, find its longest continuous increasing subsequence, meaning a subarray whose elements occupy adjacent indices. Within that subarray, every value must be strictly greater than the value immediately before it.

Return the length of the longest such continuous subsequence. A longer increasing subsequence formed by skipping intervening elements does not qualify, and equal neighboring values break the current run because the comparison is strict. Every single element is itself a valid run of length `1`.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integers

**Return value**

- The length of the longest contiguous strictly increasing segment

### Examples
**Example 1**

- Input: `nums = [1,3,5,4,7]`
- Output: `3`

**Example 2**

- Input: `nums = [2,2,2,2,2]`
- Output: `1`

**Example 3**

- Input: `nums = [1,3,5,7]`
- Output: `4`
