# Pow(x, n)

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 50 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/powx-n/) |

## Problem Description
### Goal
Given a floating-point base `x` and a signed integer exponent `n`, compute the mathematical value $x^{n}$ without delegating to a built-in exponentiation routine. The exponent may occupy the full signed 32-bit range.

A zero exponent produces `1`. For a negative exponent, use the reciprocal of the corresponding positive power, so $x^{-k} = 1 / x^{k}$. Return the floating-point result with the normal tolerance for representation error, while avoiding a number of multiplications proportional to a very large magnitude of `n`.

### Function Contract
**Inputs**

- `x`: a floating-point base
- `n`: a signed integer exponent

**Return value**

The floating-point value of $x^{n}$.

### Examples
**Example 1**

- Input: `x = 2.0, n = 10`
- Output: `1024.0`

**Example 2**

- Input: `x = 2.1, n = 3`
- Output: approximately `9.261`

**Example 3**

- Input: `x = 2.0, n = -2`
- Output: `0.25`
