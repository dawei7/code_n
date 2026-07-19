# Shortest Completing Word

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 748 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-completing-word/) |

## Problem Description

### Goal

Given a string `licensePlate` and an array `words`, ignore digits, spaces, and other nonletter characters in the plate and treat its letters case-insensitively. A completing word contains every extracted letter at least as many times as that letter appears in the plate.

Return the shortest completing word from `words`. If several candidates have the same minimum length, return the one appearing earliest in the input. Extra letters are allowed, but repeated plate letters require matching multiplicity rather than a single occurrence.

### Function Contract

**Inputs**

- `licensePlate`: a string containing letters, digits, and spaces.
- `words`: a list of lowercase candidate words containing at least one completing word.

**Return value**

- The first shortest word whose letter counts cover the license plate's required counts.

### Examples

**Example 1**

- Input: `licensePlate = "1s3 PSt"`, `words = ["step", "steps", "stripe", "stepple"]`
- Output: `"steps"`
- Explanation: A completing word needs one `s`, one `p`, and two `t` letters.

**Example 2**

- Input: `licensePlate = "1s3 456"`, `words = ["looks", "pest", "stew", "show"]`
- Output: `"pest"`
- Explanation: Both `"pest"` and `"stew"` cover `s`, but `"pest"` appears first among the shortest valid words.
