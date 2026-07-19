# Longest Substring Without Repeating Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |

## Problem Description
### Goal
Given a string `s`, examine its contiguous substrings and find the greatest length for which no character occurs more than once. A candidate may begin and end anywhere in the string, but it must retain every character between those endpoints.

Return only that maximum length, not the substring itself. Characters cannot be skipped or rearranged, so a subsequence is not a valid candidate. When the input repeats one character throughout, the best nonempty window has length one; an empty input has answer zero.

### Function Contract
**Inputs**

- `s`: the input string

**Return value**

The maximum length of a substring without a repeated character.

### Examples
**Example 1**

- Input: `s = "abcabcbb"`
- Output: `3`

**Example 2**

- Input: `s = "bbbbb"`
- Output: `1`

**Example 3**

- Input: `s = "pwwkew"`
- Output: `3`
