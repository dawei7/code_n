# Repeated Substring Pattern

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 459 |
| Difficulty | Easy |
| Topics | String, String Matching |
| Official Link | [LeetCode](https://leetcode.com/problems/repeated-substring-pattern/) |

## Problem Description
### Goal
Given a nonempty string `s`, determine whether it can be constructed by repeating one of its proper nonempty prefixes. Every repetition must use the identical substring, concatenated without gaps, overlaps, or leftover characters.

Return `True` when some shorter unit repeated an integer number of times at least two equals the complete string, and `False` otherwise. The unit length must divide `len(s)` exactly. Repeated characters alone are insufficient if no common block tiles the entire string, while a one-character string cannot use a shorter nonempty unit.

### Function Contract
**Inputs**

- `s`: a nonempty string

**Return value**

- `True` when some proper prefix repeated an integer number of times equals `s`; otherwise `False`

### Examples
**Example 1**

- Input: `s = "abab"`
- Output: `True`

**Example 2**

- Input: `s = "aba"`
- Output: `False`

**Example 3**

- Input: `s = "abcabcabcabc"`
- Output: `True`
