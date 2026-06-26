# Mean of Array After Removing Some Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1619 |
| Difficulty | Easy |
| Topics | Array, Sorting |
| Official Link | [mean-of-array-after-removing-some-elements](https://leetcode.com/problems/mean-of-array-after-removing-some-elements/) |

## Problem Description & Examples
### Goal
Remove the smallest five percent and largest five percent of values, then return
the mean of the remaining values.

### Function Contract
**Inputs**

- `arr`: an integer array whose length is divisible by `20`.

**Return value**

The trimmed mean as a floating-point value.

### Examples
**Example 1**

- Input: `arr = [6, 2, 7, 5, 1, 2, 0, 8, 1, 3, 1, 5, 7, 1, 4, 4, 8, 8, 2, 1]`
- Output: `4.0`

**Example 2**

- Input: `arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]`
- Output: `55.5`

**Example 3**

- Input: `arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]`
- Output: `10.0`

---

## Underlying Base Algorithm(s)
Sort the array. Let `trim = n / 20`; ignore the first `trim` and last `trim`
values, then average the remaining slice.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`.
- **Space Complexity**: `O(1)` extra space if sorting in place.
