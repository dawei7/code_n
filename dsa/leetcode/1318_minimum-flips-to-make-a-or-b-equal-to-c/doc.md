# Minimum Flips to Make a OR b Equal to c

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1318 |
| Difficulty | Medium |
| Topics | Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/) |

## Problem Description
### Goal
Given three positive integers `a`, `b`, and `c`, change individual bits in the binary representations of `a` and `b` until their bitwise OR equals `c`. A flip changes one selected bit from 0 to 1 or from 1 to 0.

Return the minimum number of flips needed to satisfy `(a | b) == c`. Bits may be changed in either input integer, and each changed position in each integer counts as one flip.

### Function Contract
**Inputs**

- `a`: a positive integer with $1\le a\le10^9$.
- `b`: a positive integer with $1\le b\le10^9$.
- `c`: a positive integer with $1\le c\le10^9$.

Let $M=\max(a,b,c)$.

**Return value**

The minimum number of individual bit flips in `a` and `b` required to make their bitwise OR equal `c`.

### Examples
**Example 1**

- Input: `a = 2, b = 6, c = 5`
- Output: `3`
- Explanation: Three bit changes can produce values 1 and 4, whose OR is 5.

**Example 2**

- Input: `a = 4, b = 2, c = 7`
- Output: `1`
- Explanation: The low bit is absent from both inputs, so one of them must gain it.

**Example 3**

- Input: `a = 1, b = 2, c = 3`
- Output: `0`
- Explanation: The current OR is already 3.
