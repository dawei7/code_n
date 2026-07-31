# Smallest Divisible Digit Product I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3345 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-divisible-digit-product-i/) |

## Problem Description

### Goal

Given positive integers `n` and `t`, examine integers beginning at `n`. For any candidate, its digit product is obtained by multiplying all of its decimal digits. A zero digit therefore makes the entire product zero, and zero is divisible by every permitted value of `t`.

Return the smallest candidate greater than or equal to `n` whose digit product is divisible by `t`. The search is guaranteed to terminate: every block of ten consecutive integers contains a multiple of ten, whose final digit is zero.

### Function Contract

**Inputs**

- `n`: The inclusive lower bound for the answer, with $1 \le n \le 100$.
- `t`: The positive divisor, with $1 \le t \le 10$.

For a candidate with decimal digits $d_1,d_2,\ldots,d_k$, its digit product is $\prod_{i=1}^{k} d_i$.

**Return value**

Return the least integer $x \ge n$ whose digit product is divisible by `t`.

### Examples

**Example 1**

- Input: `n = 10, t = 2`
- Output: `10`
- Explanation: The digit product is $1 \cdot 0 = 0$, which is divisible by $2$.

**Example 2**

- Input: `n = 15, t = 3`
- Output: `16`
- Explanation: The product for `15` is $5$, while the product for `16` is $6$, so `16` is the first valid candidate.

**Example 3**

- Input: `n = 1, t = 10`
- Output: `10`
- Explanation: None of `1` through `9` has a digit product divisible by $10$; the zero digit in `10` makes its product zero.
