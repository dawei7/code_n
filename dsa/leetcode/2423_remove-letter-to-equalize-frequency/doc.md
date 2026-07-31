# Remove Letter To Equalize Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2423 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Remove Letter To Equalize Frequency](https://leetcode.com/problems/remove-letter-to-equalize-frequency/) |

## Problem Description

### Goal

You are given a 0-indexed string `word` made only of lowercase English letters. The frequency of a letter is the number of times that letter occurs in the string.

Choose exactly one index and remove the character at that position. Return whether some such removal makes every letter still present in the resulting string occur the same number of times. Doing nothing is not permitted, while a letter removed completely is no longer considered present.

### Function Contract

**Inputs**

- `word`: A lowercase English string with length from 2 through 100.

**Return value**

- `true` if deleting exactly one character can equalize all positive letter frequencies; otherwise, `false`.

### Examples

**Example 1**

- Input: `word = "abcc"`
- Output: `true`

Removing one `c` leaves `a`, `b`, and `c` with frequency 1.

**Example 2**

- Input: `word = "aazz"`
- Output: `false`

Deleting either letter type produces positive frequencies 1 and 2.

**Example 3**

- Input: `word = "abbcc"`
- Output: `true`

Removing the only `a` leaves the two remaining letter types with frequency 2.
