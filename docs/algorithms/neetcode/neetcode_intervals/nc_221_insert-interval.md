## Problem Description & Examples
### Goal
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the `i`-th interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `new_interval = [start, end]` that represents the start and end of another interval.

Insert `new_interval` into `intervals` such that `intervals` is still sorted by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

Note: You should not modify the input arrays in-place.

### Function Contract
**Inputs**

- `intervals`: List[List[int]]
- `new_interval`: List[int]

**Return value**

List[List[int]] - updated intervals

### Examples
**Example 1**

- Input: `intervals = [[1, 3], [6, 9]], new_interval = [2, 5]`
- Output: `[[1, 5], [6, 9]]`

**Example 2**

- Input: `intervals = [[5, 6]], new_interval = [3, 8]`
- Output: `[[3, 8]]`

**Example 3**

- Input: `intervals = [], new_interval = [1, 4]`
- Output: `[[1, 4]]`

---

## Underlying Base Algorithm(s)
- [Activity selection / interval choice](greedy_01_activity-selection.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
