# Divide Two Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 29 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/divide-two-integers/) |

## Problem Description
### Goal
You are given a signed 32-bit `dividend` and a nonzero signed 32-bit `divisor`. Compute their integer quotient without using multiplication, division, or modulo operators. Fractional parts are discarded by truncating toward zero, not by taking the mathematical floor for negative results.

Return the quotient within the signed 32-bit range $[-2^{31}, 2^{31}-1]$. The only mathematically overflowing input is $-2^{31}$ divided by $-1$; clamp that result to $2^{31}-1$. All sign combinations and magnitudes at the negative boundary must otherwise behave normally.

### Function Contract
**Inputs**

- `dividend`: signed 32-bit `int`
- `divisor`: nonzero signed 32-bit `int`

**Return value**

The truncated and clamped signed 32-bit integer quotient.

### Examples
**Example 1**

- Input: `dividend = 10, divisor = 3`
- Output: `3`

**Example 2**

- Input: `dividend = 7, divisor = -3`
- Output: `-2`

**Example 3**

- Input: `dividend = -2147483648, divisor = -1`
- Output: `2147483647`
