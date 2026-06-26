# Reverse Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_245` |
| Frontend ID | 190 |
| Difficulty | Easy |
| Topics | Divide and Conquer, Bit Manipulation |
| Official Link | [reverse-bits](https://leetcode.com/problems/reverse-bits/) |

## Problem Description & Examples
### Goal
Reverse bits of a given 32-bit unsigned integer.

### Function Contract
**Inputs**

- `n`: int

**Return value**

int - integer with reversed bits

### Examples
**Example 1**

- Input: `n = 43261596`
- Output: `964176192`

**Example 2**

- Input: `n = 1654615998`
- Output: `2113337670`

**Example 3**

- Input: `n = 577090037`
- Output: `2945295940`

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
