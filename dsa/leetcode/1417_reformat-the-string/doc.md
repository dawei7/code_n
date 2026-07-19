# Reformat The String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1417 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/reformat-the-string/) |

## Problem Description

### Goal

The string `s` contains only lowercase English letters and decimal digits. Rearrange all of its characters so that every adjacent pair contains one letter and one digit; equivalently, character types must alternate throughout the result.

Return any rearrangement satisfying that rule while preserving every original character occurrence. If no such arrangement exists, return the empty string. Characters of the same type may appear in any relative order, so more than one returned string can be correct.

### Function Contract

**Inputs**

- `s`: a string of length $n$, where $1 \le n \le 500$, containing only lowercase English letters and digits.

**Return value**

- Any permutation of `s` whose adjacent characters alternate between letter and digit, or `""` if no such permutation exists.

### Examples

**Example 1**

- Input: `s = "a0b1c2"`
- Output: `"0a1b2c"`

**Example 2**

- Input: `s = "leetcode"`
- Output: `""`

**Example 3**

- Input: `s = "covid2019"`
- Output: `"c2o0v1i9d"`
