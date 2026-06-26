## Problem Description & Examples
### Goal
Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.

### Function Contract
**Inputs**

- `intervals`: List[List[int]]

**Return value**

int - minimum rooms required

### Examples
**Example 1**

- Input: `intervals = [[0, 30], [5, 10], [15, 20]]`
- Output: `2`

**Example 2**

- Input: `intervals = [[14, 15], [9, 18]]`
- Output: `2`

**Example 3**

- Input: `intervals = [[19, 21]]`
- Output: `1`

---

## Underlying Base Algorithm(s)
- [Activity selection / interval choice](greedy_01_activity-selection.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
