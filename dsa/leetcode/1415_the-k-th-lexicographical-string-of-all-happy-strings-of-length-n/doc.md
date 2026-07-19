# The k-th Lexicographical String of All Happy Strings of Length n

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1415 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/) |

## Problem Description

### Goal

A happy string contains only the characters `a`, `b`, and `c`, and no two adjacent characters are equal. Consider every happy string whose length is exactly `n`, sorted in lexicographical order.

Return the `k`-th string in that one-indexed ordering. If fewer than `k` happy strings of length `n` exist, return the empty string. The result must be selected from the ordering itself rather than from strings of shorter lengths.

### Function Contract

**Inputs**

- `n`: the required string length, where $1 \le n \le 10$.
- `k`: the one-indexed requested rank, where $1 \le k \le 100$.

**Return value**

- The `k`-th lexicographically smallest happy string of length `n`, or `""` when that rank does not exist.

### Examples

**Example 1**

- Input: `n = 1, k = 3`
- Output: `"c"`

**Example 2**

- Input: `n = 1, k = 4`
- Output: `""`

**Example 3**

- Input: `n = 3, k = 9`
- Output: `"cab"`
