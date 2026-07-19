# Substrings That Begin and End With the Same Letter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2083 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, String, Counting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/) |

## Problem Description

### Goal

Given a zero-indexed string containing only lowercase English letters, count its nonempty contiguous substrings whose first and last characters are equal.

Substrings are identified by their start and end indices, so equal text occurring at different positions counts separately. Every one-character substring qualifies because its only character is both endpoints. Interior positions remain contiguous and cannot be skipped. Return the total over all valid index intervals.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$, where $1 \le n \le 10^5$.

**Return value**

- Return the number of pairs of indices $(i,j)$ satisfying $0 \le i \le j < n$ and `s[i] == s[j]`.

### Examples

**Example 1**

- Input: `s = "abcba"`
- Output: `7`
- Explanation: The five single characters qualify, as do `"bcb"` and `"abcba"`.

**Example 2**

- Input: `s = "abacad"`
- Output: `9`
- Explanation: Six one-character substrings and the three substrings between pairs of `a` positions qualify.

**Example 3**

- Input: `s = "a"`
- Output: `1`
- Explanation: The sole nonempty substring starts and ends with `a`.
