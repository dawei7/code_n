## Problem Description & Examples
### Goal
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - maximum money robbed

### Examples
**Example 1**

- Input: `nums = [2, 3, 2]`
- Output: `3`

**Example 2**

- Input: `nums = [50]`
- Output: `50`

**Example 3**

- Input: `nums = [18, 73]`
- Output: `73`

---

## Underlying Base Algorithm(s)
- [Climbing stairs recurrence](dp_02_climbing-stairs.md)
- [Coin change](dp_05_coin-change.md)
- [Longest increasing subsequence](dp_07_longest-increasing-subsequence.md)
- [House robber](dp_11_house-robber.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
