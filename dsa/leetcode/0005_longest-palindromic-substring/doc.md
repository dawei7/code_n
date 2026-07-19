# Longest Palindromic Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 5 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/) |

## Problem Description
### Goal
Given a nonempty string `s`, find a contiguous portion that is a palindrome: its character sequence is unchanged when read from right to left instead of left to right. The chosen characters must occupy one uninterrupted interval of the original string.

Return a palindromic substring whose length is as large as possible. More than one interval may attain that maximum, and returning any one of them is valid. A single character is always a palindrome, so every allowed input has at least one answer.

### Function Contract
**Inputs**

- `s`: `str` with at least one character

**Return value**

A `str` containing a longest palindromic substring of `s`.

### Examples
**Example 1**

- Input: `s = "babad"`
- Output: `"bab"`

**Example 2**

- Input: `s = "cbbd"`
- Output: `"bb"`

**Example 3**

- Input: `s = "a"`
- Output: `"a"`
