# Divisible and Non-divisible Sums Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2894 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/) |

## Problem Description

### Goal

You are given two positive integers, `n` and `m`. Consider every integer in the inclusive range $[1,n]$ and divide the values into two groups according to divisibility by `m`.

Let `num1` be the sum of all values that are not divisible by `m`, and let `num2` be the sum of all values that are divisible by `m`. Return the signed difference `num1 - num2`.

### Function Contract

**Inputs**

- `n`: The inclusive upper bound of the range, with $1 \le n \le 1000$.
- `m`: The positive divisor used to partition the range, with $1 \le m \le 1000$.

**Return value**

Return the sum of the non-divisible values minus the sum of the divisible values.

### Examples

#### Example 1

- **Input:** `n = 10, m = 3`
- **Output:** `19`
- **Explanation:** The non-divisible values sum to $37$, while $3+6+9=18$, so the result is $37-18=19$.

#### Example 2

- **Input:** `n = 5, m = 6`
- **Output:** `15`
- **Explanation:** No value in $[1,5]$ is divisible by $6$, so the entire range contributes positively.

#### Example 3

- **Input:** `n = 5, m = 1`
- **Output:** `-15`
- **Explanation:** Every value is divisible by $1$, so the whole range contributes negatively.
