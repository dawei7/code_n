# Smallest K-Length Subsequence With Occurrences of a Letter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2030 |
| Difficulty | Hard |
| Topics | String, Stack, Greedy, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/) |

## Problem Description

### Goal

Given a lowercase string `s`, select a subsequence of exactly `k` characters.
The distinguished character `letter` must occur in the selected subsequence at
least `repetition` times. The input guarantees that `s` contains enough copies
of `letter` for this requirement to be possible.

Among all qualifying length-`k` subsequences, return the lexicographically
smallest one. Deleting characters must preserve the relative order of every
character that remains.

### Function Contract

Let $N$ be the length of `s`.

**Inputs**

- `s`: a string of $N$ lowercase English letters, where
  $1 \le N \le 5 \cdot 10^4$.
- `k`: the required subsequence length, where $1 \le k \le N$.
- `letter`: one lowercase English character.
- `repetition`: the minimum number of selected occurrences of `letter`, where
  $1 \le \text{repetition} \le k$ and `s` contains at least that many copies.

**Return value**

- The lexicographically smallest length-`k` subsequence containing `letter` at
  least `repetition` times.

### Examples

**Example 1**

- Input: `s = "leet", k = 3, letter = "e", repetition = 1`
- Output: `"eet"`

**Example 2**

- Input: `s = "leetcode", k = 4, letter = "e", repetition = 2`
- Output: `"ecde"`

**Example 3**

- Input: `s = "bb", k = 2, letter = "b", repetition = 2`
- Output: `"bb"`
