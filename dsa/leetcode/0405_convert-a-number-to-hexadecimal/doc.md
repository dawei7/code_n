# Convert a Number to Hexadecimal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 405 |
| Difficulty | Easy |
| Topics | Math, String, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-a-number-to-hexadecimal/) |

## Problem Description
### Goal
Given a signed 32-bit integer `num`, convert its fixed-width bit pattern to hexadecimal. Positive values use their ordinary magnitude, while negative values must be interpreted through the full 32-bit two's-complement representation rather than prefixed with a minus sign.

Return lowercase hexadecimal digits `0-9` and `a-f` without unnecessary leading zeroes. Return exactly `"0"` for zero. A negative input produces the necessary eight hexadecimal digits representing all thirty-two bits. Do not use a built-in library method to perform the conversion directly; use fixed-width numeric operations so negative values retain the required two's-complement semantics.

### Function Contract
**Inputs**

- `num`: a signed 32-bit integer

**Return value**

- Return the lowercase hexadecimal digits without leading zeroes. Return `"0"` for zero; negative values must contain their full eight-digit two's-complement representation.

### Examples
**Example 1**

- Input: `num = 26`
- Output: `"1a"`

**Example 2**

- Input: `num = -1`
- Output: `"ffffffff"`

**Example 3**

- Input: `num = 0`
- Output: `"0"`
