# Smallest Subsequence of Distinct Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1081 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/) |

## Problem Description

### Goal

Given a string `s`, choose a subsequence: retain some characters in their original relative order while deleting the others. The chosen result must contain every distinct character that occurs in `s` exactly once.

Among all subsequences satisfying that coverage and uniqueness requirement, return the lexicographically smallest one. The input contains only lowercase English letters, so comparisons use their ordinary alphabetic order.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$, where $1 \le n \le 1000$.

**Return value**

- The lexicographically smallest subsequence containing every distinct character of `s` exactly once.

### Examples

**Example 1**

- Input: `s = "bcabc"`
- Output: `"abc"`

**Example 2**

- Input: `s = "cbacdcbc"`
- Output: `"acdb"`
