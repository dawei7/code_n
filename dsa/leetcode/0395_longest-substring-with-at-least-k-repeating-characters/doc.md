# Longest Substring with At Least K Repeating Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 395 |
| Difficulty | Medium |
| Topics | Hash Table, String, Divide and Conquer, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/) |

## Problem Description
### Goal
Given a lowercase string `s` and an integer `k`, choose a contiguous substring. It is valid when every distinct character that appears inside that substring occurs there at least `k` times; frequencies elsewhere in the full string do not help.

Return the maximum length of any valid substring, or `0` when no nonempty interval qualifies. The substring cannot skip positions, and including a rare character can invalidate an otherwise long region. When $k = 1$, the complete string is valid. The function returns only the length, not the substring or its frequency table.

### Function Contract
**Inputs**

- `s`: a string of lowercase English letters
- `k`: the minimum frequency required for every character used by the substring

**Return value**

- Return the greatest valid substring length, or `0` when no nonempty substring satisfies the frequency requirement.

### Examples
**Example 1**

- Input: `s = "aaabb", k = 3`
- Output: `3`

**Example 2**

- Input: `s = "ababbc", k = 2`
- Output: `5`

**Example 3**

- Input: `s = "abc", k = 4`
- Output: `0`
