# Single Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_241` |
| Frontend ID | 136 |
| Difficulty | Easy |
| Topics | Array, Bit Manipulation |
| Official Link | [single-number](https://leetcode.com/problems/single-number/) |

## Problem Description & Examples
### Goal
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - the single number

### Examples
**Example 1**

- Input: `nums = [4, 1, 2, 1, 2]`
- Output: `4`

**Example 2**

- Input: `nums = [2, 2, 1]`
- Output: `1`

**Example 3**

- Input: `nums = [1]`
- Output: `1`

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
