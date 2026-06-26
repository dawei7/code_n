# Counting Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_243` |
| Frontend ID | 338 |
| Difficulty | Easy |
| Topics | Dynamic Programming, Bit Manipulation |
| Official Link | [counting-bits](https://leetcode.com/problems/counting-bits/) |

## Problem Description & Examples
### Goal
Given an integer `n`, return an array of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the number of `1` bits in the binary representation of `i`.

### Function Contract
**Inputs**

- `n`: int

**Return value**

List[int] - counts of set bits

### Examples
**Example 1**

- Input: `n = 5`
- Output: `[0, 1, 1, 2, 1, 2]`

**Example 2**

- Input: `n = 2`
- Output: `[0, 1, 1]`

**Example 3**

- Input: `n = 3`
- Output: `[0, 1, 1, 2]`

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
