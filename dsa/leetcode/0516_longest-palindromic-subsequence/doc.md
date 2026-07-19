# Longest Palindromic Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 516 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-palindromic-subsequence/) |

## Problem Description
### Goal
Given a nonempty lowercase string `s`, form a subsequence by deleting zero or more characters without changing the relative order of the characters retained. A palindromic subsequence reads identically from left to right and from right to left.

Return the maximum possible length of such a subsequence. Selected characters do not need to be contiguous, repeated occurrences at different positions remain separate choices, and the function returns only the optimal length rather than the subsequence itself. A one-character selection is always palindromic, while matching outer characters can surround a smaller palindromic subsequence.

### Function Contract
**Inputs**

- `s`: a nonempty lowercase English string

**Return value**

- The length of the longest palindromic subsequence of `s`

### Examples
**Example 1**

- Input: `s = "bbbab"`
- Output: `4`

**Example 2**

- Input: `s = "cbbd"`
- Output: `2`

**Example 3**

- Input: `s = "a"`
- Output: `1`
