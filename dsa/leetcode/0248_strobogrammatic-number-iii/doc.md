# Strobogrammatic Number III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 248 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/strobogrammatic-number-iii/) |

## Problem Description
### Goal
Given decimal strings `low` and `high` representing an inclusive nonnegative range without unnecessary leading zeroes, count the integers whose written digits remain unchanged after a 180-degree rotation. Valid mirrored digits use `0`, `1`, `6`, `8`, and `9` in their compatible pairings.

Return the number of strobogrammatic numerals `x` satisfying `low <= x <= high`, including either boundary when valid. Generated multi-digit forms may not begin with zero, while the single numeral `0` is allowed when inside the range. Compare potentially long bounds by numeric-string length and order rather than converting them unsafely to fixed-width integers.

### Function Contract
**Inputs**

- `low`: the inclusive lower bound without leading zeros
- `high`: the inclusive upper bound without leading zeros

**Return value**

The number of strobogrammatic integers `x` satisfying `low <= x <= high`.

### Examples
**Example 1**

- Input: `low = "50", high = "100"`
- Output: `3`

**Example 2**

- Input: `low = "0", high = "0"`
- Output: `1`

**Example 3**

- Input: `low = "0", high = "10"`
- Output: `3`
