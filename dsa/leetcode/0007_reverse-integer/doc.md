# Reverse Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 7 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-integer/) |

## Problem Description
### Goal
Given a signed 32-bit integer `x`, reverse the order of the digits in its decimal magnitude while preserving its sign. Zeroes that move to the front of the reversed magnitude are discarded by ordinary integer notation, so reversing `120` produces `21`.

Return the reversed integer only when it still lies in the signed 32-bit interval $[- 2 ^{31}, 2 ^{31} - 1]$. If the reversed magnitude would overflow that range, return `0` instead. The task assumes no wider integer type is available merely to hold an overflowing intermediate result.

### Function Contract
**Inputs**

- `x`: signed 32-bit `int`

**Return value**

An `int` containing the reversed value, or `0` when reversal overflows the signed 32-bit range.

### Examples
**Example 1**

- Input: `x = 123`
- Output: `321`

**Example 2**

- Input: `x = -123`
- Output: `-321`

**Example 3**

- Input: `x = 120`
- Output: `21`
