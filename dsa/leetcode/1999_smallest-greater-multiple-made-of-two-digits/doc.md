# Smallest Greater Multiple Made of Two Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1999 |
| Difficulty | Medium |
| Topics | Math, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/) |

## Problem Description

### Goal

Given positive integer `k` and two decimal digits `digit1` and `digit2`, find the smallest integer that satisfies all three conditions: it is strictly greater than `k`, it is divisible by `k`, and every digit in its ordinary decimal representation is either `digit1` or `digit2`.

The result must fit in a signed 32-bit integer, whose maximum is $2^{31}-1$. Return `-1` when no qualifying value exists within that limit. A representation cannot begin with zero, and the two supplied digits are allowed to be equal.

### Function Contract

**Inputs**

- `k`: an integer with $1 \le k \le 1000$.
- `digit1` and `digit2`: decimal digits from $0$ through $9$.
- Let $D=10$ be the maximum possible decimal length under the signed 32-bit ceiling.

**Return value**

Return the smallest signed 32-bit integer greater than `k` that is a multiple of `k` and uses only the supplied digits, or return `-1` if none exists.

### Examples

**Example 1**

- Input: `k = 2, digit1 = 0, digit2 = 2`
- Output: `20`
- Explanation: `20` is the first allowed-digit value above $2$ that is divisible by $2$.

**Example 2**

- Input: `k = 3, digit1 = 4, digit2 = 2`
- Output: `24`
- Explanation: Sorting the available digits during generation reveals `24` before any larger qualifying value.

**Example 3**

- Input: `k = 2, digit1 = 0, digit2 = 0`
- Output: `-1`
- Explanation: Zero cannot begin a positive decimal representation, so there is no candidate.
