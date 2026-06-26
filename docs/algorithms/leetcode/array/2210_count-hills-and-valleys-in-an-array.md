# Count Hills and Valleys in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2210 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [count-hills-and-valleys-in-an-array](https://leetcode.com/problems/count-hills-and-valleys-in-an-array/) |

## Problem Description & Examples
### Goal
Count hills and valleys after treating consecutive equal values as part of the same feature. A hill is above the nearest different value on both sides; a valley is below both.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

The total number of hill and valley features.

### Examples
**Example 1**

- Input: `nums = [2, 4, 1, 1, 6, 5]`
- Output: `3`

**Example 2**

- Input: `nums = [6, 6, 5, 5, 4, 1]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 2, 2, 1]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Compress consecutive duplicates, then inspect each interior value. Count it when it is strictly greater than both neighbors or strictly less than both. Compression ensures each plateau contributes at most one feature.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` with a streaming comparison
