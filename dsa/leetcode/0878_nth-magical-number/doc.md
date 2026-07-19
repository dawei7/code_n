# Nth Magical Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 878 |
| Difficulty | Hard |
| Topics | Math, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/nth-magical-number/) |

## Problem Description
### Goal
A positive integer is magical when it is divisible by `a` or by `b`. Consider all such positive integers once each and arrange them in increasing order, including numbers divisible by both divisors only once.

Given `n`, `a`, and `b`, find the $n$th magical number in that order. The value itself may be very large, so return it modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: the one-based target position, where $1 \leq n \leq 10^9$.
- `a`: a divisor between $2$ and $4\cdot10^4$.
- `b`: a divisor between $2$ and $4\cdot10^4$.
- Let $L=\operatorname{lcm}(a,b)$.

**Return value**

Return the $n$th positive integer divisible by `a` or `b`, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `n = 1, a = 2, b = 3`
- Output: `2`

**Example 2**

- Input: `n = 4, a = 2, b = 3`
- Output: `6`

The sequence begins `[2,3,4,6]`.

**Example 3**

- Input: `n = 5, a = 2, b = 4`
- Output: `10`

Every multiple of `4` is already a multiple of `2`, so the magical sequence is the positive even integers.
