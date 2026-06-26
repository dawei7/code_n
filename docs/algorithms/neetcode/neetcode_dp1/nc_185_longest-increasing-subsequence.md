## Problem Description & Examples
### Goal
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - LIS length

### Examples
**Example 1**

- Input: `nums = [10, 9, 2, 5, 3, 7, 101, 18]`
- Output: `4`

**Example 2**

- Input: `nums = [-1]`
- Output: `1`

**Example 3**

- Input: `nums = [-33, 22]`
- Output: `2`

---

## Underlying Base Algorithm(s)
- [Climbing stairs recurrence](dp_02_climbing-stairs.md)
- [Coin change](dp_05_coin-change.md)
- [Longest increasing subsequence](dp_07_longest-increasing-subsequence.md)
- [House robber](dp_11_house-robber.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
