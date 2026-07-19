# Palindromic Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 647 |
| Difficulty | Medium |
| Topics | Two Pointers, String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/palindromic-substrings/) |

## Problem Description
### Goal
Given a string `s`, return the number of palindromic substrings it contains. A palindrome reads the same backward as forward, and a substring is a contiguous sequence of characters within the original string.

Count occurrences by their index ranges, not only by distinct text. Therefore, equal one-character or multi-character strings appearing at different positions contribute separately, and every individual character is itself a palindrome. Noncontiguous subsequences do not count.

### Function Contract
**Inputs**

- `s`: a nonempty string

**Return value**

- The number of palindromic index ranges in `s`

### Examples
**Example 1**

- Input: `s = "abc"`
- Output: `3`

**Example 2**

- Input: `s = "aaa"`
- Output: `6`

**Example 3**

- Input: `s = "abba"`
- Output: `6`
