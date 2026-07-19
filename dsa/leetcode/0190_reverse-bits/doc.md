# Reverse Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 190 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Divide and Conquer, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-bits/) |

## Problem Description
### Goal
Given a 32-bit unsigned integer `n`, view it as exactly thirty-two binary positions, including any leading zero bits that are normally omitted from its written representation. Reverse the complete bit sequence so the least significant original bit becomes the most significant result bit and vice versa.

Return the unsigned integer represented by those reversed thirty-two bits. Do not reverse decimal digits or stop at the highest set bit, because leading zeroes can become meaningful trailing positions and trailing zeroes can become high-value bits. An all-zero input remains zero, and applying the same fixed-width reversal twice restores the original value.

### Function Contract
**Inputs**

- `n`: a 32-bit unsigned integer

**Return value**

The unsigned integer represented by the reversed 32-bit sequence.

### Examples
**Example 1**

- Input: `43261596`
- Output: `964176192`

**Example 2**

- Input: `0`
- Output: `0`

**Example 3**

- Input: `1`
- Output: `2147483648`
