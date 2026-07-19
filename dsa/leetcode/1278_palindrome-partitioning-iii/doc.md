# Palindrome Partitioning III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1278 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-partitioning-iii/) |

## Problem Description

### Goal

Given a lowercase string `s`, change as few of its characters as possible and then divide the resulting string into exactly `k` non-empty, contiguous, disjoint substrings. Every substring in the partition must be a palindrome.

A character change replaces the letter at one position with another lowercase English letter. Partition boundaries do not reorder or discard characters. Return the minimum number of changed positions needed to make some valid partition of exactly `k` palindromic pieces.

### Function Contract

**Inputs**

- `s`: a string of $n$ lowercase English letters, where $1 \le n \le 100$.
- `k`: the exact number of non-empty substrings required, where $1 \le k \le n$.

**Return value**

- Return the minimum number of character replacements required across all `k` pieces.

### Examples

**Example 1**

- Input: `s = "abc", k = 2`
- Output: `1`

**Example 2**

- Input: `s = "aabbc", k = 3`
- Output: `0`

**Example 3**

- Input: `s = "leetcode", k = 8`
- Output: `0`
