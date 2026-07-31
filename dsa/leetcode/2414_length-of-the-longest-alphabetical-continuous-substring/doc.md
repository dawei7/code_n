# Length of the Longest Alphabetical Continuous Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2414 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/) |

## Problem Description

### Goal

An alphabetical continuous string consists of consecutive letters in ascending alphabet order. Equivalently, it is a substring of `"abcdefghijklmnopqrstuvwxyz"`: `"abc"` qualifies, while `"acb"` does not because it skips and reverses letters, and `"za"` does not because the alphabet does not wrap.

Given a non-empty lowercase English string `s`, examine its contiguous substrings and return the greatest length among those that are alphabetical continuous. Repeated letters, gaps, descending steps, and the transition from `z` to `a` all end the current qualifying substring.

### Function Contract

**Inputs**

- `s`: A string containing only lowercase English letters.

Let $n = \lvert s\rvert$, where $1 \le n \le 10^5$.

**Return value**

Return the length of the longest contiguous substring whose adjacent letters each advance by exactly one alphabet position.

### Examples

**Example 1**

- Input: `s = "abacaba"`
- Output: `2`

**Example 2**

- Input: `s = "abcde"`
- Output: `5`

**Example 3**

- Input: `s = "za"`
- Output: `1`
