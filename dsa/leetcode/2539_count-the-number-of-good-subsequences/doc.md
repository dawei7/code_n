
# Count the Number of Good Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2539 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, String, Combinatorics, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [count-the-number-of-good-subsequences](https://leetcode.com/problems/count-the-number-of-good-subsequences/) |

## Problem Description

### Goal

A subsequence is formed from a string by deleting zero or more characters while preserving the relative order of those that remain. A nonempty subsequence is good when every distinct character present in it occurs the same number of times. Different choices of source-string positions count as different subsequences, even if they produce identical text.

Given a lowercase English string `s`, count all of its good subsequences. Because this count can be large, return it modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `s`: A nonempty string containing only lowercase English letters.

Let $n = \lvert s\rvert$. The public constraints permit $n \leq 10^4$.

**Return value**

Return the number of nonempty subsequences in which all included characters have one common positive frequency, modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `s = "aabb"`
- Output: `11`
- Explanation: Of the $2^4$ position subsets, four nonempty choices have unequal positive character frequencies and the empty choice is not allowed.

**Example 2**

- Input: `s = "leet"`
- Output: `12`

**Example 3**

- Input: `s = "abcd"`
- Output: `15`
- Explanation: Every nonempty subsequence contains each selected character exactly once.
