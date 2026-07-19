# Power of Four

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 342 |
| Difficulty | Easy |
| Topics | Math, Bit Manipulation, Recursion |
| Official Link | [LeetCode](https://leetcode.com/problems/power-of-four/) |

## Problem Description
### Goal
Given a signed 32-bit integer `n`, determine whether it can be written exactly as $4^{x}$ for an integer exponent $x \ge 0$. Valid values begin with $1 = 4^{0}$, then `4`, `16`, `64`, and continue by repeated multiplication by four.

Return `True` only for positive exact powers of four. Return `False` for zero, negative values, powers of two whose single set bit lies at an odd binary position, and all other integers. The task asks for a boolean rather than the exponent. Meet the follow-up without loops or recursion by using fixed-width arithmetic properties where required.

### Function Contract
**Inputs**

- `n`: the integer to classify

**Return value**

- `True` if `n` is an exact non-negative integer power of four; otherwise `False`.

### Examples
**Example 1**

- Input: `n = 16`
- Output: `True`

**Example 2**

- Input: `n = 5`
- Output: `False`

**Example 3**

- Input: `n = 1`
- Output: `True`
