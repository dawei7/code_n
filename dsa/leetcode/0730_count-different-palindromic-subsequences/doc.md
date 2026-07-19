# Count Different Palindromic Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 730 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/count-different-palindromic-subsequences/) |

## Problem Description
### Goal
Given a string `s` containing only `a`, `b`, `c`, and `d`, consider every nonempty subsequence formed by deleting zero or more characters without changing the order of those that remain. A subsequence is palindromic when it equals its reverse.

Return the number of different palindromic subsequence strings, modulo `1,000,000,007`. Identical text produced from different index choices counts only once, whereas two sequences that differ at any character position are distinct.

### Function Contract
**Inputs**

- `s`: a nonempty string whose characters are limited to `a`, `b`, `c`, and `d`

**Return value**

- The number of different nonempty palindromic subsequence strings, modulo `1,000,000,007`

### Examples
**Example 1**

- Input: `s = "bccb"`
- Output: `6`

**Example 2**

- Input: `s = "abcd"`
- Output: `4`

**Example 3**

- Input: `s = "aaa"`
- Output: `3`
