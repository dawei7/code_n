# Second Largest Digit in a String

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/second-largest-digit-in-a-string/) |
| Frontend ID | 1796 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given an alphanumeric string `s`, meaning that every character is either a lowercase English letter or a decimal digit.

Consider the distinct numerical digit values that occur in the string. Return the second largest of those values. Repeated appearances of one digit count as the same value, and letters do not participate in the ranking. If fewer than two distinct digits occur, return `-1`.

### Function Contract

**Inputs**

- `s`: an alphanumeric string of length $n$, where $1 \le n \le 500$.

**Return value**

- Return the second largest distinct integer digit from `0` through `9` that appears in `s`.
- Return `-1` when no second distinct digit exists.

### Examples

**Example 1**

- Input: `s = "dfa12321afd"`
- Output: `2`

The distinct digits are `1`, `2`, and `3`, so `2` is second largest.

**Example 2**

- Input: `s = "abc1111"`
- Output: `-1`

Only digit `1` appears, regardless of its repetitions.

**Example 3**

- Input: `s = "ck077"`
- Output: `0`

The distinct digits are `0` and `7`; therefore zero is the second largest.
