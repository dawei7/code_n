# Longest Subsequence Repeated k Times

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2014 |
| Difficulty | Hard |
| Topics | Hash Table, Two Pointers, String, Backtracking, Counting, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-subsequence-repeated-k-times/) |

## Problem Description

### Goal

A subsequence is obtained from a string by deleting zero or more characters
without changing the order of those retained. A candidate `seq` is repeated
`k` times in `s` when concatenating `k` copies of `seq` produces another
subsequence of `s`.

Find the longest candidate satisfying that repetition condition. When several
candidates share the maximum length, return the lexicographically largest one.
Return the empty string if no nonempty candidate can be repeated `k` times.

### Function Contract

Let $N=\lvert s\rvert$, let $L$ be the maximum candidate length, and let $C$
be the number of candidate extensions tested by the search. The constraints
imply $L\le7$.

**Inputs**

- `s`: a lowercase English string of length $N$, where
  $2\le N<\min(2001,8k)$.
- `k`: the required repetition count, where $2\le k\le2000$.

**Return value**

Return the longest repeated subsequence, breaking equal-length ties by
lexicographically larger value.

### Examples

**Example 1**

- Input: `s = "letsleetcode", k = 2`
- Output: `"let"`
- Explanation: Both `"let"` and `"ete"` have maximum length three, and
  `"let"` is lexicographically larger.

**Example 2**

- Input: `s = "bb", k = 2`
- Output: `"b"`
- Explanation: Two copies of `"b"` form the complete string.

**Example 3**

- Input: `s = "ab", k = 2`
- Output: `""`
- Explanation: Neither character occurs often enough to appear in two copies.
