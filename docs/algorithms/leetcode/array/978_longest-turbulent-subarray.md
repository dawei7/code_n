# Longest Turbulent Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_210` |
| Frontend ID | 978 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Sliding Window |
| Official Link | [longest-turbulent-subarray](https://leetcode.com/problems/longest-turbulent-subarray/) |

## Problem Description & Examples
### Goal
Given an integer array `arr`, return the length of a maximum size turbulent subarray of `arr`.

A subarray `arr[i], arr[i+1], ..., arr[j]` is said to be turbulent if and only if:
- For i <= k < j:
  - `arr[k] > arr[k+1]` when `k` is odd, and `arr[k] < arr[k+1]` when `k` is even;
  - OR, `arr[k] < arr[k+1]` when `k` is odd, and `arr[k] > arr[k+1]` when `k` is even.

### Function Contract
**Inputs**

- `arr`: List[int]

**Return value**

int - length of longest turbulent subarray

### Examples
**Example 1**

- Input: `arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]`
- Output: `5`

**Example 2**

- Input: `arr = [98, 54]`
- Output: `2`

**Example 3**

- Input: `arr = [73]`
- Output: `1`

---

## Underlying Base Algorithm(s)
- [Gas station](greedy_06_gas-station.md)
- [Jump game](greedy_07_jump-game.md)
- [Candy distribution](greedy_08_candy-distribution.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
