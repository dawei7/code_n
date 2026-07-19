# Non-decreasing Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 491 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Backtracking, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/non-decreasing-subsequences/) |

## Problem Description
### Goal
Given an integer array `nums`, form subsequences by selecting indices in their original left-to-right order without requiring the positions to be contiguous. A subsequence is non-decreasing when every selected value is greater than or equal to the preceding selected value.

Return all the different possible non-decreasing subsequences containing at least two elements, in any order. Equal values from different indices may appear together, but different index selections that produce the same value sequence must not duplicate the answer. Values may be negative, and a decrease between selected values invalidates that candidate.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array

**Return value**

- All distinct non-decreasing subsequences of length at least two

### Examples
**Example 1**

- Input: `nums = [4, 6, 7, 7]`
- Output: `[[4,6],[4,7],[4,6,7],[4,6,7,7],[4,7,7],[6,7],[6,7,7],[7,7]]`

**Example 2**

- Input: `nums = [4, 4, 3, 2, 1]`
- Output: `[[4,4]]`

**Example 3**

- Input: `nums = [3, 2, 1]`
- Output: `[]`
