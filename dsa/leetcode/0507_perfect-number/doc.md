# Perfect Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 507 |
| Difficulty | Easy |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/perfect-number/) |

## Problem Description
### Goal
Given a positive integer `num`, a positive divisor is an integer that divides it evenly. The proper positive divisors exclude `num` itself but include `1`; paired factors must each be counted once, including the square root only once when `num` is a perfect square.

Return `True` exactly when `num` equals the sum of all its proper positive divisors, which makes it a perfect number, and return `False` otherwise. The value `1` is not perfect because it has no positive divisor smaller than itself. The function returns only the classification, not the divisor list or sum.

### Function Contract
**Inputs**

- `num`: a positive integer

**Return value**

- `True` when `num` is perfect; otherwise `False`

### Examples
**Example 1**

- Input: `num = 28`
- Output: `True`

**Example 2**

- Input: `num = 7`
- Output: `False`

**Example 3**

- Input: `num = 1`
- Output: `False`
