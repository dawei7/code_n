# Number of Ways to Separate Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1977 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-separate-numbers/) |

## Problem Description
### Goal
A string `num` was formed by writing a list of positive integers consecutively
and omitting the commas between them. The original list was non-decreasing:
each integer was at least the integer immediately before it. No integer used a
leading zero.

Count the ways to insert separators so the complete string becomes such a
valid list. Every digit must belong to exactly one number, values are compared
mathematically even when they exceed machine integer range, and the result is
returned modulo $10^9+7$.

### Function Contract
**Inputs**

- `num`: a digit string of length $N$, where $1 \le N \le 3500$.

**Return value**

- The number of partitions of `num` into positive, leading-zero-free decimal
  integers in non-decreasing order, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `num = "327"`
- Output: `2`

**Example 2**

- Input: `num = "094"`
- Output: `0`

**Example 3**

- Input: `num = "0"`
- Output: `0`
