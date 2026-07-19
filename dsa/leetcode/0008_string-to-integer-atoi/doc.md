# String to Integer (atoi)

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 8 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/string-to-integer-atoi/) |

## Problem Description
### Goal
Convert the initial numeric portion of a string `s` into a 32-bit signed integer using a fixed parsing order. First ignore leading whitespace, then determine signedness from at most one `+` or `-`, and finally convert the longest consecutive run of decimal digits. Leading zeroes within that run do not change the value.

Conversion stops at the first non-digit after parsing begins; all later characters are ignored. If no digit is consumed, return `0`. Otherwise apply the parsed sign and clamp a value outside $[- 2 ^{31}, 2 ^{31} - 1]$ to the nearest signed 32-bit boundary before returning it.

### Function Contract
**Inputs**

- `s`: `str`

**Return value**

An `int` in $[- 2 ^{31}, 2 ^{31} - 1]$ produced by the parsing rules.

### Examples
**Example 1**

- Input: `s = "42"`
- Output: `42`

**Example 2**

- Input: `s = "   -042"`
- Output: `-42`

**Example 3**

- Input: `s = "1337c0d3"`
- Output: `1337`
