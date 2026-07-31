# Majority Frequency Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3692 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/majority-frequency-characters/) |

## Problem Description
### Goal

Count how often every distinct lowercase English letter occurs in `s`. Letters with the same occurrence count belong to one frequency group. Select the group containing the greatest number of distinct letters and return a string containing every letter in that group.

The returned letters may appear in any order. When multiple frequency groups contain the same greatest number of distinct letters, choose the tied group with the larger occurrence count. Group size counts different letters, not their total appearances in the original string.

### Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters with $1 \le \lvert s\rvert \le 100$.

**Return value**

Return exactly the distinct letters in the selected frequency group, in any order and with each selected letter appearing once.

### Examples

**Example 1**

- Input: `s = "aaabbbccdddde"`
- Output: `"ab"`

Two letters occur three times, while every other frequency group contains only one letter.

**Example 2**

- Input: `s = "abcd"`
- Output: `"abcd"`

All four distinct letters belong to the frequency-one group.

**Example 3**

- Input: `s = "pfpfgi"`
- Output: `"fp"`

Frequency groups one and two each contain two letters, so the larger frequency wins the tie.
