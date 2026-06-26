# Subarray Sum Equals K

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_21` |
| Frontend ID | 560 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [subarray-sum-equals-k](https://leetcode.com/problems/subarray-sum-equals-k/) |

## Problem Description & Examples
### Goal
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.

### Function Contract
**Inputs**

- `nums`: List[int]
- `k`: int

**Return value**

int - number of subarrays with sum k

### Examples
**Example 1**

- Input: `nums = [1, 1, 1], k = 2`
- Output: `2`

**Example 2**

- Input: `nums = [1, 1], k = -5`
- Output: `0`

**Example 3**

- Input: `nums = [-3, 4], k = -4`
- Output: `0`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
