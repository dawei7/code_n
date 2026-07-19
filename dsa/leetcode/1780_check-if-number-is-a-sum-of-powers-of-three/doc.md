# Check if Number is a Sum of Powers of Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1780 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/) |

## Problem Description

### Goal

Given a positive integer `n`, determine whether it can be written as a sum of distinct powers of three. A power of three has the form $3^k$ for a nonnegative integer exponent $k$.

Each power may appear at most once in the sum, but any collection of different exponents is allowed. Return `true` when such a representation exists and `false` otherwise.

### Function Contract

**Inputs**

- `n`: an integer satisfying $1 \le n \le 10^7$.
- The input bound means `n` has at most fifteen base-three digits.

**Return value**

Return `true` exactly when there is a set $S$ of distinct nonnegative integers such that

$$
n=\sum_{k\in S}3^k.
$$

### Examples

**Example 1**

- Input: `n = 12`
- Output: `true`
- Explanation: $12=3^1+3^2$.

**Example 2**

- Input: `n = 91`
- Output: `true`
- Explanation: $91=3^0+3^2+3^4$.

**Example 3**

- Input: `n = 21`
- Output: `false`
- Explanation: Its base-three representation requires a digit `2`, which would repeat one power.
