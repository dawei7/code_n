# Count Good Numbers

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-good-numbers/) |
| Frontend ID | 1922 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A digit string is good when its digits obey rules based on their zero-based positions. At every even index, the digit must itself be even, so the choices are `0`, `2`, `4`, `6`, and `8`. At every odd index, the digit must be prime, so the choices are `2`, `3`, `5`, and `7`.

Given the length `n`, count all good digit strings of that length. Leading zeroes are allowed, meaning the objects are strings rather than ordinary decimal representations. Since the count grows rapidly, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: the required digit-string length, with $1 \le n \le 10^{15}$.

**Return value**

- Return the number of length-$n$ good digit strings modulo $10^9+7$.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `5`

The valid strings are `"0"`, `"2"`, `"4"`, `"6"`, and `"8"`.

**Example 2**

- Input: `n = 4`
- Output: `400`

There are two even-indexed and two odd-indexed positions, giving $5^2 \cdot 4^2=400$ choices.

**Example 3**

- Input: `n = 50`
- Output: `564908303`
