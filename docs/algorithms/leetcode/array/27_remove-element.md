# Remove Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_7` |
| Frontend ID | 27 |
| Difficulty | Easy |
| Topics | Array, Two Pointers |
| Official Link | [remove-element](https://leetcode.com/problems/remove-element/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place. Return the number of elements `k` not equal to `val`. The first `k` elements of `nums` should hold the remaining values.

### Function Contract
**Inputs**

- `nums`: List[int]
- `val`: int

**Return value**

int k - count of elements not equal to val

### Examples
**Example 1**

- Input: `nums = [3, 2, 2, 3], val = 3`
- Output: `2`

**Example 2**

- Input: `nums = [3, 3], val = 3`
- Output: `0`

**Example 3**

- Input: `nums = [1, 4], val = 4`
- Output: `1`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
