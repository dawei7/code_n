# Distinct Subsequences II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 940 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [distinct-subsequences-ii](https://leetcode.com/problems/distinct-subsequences-ii/) |

## Problem Description

### Goal

Given a string `s`, count its distinct non-empty subsequences. A subsequence is formed by deleting zero or more characters without changing the relative order of the characters that remain. Different choices of deleted positions can produce the same string, and such equal results must be counted only once.

Because the number of distinct subsequences can be very large, return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `s`: a string of $N$ lowercase English letters, where $1 \le N \le 2000$.

**Return value**

Return the number of distinct non-empty subsequences of `s`, modulo $10^9+7$.

### Examples

**Example 1**

- Input: `s = "abc"`
- Output: `7`
- Explanation: The distinct results are `"a"`, `"b"`, `"c"`, `"ab"`, `"ac"`, `"bc"`, and `"abc"`.

**Example 2**

- Input: `s = "aba"`
- Output: `6`
- Explanation: The distinct results are `"a"`, `"b"`, `"ab"`, `"aa"`, `"ba"`, and `"aba"`.

**Example 3**

- Input: `s = "aaa"`
- Output: `3`
- Explanation: Only `"a"`, `"aa"`, and `"aaa"` are distinct.
