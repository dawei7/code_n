# Two Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_4` |
| Frontend ID | 1 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [two-sum](https://leetcode.com/problems/two-sum/) |

## Problem Description & Examples
### Goal
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`. You may assume each input has exactly one solution, and you may not use the same element twice.

### Function Contract
**Inputs**

- `nums`: List[int]
- `target`: int

**Return value**

List[int] - indices of the two numbers

### Examples
**Example 1**

- Input: `nums = [2, 7, 11, 15], target = 9`
- Output: `[0, 1]`

**Example 2**

- Input: `nums = [3, 2, 4], target = 6`
- Output: `[1, 2]`

**Example 3**

- Input: `nums = [3, 3], target = 6`
- Output: `[0, 1]`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
