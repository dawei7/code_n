# Monotone Increasing Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 738 |
| Difficulty | Medium |
| Topics | Math, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/monotone-increasing-digits/) |

## Problem Description
### Goal
An integer has monotone increasing digits when each adjacent decimal pair `x`, `y` from left to right satisfies $x \le y$. Equal neighboring digits are allowed; only a decrease violates the condition.

Given a non-negative integer `n`, return the largest integer less than or equal to `n` whose digits are monotone increasing. The result may contain fewer digits than `n`, and leading zeroes are not part of an integer's ordinary decimal representation.

### Function Contract
**Inputs**

- `n`: an integer from `0` through $10^{9}$

**Return value**

- The largest integer $x \le n$ whose adjacent decimal digits satisfy $x_i \le x_{i+1}$

### Examples
**Example 1**

- Input: `n = 10`
- Output: `9`

**Example 2**

- Input: `n = 1234`
- Output: `1234`

**Example 3**

- Input: `n = 332`
- Output: `299`
