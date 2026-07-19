# Reordered Power of 2

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 869 |
| Difficulty | Medium |
| Topics | Hash Table, Math, Sorting, Counting, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/reordered-power-of-2/) |

## Problem Description
### Goal
Given a positive integer `n`, rearrange all of its decimal digits in any order, including their original order. Every digit must be used exactly once, and the resulting decimal representation may not begin with `0`.

Return `true` if at least one permitted ordering forms a power of two, and return `false` otherwise. A valid target has the form $2^e$ for some nonnegative integer exponent $e$; the task asks only whether such an ordering exists, not which ordering produces it.

### Function Contract
**Inputs**

- `n`: a positive integer where $1 \leq n \leq 10^9$.

Let $d$ be the number of decimal digits in `n`, so $1 \leq d \leq 10$.

**Return value**

Return `true` exactly when the digits of `n` can be reordered, without a leading zero, to equal a power of two.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `true`

The original ordering is $2^0$.

**Example 2**

- Input: `n = 10`
- Output: `false`

Neither `10` nor the only other ordering `01` is a valid power-of-two representation.

**Example 3**

- Input: `n = 46`
- Output: `true`

Reordering the digits produces `64`, which is $2^6$.
