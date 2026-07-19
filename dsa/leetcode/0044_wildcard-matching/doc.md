# Wildcard Matching

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 44 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Greedy, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/wildcard-matching/) |

## Problem Description
### Goal
You are given a text string `s` and a wildcard pattern `p`. Ordinary pattern characters match themselves, `?` matches exactly one arbitrary character, and `*` matches any consecutive sequence of characters, including an empty sequence.

Determine whether the pattern matches the complete text from beginning to end rather than merely a prefix or substring. Each asterisk may consume a different number of characters, and consecutive asterisks have the same expressive effect as one. Return a boolean indicating whether some valid assignment of wildcard lengths covers all of `s`.

### Function Contract
**Inputs**

- `s`: `str`
- `p`: `str` containing ordinary characters, `?`, and `*`

**Return value**

`True` when the complete pattern matches the complete string; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "aa", p = "a"`
- Output: `False`

**Example 2**

- Input: `s = "aa", p = "*"`
- Output: `True`

**Example 3**

- Input: `s = "cb", p = "?a"`
- Output: `False`
