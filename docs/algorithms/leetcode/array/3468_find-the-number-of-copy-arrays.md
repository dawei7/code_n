# Find the Number of Copy Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3468 |
| Difficulty | Medium |
| Topics | Array, Math |
| Official Link | [find-the-number-of-copy-arrays](https://leetcode.com/problems/find-the-number-of-copy-arrays/) |

## Problem Description & Examples
### Goal
Given an original array `original` and a list of constraints `bounds` where each element `bounds[i]` specifies a range `[min_i, max_i]` for the `i`-th element of a new array `copy`, determine how many distinct arrays `copy` can be formed such that the difference between consecutive elements in `copy` is identical to the difference between consecutive elements in `original`.

### Function Contract
**Inputs**

- `original`: A list of integers representing the base sequence.
- `bounds`: A list of lists, where each `bounds[i]` contains two integers `[min_i, max_i]` representing the inclusive range for the `i`-th element of the resulting array.

**Return value**

- An integer representing the total number of valid arrays that satisfy the difference constraints and the range bounds.

### Examples
**Example 1**

- Input: `original = [1, 2, 3]`, `bounds = [[1, 2], [2, 3], [3, 4]]`
- Output: `1`

**Example 2**

- Input: `original = [1, 2, 3]`, `bounds = [[1, 2], [1, 2], [1, 2]]`
- Output: `0`

**Example 3**

- Input: `original = [1, 1, 1]`, `bounds = [[1, 10], [2, 9]]`
- Output: `8`

---

## Underlying Base Algorithm(s)
The problem is solved using a greedy range-tracking approach. Since the difference between consecutive elements is fixed by the `original` array, if we choose a value `x` for the first element, all subsequent elements are determined by `copy[i] = copy[i-1] + (original[i] - original[i-1])`. This implies that for each index `i`, the value `copy[i]` must fall within `[bounds[i][0], bounds[i][1]]`. By shifting these bounds relative to the first element, we can find the intersection of all valid ranges for the first element.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the `original` array, as we iterate through the array exactly once.
- **Space Complexity**: `O(1)`, as we only store the current valid range boundaries.
