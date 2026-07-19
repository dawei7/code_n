# Smallest Good Base

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 483 |
| Difficulty | Hard |
| Topics | Math, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-good-base/) |

## Problem Description
### Goal
Given a decimal string `n` representing an integer without leading zeroes, call an integer $k \ge 2$ a good base when every digit of `n` written in base `k` is `1`. Such a representation contains at least two ones and therefore expresses `n` as a geometric sum $1 + k + k ^{2} + \ldots$.

Return the smallest good base as a decimal string. Compare candidate bases using the full represented integer rather than a floating-point approximation that can round incorrectly near $10^{18}$. A two-digit representation `11` always supplies a fallback base, but a smaller base with more one digits must be preferred when it exists.

### Function Contract
**Inputs**

- `n`: the decimal integer supplied as a string

**Return value**

- The smallest good base as a decimal string

### Examples
**Example 1**

- Input: `n = "13"`
- Output: `"3"`

**Example 2**

- Input: `n = "4681"`
- Output: `"8"`

**Example 3**

- Input: `n = "1000000000000000000"`
- Output: `"999999999999999999"`
