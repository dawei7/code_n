## Problem Description & Examples
### Goal
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - maximum subarray sum

### Examples
**Example 1**

- Input: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
- Output: `6`

**Example 2**

- Input: `nums = [3, -9]`
- Output: `3`

**Example 3**

- Input: `nums = [8]`
- Output: `8`

---

## Underlying Base Algorithm(s)
- [Gas station](greedy_06_gas-station.md)
- [Jump game](greedy_07_jump-game.md)
- [Candy distribution](greedy_08_candy-distribution.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
