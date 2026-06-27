# Minimum Right Shifts to Sort the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2855 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [minimum-right-shifts-to-sort-the-array](https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/) |

## Problem Description & Examples
### Goal
Determine the minimum number of right cyclic shifts required to transform a given list of integers into a non-decreasingly sorted sequence. If the array cannot be sorted via cyclic shifts, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the minimum number of right shifts, or -1 if it is impossible to sort the array.

### Examples
**Example 1**

- Input: `nums = [3, 4, 5, 1, 2]`
- Output: `2`

**Example 2**

- Input: `nums = [1, 3, 5]`
- Output: `0`

**Example 3**

- Input: `nums = [2, 1, 4]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem relies on identifying the "pivot" point in a cyclically sorted array. A valid cyclically sorted array can have at most one index `i` where `nums[i] > nums[i+1]`. If such a point exists, the array can be sorted by shifting the suffix starting at `i+1` to the front. We must also verify that the last element is less than or equal to the first element to ensure the cyclic property holds.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we perform a single pass to identify the pivot and validate the sorted order.
- **Space Complexity**: `O(1)`, as we only use a constant amount of extra space for pointers and counters.
