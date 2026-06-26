# Sum of Two Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_247` |
| Frontend ID | 371 |
| Difficulty | Medium |
| Topics | Math, Bit Manipulation |
| Official Link | [sum-of-two-integers](https://leetcode.com/problems/sum-of-two-integers/) |

## Problem Description & Examples
### Goal
Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

### Function Contract
**Inputs**

- `a`: int
- `b`: int

**Return value**

int - sum

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
