# Closest Fair Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2417 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/closest-fair-integer/) |

## Problem Description

### Goal

A positive integer is called fair when its decimal representation contains the same number of even digits and odd digits. Digit parity is based on the digit itself, so `0` is even. Consequently, a fair integer must contain an even total number of digits.

Given a positive integer `n`, return the smallest fair integer greater than or equal to `n`. The answer may have more digits than `n`: if no fair integer remains at the current even length, or if `n` has odd length, the search continues at the next possible even digit length.

### Function Contract

**Inputs**

- `n`: A positive integer satisfying $1 \le n \le 10^9$.

Let $d$ be the number of decimal digits in the answer. Under the legal contract, $d \le 10$.

**Return value**

Return the least integer $k \ge n$ whose decimal digits contain exactly $d/2$ even digits and $d/2$ odd digits.

### Examples

#### Example 1

- **Input:** `n = 2`
- **Output:** `10`

#### Example 2

- **Input:** `n = 403`
- **Output:** `1001`

#### Example 3

- **Input:** `n = 99`
- **Output:** `1001`
