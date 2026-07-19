# Reverse String II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 541 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-string-ii/) |

## Problem Description
### Goal
Given a string `s` and positive integer `k`, process consecutive blocks of `2k` characters from left to right. In every full block, reverse the first `k` characters and leave the following `k` characters in their existing order.

For the final partial block, reverse all remaining characters when fewer than `k` remain. When at least `k` but fewer than `2k` remain, reverse only its first `k` and leave the rest unchanged. Return the resulting string with every original character present exactly once; block boundaries are based on original positions, not on character values.

### Function Contract
**Inputs**

- `s`: a lowercase string
- `k`: a positive reversal length

**Return value**

- The transformed string after applying the rule independently to each `2k` block

### Examples
**Example 1**

- Input: `s = "abcdefg", k = 2`
- Output: `"bacdfeg"`

**Example 2**

- Input: `s = "abcd", k = 2`
- Output: `"bacd"`

**Example 3**

- Input: `s = "abcdef", k = 2`
- Output: `"bacdfe"`
