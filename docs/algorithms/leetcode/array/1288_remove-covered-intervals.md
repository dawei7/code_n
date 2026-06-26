# Remove Covered Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1288 |
| Difficulty | Medium |
| Topics | Array, Sorting |
| Official Link | [remove-covered-intervals](https://leetcode.com/problems/remove-covered-intervals/) |

## Problem Description & Examples
### Goal
Remove every interval that is fully covered by another interval and return how many intervals remain.

### Function Contract
**Inputs**

- `intervals`: list of `[start, end]` intervals.

**Return value**

The count of intervals not covered by another interval.

### Examples
**Example 1**

- Input: `intervals = [[1,4],[3,6],[2,8]]`
- Output: `2`

**Example 2**

- Input: `intervals = [[1,4],[2,3]]`
- Output: `1`

**Example 3**

- Input: `intervals = [[0,10],[5,12]]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Sorting with sweep-line maximum endpoint tracking.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` or `O(1)` extra depending on sort implementation.
