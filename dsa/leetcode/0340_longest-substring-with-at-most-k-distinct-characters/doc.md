# Longest Substring with At Most K Distinct Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 340 |
| Difficulty | Medium |
| Topics | Hash Table, String, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) |

## Problem Description
### Goal
Given a string `s` and a nonnegative integer `k`, consider every contiguous substring and the set of character values appearing within it. A substring is valid when that set contains no more than `k` distinct characters, regardless of how often each character repeats.

Return the maximum length among valid substrings. The interval cannot skip positions or join separate portions of the string. When $k = 0$ or the string is empty, return `0`; when the entire string uses at most `k` character types, return its full length. The function returns only the length, not the substring or its character set.

### Function Contract
**Inputs**

- `s`: the string to examine
- `k`: the maximum number of distinct characters allowed in a candidate substring

**Return value**

- The length of the longest contiguous substring satisfying the distinct-character limit.

### Examples
**Example 1**

- Input: `s = "eceba", k = 2`
- Output: `3`
- Explanation: `"ece"` contains only `e` and `c`.

**Example 2**

- Input: `s = "aa", k = 1`
- Output: `2`

**Example 3**

- Input: `s = "a", k = 0`
- Output: `0`
