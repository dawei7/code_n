# Multiply Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 43 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/multiply-strings/) |

## Problem Description
### Goal
You are given two non-negative integers as decimal strings `num1` and `num2`. Each string contains only digits and has no leading zero unless it is exactly `"0"`; the numbers may be too long for ordinary fixed-width integer types.

Return their exact product as a canonical decimal string. Do not convert either complete operand to an integer or rely on arbitrary-precision multiplication. The result must contain no leading zeroes, and multiplying by zero must produce the single-character string `"0"`.

### Function Contract
**Inputs**

- `num1`: decimal `str` without leading zeros except `"0"`
- `num2`: decimal `str` without leading zeros except `"0"`

**Return value**

A decimal `str` representing the exact product.

### Examples
**Example 1**

- Input: `num1 = "2", num2 = "3"`
- Output: `"6"`

**Example 2**

- Input: `num1 = "123", num2 = "456"`
- Output: `"56088"`

**Example 3**

- Input: `num1 = "0", num2 = "999"`
- Output: `"0"`
