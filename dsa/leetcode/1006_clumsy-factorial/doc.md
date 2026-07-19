# Clumsy Factorial

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1006 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Stack, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/clumsy-factorial/) |

## Problem Description

### Goal

The factorial of a positive integer $n$ multiplies all positive integers from $n$ down through $1$. A clumsy factorial keeps those integers in decreasing order but replaces the multiplication signs with the repeating operator sequence multiplication, division, addition, and subtraction.

Evaluate the resulting expression with the usual arithmetic order of operations: multiplication and division occur before addition and subtraction, and adjacent multiplication and division operations are processed from left to right. Division is floor division as defined by the problem; for example, `10 * 9 / 8` evaluates as `90 / 8`, giving `11`. Given `n`, return its clumsy factorial.

### Function Contract

**Inputs**

- `n`: a positive integer satisfying $1\le n\le10^4$.

**Return value**

- The integer value of the clumsy-factorial expression formed from `n` down through `1`.

### Examples

**Example 1**

- Input: `n = 4`
- Output: `7`
- Explanation: The expression is `4 * 3 / 2 + 1`, which evaluates to `7`.

**Example 2**

- Input: `n = 10`
- Output: `12`
- Explanation: The expression is `10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1`.

**Example 3**

- Input: `n = 3`
- Output: `6`
- Explanation: The available operators produce `3 * 2 / 1`.
