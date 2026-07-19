# Fibonacci Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 509 |
| Difficulty | Easy |
| Topics | Math, Dynamic Programming, Recursion, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/fibonacci-number/) |

## Problem Description
### Goal
The Fibonacci sequence starts with $F(0) = 0$ and $F(1) = 1$. For every index $n > 1$, its value is defined by the recurrence $F(n) = F(n - 1) + F(n - 2)$.

Given an integer `n` from `0` through `30`, return `F(n)`. The index is zero-based, so input zero returns zero and input one returns one. Compute the numeric sequence value rather than returning the preceding pair, a generated list, or the number of additions performed.

### Function Contract
**Inputs**

- `n`: an integer index from `0` through `30`

**Return value**

- The integer `F(n)` defined by the Fibonacci recurrence

### Examples
**Example 1**

- Input: `n = 0`
- Output: `0`

**Example 2**

- Input: `n = 5`
- Output: `5`

**Example 3**

- Input: `n = 8`
- Output: `21`
