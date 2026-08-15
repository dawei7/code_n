# Check Divisibility by Digit Sum and Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3622 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/) |

## Problem Description

### Goal

Given a positive integer `n`, examine every digit in its ordinary decimal representation. Form the digit sum by adding all of those digits, and independently form the digit product by multiplying them. Every occurrence contributes, including repeated digits; if any digit is zero, the complete product is consequently zero.

Add the digit sum and digit product to obtain one positive divisor. Determine whether that combined value divides the original `n` evenly. Return `true` exactly when the remainder is zero, and return `false` otherwise.

### Function Contract

**Inputs**

- `n`: The positive integer whose decimal digits and divisibility are examined.

The constraint is $1 \le n \le 10^6$.

**Return value**

Return whether `n` is divisible by the sum of its digit sum and digit product.

### Examples

#### Example 1

- **Input:** `n = 99`
- **Output:** `true`
- **Explanation:** The digit sum is 18 and the digit product is 81; their total is 99, which divides 99.

#### Example 2

- **Input:** `n = 23`
- **Output:** `false`
- **Explanation:** The digit sum is 5 and the digit product is 6, so the divisor is 11 and leaves a remainder when dividing 23.

#### Example 3

- **Input:** `n = 10`
- **Output:** `true`
- **Explanation:** The zero digit makes the product zero, while the digit sum is 1; their total is 1.
