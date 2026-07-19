# Largest Odd Number in String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1903 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Largest Odd Number in String](https://leetcode.com/problems/largest-odd-number-in-string/) |

## Problem Description

### Goal

`num` is the decimal representation of a positive integer that may be too large for ordinary numeric types. Choose a nonempty contiguous substring whose represented integer is odd, and among all such substrings return the one with the greatest numeric value.

Return the chosen digits as a string. If no substring represents an odd integer, return the empty string. The input contains no leading zero, although zeros may appear elsewhere.

### Function Contract

**Inputs**

- `num`: a digit string of length $n$, where $1 \le n \le 10^5$.
- `num` has no leading zero.

**Return value**

Return the largest-valued odd integer obtainable as a nonempty substring of `num`, represented as a string, or `""` when none exists.

### Examples

**Example 1**

- Input: `num = "52"`
- Output: `"5"`
- Explanation: `"5"` is the only odd-valued substring.

**Example 2**

- Input: `num = "4206"`
- Output: `""`
- Explanation: Every digit is even, so every substring ends in an even digit.

**Example 3**

- Input: `num = "35427"`
- Output: `"35427"`
- Explanation: The full input is already odd and is longer than every proper substring.
