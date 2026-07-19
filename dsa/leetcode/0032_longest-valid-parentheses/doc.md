# Longest Valid Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 32 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-valid-parentheses/) |

## Problem Description
### Goal
You are given a string `s` containing only opening and closing parentheses. Among all contiguous substrings, find the greatest length of one that forms a well-balanced sequence.

A valid sequence never closes more pairs than it has opened in any prefix, and it finishes with equal opening and closing counts. Characters outside the chosen interval do not affect its validity, but characters inside cannot be skipped. Return the maximum length, using zero when the string contains no nonempty valid interval.

### Function Contract
**Inputs**

- `s`: `str` containing only `(` and `)`

**Return value**

An `int` equal to the maximum valid substring length.

### Examples
**Example 1**

- Input: `s = "(()"`
- Output: `2`

**Example 2**

- Input: `s = ")()())"`
- Output: `4`

**Example 3**

- Input: `s = ""`
- Output: `0`
