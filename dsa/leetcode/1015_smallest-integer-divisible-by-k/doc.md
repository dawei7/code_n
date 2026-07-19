# Smallest Integer Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1015 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/smallest-integer-divisible-by-k/) |

## Problem Description

### Goal

You are given a positive integer `k`. Find the length of the smallest positive integer `n` that is divisible by `k` and whose decimal representation contains only the digit `1`.

Return that length, or return `-1` if no such integer exists. The all-ones integer itself may be far too large for a signed 64-bit type, so the required result is its digit count rather than its numeric value.

### Function Contract

**Inputs**

- `k`: a positive divisor satisfying $1\le k\le10^5$.

**Return value**

- The length of the shortest positive all-ones decimal integer divisible by `k`, or `-1` if none exists.

### Examples

**Example 1**

- Input: `k = 1`
- Output: `1`
- Explanation: The one-digit integer `1` is divisible by `1`.

**Example 2**

- Input: `k = 2`
- Output: `-1`
- Explanation: An all-ones integer is odd and cannot be divisible by `2`.

**Example 3**

- Input: `k = 3`
- Output: `3`
- Explanation: `111` is divisible by `3`, while `1` and `11` are not.
