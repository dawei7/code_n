# Reverse Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_248` |
| Frontend ID | 7 |
| Difficulty | Medium |
| Topics | Math |
| Official Link | [reverse-integer](https://leetcode.com/problems/reverse-integer/) |

## Problem Description & Examples
### Goal
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

### Function Contract
**Inputs**

- `x`: int

**Return value**

int - reversed integer

### Examples
**Example 1**

- Input: `x = 123`
- Output: `321`

**Example 2**

- Input: `x = -123`
- Output: `-321`

**Example 3**

- Input: `x = 120`
- Output: `21`

---

## Underlying Base Algorithm(s)
- [Count set bits](bit_01_count-set-bits.md)
- [Single number XOR](bit_03_single-number-xor.md)
- [Missing number](bit_10_missing-number.md)
- [Reverse bits](bit_12_reverse-bits.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
