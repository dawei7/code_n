# 3Sum Closest

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 16 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Sorting |
| Official Link | [3sum-closest](https://leetcode.com/problems/3sum-closest/) |

## Problem Description & Examples
### Goal
Choose three numbers from the array whose sum is closest to a given target.

### Function Contract
**Inputs**

- `nums`: a list of integers.
- `target`: the desired sum.

**Return value**

Return the three-number sum with the smallest absolute difference from `target`.

### Examples
**Example 1**

- Input: `nums = [-1,2,1,-4], target = 1`
- Output: `2`

**Example 2**

- Input: `nums = [0,0,0], target = 1`
- Output: `0`

**Example 3**

- Input: `nums = [1,1,1,0], target = -100`
- Output: `2`

---

## Underlying Base Algorithm(s)
Sort the array. Fix one number, then use two pointers over the suffix to test candidate triples. Move the left pointer right when the sum is too small and the right pointer left when it is too large, tracking the closest sum seen.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(1)` besides sorting storage
