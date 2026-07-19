# Longest Happy Prefix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1392 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Rolling Hash, String Matching, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/longest-happy-prefix/) |

## Problem Description

### Goal

A string prefix consists of one or more characters taken from its beginning, while a suffix consists of one or more characters taken from its end. A prefix is called happy when the same sequence is also a suffix, but it must be a proper prefix: it cannot equal the entire string.

Given a lowercase English string `s`, return its longest happy prefix. If no nonempty proper prefix also occurs as a suffix, return the empty string.

### Function Contract

**Inputs**

- `s`: a string of $n$ lowercase English letters, where $1 \le n \le 10^5$.

**Return value**

- The longest nonempty proper prefix of `s` that is also a suffix, or `""` when no such prefix exists.

### Examples

**Example 1**

- Input: `s = "level"`
- Output: `"l"`

**Example 2**

- Input: `s = "ababab"`
- Output: `"abab"`

**Example 3**

- Input: `s = "leetcodeleet"`
- Output: `"leet"`
