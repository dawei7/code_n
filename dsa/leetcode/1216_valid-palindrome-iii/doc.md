# Valid Palindrome III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1216 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-palindrome-iii/) |

## Problem Description

### Goal

A string is a **`k`-palindrome** when it can be transformed into a palindrome by removing at most `k` characters. The remaining characters keep their original relative order; removals may be made at any positions and do not need to be contiguous.

Given a string `s` and an integer `k`, return `true` if `s` is a `k`-palindrome. Otherwise, return `false`.

### Function Contract

**Inputs**

- `s`: A string of $n$ lowercase English letters, where $1\le n\le1000$.
- `k`: The maximum permitted number of removed characters, where $1\le k\le n$.

**Return value**

- `true` if removing at most `k` characters from `s` can leave a palindrome; otherwise `false`.

### Examples

**Example 1**

- Input: `s = "abcdeca"`, `k = 2`
- Output: `true`

Removing `b` and `e` leaves `acdca`, which is a palindrome.

**Example 2**

- Input: `s = "abbababa"`, `k = 1`
- Output: `true`

Removing the second character leaves `abababa`.

**Example 3**

- Input: `s = "abc"`, `k = 1`
- Output: `false`

At least two removals are needed to leave a palindrome.
