# Find Right Interval

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 436 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-right-interval/) |

## Problem Description
### Goal
Given intervals with unique start values, find a right interval for every original interval `i`. A candidate `j` is on the right when `intervals[j].start >= intervals[i].end`; among candidates, choose the one with the smallest qualifying start.

Return one original index per input interval in the same order as the input. Use `-1` when no start reaches the required end. The chosen interval need not be adjacent in input order, and endpoint equality qualifies. Return indices rather than interval values, preserving the unique-start tie guarantee.

### Function Contract
**Inputs**

- `intervals`: a list of `[start, end]` pairs whose start values are unique

**Return value**

- Return one index per input interval. Use the chosen right interval's original index, or `-1` when no start is large enough.

### Examples
**Example 1**

- Input: `intervals = [[1, 2]]`
- Output: `[-1]`

**Example 2**

- Input: `intervals = [[3, 4], [2, 3], [1, 2]]`
- Output: `[-1, 0, 1]`

**Example 3**

- Input: `intervals = [[1, 4], [2, 3], [3, 4]]`
- Output: `[-1, 2, -1]`
