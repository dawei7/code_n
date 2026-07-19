# Largest Substring Between Two Equal Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1624 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-substring-between-two-equal-characters/) |

## Problem Description
### Goal
Given a string `s`, choose two occurrences of the same character and consider the contiguous substring strictly between them. The two matching endpoint characters are excluded from its length.

Return the greatest possible length of such an interior substring. If no character appears at least twice, no valid pair of endpoints exists, so return `-1`. An adjacent equal pair is valid and encloses an empty substring of length zero.

### Function Contract
**Inputs**

- `s`: a string of length $n$, where $1 \le n \le 300$.
- Every character of `s` is a lowercase English letter.

**Return value**

Return the maximum value of $j-i-1$ over indices $i<j$ for which `s[i] == s[j]`, or `-1` when no such pair exists.

### Examples
**Example 1**

- Input: `s = "aa"`
- Output: `0`

The equal characters are adjacent, so there is no character between them.

**Example 2**

- Input: `s = "abca"`
- Output: `2`

The two `a` characters enclose `"bc"`.

**Example 3**

- Input: `s = "cbzxy"`
- Output: `-1`

No character occurs twice.
