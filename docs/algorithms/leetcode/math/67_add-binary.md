# Add Binary

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_244` |
| Frontend ID | 67 |
| Difficulty | Easy |
| Topics | Math, String, Bit Manipulation, Simulation |
| Official Link | [add-binary](https://leetcode.com/problems/add-binary/) |

## Problem Description & Examples
### Goal
Given two binary strings `a` and `b`, return their sum as a binary string.

### Function Contract
**Inputs**

- `a`: str
- `b`: str

**Return value**

str - binary sum string

### Examples
**Example 1**

- Input: `a = "11", b = "1"`
- Output: `"100"`

**Example 2**

- Input: `a = '1', b = '10'`
- Output: `'11'`

**Example 3**

- Input: `a = '1', b = '1'`
- Output: `'10'`

---

## Underlying Base Algorithm(s)
- [Count set bits](bit_01_count-set-bits.md)
- [Single number XOR](bit_03_single-number-xor.md)
- [Missing number](bit_10_missing-number.md)
- [Reverse bits](bit_12_reverse-bits.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
