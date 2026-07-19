# Additive Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 306 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/additive-number/) |

## Problem Description
### Goal
Given a nonempty string of decimal digits, divide the entire string into at least three consecutive numbers. Beginning with the third number, every value must equal the sum of the two values immediately before it.

Return `True` when at least one complete additive partition exists and `False` otherwise. Number boundaries may have different widths, but a multi-digit number cannot begin with `0`; the single value `0` is allowed. Every input digit must be consumed in order with no separators or leftovers. Values may exceed fixed-width integer ranges, so their decimal substrings must be handled without overflow assumptions.

### Function Contract
**Inputs**

- `num`: a nonempty string of decimal digits

**Return value**

`True` when the complete string forms an additive sequence without illegal leading zeroes; otherwise `False`.

### Examples
**Example 1**

- Input: `num = "112358"`
- Output: `True`

**Example 2**

- Input: `num = "199100199"`
- Output: `True`

**Example 3**

- Input: `num = "1023"`
- Output: `False`
