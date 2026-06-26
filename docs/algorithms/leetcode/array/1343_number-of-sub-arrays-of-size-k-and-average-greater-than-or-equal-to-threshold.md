# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1343 |
| Difficulty | Medium |
| Topics | Array, Sliding Window |
| Official Link | [number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) |

## Problem Description & Examples
### Goal
Count contiguous subarrays of length `k` whose average is at least `threshold`.

### Function Contract
**Inputs**

- `arr`: integer array.
- `k`: fixed window size.
- `threshold`: minimum required average.

**Return value**

The number of qualifying windows.

### Examples
**Example 1**

- Input: `arr = [2,2,2,2,5,5,5,8]`, `k = 3`, `threshold = 4`
- Output: `3`

**Example 2**

- Input: `arr = [11,13,17,23,29,31,7,5,2,3]`, `k = 3`, `threshold = 5`
- Output: `6`

**Example 3**

- Input: `arr = [1,1,1,1]`, `k = 2`, `threshold = 2`
- Output: `0`

---

## Underlying Base Algorithm(s)
Sliding window sum.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
