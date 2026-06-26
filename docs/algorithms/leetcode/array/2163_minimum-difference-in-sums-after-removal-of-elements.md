# Minimum Difference in Sums After Removal of Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2163 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Heap (Priority Queue) |
| Official Link | [minimum-difference-in-sums-after-removal-of-elements](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/) |

## Problem Description & Examples
### Goal
Given an array of length `3n`, remove exactly `n` elements. Split the remaining `2n` elements after its first `n` positions and minimize the first-half sum minus the second-half sum.

### Function Contract
**Inputs**

- `nums`: an integer array whose length is a multiple of three.

**Return value**

The minimum possible difference between the two remaining half sums.

### Examples
**Example 1**

- Input: `nums = [3, 1, 2]`
- Output: `-1`

**Example 2**

- Input: `nums = [7, 9, 5, 8, 1, 3]`
- Output: `1`

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `-2`

---

## Underlying Base Algorithm(s)
Consider each original split between indices `n - 1` and `2n - 1`. From the prefix ending at the split, retain the `n` smallest values with a max-heap and record their sum. From the suffix after the split, retain the `n` largest values with a min-heap and record their sum. Minimize `left_smallest_sum - right_largest_sum` over all compatible splits.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
