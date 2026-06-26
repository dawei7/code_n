# Longest Consecutive Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_18` |
| Frontend ID | 128 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Union-Find |
| Official Link | [longest-consecutive-sequence](https://leetcode.com/problems/longest-consecutive-sequence/) |

## Problem Description & Examples
### Goal
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - length of the longest consecutive sequence

### Examples
**Example 1**

- Input: `nums = [100, 4, 200, 1, 3, 2]`
- Output: `4`

**Example 2**

- Input: `nums = [50, 51, 11, 52]`
- Output: `3`

**Example 3**

- Input: `nums = [66, 19, 18]`
- Output: `2`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
