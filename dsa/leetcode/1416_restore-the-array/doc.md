# Restore The Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1416 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/restore-the-array/) |

## Problem Description

### Goal

An integer array was converted into one digit string by concatenating the decimal representations of its elements. Every original element was between $1$ and `k`, inclusive, and none of those decimal representations had a leading zero.

Given the resulting string `s` and the limit `k`, count how many different arrays could have produced `s`. Different split positions define different arrays. Return the count modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `s`: a digit string of length $n$, where $1 \le n \le 10^5$ and every character is from `0` through `9`.
- `k`: the largest permitted array value, where $1 \le k \le 10^9$.

**Return value**

- The number of valid ways to split `s` into decimal integers from $1$ through `k` with no leading zeros, modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `s = "1000", k = 10000`
- Output: `1`

**Example 2**

- Input: `s = "1000", k = 10`
- Output: `0`

**Example 3**

- Input: `s = "1317", k = 2000`
- Output: `8`
