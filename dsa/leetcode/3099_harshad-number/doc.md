# Harshad Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3099 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [harshad-number](https://leetcode.com/problems/harshad-number/) |

## Problem Description

### Goal

A positive integer is a Harshad number when it is divisible by the sum of its decimal digits. You are given a positive integer `x`.

Compute the sum of the digits of `x`. If that sum divides `x` evenly, return the digit sum; otherwise, return `-1`. The input is always positive, so its digit sum is also positive and the divisibility test is well-defined.

### Function Contract

**Inputs**

- `x`: A positive integer satisfying $1 \le x \le 100$.

**Return value**

- The sum of the decimal digits of `x` when `x` is a Harshad number, or `-1` when it is not.

### Examples

**Example 1**

- Input: `x = 18`
- Output: `9`
- Explanation: The digit sum is $1 + 8 = 9$, and $18$ is divisible by $9$.

**Example 2**

- Input: `x = 23`
- Output: `-1`
- Explanation: The digit sum is $2 + 3 = 5$, which does not divide $23$ evenly.
