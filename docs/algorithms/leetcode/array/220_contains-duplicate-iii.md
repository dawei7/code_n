# Contains Duplicate III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 220 |
| Difficulty | Hard |
| Topics | Array, Sliding Window, Sorting, Bucket Sort, Ordered Set |
| Official Link | [contains-duplicate-iii](https://leetcode.com/problems/contains-duplicate-iii/) |

## Problem Description & Examples
### Goal
Determine whether two distinct array positions are close in both index and value: their index distance must be at most `indexDiff` and their value difference at most `valueDiff`.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `indexDiff`: the maximum allowed index distance.
- `valueDiff`: the maximum allowed absolute value difference.

**Return value**

`true` if at least one qualifying pair exists; otherwise `false`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 1]`, `indexDiff = 3`, `valueDiff = 0`
- Output: `true`

**Example 2**

- Input: `nums = [1, 5, 9, 1, 5, 9]`, `indexDiff = 2`, `valueDiff = 3`
- Output: `false`

**Example 3**

- Input: `nums = [1, 4]`, `indexDiff = 1`, `valueDiff = 3`
- Output: `true`

---

## Underlying Base Algorithm(s)
Maintain a sliding window of at most `indexDiff` previous values using buckets of width `valueDiff + 1`. Two values within `valueDiff` must lie in the same or neighboring bucket. For each value, inspect those three buckets, then insert it and remove the value falling out of the index window. Use floor-consistent bucket ids for negative values.

---

## Complexity Analysis
- **Time Complexity**: `O(n)` expected
- **Space Complexity**: `O(min(n, indexDiff))`
