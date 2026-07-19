# Roman to Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 13 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/roman-to-integer/) |

## Problem Description
### Goal
You are given a valid Roman numeral composed of `I`, `V`, `X`, `L`, `C`, `D`, and `M`, representing `1`, `5`, `10`, `50`, `100`, `500`, and `1000`. Most symbols contribute their values additively from left to right, and repeated symbols represent repeated contributions.

The notation also permits the standard subtractive pairs: `I` before `V` or `X`, `X` before `L` or `C`, and `C` before `D` or `M`. Convert the complete numeral to its integer value between `1` and `3999`. Because the input is guaranteed canonical, invalid or nonstandard symbol arrangements do not need to be diagnosed.

### Function Contract
**Inputs**

- `s`: non-empty `str` containing `I`, `V`, `X`, `L`, `C`, `D`, and `M`

**Return value**

An `int` equal to the value represented by `s`.

### Examples
**Example 1**

- Input: `s = "III"`
- Output: `3`

**Example 2**

- Input: `s = "LVIII"`
- Output: `58`

**Example 3**

- Input: `s = "MCMXCIV"`
- Output: `1994`
