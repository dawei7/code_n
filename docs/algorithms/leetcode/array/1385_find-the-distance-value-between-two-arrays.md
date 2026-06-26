# Find the Distance Value Between Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1385 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Official Link | [find-the-distance-value-between-two-arrays](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/) |

## Problem Description & Examples
### Goal
Count how many values in `arr1` are farther than distance `d` from every value in `arr2`.

### Function Contract
**Inputs**

- `arr1`: the first list of integers.
- `arr2`: the second list of integers.
- `d`: the allowed distance threshold.

**Return value**

The number of elements `x` in `arr1` such that `abs(x - y) > d` for every `y` in `arr2`.

### Examples
**Example 1**

- Input: `arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2`
- Output: `2`

**Example 2**

- Input: `arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3`
- Output: `2`

**Example 3**

- Input: `arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6`
- Output: `1`

---

## Underlying Base Algorithm(s)
Sorting plus binary search. Sort `arr2`; for each value in `arr1`, only its insertion neighbors in `arr2` can be closest, so checking those neighbors is enough.

---

## Complexity Analysis
- **Time Complexity**: `O(m log m + n log m)` where `n = len(arr1)` and `m = len(arr2)`.
- **Space Complexity**: `O(m)` if sorting a copy of `arr2`, or `O(1)` extra if sorting in place.
