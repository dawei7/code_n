# Maximum Product of Two Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3536 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-two-digits/) |

## Problem Description

### Goal

Given a positive integer `n`, choose two different digit positions from its decimal representation and multiply the digits stored at those positions. Return the greatest product obtainable from any such pair.

Equal digit values may be selected together only when that digit occurs in at least two positions. For example, both `2` digits in `22` may be used, but a single occurrence cannot be reused.

### Function Contract

**Inputs**

- `n`: A positive integer with at least two decimal digits, where $10 \le n \le 10^9$.

**Return value**

- The maximum product of the digits at two distinct positions in `n`.

### Examples

**Example 1**

- Input: `n = 31`
- Output: `3`
- Explanation: The only pair of digits is `3` and `1`, whose product is `3`.

**Example 2**

- Input: `n = 22`
- Output: `4`
- Explanation: The two separate occurrences of `2` may be multiplied together.

**Example 3**

- Input: `n = 124`
- Output: `8`
- Explanation: Among the three digit pairs, `2 * 4` gives the largest product.
