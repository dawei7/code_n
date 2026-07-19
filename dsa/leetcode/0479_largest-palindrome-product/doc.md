# Largest Palindrome Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 479 |
| Difficulty | Hard |
| Topics | Math, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-palindrome-product/) |

## Problem Description
### Goal
Given a digit count `n` from `1` through `8`, consider products $a \cdot b$ where both factors are positive decimal integers with exactly `n` digits. A product qualifies when its decimal representation reads the same forward and backward.

Find the largest qualifying palindrome product, then return that palindrome modulo `1337`. The factors may be equal, and the modulo operation is applied only to the final largest palindrome rather than used to compare candidate sizes. The function returns the reduced value, not the factors or unreduced palindrome. For $n = 1$, the largest product is included under the same rule.

### Function Contract
**Inputs**

- `n`: the factor digit count, restricted to $1 \le n \le 8$

**Return value**

- The largest qualifying palindrome product modulo `1337`

### Examples
**Example 1**

- Input: `n = 1`
- Output: `9`

**Example 2**

- Input: `n = 2`
- Output: `987`

**Example 3**

- Input: `n = 3`
- Output: `123`
