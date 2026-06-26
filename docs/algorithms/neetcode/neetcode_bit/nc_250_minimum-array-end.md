## Problem Description & Examples
### Goal
You are given two integers `n` and `x`. You want to construct an array of positive integers `nums` of size `n` where for every `0 <= i < n - 1`, `nums[i + 1] > nums[i]`, and the bitwise AND of all elements in `nums` is `x`.

Return the minimum possible value of `nums[n - 1]`.

### Function Contract
**Inputs**

- `n`: int
- `x`: int

**Return value**

int - minimum possible value of nums[n - 1]

### Examples
**Example 1**

- Input: `n = 3, x = 4`
- Output: `6`

**Example 2**

- Input: `n = 2, x = 7`
- Output: `15`

**Example 3**

- Input: `n = 4, x = 1`
- Output: `7`

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
