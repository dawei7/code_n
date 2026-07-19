# Longest Repeating Character Replacement

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 424 |
| Difficulty | Medium |
| Topics | Hash Table, String, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/) |

## Problem Description
### Goal
Given a string of uppercase English letters and a nonnegative integer `k`, choose a contiguous substring. You may replace at most `k` character occurrences inside that substring with any uppercase letters.

Return the maximum possible substring length that can be transformed into repetitions of one identical character. Positions outside the chosen interval are irrelevant and need not be changed. The retained majority character may be any letter, and using fewer than `k` replacements is allowed. The substring cannot skip positions, while the entire string qualifies when all nonmatching occurrences can be replaced within the budget.

### Function Contract
**Inputs**

- `s`: a string of uppercase English letters
- `k`: the maximum number of characters that may be replaced

**Return value**

- Return the maximum length of a contiguous substring transformable into one repeated character using at most `k` replacements.

### Examples
**Example 1**

- Input: `s = "ABAB", k = 2`
- Output: `4`

**Example 2**

- Input: `s = "AABABBA", k = 1`
- Output: `4`

**Example 3**

- Input: `s = "AAAA", k = 0`
- Output: `4`
