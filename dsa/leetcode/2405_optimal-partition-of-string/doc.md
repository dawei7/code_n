# Optimal Partition of String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2405 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/optimal-partition-of-string/) |

## Problem Description

### Goal

Partition a lowercase string `s` into one or more contiguous, nonempty
substrings. Every original character must belong to exactly one part, so the
parts appear in order and concatenate back to `s`.

Within each substring, every character must be unique: no letter may occur
twice in the same part. Return the minimum possible number of substrings in a
partition satisfying this rule.

### Function Contract

**Inputs**

- `s`: A lowercase English string with
  $1 \le n=\lvert\texttt{s}\rvert\le10^5$.

**Return value**

Return the smallest number of contiguous substrings whose concatenation is
`s` and in which each individual substring contains no repeated character.

### Examples

**Example 1**

- Input: `s = "abacaba"`
- Output: `4`
- Explanation: One optimal partition is `("ab", "a", "ca", "ba")`.

**Example 2**

- Input: `s = "ssssss"`
- Output: `6`
- Explanation: Every repeated `s` must begin a new substring.

**Example 3**

- Input: `s = "abcdefghijklmnopqrstuvwxyz"`
- Output: `1`
- Explanation: All 26 characters are distinct, so the whole string is valid.
