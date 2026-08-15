# Minimize XOR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2429 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Greedy, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Minimize XOR](https://leetcode.com/problems/minimize-xor/) |

## Problem Description

### Goal

You are given two positive integers `num1` and `num2`. Choose a positive integer $x$ whose binary representation contains exactly as many set bits as `num2`.

Among every integer satisfying that bit-count requirement, minimize the value of `x ^ num1`, where `^` is bitwise XOR. Return $x$ itself, not the minimized XOR value. The test data guarantees that the minimizing integer is unique.

### Function Contract

**Inputs**

- `num1`: A positive integer.
- `num2`: A positive integer whose set-bit count $k$ must be matched by the result.

Both inputs lie in $[1,10^9]$. Let $U=\max(\texttt{num1},\texttt{num2})$; every legal input fits within 30 binary positions.

**Return value**

- The unique positive integer $x$ with exactly $k$ set bits that minimizes `x ^ num1`.

### Examples

#### Example 1

- **Input:** `num1 = 3, num2 = 5`
- **Output:** `3`

Both `3` and `5` contain two set bits, and choosing 3 makes the XOR zero.

#### Example 2

- **Input:** `num1 = 1, num2 = 12`
- **Output:** `3`

Two set bits are required. Keeping the low set bit of `num1` and adding the next-lowest zero bit produces `3`.

#### Example 3

- **Input:** `num1 = 15, num2 = 1`
- **Output:** `8`

Only one set bit is allowed, so matching the highest set bit of `num1` minimizes the XOR.
