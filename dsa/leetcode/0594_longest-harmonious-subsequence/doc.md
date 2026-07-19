# Longest Harmonious Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 594 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sliding Window, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-harmonious-subsequence/) |

## Problem Description
### Goal
A harmonious array is one whose maximum value and minimum value differ by exactly `1`. Given an integer array `nums`, consider all subsequences obtainable by deleting zero or more elements while preserving the relative order of those that remain.

Return the length of the longest harmonious subsequence. A valid result must contain values at both ends of the one-value difference; a subsequence containing only repeated copies of one number has difference `0` and is not harmonious. If no pair of values differing by exactly `1` occurs, return `0`.

### Function Contract
**Inputs**

- `nums: list[int]`: the source values

**Return value**

- The length of the longest subsequence containing exactly two values that differ by one
- Return `0` when no such pair of values occurs

### Examples
**Example 1**

- Input: `nums = [1,3,2,2,5,2,3,7]`
- Output: `5`

**Example 2**

- Input: `nums = [1,2,3,4]`
- Output: `2`

**Example 3**

- Input: `nums = [1,1,1,1]`
- Output: `0`
