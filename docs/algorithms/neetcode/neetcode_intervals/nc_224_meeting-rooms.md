## Problem Description & Examples
### Goal
Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, determine if a person could attend all meetings.

### Function Contract
**Inputs**

- `intervals`: List[List[int]]

**Return value**

bool - True if all meetings can be attended

### Examples
**Example 1**

- Input: `intervals = [[0, 30], [5, 10], [15, 20]]`
- Output: `False`

**Example 2**

- Input: `intervals = [[5, 6]]`
- Output: `True`

**Example 3**

- Input: `intervals = []`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Activity selection / interval choice](greedy_01_activity-selection.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
