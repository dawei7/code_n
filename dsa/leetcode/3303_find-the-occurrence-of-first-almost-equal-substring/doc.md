# Find the Occurrence of First Almost Equal Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3303 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/) |

## Problem Description

### Goal

Two strings of the same length are almost equal when changing at most one character in the first makes the strings identical. Given a source string `s` and a shorter `pattern`, examine every contiguous substring of `s` whose length equals `pattern.length`.

Return the smallest starting index of a window that is almost equal to `pattern`. An exact match also qualifies because it needs zero changes. If every candidate window differs from the pattern in at least two positions, return `-1`.

### Function Contract

**Inputs**

- `s`: The lowercase source string containing candidate windows.
- `pattern`: The non-empty lowercase string against which equal-length windows are compared.

The pattern is strictly shorter than `s`, and `s.length` is at most $10^5$.

**Return value**

- The first starting index whose length-`pattern.length` substring differs from `pattern` in at most one position, or `-1` if no such window exists.

### Examples

#### Example 1

- **Input:** `s = "abcdefg"`, `pattern = "bcdffg"`
- **Output:** `1`
- **Explanation:** `s[1..6]` is `"bcdefg"`, which differs from the pattern only at its fourth character.

#### Example 2

- **Input:** `s = "ababbababa"`, `pattern = "bacaba"`
- **Output:** `4`
- **Explanation:** The window `"bababa"` starting at 4 has one mismatching character.

#### Example 3

- **Input:** `s = "abcd"`, `pattern = "dba"`
- **Output:** `-1`
- **Explanation:** Neither length-three window is within one character change of the pattern.

#### Example 4

- **Input:** `s = "dde"`, `pattern = "d"`
- **Output:** `0`
- **Explanation:** The first one-character window is already an exact match.
