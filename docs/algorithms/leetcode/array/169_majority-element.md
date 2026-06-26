# Majority Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_8` |
| Frontend ID | 169 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Divide and Conquer, Sorting, Counting |
| Official Link | [majority-element](https://leetcode.com/problems/majority-element/) |

## Problem Description & Examples
### Goal
Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than `n/2` times. You may assume that the majority element always exists.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - the majority element

### Examples
**Example 1**

- Input: `nums = [3, 2, 3]`
- Output: `3`

**Example 2**

- Input: `nums = [50]`
- Output: `50`

**Example 3**

- Input: `nums = [18, 18]`
- Output: `18`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
