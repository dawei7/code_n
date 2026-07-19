# Sum of Square Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 633 |
| Difficulty | Medium |
| Topics | Math, Two Pointers, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-square-numbers/) |

## Problem Description
### Goal
Given a non-negative integer `c`, decide whether there are two integers `a` and `b` such that $a^{2} + b^{2} = c$. The same value may be used twice, and either square may be zero.

Return `True` when at least one such pair exists and `False` otherwise. Only exact integer equality counts; an approximate square-root match is insufficient. Because changing a sign does not change a square, a valid representation can always be expressed with non-negative `a` and `b` even though the question permits integers.

### Function Contract
**Inputs**

- `c`: a nonnegative integer

**Return value**

- `true` if integers $a \ge 0$ and $b \ge 0$ exist with $a^{2} + b^{2} = c$
- `false` otherwise

### Examples
**Example 1**

- Input: `c = 5`
- Output: `true`, because $1^2+2^2=5$

**Example 2**

- Input: `c = 3`
- Output: `false`

**Example 3**

- Input: `c = 0`
- Output: `true`, because $0^2+0^2=0$
