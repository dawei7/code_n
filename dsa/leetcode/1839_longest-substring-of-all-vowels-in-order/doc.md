# Longest Substring Of All Vowels in Order

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/) |
| Frontend ID | 1839 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A string is beautiful when it contains each of the five vowels `a`, `e`, `i`, `o`, and `u` at least once, and its characters are in alphabetical order. Thus all `a` characters precede all `e` characters, which precede all `i`, `o`, and `u` characters in that order.

Given `word`, a string containing only those five lowercase vowels, return the length of its longest contiguous beautiful substring. Repeated copies within a vowel group are allowed. If no substring contains all five groups in the required order, return 0.

### Function Contract

**Inputs**

- `word`: a string of $n$ characters drawn only from `a`, `e`, `i`, `o`, and `u`, where $1 \le n \le 5\cdot10^5$.

**Return value**

- Return the greatest length of a contiguous substring whose characters are non-decreasing and include all five vowels.
- Return 0 when no such substring exists.

### Examples

**Example 1**

- Input: `word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"`
- Output: `13`

The longest beautiful substring is `"aaaaeiiiiouuu"`.

**Example 2**

- Input: `word = "aeeeiiiioooauuuaeiou"`
- Output: `5`

The descending transition from `o` to `a` resets the first run; the final `"aeiou"` is beautiful.

**Example 3**

- Input: `word = "a"`
- Output: `0`

Four required vowel groups are absent.
