# Minimum Window Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 727 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-window-subsequence/) |

## Problem Description
### Goal
Given strings `s1` and `s2`, find a contiguous substring of `s1` within which every character of `s2` appears in order as a subsequence. The matched characters need not occupy adjacent positions inside the window, but their relative order must be preserved.

Return the shortest qualifying substring. If several windows have the same minimum length, return the one with the leftmost starting position. If `s2` cannot be obtained as a subsequence of any substring of `s1`, return the empty string.

### Function Contract
**Inputs**

- `s1`: the source string from which one contiguous window may be selected
- `s2`: the nonempty target string whose characters must appear in order within that window

**Return value**

- The minimum qualifying substring of `s1`, or the empty string when `s2` is not a subsequence of any window

### Examples
**Example 1**

- Input: `s1 = "abcdebdde", s2 = "bde"`
- Output: `"bcde"`

**Example 2**

- Input: `s1 = "abc", s2 = "abc"`
- Output: `"abc"`

**Example 3**

- Input: `s1 = "abc", s2 = "d"`
- Output: `""`
