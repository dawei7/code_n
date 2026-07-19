# Armstrong Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1134 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/armstrong-number/) |

## Problem Description

### Goal

You are given a positive integer `n` containing $d$ decimal digits. The number is an Armstrong number when the sum obtained by raising each of its digits to the $d$th power is exactly equal to `n` itself.

Determine whether `n` is an Armstrong number and return the corresponding boolean value. Repeated digits contribute separately, and a digit `0` contributes $0^d=0$. The exponent is the digit count of the complete input, not a fixed value such as three.

### Function Contract

**Inputs**

- `n`: an integer satisfying $1 \le n \le 10^8$.

Let $d=\lfloor \log_{10} n \rfloor+1$ be the number of decimal digits in `n`; the input bound guarantees $1 \le d \le 9$.

**Return value**

`true` exactly when the sum of the $d$th powers of all decimal digits equals `n`; otherwise `false`.

### Examples

**Example 1**

- Input: `n = 153`
- Output: `true`
- Explanation: $1^3+5^3+3^3=153$.

**Example 2**

- Input: `n = 123`
- Output: `false`
- Explanation: $1^3+2^3+3^3=36$, which is not `123`.
