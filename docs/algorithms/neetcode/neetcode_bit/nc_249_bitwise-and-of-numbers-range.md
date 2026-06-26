## Problem Description & Examples
### Goal
Given two integers `left` and `right` that represent the range `[left, right]`, return the bitwise AND of all numbers in this range, inclusive.

### Function Contract
**Inputs**

- `left`: int
- `right`: int

**Return value**

int - bitwise AND result

### Examples
**Example 1**

- Input: `left = 5, right = 7`
- Output: `4`

**Example 2**

- Input: `left = 49, right = 62`
- Output: `48`

**Example 3**

- Input: `left = 17, right = 35`
- Output: `0`

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
