# Number of 1 Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 191 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Divide and Conquer, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-1-bits/) |

## Problem Description
### Goal
Given a 32-bit unsigned integer, inspect its fixed-width binary representation and count the positions whose bit value is `1`. This count is also known as the population count or Hamming weight of the integer.

Return the number of set bits as an integer between `0` and `32`. Leading zero positions are part of the representation but add nothing, and the task counts bits rather than runs of adjacent ones or decimal digits. Zero therefore returns `0`, while the value with all thirty-two positions set returns `32`; the input is interpreted as unsigned throughout.

### Function Contract
**Inputs**

- `n`: a 32-bit unsigned integer

**Return value**

The number of bit positions containing one.

### Examples
**Example 1**

- Input: `11`
- Output: `3`

**Example 2**

- Input: `128`
- Output: `1`

**Example 3**

- Input: `2147483645`
- Output: `30`
