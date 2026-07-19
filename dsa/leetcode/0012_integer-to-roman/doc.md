# Integer to Roman

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 12 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/integer-to-roman/) |

## Problem Description
### Goal
Convert an integer `num` from `1` through `3999` into its standard Roman-numeral representation. The symbols `I`, `V`, `X`, `L`, `C`, `D`, and `M` represent `1`, `5`, `10`, `50`, `100`, `500`, and `1000`, respectively.

Write symbols from larger values toward smaller ones. Powers-of-ten symbols may repeat at most three consecutive times, while `V`, `L`, and `D` are never repeated. Values beginning with `4` or `9` use the six subtractive forms `IV`, `IX`, `XL`, `XC`, `CD`, and `CM`. Return the unique conventional representation without spaces or nonstandard subtractive pairs.

### Function Contract
**Inputs**

- `num`: `int` in `[1, 3999]`

**Return value**

A `str` containing the canonical Roman representation of `num`.

### Examples
**Example 1**

- Input: `num = 3749`
- Output: `"MMMDCCXLIX"`

**Example 2**

- Input: `num = 58`
- Output: `"LVIII"`

**Example 3**

- Input: `num = 1994`
- Output: `"MCMXCIV"`
