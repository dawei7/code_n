# Missing Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_246` |
| Frontend ID | 268 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting |
| Official Link | [missing-number](https://leetcode.com/problems/missing-number/) |

## Problem Description & Examples
### Goal
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - the missing number

### Examples
**Example 1**

- Input: `nums = [3, 0, 1]`
- Output: `2`

**Example 2**

- Input: `nums = [2, 0]`
- Output: `1`

**Example 3**

- Input: `nums = [1]`
- Output: `0`

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
