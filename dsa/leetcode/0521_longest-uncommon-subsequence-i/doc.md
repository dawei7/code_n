# Longest Uncommon Subsequence I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 521 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-uncommon-subsequence-i/) |

## Problem Description
### Goal
A subsequence is formed by deleting zero or more characters without changing the relative order of those retained. Given strings `a` and `b`, an uncommon subsequence is a string that is a subsequence of exactly one input: it belongs to one string but not the other.

Return the maximum possible length of an uncommon subsequence, or `-1` when none exists. The candidate may equal one complete input string, and it need not be contiguous inside its source. If the two inputs are identical, every subsequence of one also belongs to the other; otherwise their unequal complete texts determine the longest possible length.

### Function Contract
**Inputs**

- `a`, `b`: two lowercase English strings

**Return value**

- The longest uncommon-subsequence length, or `-1` when every subsequence is shared

### Examples
**Example 1**

- Input: `a = "aba", b = "cdc"`
- Output: `3`

**Example 2**

- Input: `a = "aaa", b = "bbb"`
- Output: `3`

**Example 3**

- Input: `a = "aaa", b = "aaa"`
- Output: `-1`
