# Number of 1 Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_242` |
| Frontend ID | 191 |
| Difficulty | Easy |
| Topics | Divide and Conquer, Bit Manipulation |
| Official Link | [number-of-1-bits](https://leetcode.com/problems/number-of-1-bits/) |

## Problem Description & Examples
### Goal
Given a positive integer `n`, write a function that returns the number of set bits (also known as Hamming weight) it has.

### Function Contract
**Inputs**

- `n`: int

**Return value**

int - number of set bits

### Examples
**Example 1**

- Input: `n = 11`
- Output: `3`

**Example 2**

- Input: `n = 8`
- Output: `1`

**Example 3**

- Input: `n = 7`
- Output: `3`

---

## Underlying Base Algorithm(s)
- [Count set bits](bit_01_count-set-bits.md)
- [Single number XOR](bit_03_single-number-xor.md)
- [Missing number](bit_10_missing-number.md)
- [Reverse bits](bit_12_reverse-bits.md)

---

## Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
