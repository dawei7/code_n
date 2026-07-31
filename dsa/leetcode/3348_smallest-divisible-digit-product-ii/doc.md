# Smallest Divisible Digit Product II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3348 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Backtracking, Greedy, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-divisible-digit-product-ii/) |

## Problem Description

### Goal

The string `num` represents a positive integer and may contain as many as 200,000 decimal digits. An integer is zero-free when every one of its decimal digits belongs to `1` through `9`. For such an integer, multiply all digits to obtain its digit product.

Return the decimal string for the smallest zero-free integer that is greater than or equal to `num` and whose digit product is divisible by `t`. The answer may contain more digits than `num`. If no zero-free integer can have a digit product divisible by `t`, return `"-1"`.

### Function Contract

**Inputs**

- `num`: A decimal string of length $L$, where $2 \le L \le 2\cdot 10^5$; it contains only digits and has no leading zero.
- `t`: The required positive divisor, with $1 \le t \le 10^{14}$.

A returned number is valid only if none of its digits is zero and the product of all its digits is a multiple of `t`.

**Return value**

Return the smallest valid decimal string representing an integer at least as large as `num`, or `"-1"` when no valid integer exists.

### Examples

**Example 1**

- Input: `num = "1234", t = 256`
- Output: `"1488"`
- Explanation: The digit product of `1488` is $1\cdot4\cdot8\cdot8=256$, and no smaller zero-free integer at least `1234` has a product divisible by $256$.

**Example 2**

- Input: `num = "12355", t = 50`
- Output: `"12355"`
- Explanation: The input is already zero-free and its digit product is $150$, which is divisible by $50$.

**Example 3**

- Input: `num = "11111", t = 26`
- Output: `"-1"`
- Explanation: A product of nonzero decimal digits has no prime factors other than $2$, $3$, $5$, and $7$, while $26$ contains the factor $13$.
