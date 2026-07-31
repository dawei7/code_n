# Find the Divisibility Array of a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2575 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [find-the-divisibility-array-of-a-string](https://leetcode.com/problems/find-the-divisibility-array-of-a-string/) |

## Problem Description

### Goal

You are given a 0-indexed digit string `word` of length $n$ and a positive integer `m`. For every index $i$, consider the numeric value represented by the prefix `word[0:i + 1]`.

Build the divisibility array `div` of length $n`: set `div[i]` to `1` when that prefix value is divisible by `m`, and set it to `0` otherwise. Return the completed array.

The prefixes can contain far more digits than a built-in integer type can hold, so their divisibility must be determined without converting the complete values directly.

### Function Contract

**Inputs**

- `word`: A non-empty string containing only the digits `0` through `9`.
- `m`: The positive divisor used for every prefix.

The string length satisfies $1 \le n \le 10^5$, and $1 \le m \le 10^9$.

**Return value**

- Return a length-$n$ list of zeroes and ones indicating whether each prefix of `word` is divisible by `m`.

### Examples

**Example 1**

- Input: `word = "998244353", m = 3`
- Output: `[1,1,0,0,0,1,1,0,0]`
- Explanation: The divisible prefixes represent `9`, `99`, `998244`, and `9982443`.

**Example 2**

- Input: `word = "1010", m = 10`
- Output: `[0,1,0,1]`
- Explanation: The prefixes representing `10` and `1010` are divisible by ten.
