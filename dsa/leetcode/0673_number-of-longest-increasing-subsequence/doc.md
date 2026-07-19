# Number of Longest Increasing Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 673 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Binary Indexed Tree, Segment Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) |

## Problem Description
### Goal
Given an integer array `nums`, consider all subsequences formed without changing the relative order of selected elements. Find the maximum possible length of a strictly increasing subsequence.

Return the number of longest increasing subsequences having that maximum length. Equal values cannot extend one another because the sequence must be strictly increasing, but subsequences choosing different index occurrences are counted separately even when their value sequences are identical. The required result is the count, not the length itself.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integers

**Return value**

- The number of longest strictly increasing subsequences in `nums`

### Examples
**Example 1**

- Input: `nums = [1,3,5,4,7]`
- Output: `2`

**Example 2**

- Input: `nums = [2,2,2,2,2]`
- Output: `5`

**Example 3**

- Input: `nums = [1,2,4,3,5,4,7,2]`
- Output: `3`
