# Number of Subsequences with Odd Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3247 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-subsequences-with-odd-sum/) |

## Problem Description

### Goal

Given an integer array `nums`, count the subsequences whose selected elements have an odd sum. A subsequence is determined by choosing any set of indices while preserving their original relative order; equal values at different indices represent different choices.

The empty subsequence has sum zero and therefore is not counted. Return the number of odd-sum subsequences modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: An array of length $n$, where $1 \le n \le 10^5$ and every value lies from 1 through $10^9$.

**Return value**

- The number of index-defined subsequences with odd element sum, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums = [1,1,1]`
- Output: `4`

**Example 2**

- Input: `nums = [1,2,2]`
- Output: `4`

**Example 3**

- Input: `nums = [2,4,6]`
- Output: `0`
