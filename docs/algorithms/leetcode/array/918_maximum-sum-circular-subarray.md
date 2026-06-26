# Maximum Sum Circular Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_209` |
| Frontend ID | 918 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Dynamic Programming, Queue, Monotonic Queue |
| Official Link | [maximum-sum-circular-subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) |

## Problem Description & Examples
### Goal
Given a circular integer array `nums` of length `n`, return the maximum possible sum of a non-empty subarray of `nums`.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of `nums[i]` is `nums[(i + 1) % n]` and the previous element of `nums[i]` is `nums[(i - 1 + n) % n]`.

A subarray may only include each element of the fixed buffer `nums` at most once.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - maximum circular subarray sum

### Examples
**Example 1**

- Input: `nums = [5, -3, 5]`
- Output: `10`

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
