# Minimum ASCII Delete Sum for Two Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 712 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) |

## Problem Description
### Goal
Given two strings `s1` and `s2`, delete characters from either string until their remaining character sequences are equal. Every deletion costs the ASCII value of the character removed.

Return the lowest possible total ASCII sum of all deleted characters. Remaining characters keep their relative order, and the two final strings may be empty when that is optimal. The objective minimizes deletion cost rather than merely the number of deletions, so removing fewer high-valued characters may cost more than removing several lower-valued ones.

### Function Contract
**Inputs**

- `s1`: the first lowercase English string
- `s2`: the second lowercase English string

**Return value**

- The minimum possible total ASCII deletion cost

### Examples
**Example 1**

- Input: `s1 = "sea", s2 = "eat"`
- Output: `231`

**Example 2**

- Input: `s1 = "delete", s2 = "leet"`
- Output: `403`

**Example 3**

- Input: `s1 = "abc", s2 = "abc"`
- Output: `0`
