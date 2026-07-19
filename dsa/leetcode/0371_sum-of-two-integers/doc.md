# Sum of Two Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 371 |
| Difficulty | Medium |
| Topics | Math, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-two-integers/) |

## Problem Description
### Goal
Given two signed integers `a` and `b`, compute their arithmetic sum under the problem's 32-bit two's-complement model. Positive and negative operands, zero, carries, and sign-bit behavior must all be handled consistently with that fixed width.

Return the signed integer result without using the arithmetic `+` or `-` operators to perform the addition. Combine bitwise sum and carry information until no carry remains, then interpret the fixed-width pattern as signed when its high bit is set. The task returns the sum only and does not require exposing intermediate binary representations.

### Function Contract
**Inputs**

- `a`: a signed integer
- `b`: a signed integer

**Return value**

- Their signed integer sum under the problem's 32-bit two's-complement model.

### Examples
**Example 1**

- Input: `a = 1, b = 2`
- Output: `3`

**Example 2**

- Input: `a = -1, b = 47`
- Output: `46`

**Example 3**

- Input: `a = -33, b = 22`
- Output: `-11`
