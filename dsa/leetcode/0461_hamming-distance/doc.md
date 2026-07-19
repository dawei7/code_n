# Hamming Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 461 |
| Difficulty | Easy |
| Topics | Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/hamming-distance/) |

## Problem Description
### Goal
Given two nonnegative integers `x` and `y`, compare their binary representations position by position. A bit contributes to the Hamming distance when one integer has `0` at that position and the other has `1`.

Return the total number of differing positions. Leading zeroes beyond both numbers' highest set bits match and add nothing, while a set bit present in only the larger-width representation does count. Equivalently, count set bits in $x \oplus y$. The task returns the distance only, not the differing indices or a binary string.

### Function Contract
**Inputs**

- `x`: a nonnegative integer
- `y`: a nonnegative integer

**Return value**

- The number of binary positions containing different bits in `x` and `y`

### Examples
**Example 1**

- Input: `x = 1, y = 4`
- Output: `2`

**Example 2**

- Input: `x = 3, y = 1`
- Output: `1`

**Example 3**

- Input: `x = 0, y = 0`
- Output: `0`
